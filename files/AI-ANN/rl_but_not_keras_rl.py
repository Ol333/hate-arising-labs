import random
import math
import numpy as np

from keras.models import Sequential, Model
from keras.layers import Dense, Activation, Flatten, Input, Concatenate
from keras.optimizers import Adam

import rl.core as krl
from rl.agents import DDPGAgent
from rl.memory import SequentialMemory
from rl.random import OrnsteinUhlenbeckProcess

# from gymnasium.spaces import Box

from celluloid import Camera
import matplotlib.pyplot as plt  

from car_track import Track

class actionSpace(krl.Space):
    def __init__(self):
        self.shape = (3,)

class observationSpace(krl.Space):
    def __init__(self):
        self.shape = (6,)
    def sample(self, seed=None): pass
    def contains(self, x): pass


class Cure(krl.Env):
    tr : Track
    D : float # радиус обзора
    I : int # индекс нашего автомобиля на треке
    v_max = 10

    def __init__(self, N, R, fl=False):
        self.tr = Track(N, R, fl)
        self.n = N
        self.r = R
        self.reward_range = (-1,1)
        self.action_space = actionSpace()
        self.observation_space = observationSpace()
        self.D = 10
        self.reset()

    def observe_area(self):
        observe_stuff = self.tr.observe_short(self.tr.l[self.I][0], self.tr.line[self.I], self.D)
        for k in range(2):
            intr_line = self.tr.get_line_number(self.I, k)
            if intr_line != None:
                observe_stuff = np.append(observe_stuff, self.tr.observe_short(self.tr.l[self.I][0], intr_line, self.D))
            else:
                observe_stuff = np.append(observe_stuff, [(2*np.pi*self.tr.r), (2*np.pi*self.tr.r)])
        return observe_stuff

    def reset(self):
        self.tr.reset(self.n, self.r)
        # задаем один автомобиль, управляемый нейронкой, и получаем его индекс:
        self.I = self.tr.set_vehicles_type(2)[0]
        observation = self.observe_area()
        return observation

    def step(self, action):
        # 0,1 - left, right .... для полосы
        if action.shape == (1,3): # в какой-то момент что-то ломается, 
            action = action[0]    # поэтому эти костыли фиксят появления нового уровня вложенности для action
        v = ((action[0]+1.0)/2) * self.v_max
        previous_obs = self.tr.observe(self.tr.l[self.I], self.tr.line[self.I], self.D)
        pre_way = self.tr.line[self.I]
        if action[1] < 0 and action[2] < 0: # остаемся в своем коридоре
            self.tr.set_CNN_speed_and_line(np.array([v]), np.array([self.I]), -1) 
        else: # или перестраиваемся в сторону, где action больше
            self.tr.set_CNN_speed_and_line(np.array([v]), np.array([self.I]), list(action[1:]).index(max(action[1:])))

        self.tr.step() # шаг среды
        observation = self.tr.observe(self.tr.l[self.I], self.tr.line[self.I], self.D)
        aft_way = self.tr.line[self.I]
        # определить, не перелетели ли мы кого-нибудь
        done = False
        reward = 0

        # попытка сделать плавную награду за дистанцию до столкновения
        if ((self.tr.get_safe_distance(v) <= self.tr.get_forward_distance(self.tr.l[self.I][0], observation[0]))
            and (self.tr.get_safe_distance(v) <= self.tr.get_forward_distance(self.tr.l[self.I][0], previous_obs[0]))):
            reward += 0.4 
        else: # дистанция до лидера была и осталась больше безопасной
            reward -= 0.3

        if ((self.tr.get_safe_distance(v) <= self.tr.get_forward_distance(observation[1], self.tr.l[self.I][0]))
            and (self.tr.get_safe_distance(v) <= self.tr.get_forward_distance(previous_obs[1], self.tr.l[self.I][0]))):
            reward += 0.05
        else: # дистанция с позади идущим была и осталась больше безопасной
            reward -= 0.05

        if v > 1:
            reward += ((v - 1) / (self.v_max - 1))
        else: # скорость не опускается в ноль
            reward -= 0.2

        forward_distance = self.tr.get_forward_distance(self.tr.l[self.I][0], observation[0])
        pre_forward_distance = self.tr.get_forward_distance(self.tr.l[self.I][0], previous_obs[0])
        if pre_way != aft_way: # случай смены полосы
            if forward_distance > pre_forward_distance:
                reward += 0.4
            elif forward_distance == pre_forward_distance:
                reward += 0.1
            else: # было выгодное перестроение
                reward -= 0.3                
        else:
            if (forward_distance - pre_forward_distance) < 1.0:
                reward += 0.2
            else: # дистанция до лидера сократилась или увеличилась не более, чем на 1м
                reward -= 0.2

        temp_pre_observation = np.array([(self.tr.get_forward_distance(self.tr.l[self.I][0], previous_obs[0])),
                                (self.tr.get_forward_distance(previous_obs[2], self.tr.l[self.I][0]))])
        for k in range(2):
            intr_line = self.tr.get_line_number(self.I, k)
            if intr_line != None:
                temp_pre_observation = np.append(temp_pre_observation, self.tr.observe_short(self.tr.l[self.I][0], intr_line, self.D))
            else:
                temp_pre_observation = np.append(temp_pre_observation, [0, 0])

        out_observation = np.array([(self.tr.get_forward_distance(self.tr.l[self.I][0], observation[0])),
                                (self.tr.get_forward_distance(observation[2], self.tr.l[self.I][0]))])
        for k in range(2):
            intr_line = self.tr.get_line_number(self.I, k)
            if intr_line != None:
                out_observation = np.append(out_observation, self.tr.observe_short(self.tr.l[self.I][0], intr_line, self.D))
            else:
                out_observation = np.append(out_observation, [0, 0])

        if temp_pre_observation[2] == 0 and temp_pre_observation[3] == 0 and action[1] > 0:
            reward -= 0.2
        if temp_pre_observation[4] == 0 and temp_pre_observation[5] == 0 and action[2] > 0:
            reward -= 0.2

        if (pre_forward_distance > 3*self.tr.get_safe_distance(v) 
            and action[1]<0 and action[2]<0):
            reward += 0.1

        if temp_pre_observation[2] > out_observation[2] and action[1]>0:
            reward += 0.2
        if temp_pre_observation[4] > out_observation[4] and action[2]>0:
            reward += 0.2

        if (observation[1] == previous_obs[3]) or (observation[3] == previous_obs[1]):
            done = True

        return out_observation, reward, done, {}

    def get_position(self):
        return self.tr.l[self.I][0], self.D, self.tr.line[self.I]

    def get_vehicle(self):
        return self.tr.get_vehicles(), self.tr.get_lines()
    
    def render(self, mode='human', close=False):
        pass

    def close(self): pass

## создание и обучение модели

Epochs = 250
our_env = Cure(42, 36) # расположение на треке шахматное, чтобы модель обучалась
np.random.seed(123)
assert len(our_env.action_space.shape) == 1
nb_actions = our_env.action_space.shape[0]

actor = Sequential()
actor.add(Flatten(input_shape=(1,) + our_env.observation_space.shape))
actor.add(Dense(4, use_bias=True))
actor.add(Activation('relu'))
actor.add(Dense(4, use_bias=True))
actor.add(Activation('relu'))
actor.add(Dense(nb_actions, use_bias=True))
actor.add(Activation('tanh'))
print(actor.summary())

action_input = Input(shape=(nb_actions,), name='action_input')
observation_input = Input(shape=(1,) + our_env.observation_space.shape, name='observation_input')
flattended_observation = Flatten()(observation_input)
x = Concatenate()([action_input, flattended_observation])
x = Dense(8, use_bias=False)(x)
x = Activation('relu')(x)
x = Dense(5, use_bias=True)(x)
x = Activation('relu')(x)
x = Dense(1)(x)
x = Activation('linear')(x)
critic = Model(inputs=[action_input, observation_input], outputs=x)
print(critic.summary())

memory = SequentialMemory(limit=100000, window_length=1)
random_process = OrnsteinUhlenbeckProcess(size=nb_actions, theta=.15, mu=0., sigma=.3)
agent = DDPGAgent(nb_actions=nb_actions, actor=actor, critic=critic, 
                critic_action_input=action_input, memory=memory, 
                nb_steps_warmup_critic=100, nb_steps_warmup_actor=100,
                random_process=random_process, gamma=.99, target_model_update=1e-3)

agent.compile(Adam(learning_rate=.001, clipnorm=1.), metrics=['mae'])

agent.fit(our_env, nb_steps=10000, visualize=True, verbose=1, nb_max_episode_steps=Epochs)

agent.test(our_env, nb_episodes=3, visualize=True, nb_max_episode_steps=Epochs)
our_env.close()

# actor.save('actor_{}.h5'.format(datetime.now().strftime("%H_%M_%S")))

########
## тестирование модели

N = 20      # количество автомобилей
R = 10      # радиус трека

fig = plt.figure()
camera = Camera(fig)
random.seed(123)
theCure = Cure(N, R, True) # расположение на треке будет случайным
observation = theCure.reset()

# информационная плашка
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
sum_reward = 0
for i in range(200):
    action = actor.predict(observation.reshape((1,1,6)))
    print('observation', observation, 'action', action)
    observation, reward, done, _ = theCure.step(action)
    sum_reward += reward
    if done:
      print('Столкновение на шаге', i, '. Награда ', sum_reward)
      break
    # покажем автомобили
    vehicles_l, vehicles_lines = theCure.get_vehicle()
    fi = vehicles_l / R
    vehicles_x = np.cos(fi)
    vehicles_y = np.sin(fi)
    for j in range(len(vehicles_l)):
        x_add = vehicles_lines[j] % 3
        y_add = vehicles_lines[j] // 3
        temp_r = R + (2*theCure.tr.car_radius*x_add)
        plt.scatter(vehicles_x[j]*temp_r, vehicles_y[j]*temp_r, c='red')
    # если что, то тут один из автомобилей является нашим автопилотом, а дальше мы просто поверх красного кружочка рисуем синий
# покажем робота
    l, r, line = theCure.get_position()
    fi_ = l / R
    temp_r_ = R + (2 * theCure.tr.car_radius * (line % 3))
    x_ = math.cos(fi_) * temp_r_
    y_ = math.sin(fi_) * temp_r_

    plt.scatter(x_, y_, c='blue')
    fig = plt.gcf()
    ax = fig.gca()

    textstr = '\n'.join((
    r'epoch=%d' % (i, ),
    r'points=%d' % (reward, ),
    ))

    ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14,
      verticalalignment='top', bbox=props)

    camera.snap()

print('Итоговое вознаграждение',sum_reward)
theCure.close()
animation = camera.animate()
animation.save('celluloid_minimal.gif')
animation