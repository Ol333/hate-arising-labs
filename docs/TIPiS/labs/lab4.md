<ol class="breadcrumb">
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}">Главная</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/TIPiS/index.html">ТИПиС</a></li>
  <li class="breadcrumb-item active">ЛР №4</li>
</ol>

<nav>
  <ul></ul>
</nav>

# Математика

У вас есть [википедия](https://ru.wikipedia.org/wiki/%D0%9E%D0%BF%D1%82%D0%B8%D0%BC%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F_(%D0%BC%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B0)){:target="_blank"}:

Стандартная математическая задача оптимизации формулируется таким образом. **Среди элементов $χ$, образующих множество $Χ$, найти такой элемент $ χ* $, который доставляет минимальное значение $ f(χ*) $ заданной функции $ f(χ) $.**

Также вы можете использовать знания, полученные ранее при изучения методов оптимизации, и любые материалы, которые вы сможете найти.

## Задание

Поставить задачу оптимизации для своего варианта.

Для этого нужно определить допустимое множество $X$, целевую функцию $f$ и критерий поиска.

<table class="table table-hover">
  <thead>
    <tr>
      <th scope="col">№ варианта</th>
      <th scope="col">Оптимизация</th>
    </tr>
  </thead>
  <tbody>
    <tr class="table-active">
      <th scope="row">1</th>
      <td>Жизни</td>
    </tr>
    <tr class="table-primary">
      <th scope="row">2</th>
      <td>Перемещения из дома в универ</td>
    </tr>
    <tr class="table-active">
      <th scope="row">3</th>
      <td>Прохождения игры</td>
    </tr>
    <tr class="table-primary">
      <th scope="row">4</th>
      <td>Записи к врачу</td>
    </tr>
    <tr class="table-active">
      <th scope="row">5</th>
      <td>Сбора мнений</td>
    </tr>
    <tr class="table-primary">
      <th scope="row">6</th>
      <td>Сбора рюкзака/сумки</td>
    </tr>
    <tr class="table-active">
      <th scope="row">7</th>
      <td>Поиска подходящего к ситуации стикера/эмоджи/мема</td>
    </tr>
    <tr class="table-primary">
      <th scope="row">8</th>
      <td>Прохождения преподов, к которым нужно подойти</td>
    </tr>
    <tr class="table-active">
      <th scope="row">9</th>
      <td>Распространения информации</td>
    </tr>
    <tr class="table-primary">
      <th scope="row">10</th>
      <td>Подготовки к экзамену</td>
    </tr>
    <tr class="table-active">
      <th scope="row">11</th>
      <td>Программы</td>
    </tr>
    <tr class="table-primary">
      <th scope="row">12</th>
      <td>Презентации (представления информации)</td>
    </tr>
   </tbody>
</table>

## Как делать:

* Выбрать один критерий (желательно, количественный), по которому вы определяете успешность процесса. Определить максимум или минимум соответствует успеху.
* Определить, от чего зависит значение этого критерия — это будут переменные. Они являются аргументами целевой функции.
* Определить, на что из переменных мы можем повлиять — это допустимое множество(а) $X$.

Сформулировать постановку задачи оптимизации, представить на паре в виде текста (какими угодно средствами).

Сделать устное предположение, как поставленную задачу можно решить.

## Пример

*Оптимизировать прогулку.*

Задача оптимизации -- среди элементов конечного множества $X = \\{ x \, \vert \, 0 \le x \le 1440 \\}$ времени начала движения в мин от полуночи; найти такое $x^* \in X$, для которого значение $f ( x^* ) = \max\limits_{x \in X} f$ для заданного функционала $f(x, dn, wth, pth, att) = a \in \Bbb R^1$, где $x$ -- время начала движения, рассмотренное ранее, $dn$ -- день недели, $wth \in WTH$ *= {ясно, снег, дождь, штормовое предупреждение}* -- погода, $pth$ -- маршрут движения, заданный последовательностью GPS координат, $att \in ATT= \\{ at \, \vert \, 0 \le at \le 1 \\}$ -- уровень внимания прогуливающегося; который определяет количество встреченных в процессе движения оранжевых тракторов.

<div class="row">
  <div class="col-lg-12">
   <ul class="list-unstyled">
     <li class="float-end">
       <button type="button" class="btn btn-outline-primary" onclick="window.location.href='#математика';">Вверх</button>
     </li>
     <li  class="float-end">
       <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/TIPiS/labs/lab5.html';">ЛР №5 →</button>
     </li>
     <li>
       <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/TIPiS/labs/lab3.html';">← ЛР №3</button>
     </li>
   </ul>
  </div>
</div>
