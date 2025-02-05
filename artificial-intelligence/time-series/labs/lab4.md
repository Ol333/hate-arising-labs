<ol class="breadcrumb">
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}">Главная</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/artificial-intelligence/index.html">ИИ</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/artificial-intelligence/time-series/index.html">Временные ряды</a></li>
  <li class="breadcrumb-item active">ЛР №4</li>
</ol>

# Преобразование Тейлора

Члены ряда Тейлора определяются выражением

<div class="table-responsive">
$ \sum_{n=0}^\infty \frac{f^{(n)}(a)}{n!} (x-a)^n = f(a) + \frac{f'(a)}{1!} (x-a) + \frac{f ' ' (a)}{2!} (x-a)^2 + .. $
</div>

## Задание

* Реализовать функцию или класс для рассчета коэффициентов $\frac{f^{(n)}(a)}{n!}$ ряда Тейлора в точке 0.
* Исходную функцию разложить на ряд с количеством членов 3, 5, 10, 25, 50. Сравнить с известным аналитическим решением.
* Построить график апроксимации значений функции с помощью ряда Тейлора.


<div class="table-responsive">
<table class="table table-hover border-primary table-bordered">
   <thead>
     <tr>
       <th scope="col">№ варианта</th>
       <th scope="col">Функция</th>
     </tr>
   </thead>
   <tbody>
     <tr>
       <th scope="row">1</th>
       <td>$cos(x)$</td>
     </tr>
     <tr>
       <th scope="row">2</th>
       <td>$\frac{1}{1-x}$</td>
     </tr>
     <tr>
       <th scope="row">3</th>
       <td>$ln(1+x)$</td>
     </tr>
     <tr>
       <th scope="row">4</th>
       <td>$e^x$</td>
     </tr>
     <tr>
       <th scope="row">5</th>
       <td>$sin(x)$</td>
     </tr>
     <tr>
       <th scope="row">6</th>
       <td>$(1+x)^a$</td>
     </tr>
    </tbody>
</table>
</div>

<div class="row">
  <div class="col-lg-12">
    <ul class="list-unstyled">
      <li class="float-end">
        <button type="button" class="btn btn-outline-primary" onclick="window.location.href='#преобразование-тейлора';">Вверх</button>
      </li>
      <li  class="float-end">
       <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/artificial-intelligence/time-series/labs/lab5.html';">ЛР №5 →</button>
     </li>
      <li>
        <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/artificial-intelligence/time-series/labs/lab3.html';">← ЛР №3</button>
      </li>
    </ul>
  </div>
</div>
