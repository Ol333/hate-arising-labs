<ol class="breadcrumb">
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}">Главная</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/artificial-intelligence/index.html">ИИ</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/artificial-intelligence/time-series/index.html">Временные ряды</a></li>
  <li class="breadcrumb-item active">ЛР №5</li>
</ol>

<nav>
  <ul></ul>
</nav>


# Преобразование Фурье

Прямое преобразование Фурье (обозначается также $F_+$) сопоставляет кусочно-гладкой абсолютно интегрируемой функции $f(x)$ новую функцию

$\widehat f(y) = \frac{1}{\sqrt{2 \pi}} \int_{- \infty}^{+ \infty}{f(x)e^{-ixy} dy}$

Обратное преобразование Фурье ($F_−$) сопоставляет кусочно-гладкой абсолютно интегрируемой функции $f(x)$ новую функцию

$\breve f(y) = \frac{1}{\sqrt{2 \pi}} \int_{- \infty}^{+ \infty}{f(x)e^{ixy} dy}$

# Дискретное преобразование Фурье

Прямое дискретное преобразование Фурье (ДПФ):

$X_k = \sum_{n=0}^{N-1}x_n \cdot e^{-i 2 \pi k n / N}$, где $k = 0, ..., N-1$

Обратное дискретное преобразование Фурье (ОДПФ):

$x_n = \frac{1}{N} \sum_{k=0}^{N-1}X_k e^{i 2 \pi k n / N}$, где $k = 0, ..., N-1$

# Быстрое преобразование Фурье

Модификация, позволяющая получить результат за время, меньшее чем $O(N^{2})$. 

## Задание 1

Исходный сигнал представляет собой синусоиду $f(x) = A_0 \sin(w_0 x + \varphi _0 )$.

* Подготовить данные (набор координат $x$, $y$). Построить график исходного сигнала.

* Осуществить прямое преобразование Фурье **(не используя библиотеки)**. Построить график.

* Осуществить обратное преобразование Фурье. Построить график, который должен совпадать с исходным.

* Реализовать то же с помощью библиотек и сравнить результаты.


## Задание 2

* Построить графики АЧХ и ФЧХ для сигналов (тремор) по вариантам.

## Задание 3

* Найти описание одного из алгоритмов БПФ и реализовать.
* Сравнить время выполнения с кодом из Задания [1](#задание-1).




<div class="table-responsive">
<table class="table table-hover border-primary">
   <thead>
     <tr class="table-dark">
       <th scope="col">№ варианта</th>
       <th scope="col">Данные</th>
     </tr>
   </thead>
   <tbody>
     <tr>
       <th scope="row">1</th>
       <td><a href="https://disk.yandex.ru/d/bnqTyeOGDRYc3w" target="_blank">Файл</a></td>
     </tr>
     <tr>
       <th scope="row">2</th>
       <td><a href="https://disk.yandex.ru/d/IbGzaFNgpxMxtw" target="_blank">Файл</a></td>
     </tr>
     <tr>
       <th scope="row">3</th>
       <td><a href="https://disk.yandex.ru/d/5iD8Y0tnvu0o6A" target="_blank">Файл</a></td>
     </tr>
     <tr>
       <th scope="row">4</th>
       <td><a href="https://disk.yandex.ru/d/8afhtsPSK2_ZkQ" target="_blank">Файл</a></td>
     </tr>
     <tr>
       <th scope="row">5</th>
       <td><a href="https://disk.yandex.ru/d/HJOfJTaAD6dIug" target="_blank">Файл</a></td>
     </tr>
     <tr>
       <th scope="row">6</th>
       <td><a href="https://disk.yandex.ru/d/HZbg5FX8XpQ3LQ" target="_blank">Файл</a></td>
     </tr>
    </tbody>
</table>
</div>

<div class="row">
  <div class="col-lg-12">
    <ul class="list-unstyled">
      <li class="float-end">
        <button type="button" class="btn btn-outline-primary" onclick="window.location.href='#преобразование-фурье';">Вверх</button>
      </li>
      <li  class="float-end">
       <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/artificial-intelligence/time-series/labs/lab6.html';">ЛР №6 →</button>
     </li>
      <li>
        <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/artificial-intelligence/time-series/labs/lab4.html';">← ЛР №4</button>
      </li>
    </ul>
  </div>
</div>
