<ol class="breadcrumb">
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}">Главная</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/artificial-intelligence/index.html">ИИ</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/artificial-intelligence/pattern-recognition/index.html">Распознавание образов</a></li>
  <li class="breadcrumb-item active">ЛР №2</li>
</ol>

<nav>
  <ul></ul>
</nav>


# Опознание объекта. Обнаружение объекта

Классифицировать объект на изображении относительно легко с помощью сверточной сети.
Но на реальных неподготовленных изображениях сначала нужно выделить область, в которой расположен объект. [Задача нахождения объектов на изображении (ИТМО)](https://neerc.ifmo.ru/wiki/index.php?title=%D0%97%D0%B0%D0%B4%D0%B0%D1%87%D0%B0_%D0%BD%D0%B0%D1%85%D0%BE%D0%B6%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F_%D0%BE%D0%B1%D1%8A%D0%B5%D0%BA%D1%82%D0%BE%D0%B2_%D0%BD%D0%B0_%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B8).

Одним из первых успешных подходов, примененных для определения нахождения объекта на изображении, был R-CNN (Region Convolution Neural Network)[*](https://habr.com/ru/companies/jetinfosystems/articles/498294/){:target="_blank"}. В общих чертах: определяется набор гипотез, они сворачиваются и классифицируются.

**Ограничивающая рамка (bounding box)** – координаты, ограничивающие определенную область изображения, – чаще всего в форме прямоугольника. Может быть представлена 4 координатами в двух форматах: центрированный $(c_{x},c_{y},w,h)$ и обычный $(x_{min},y_{min},x_{max},y_{max})$.

**Гипотеза (Proposal)**, P – определенный регион изображения (заданный с помощью ограничивающей рамки), в котором, предположительно, находится объект.

**IoU (Intersection-over-Union)** – метрика степени пересечения между двумя ограничивающими рамками.


Поиск гипотез - регионов, в которых может находиться объект, можно осуществлять разными методами[*](https://learnopencv.com/selective-search-for-object-detection-cpp-python/){:target="_blank"} (object proposal / region proposal methods):

* Sliding window - вырезаем из изображения все возможные прямоугольники (и по позиции, и по размеру).
* Region proposal:
  1. Objectness - используем меру объектности (отличие от окружения и наличие замкнутой границы), количественно определяющую вероятность того, что окно будет содержать объект.
  2. Constrained Parametric Min-Cuts for Automatic Object Segmentation - снизу-вверх на регулярной сетке изображения генерируются гипотезы, которые ранжируются по правдоподобности.
  3. Category Independent Object Proposals - на основе иерархической сегментации, вычисленной по границам окклюзии, собирается начальный набор регионов. Для пар регионов вычисляются вероятности принадлежности одному объекту. Затем происходит ранжирование и оставляются лучшие разнообразные варианты на основе комбинации оценки внешнего вида объекта и штрафа IoU.
  4. Randomized Prim - сегментируем изображение на суперпиксели, а затем увеличиваем группы суперпикселей при высокой вероятности принадлежности одному объекту.
  5. Selective Search - выделяем области похожих по яркости пискелей, а затем объединяем близкие области (по цвету, текстуре, размеру и форме), под конец получая области, в которых с высокой вероятностью есть объекты.


### Таблица

Оценка работы метода обнаружения объекта рассчитывается как $Accuracy = \frac{TP+TN}{P+N}$.

<div class="table-responsive">
<table class="table table-hover border-primary table-bordered">
  <thead>
    <tr>
      <td></td>
      <td></td>
      <th scope="col" colspan="2" class="table-dark">Predicted condition</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td>Total population = P + N</td>
      <td class="table-primary">Positive (PP)</td>
      <td class="table-primary">Negative (PN)</td>
    </tr>
    <tr>
      <td rowspan="2" class="table-dark">Actual condition</td>
      <td class="table-primary">Positive (P)</td>
      <td>True positive (TP), hit</td>
      <td>False negative (FN), miss, underestimation</td>
    </tr>
    <tr>
      <td class="table-primary">Negative (N)</td>
      <td>False positive (FP), false alarm, overestimation</td>
      <td>True negative (TN), correct rejection</td>
    </tr>
   </tbody>
</table>
</div>

## Задание 👾

* Необходимо осуществить поиск гипотез по варианту одним из способов:
  * запустить код авторов метода;
  * реализовать метод самостоятельно.
* Для классификации можно использовать (найти/реализовать):
  * R-CNN модель;
  * CNN + классификацию.
* Подготовить набор из 10 картинок или взять [этот](https://disk.yandex.ru/d/aj4nMMZrYYtGZQ){:target="_blank"}. *На изображениях должен быть один и больше искомых объектов, в примере - это кот.*
* Для каждого из изображений:
  1. Запустить поиск гипотез по варианту. Вывести количество гипотез, предлагаемых для дальнейшей классификации (*Positive*). Если ваш метод отсеивает гипотезы на основе каких-то эвристик, то отсеянные гипотезы будут *Negative*.
  2. Осуществить классификацию гипотез. *Классификатор определяет: присутствует ли на изображении объект искомого класса. Можно найти обученный, можно обучить на любом наборе с Kaggle.* (*True Positive* - если объект нашелся, *False Positive* - иначе.)
  3. Посчитать и вывести количество гипотез по всем ячейкам [таблицы](#таблица) + Accuracy.


<div class="table-responsive">
<table class="table table-hover border-primary  table-bordered ">
  <thead>
    <tr class="table-dark">
      <th scope="col">№ варианта</th>
      <th scope="col">Задача</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">1</th>
      <td>Sliding window</td>
    </tr>
    <tr>
      <th scope="row">2</th>
      <td><a href="https://calvin-vision.net/bigstuff/objectness/"  target="_blank">Objectness</a></td>
    </tr>
    <tr>
      <th scope="row">3</th>
      <td>PMC: Automatic Object Segmentation Using
Constrained Parametric Min-Cuts (<a href="https://www.cs.jhu.edu/~ayuille/JHUcourses/VisionAsBayesianInference2022/10/CPMC_Carreira_PAMI_2012.pdf"  target="_blank">статья</a>, <a href="https://github.com/m1ha1f/cpmc"  target="_blank">код</a>)</td>
    </tr>
    <tr>
      <th scope="row">4</th>
      <td><a href="https://vision.cs.uiuc.edu/proposals/" target="_blank">Category Independent Object Proposals</a></td>
    </tr>
    <tr>
      <th scope="row">5</th>
      <td><a href="https://github.com/smanenfr/rp#rp" target="_blank">Prime Object Proposals with Randomized Prim's Algorithm (RP)</a></td>
    </tr>
    <tr>
      <th scope="row">6</th>
      <td><a href="https://www.koen.me/research/selectivesearch/"  target="_blank">Selective Search</a></td>
    </tr>
   </tbody>
</table>
</div>

<div class="row">
  <div class="col-lg-12">
    <ul class="list-unstyled">
      <li class="float-end">
        <button type="button" class="btn btn-outline-primary" onclick="window.location.href='#опознание-объекта-обнаружение-объекта';">Вверх</button>
      </li>
      <li  class="float-end">
       <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/artificial-intelligence/pattern-recognition/labs/lab3.html';">ЛР №3 →</button>
     </li>
      <li>
        <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/artificial-intelligence/pattern-recognition/labs/lab1.html';">← ЛР №1</button>
      </li>
    </ul>
  </div>
</div>