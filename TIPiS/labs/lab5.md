<ol class="breadcrumb">
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}">Главная</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/TIPiS/index.html">ТИПиС</a></li>
  <li class="breadcrumb-item active">ЛР №5</li>
</ol>

<nav>
  <ul></ul>
</nav>

# IDEF0

Читаем [стандарт](http://www.nicevt.ru/wp-content/uploads/2019/10/%D0%A0-50.1.028-2001-%D0%9C%D0%B5%D1%82%D0%BE%D0%B4%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D1%8F-IDEF0.pdf){:target="_blank"}. Нас интересуют синтаксис и семантика графического языка IDEF0. Дополнительно, методика разработки функциональных моделей.

Если кратко, то синтаксис следующий:

<div class="card border-primary mb-2" style="max-width: 40rem;">
  <div class="card-body">
  <img src="{{ site.baseurl }}/img/idef0.svg"
        alt="Синтаксис нотаций"  focusable="false" width="100%"
        class="d-block user-select-none" />
  </div>
</div>

## Задание 🎇

Спроектировать информационную систему в нотации IDEF0:
* Составить контекстную диаграмму, на которой должно быть выделено не менее **3 функциональных задач** (выходы системы).
* Провести декомпозицию контекстной диаграммы на **пять блоков**.

Советую использовать [draw.io](https://app.diagrams.net/){:target="_blank"}.

Не забудьте сохранить результат!

<div class="table-responsive">
<table class="table table-hover border-primary table-bordered">
  <thead>
    <tr>
      <th scope="col">№ варианта</th>
      <th scope="col">Тема</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">1</th>
      <td>ИС склада</td>
    </tr>
    <tr>
      <th scope="row">2</th>
      <td>ИС службы заказа такси</td>
    </tr>
    <tr>
      <th scope="row">3</th>
      <td>ИС службы доставки еды</td>
    </tr>
    <tr>
      <th scope="row">4</th>
      <td>ИС выдачи музыкальных рекомендаций</td>
    </tr>
    <tr>
      <th scope="row">5</th>
      <td>ИС фирмы проката автомобилей</td>
    </tr>
    <tr>
      <th scope="row">6</th>
      <td>ИС частной поликлиники</td>
    </tr>
    <tr>
      <th scope="row">7</th>
      <td>ИС кредитной компании</td>
    </tr>
    <tr>
      <th scope="row">8</th>
      <td>ИС приемной компании в университете</td>
    </tr>
    <tr>
      <th scope="row">9</th>
      <td>ИС документооборота для малого предприятия (частная школа)</td>
    </tr>
    <tr>
      <th scope="row">10</th>
      <td>ИС сборочного производства</td>
    </tr>
    <tr>
      <th scope="row">11</th>
      <td>ИС ресторана</td>
    </tr>
    <tr>
      <th scope="row">12</th>
      <td>ИС психолога</td>
    </tr>
   </tbody>
</table>
</div>

## Пример информационной системы

*Информационная система анализа ходов игрока сёги.*

Контекстная диаграмма.

<div class="card border-primary mb-2" style="max-width: 40rem;">
  <div class="card-body">
  <img src="{{ site.baseurl }}/img/IDEF0_shogi.svg"
        alt="Синтаксис нотаций"  focusable="false" width="100%"
        class="d-block user-select-none" />
  </div>
</div>

Декомпозиция.

<div class="card border-primary mb-2" style="max-width: 40rem;">
  <div class="card-body">
  <img src="{{ site.baseurl }}/img/IDEF0_shogi_decomp.svg"
        alt="Синтаксис нотаций"  focusable="false" width="100%"
        class="d-block user-select-none" />
  </div>
</div>

<div class="row">
  <div class="col-lg-12">
   <ul class="list-unstyled">
     <li class="float-end">
       <button type="button" class="btn btn-outline-primary" onclick="window.location.href='#idef0';">Вверх</button>
     </li>
     <li  class="float-end">
       <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/TIPiS/labs/lab6.html';">ЛР №6 →</button>
     </li>
     <li>
       <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/TIPiS/labs/lab4.html';">← ЛР №4</button>
     </li>
   </ul>
  </div>
</div>