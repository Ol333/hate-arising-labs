<ol class="breadcrumb">
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}">Главная</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/artificial-intelligence/index.html">ИИ</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/artificial-intelligence/ANN/index.html">ИНС</a></li>
  <li class="breadcrumb-item active">ЛР №4</li>
</ol>

<nav>
  <ul></ul>
</nav>

# Keras

Читаем [Шолле](https://codernet.ru/books/python/glubokoe_obuchenie_na_python_sholle_fransua/){:target="_blank"} стр. 81 – 119:
* стр. 92 – 102. Пример бинарной классификации (отзывы к фильмам);
* стр. 102 – 111. Пример многоклассивой классификации (новостные ленты);
* стр. 111 – 118. Пример регрессии (предсказание цен на дома – *вы уже немного читали это*).

**В процессе чтения реализуем то, что описывается.**

# Задание

Используя библиотеку Keras на Python:

1. Обучить нейронку, аппроксимирующую $f(x) = x$. (Создать набор данных от -20 до 20 с шагом 0.1. Разделить на обучающую и тестовую выборки. Обучить. Вывести график функции и точек предсказания нейронки на тестовом наборе.)

2. Обучить нейронку, аппроксимирующую $f(x) = \\\\|x\\\\| $.

3. Обучить нейронку, аппроксимирующую окружность.

4. Обучить нейронку, аппроксимирующую $f(x) = sin(x)$.

5. Найти на [Kaggle](https://www.kaggle.com/datasets){:target="_blank"} набор данных для классификации и обучить на нем модель.

6. Показать на графиках, как меняется ошибка в процессе обучения (для одной из предыдущих НС).

<div class="row">
  <div class="col-lg-12">
    <ul class="list-unstyled">
      <li class="float-end">
        <button type="button" class="btn btn-outline-primary" onclick="window.location.href='#обратное-распространение-ошибки';">Вверх</button>
      </li>
      <!-- <li  class="float-end">
       <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/artificial-intelligence/ANN/labs/lab5.html';">Лабораторная работа №5 →</button>
     </li> -->
      <li>
        <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/artificial-intelligence/ANN/labs/lab3.html';">← Лабораторная работа №3</button>
      </li>
    </ul>
  </div>
</div>
