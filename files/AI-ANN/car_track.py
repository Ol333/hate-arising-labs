import numpy as np
from random import randint
import math

class Track:
    r : int        # радиус трека
    n : int        # количество ТС
    l : np.ndarray # координата вдоль трека в метрах
    v : np.ndarray # скорость вдоль трека
    a : np.ndarray # ускорение
    line : np.ndarray # полоса
    rlt : np.ndarray # время запрета на перестроения

    k_ott = 10.6
    k_prit = 0.301
    speed_limit = 3
    car_radius = 2
    delta_t = 0.1

    time = 0

    def get_safe_distance(self, s):
        if (s < 5.5):
            return 2
        if (s < 16.7):
            return 10
        if (s < 25):
            return 25
        if (s < 36.1):
            return 50
        return 100

    def __init__(self, N, R, fl=False):
        self.fl = fl
        self.reset(N, R)

    def reset(self, N, R):
        self.n = N
        self.r = R
        self.l = None
        self.time = 0
        np.random.seed(1000)

        if self.fl:                                         # случайное равномерное распределение от numpy
            self.l = np.random.rand(self.n,1)*(2*np.pi*self.r)
            self.line = np.random.randint(3, size=self.n)
        else:                                    # самопальное равномерное начальное распределение агентов
            # распределяем шахматами по 3 полосам
            temp_vehicles_counter_for_rl = self.n // 3
            temp_l = []
            g_l = (2*np.pi*self.r) / temp_vehicles_counter_for_rl
            for i in range(temp_vehicles_counter_for_rl):
                g_length_1 = i*2 * g_l
                g_length_2 = (i*2+1) * g_l
                s = g_length_1 + 0.001
                temp_l.append(s)
                s = g_length_2 + 0.001
                temp_l.append(s)
                s = g_length_1 + 0.001
                temp_l.append(s)
            self.l = np.array(temp_l)
            self.l.shape = (self.n, 1)
            self.line = np.array(list(range(3))*temp_vehicles_counter_for_rl)
            # temp_l = []
            # g_l = (2*np.pi*self.r) / self.n
            # temp_l.append(5.0)
            # for i in range(1, self.n):
            #     g_length = i * g_l
            #     s = g_length + 0.001
            #     temp_l.append(s)
            # self.l = np.array(temp_l)
            # self.l.shape = (self.n, 1)

        self.v = np.ones((self.n,1))*8
        # self.v = np.random.rand(self.n,1)*6
        self.a = np.zeros((self.n,1))
        # self.line = np.random.randint(3, size=self.n)
        # self.line = np.array([0]*self.n)
        # self.line = np.array([4]*self.n) # центр для 3x3 коридоров
        
        self.rlt = np.zeros((self.n,1))
        self.lines = np.arange(3)

    # получить последовательность расположений ТС на дороге
    def construct_sequence(self):
        counts_of_lines = self.lines.shape[0]
        temp = [[] for _ in range(counts_of_lines)]
        for i in range(self.n):
            temp[self.line[i]].append((self.l[i][0],i))
        for i in range(counts_of_lines):
            temp[i].sort()
        for i in range(counts_of_lines):
            temp[i] = list(map(lambda x: x[1], temp[i]))
        return temp
    
    def set_vehicles_type(self, t):
        if t == 2: # это для размещение rl-обучающегося на 2-й полосе
            return [1]
        
    def step(self):
        self.collision_check(*self.pre_step())
        self.time += 1

    def pre_step(self):
        index_list = self.construct_sequence()
        v_temp = np.zeros((self.n,1))
        for cl in range(self.lines.shape[0]):
            i = 0 # за счет перестроений, меняется количество агентов в коридорах
            while i < len(index_list[cl]):
                cur_id = index_list[cl][i]
                temp_n = len(index_list[cl])
                if temp_n > 1:
                    l_f = self.get_forward_distance(self.l[cur_id][0], self.l[index_list[cl][(i+1)%temp_n]][0])
                    l_b = self.get_forward_distance(self.l[index_list[cl][i-1]][0], self.l[cur_id][0])
                    v_temp_cur_id, veh_lea_id = self.one_car_move(cur_id, temp_n, l_f, l_b)
                    v_temp[cur_id] = v_temp_cur_id
                    if veh_lea_id != -1:
                        index_list[cl].remove(cur_id)
                        i -= 1
                        if veh_lea_id == None:
                            index_list[self.line[cur_id]].append(cur_id)
                        else:
                            index_list[self.line[cur_id]].insert(index_list[self.line[cur_id]].index(veh_lea_id), cur_id)
                else:
                    l_f = 2*math.pi*self.r
                    l_b = 2*math.pi*self.r
                    v_temp_cur_id, veh_lea_id = self.one_car_move(cur_id, temp_n, l_f, l_b)
                    v_temp[cur_id] = v_temp_cur_id
                    # v_temp[cur_id] = self.v[cur_id] # или придумать что-нибудь по-умнее
                i += 1
        l_temp = np.copy(self.l)
        self.l = (self.l + v_temp*self.delta_t) % (2*np.pi*self.r)
        return (index_list, l_temp, v_temp, self.delta_t)
    
    def one_car_move(self, cur_id, temp_n, l_f, l_b):
        veh_lea_id = -1
        v_temp = 0
        safe_distance = self.get_safe_distance(self.v[cur_id])
        if self.v[cur_id] != 0 and temp_n != 1 and l_f < 0.1 + self.car_radius * 2: # можно переформулировать в else
            pass
        else:
            if temp_n == 1:
                a_f = max(0.1, self.k_prit * (2*math.pi*self.r))
                a_b = 0
            else:
                if l_b < safe_distance + self.car_radius * 2:
                    a_b = (self.k_ott/100) / l_b
                else:
                    a_b = 0
                if l_f < safe_distance + self.car_radius * 2:
                    a_f = -self.k_ott / l_f
                else:
                    a_f = self.k_prit * l_f
            self.a[cur_id] = a_b + a_f
            v_temp = min(max((self.v[cur_id]+self.a[cur_id]*self.delta_t),0), self.speed_limit-1)
            self.rlt[cur_id] = max(self.rlt[cur_id]-1, 0)
        return v_temp, veh_lea_id

    def get_line_number(self, cur_id, k):
        intr_line = None
        if k == 0 and self.line[cur_id] > 0:
            intr_line = self.line[cur_id] - 1
        elif k == 1 and self.line[cur_id] < (self.lines.shape[0] - 1):
            intr_line = self.line[cur_id] + 1
        # print(self.line[cur_id], self.lines.shape[0], k, intr_line)
        return intr_line

    def collision_check(self, index_list, l_temp, v_temp, delta_t): # проверка на столкновения
        new_index_list = self.construct_sequence()
        temp = np.copy(l_temp)
        l_temp = np.copy(self.l)
        self.l = np.copy(temp)
        if index_list != new_index_list:
            for cl in range(self.lines.shape[0]):
                temp_n = len(index_list[cl])
                counter = 0
                for i in range(temp_n):
                    if index_list[cl][i%temp_n] == new_index_list[cl][(i+1)%temp_n]:
                        counter += 1
                if counter > 3:
                    new_index_list[cl] = new_index_list[cl][1:]+new_index_list[cl][:1]
        for cl in range(self.lines.shape[0]):
            temp_n = len(index_list[cl])
            for i in range(temp_n): # что тут вообще происходит?
                i1 = index_list[cl][i]
                i2 = index_list[cl][(i+1) % temp_n]
                ni1 = new_index_list[cl][(i+1) % temp_n]
                ni2 = new_index_list[cl][i]
                if i1 == ni1 and i2 == ni2 and i1!=i2 and self.type[i1] != 2 and self.type[i2] != 2:
                    # иногда бывает отрицательная скорость
                    temporary_v = (self.get_forward_distance(self.l[i1], l_temp[i2])-self.get_safe_distance(self.v[i1])-2*self.car_radius) / delta_t
                    self.v[i1] = max(temporary_v, 0)
                    # self.v[i1] = max(min(temporary_v, self.speed_limit), 0) # ВЕРНУТЬ!
                    # print('STOP')
                    self.v[i2] = v_temp[i2]
                else:
                    self.v[i1] = v_temp[i1]
                    self.v[i2] = v_temp[i2]
        self.l = (self.l + self.v*delta_t) % (2*np.pi*self.r)
    
    # позволяем rl модели вмешиваться в наш порядок
    def set_CNN_speed_and_line(self, vel, ind, k):
        for i in range(len(ind)):
            self.v[ind[i]] = max(vel[i], 0)
            print('направление -', k, 'текущая полоса:', self.line[ind[i]])
            if k >= 0:
                intr_line = self.get_line_number(ind[i], k)
                if intr_line != None:
                    self.line[ind[i]] = intr_line

    def get_shortest_distance_on_circle(self,we,target):
        d = abs(target - we)
        lenght = (2*math.pi*self.r) / 2
        fl = False
        if d > lenght:
            d = 2*lenght - d
            fl = not fl
        if (target > we and fl) or (we > target and (not fl)):
            d = -d
        return d

    def get_forward_distance(self, we, target):
        if target > we:
            return target - we
        else:
            return ((2*math.pi*self.r) - we) + target

    def observe_short(self, point, cl, d=None):
        obs = self.observe(point, cl)
        if obs[0] != None and obs[2] != None:
            return np.array([self.get_forward_distance(point, obs[0]), self.get_forward_distance(obs[2], point)])
        return np.array([(2*np.pi*self.r), (2*np.pi*self.r)])

    def observe(self,point, cl, d=None): # получить 2-х ближайших соседей от заданной точки
        # на заданной полосе, (в пределах заданной дистанции)
        if cl == None:
            return np.array([0, 0])
        res = []
        leader = []
        behind = []
        for i in range(self.n):
            if self.line[i] == cl:
                distance = self.get_shortest_distance_on_circle(point, self.l[i][0])
                if distance > 0:
                    leader.append((distance, self.l[i][0]))
                elif distance < 0:
                    behind.append((-distance, self.l[i][0]))
        leader.sort()
        behind.sort()
        if len(leader) > 0:
            res.append(leader[0][1])
            res.append(np.where(self.l == leader[0][1])[0][0])
        elif len(behind) > 0:
            res.append(behind[-1][1])
            res.append(np.where(self.l == behind[-1][1])[0][0])
        else:
            res.append(None)
            res.append(None)
        if len(behind) > 0:
            res.append(behind[0][1])
            res.append(np.where(self.l == behind[0][1])[0][0])
        elif len(leader) > 0:
            res.append(leader[-1][1])
            res.append(np.where(self.l == leader[-1][1])[0][0])
        else:
            res.append(None)
            res.append(None)
        # найти только впереди идущего и позади идущего 
        # (с их индексами), чтобы был массив (4, 1)
        return np.array(res)

    def get_vehicles(self):
        return self.l
    
    def get_vehicles_speed(self):
        return self.v

    def get_lines(self):
        return self.line

