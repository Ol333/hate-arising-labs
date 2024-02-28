<ol class="breadcrumb">
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}">Главная</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/artificial-intelligence/index.html">ИИ</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/artificial-intelligence/ANN/index.html">ИНС</a></li>
  <li class="breadcrumb-item active">ЛР №6</li>
</ol>

<nav>
  <ul></ul>
</nav>

# Свертка

[Цифровая обработка изображений](https://vk.com/doc252264187_555814746?hash=pW7MVoAWCVC99RlZlMuyp95ZQPz6IJfpR1gMNrESxJc&dl=VKBY1ZInOSdIgCQPPHPEvGcZd0nfVty0rVwE5GO5RzL) со стр. 188.

Свёртка задается уравнением:

$ w(x,y) \star f(x,y) = \sum_{s=-a}^a \sum_{t=-b}^b w(s,t)f(x-s,y-t) $

где $f(x,y)$ - фрагмент изображения (x,y - координаты, f - цвет), $w(x,y)$ - ядро свертки.

## Задание 1

* Найти черно-белое изображение (цвет должен кодироваться одним числом). **Изображения не должны повторяться в подгруппе.**

* Представить изображение в виде массива `numpy`. Расширить границы нулями.

* Реализовать свертку с ядрами 3x3:
  * заполненным нулями;
  * заполненным единицами;
  * заполненным произвольными значениями.

* Реализовать пулинг ядром 2x2 с функцией по вариантам.

# Сверточная сеть в Keras

Читать [Шолле](https://codernet.ru/books/python/glubokoe_obuchenie_na_python_sholle_fransua/){:target="_blank"} 5 глава со стр. 148.

## Задание 2

* Загрузить подготовленные [данные](https://disk.yandex.ru/d/Y3jZx0DtF9F78g){:target="_blank"}. Данные представляют собой png изображения размером 640x480. В 6 папках сгруппированны графики функций, формулы которых приведены в таблице ниже. 

* По вариантам обучить нейронную сеть, которая осуществляет задачу бинарной классификации графиков функций. Ваш вариант - функция, которую нейросеть должна научиться узнавать. Все остальные функции должны классифицироваться как "не ваша функция".

* [Памятка]({{ site.baseurl }}/artificial-intelligence/ANN/compendium.html) для тех, кто забыл, как работать с нейронными сетями.

* Для тестовой выборки сохранить результаты работы модели в виде исходных изображений с подписями настоящего класса и определенного вашей нейронкой.

<div class="table-responsive">
<table class="table table-hover">
  <thead>
    <tr>
      <th scope="col">№ варианта</th>
      <th scope="col">1. Формула</th>
      <th scope="col">2. Искомый класс</th>
    </tr>
  </thead>
  <tbody>
    <tr class="table-active">
      <th scope="row">1</th>
      <td>$max()$</td>
      <td>$y=ax^2+bx+c, a > 0, b, c \in R$</td>
    </tr>
    <tr class="table-primary">
      <th scope="row">2</th>
      <td>$min()$</td>
      <td>$y=ax^3+bx^2+cx+d, a < 0, b, c, d \in R$</td>
    </tr>
    <tr class="table-active">
      <th scope="row">3</th>
      <td>$np.average()$</td>
      <td>$y = \frac{k}{x-a}+b, a,b \in R, r > 0$</td>
    </tr>
    <tr class="table-primary">
      <th scope="row">4</th>
      <td>$np.linalg.norm()$ - L2</td>
      <td>$y=c* |x-k| + b, k,b \in R, c > 0$</td>
    </tr>
    <tr class="table-active">
      <th scope="row">5</th>
      <td>$sum()$</td>
      <td>$y = \frac{k}{|x-a| - c}+b, a,b \in R, k < 0, c < 0$</td>
    </tr>
    <tr class="table-primary">
      <th scope="row">6</th>
      <td>$np.median()$</td>
      <td>$y=k |x-b| + ax + c, k < 0, a > 0, b,c \in R$</td>
    </tr>
  </tbody>
</table>
</div>



<div class="row">
  <div class="col-lg-12">
    <ul class="list-unstyled">
      <li class="float-end">
        <button type="button" class="btn btn-outline-primary" onclick="window.location.href='#свертка';">Вверх</button>
      </li>
      <li  class="float-end">
       <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/artificial-intelligence/ANN/labs/lab7.html';">ЛР №7 →</button>
     </li>
      <li>
        <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/artificial-intelligence/ANN/labs/lab5.html';">← ЛР №5</button>
      </li>
    </ul>
  </div>
</div>
