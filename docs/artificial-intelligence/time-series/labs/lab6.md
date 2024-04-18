<ol class="breadcrumb">
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}">Главная</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/artificial-intelligence/index.html">ИИ</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/artificial-intelligence/time-series/index.html">Временные ряды</a></li>
  <li class="breadcrumb-item active">ЛР №6</li>
</ol>

<nav>
  <ul></ul>
</nav>

# Фильтры

Фильтр - это частотно-избирательное устройство, которое пропускает сигналы определенных частот и задерживает или ослабляет сигналы других частот.

По виду АЧХ фильтры могут быть классифицированы на следующие:
* **фильтры нижних частот (ФНЧ)** - пропускает низкие частоты и задерживает высокие; 
* **фильтры верхних частот (ФВЧ)** - задерживает  низкие   частоты  и  пропускает  высокие;
* **полосовые фильтры (ПФ)** - пропускает полосу частот от $ω_1$ до $ω_2$ и задерживает те частоты, которые расположены выше или ниже этой полосы частот;
* **режекторные (заграждающие) фильтры (РЖ)** - задерживает полосу частот от $ω_1$ до $ω_2$  и пропускает частоты, расположенные выше или ниже  этой полосы частот.

# Задание

* Почитать про фильтр вашего варианта.
* Найти подходящую реализацию (например, в библиотеке `scipy.signal`).
* Разобраться со значением всех агрументов используемой/ых функции/й.
* Реализовать фильтр.
* Используя данные из предыдущей лабораторной, осуществить фильтрацию сигнала.

<div class="table-responsive">
<table class="table table-hover border-primary">
   <thead>
     <tr class="table-dark">
       <th scope="col">№ варианта</th>
       <th scope="col">Фильтр</th>
     </tr>
   </thead>
   <tbody>
     <tr>
       <th scope="row">1</th>
       <td>Полосовой</td>
     </tr>
     <tr>
       <th scope="row">2</th>
       <td>Нижних частот</td>
     </tr>
     <tr>
       <th scope="row">3</th>
       <td>Верхних частот</td>
     </tr>
     <tr>
       <th scope="row">4</th>
       <td>Режекторный</td>
     </tr>
    </tbody>
</table>
</div>


<div class="row">
  <div class="col-lg-12">
    <ul class="list-unstyled">
      <li class="float-end">
        <button type="button" class="btn btn-outline-primary" onclick="window.location.href='#фильтры';">Вверх</button>
      </li>
      <li  class="float-end">
       <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/artificial-intelligence/time-series/labs/lab7.html';">ЛР №7 →</button>
     </li>
      <li>
        <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/artificial-intelligence/time-series/labs/lab5.html';">← ЛР №5</button>
      </li>
    </ul>
  </div>
</div>
