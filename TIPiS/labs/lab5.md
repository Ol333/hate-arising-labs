<ol class="breadcrumb">
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}">Главная</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/TIPiS/index.html">ТИПиС</a></li>
  <li class="breadcrumb-item active">ЛР №5</li>
</ol>

<nav>
  <ul></ul>
</nav>

# IDEF0

Почитайте [стандарт](https://docs.cntd.ru/document/1200028629), пожалуйста. Хотя бы попытайтесь.

Если кратко, то синтаксис следующий:

<div class="card border-primary mb-2" style="max-width: 40rem;">
  <div class="card-body">
  <img src="{{ site.baseurl }}/img/idef0.svg"
        alt="Синтаксис нотаций"  focusable="false" width="100%"
        class="d-block user-select-none" />
  </div>
</div>

## Задание

Спроектировать информационную систему в нотации IDEF0.

Для этого составить контекстную диаграмму, на которой должно быть выделено **3 функциональные задачи** (выхода системы).

Затем провести декомпозицию контекстной диаграммы на **пять блоков**.

Советую использовать [draw.io](https://app.diagrams.net/){:target="_blank"}.

Не забудьте сохранить результат!

<table class="table table-hover">
  <thead>
    <tr>
      <th scope="col">№ варианта</th>
      <th scope="col">Тема</th>
    </tr>
  </thead>
  <tbody>
    <tr class="table-active">
      <th scope="row">1</th>
      <td>Автоматизация функций складского учета</td>
    </tr>
    <tr class="table-primary">
      <th scope="row">2</th>
      <td>ИС службы заказа такси</td>
    </tr>
    <tr class="table-active">
      <th scope="row">3</th>
      <td>ИС службы доставки еды</td>
    </tr>
    <tr class="table-primary">
      <th scope="row">4</th>
      <td>ИС выдачи музыкальных рекомендаций</td>
    </tr>
    <tr class="table-active">
      <th scope="row">5</th>
      <td>ИС фирмы проката автомобилей</td>
    </tr>
    <tr class="table-primary">
      <th scope="row">6</th>
      <td>ИС Частной поликлиники/сумки</td>
    </tr>
    <tr class="table-active">
      <th scope="row">7</th>
      <td>ИС кредитной компания</td>
    </tr>
    <tr class="table-primary">
      <th scope="row">8</th>
      <td>ИС автоматизации приемной компании в университете</td>
    </tr>
    <tr class="table-active">
      <th scope="row">9</th>
      <td>Система документооборота для малого предприятия (частная школа)</td>
    </tr>
    <tr class="table-primary">
      <th scope="row">10</th>
      <td>ИС планирования и подготовки сборочного производства</td>
    </tr>
    <tr class="table-active">
      <th scope="row">11</th>
      <td>ИС ресторана</td>
    </tr>
    <tr class="table-primary">
      <th scope="row">12</th>
      <td>ИС психолога</td>
    </tr>
   </tbody>
</table>

## Пример

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