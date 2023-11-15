<ol class="breadcrumb">
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}">Главная</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/artificial-intelligence/index.html">ИИ</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/artificial-intelligence/ANN/index.html">ИНС</a></li>
  <li class="breadcrumb-item active">ЛР №5</li>
</ol>

<nav>
  <ul></ul>
</nav>

# Multihead



# Задание

Используя библиотеку Keras на Python:

<ol>
<li>
  Обучить нейронку, аппроксимирующую $f(x) = sin(x)+sin(\sqrt{2}*x)$. <b>(Создать набор данных на две колонки: $X$ от -20 до 20 с шагом 0.1 и $Y$. Разделить на обучающую и тестовую выборки. Обучить. Вывести график функции и точек предсказания нейронки на тестовом наборе.)</b>
<br>
Сравнить с рис. ниже.

<div class="card border-primary mb-2" style="max-width: 30rem;">
  <div class="card-body">
  <img src="{{ site.baseurl }}/img/ANN_aperiod.jpg"
        alt="sin"  focusable="false" width="100%"
        class="d-block user-select-none" />
  </div>
</div>
</li>
</ol>

<div class="row">
  <div class="col-lg-12">
    <ul class="list-unstyled">
      <li class="float-end">
        <button type="button" class="btn btn-outline-primary" onclick="window.location.href='#keras';">Вверх</button>
      </li>
      <!-- <li  class="float-end">
       <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/artificial-intelligence/ANN/labs/lab6.html';">ЛР №6 →</button>
     </li> -->
      <li>
        <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/artificial-intelligence/ANN/labs/lab4.html';">← ЛР №4</button>
      </li>
    </ul>
  </div>
</div>
