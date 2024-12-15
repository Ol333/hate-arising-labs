<ol class="breadcrumb">
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}">Главная</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/TIPiS/index.html">ТИПиС</a></li>
  <li class="breadcrumb-item active">ЛР №10</li>
</ol>


# Помехоустойчивое кодирование


## Задание

* Получить от пользователя сообщение произвольной длины, состоящее из произвольного количества символов, и возможную кратность ошибок $t \le 4$, подлежащих обнаружению и исправлению.
* Вычислить мощность $M$ первичного алфавита.
* Определить количество информационных разрядов $k$.
* Определить количество дополнительных проверочных разрядов $r$, которе вместе с информационными определят длину кода $n$.
* Рассчитать границу Хемминга.
* Оценить избыточность.
* Вывести порождающую матрицу для помехоустойчивого кода по варианту.
* Изобразить любыми средствами исходный сигнал, принятый сингнал с шумом *(инверсия от 0 до $t$ битов)*, восстановленный сигнал.


<div class="table-responsive">
<table class="table table-hover border-primary  table-bordered">
   <thead>
     <tr class="table-dark">
       <th scope="col">№ варианта</th>
       <th scope="col">Помехустойчивый код</th>
     </tr>
   </thead>
   <tbody>
     <tr>
       <th scope="row">1</th>
       <td>Код с проверкой на четность (линейный блочный код) $u = (m_1,m_2,m_3,m_1+m_2+m_3)$</td>
     </tr>
     <tr>
       <th scope="row">2</th>
       <td>Итеративный код (табличка по строкам и столбцам)</td>
     </tr>
     <tr>
       <th scope="row">3</th>
       <td>"Облачный" код (пересекающиеся круги Эйлера)</td>
     </tr>
    </tbody>
</table>
</div>


<div class="row">
  <div class="col-lg-12">
   <ul class="list-unstyled">
     <li class="float-end">
       <button type="button" class="btn btn-outline-primary" onclick="window.location.href='#помехоустойчивое-кодирование';">Вверх</button>
     </li>
     <li  class="float-end">
       <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/TIPiS/labs/lab11.html';">ЛР №11 →</button>
     </li>
     <li>
       <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/TIPiS/labs/lab9.html';">← ЛР №9</button>
     </li>
   </ul>
  </div>
</div>