<ol class="breadcrumb">
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}">Главная</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/icpc/index.html">Спортивное программирование</a></li>
  <li class="breadcrumb-item active">Сортировки</li>
</ol>

# Сортировки

Сортировка — упорядочивание набора однотипных данных по
возрастанию или убыванию.
Цель сортировки — облегчить последующий поиск элементов в
таком отсортированном массиве.

Прямые методы сортировки можно разбить на:
* сортитровки с помощью включения;
* сортировки с помощью выбора;
* сортировки с помощью обмена.

# Сортировка вставками

<div class="card border-primary mb-2" style="max-width: 20rem;">
  <div class="card-body">
  <img src="{{baseurl}}/img/vkluch2.png"
        focusable="false" width="100%"
        class="d-block user-select-none" />
  </div>
</div>

# Сортировка с помощью выбора

<div class="card border-primary mb-2" style="max-width: 20rem;">
  <div class="card-body">
  <img src="{{baseurl}}/img/vibor1.png"
        focusable="false" width="100%"
        class="d-block user-select-none" />
  </div>
</div>

# Сортировка с помощью обмена, пузырьковая сортировка
(bubble sort)

<div class="card border-primary mb-2" style="max-width: 20rem;">
  <div class="card-body">
  <img src="{{baseurl}}/img/puzir2.png"
        focusable="false" width="100%"
        class="d-block user-select-none" />
  </div>
</div>

# Шейкерная сортировка (shaker sort)

<div class="card border-primary mb-2" style="max-width: 20rem;">
  <div class="card-body">
  <img src="{{baseurl}}/img/sheicer1.png"
        focusable="false" width="100%"
        class="d-block user-select-none" />
  </div>
</div>

# <a id="quick_sort">Быстрая сортировка</a>

Метод сортировки (QuickSort) с разделением или быстрая сортировка.

<div class="card border-primary mb-2" style="max-width: 20rem;">
  <div class="card-body">
  <img src="{{baseurl}}/img/bistro.png"
        focusable="false" width="100%"
        class="d-block user-select-none" />
  </div>
</div>

# Слияние (merge sort)

<div class="card border-primary mb-2" style="max-width: 20rem;">
  <div class="card-body">
  <img src="{{baseurl}}/img/sli.png"
        focusable="false" width="100%"
        class="d-block user-select-none" />
  </div>
</div>

# Сортировка деревом (tree sort)

<div class="card border-primary mb-2" style="max-width: 20rem;">
  <div class="card-body">
  <img src="{{baseurl}}/img/tree2.png"
        focusable="false" width="100%"
        class="d-block user-select-none" />
  </div>
</div>

# Пирамидальная сортировка (англ. Heapsort) или сортировка кучей

<div class="card border-primary mb-2" style="max-width: 20rem;">
  <div class="card-body">
  <img src="{{baseurl}}/img/pira0.2.png"
        focusable="false" width="100%"
        class="d-block user-select-none" />
  </div>
</div>

# J-сортировка (JSort)

<div class="card border-primary mb-2" style="max-width: 20rem;">
  <div class="card-body">
  <img src="{{baseurl}}/img/jsort.png"
        focusable="false" width="100%"
        class="d-block user-select-none" />
  </div>
</div>

# Поразрядная сортировка или цифровая сортировка (radix sort)

<div class="card border-primary mb-2" style="max-width: 20rem;">
  <div class="card-body">
  <img src="{{baseurl}}/img/por.png"
        focusable="false" width="100%"
        class="d-block user-select-none" />
  </div>
</div>

# Сравнение

Простые алгоритмы

<table border="1">
<tbody>
<tr>
  <td>название</td>
  <td>сложность</td>
  <td>кол-во сравнений<br>
  min/avg/max</td>
  <td>кол-во перестановок<br>
  min/avg/max</td>
  <td><a href="sl.html#us">устойчивость</a></td>
  <td>достоинства</td>
  <td>недостатки</td>
</tr>
<tr>
  <td>включение</td>
  <td>O(n<sup>2</sup>)</td>
  <td>
  <table border="1" width="100%">
  <tbody>
  <tr>
  <td>n-1</td>
  <td>(n<sup>2</sup>+n-2)/4</td>
  <td>(n<sup>2</sup>-n)/2</td>
  </tr>
  </tbody>
  </table>
  </td>
  <td>
  <table border="1" width="100%">
  <tbody>
  <tr>
  <td>2(n-1)</td>
  <td>(n<sup>2</sup>+9n-10)/4</td>
  <td>(n<sup>2</sup>+3n-4)/2</td>
  </tr>
  </tbody>
  </table>
  </td>
  <td>устойчив</td>
  <td>прост в реализации, эффективен на малых массивах,
  упорядоченных массивах</td>
  <td>долго работает на больших массивах</td>
</tr>
  <tr>
  <td>выбор</td>
  <td>O(n<sup>2</sup>)</td>
  <td>
  <table border="1" width="100%">
  <tbody>
  <tr>
  <td>(n<sup>2</sup>-n)/2</td>
  <td>(n<sup>2</sup>-n)/2</td>
  <td>(n<sup>2</sup>-n)/2</td>
  </tr>
  </tbody>
  </table>
  </td>
  <td>
  <table border="1" width="100%">
  <tbody>
  <tr>
  <td>3(n-1)</td>
  <td>n(ln n +0,57)</td>
  <td>n<sup>2</sup>/4+3(n-1)</td>
  </tr>
  </tbody>
  </table>
  </td>
  <td>устойчив</td>
  <td>прост в реализации, эффективен на малых массивах,
  упорядоченных массивах, наименьшее число перестановок</td>
  <td>долго работает на больших массивах</td>
</tr>
<tr>
  <td>обмен</td>
  <td>O(n<sup>2</sup>)</td>
  <td>
  <table border="1" width="100%">
  <tbody>
  <tr>
  <td>(n<sup>2</sup>-n)/2</td>
  <td>(n<sup>2</sup>-n)/2</td>
  <td>(n<sup>2</sup>-n)/2</td>
  </tr>
  </tbody>
  </table>
  </td>
  <td>
  <table border="1" width="100%">
  <tbody>
  <tr>
  <td>0</td>
  <td>(n<sup>2</sup>-n)*1,5</td>
  <td>(n<sup>2</sup>-n)/4</td>
  </tr>
  </tbody>
  </table>
  </td>
  <td>устойчив</td>
  <td>прост в реализации, эффективен на малых массивах,
  упорядоченных массивах</td>
  <td>долго работает на больших массивах</td>
</tr>
</tbody>
</table>

Сложные алгоритмы

<table class="table table-hover">
<thead>
<tr>
  <th scope="col">Название</th>
  <th scope="col">Сложность</th>
  <th scope="col">Доп. память</th>
  <th scope="col">Устойчивость</th>
  <th scope="col">Достоинства</th>
  <th scope="col">Недостатки</th>
</tr>
</thead>
<tbody>
<tr class="table-active">
  <th scope="row">Шейкерная</th>
  <td>O(n<sup>2</sup>)</td>
  <td>O(1)</td>
  <td>устойчив</td>
  <td>быстрее сортировки пузырьком</td>
  <td>все равно долго работает</td>
</tr>
<tr class="table-primary">
  <th scope="row">Быстрая</th>
  <td>O(n log n)</td>
  <td>O(log n)</td>
  <td>неустойчив (используя O(n) дополнительной
  памяти, можно сделать сортировку устойчивой)</td>
  <td>один из самых быстродействующих алгоритмов</td>
  <td>плохо работает при неудачных данных</td>
</tr>
<tr class="table-active">
  <th scope="row">Пирамидальная</th>
  <td>O(n log n)</td>
  <td>O(1)</td>
  <td>неустойчив</td>
  <td>стабильность метода</td>
  <td>сложен в реализации, на почти отсортированных
  массивах работает столь же долго, как и на
  хаотических данных</td>
</tr>
<tr class="table-primary">
  <th scope="row">J-сортировка</th>
  <td>O(3n)/O(n<sup>2</sup>)</td>
  <td>O(1)</td>
  <td>неустойчив</td>
  <td>хорошо работает на малых массивах</td>
  <td>чем длиннее массив, тем дольше работает
  сортировка вставками</td>
</tr>
<tr class="table-active">
  <th scope="row">Слиянием</th>
  <td>O(n log n)</td>
  <td>O(n)</td>
  <td>устойчив</td>
  <td>Не имеет «трудных» входных данных</td>
  <td>На «почти отсортированных» массивах работает
  столь же долго, как на хаотичных</td>
</tr>
<tr class="table-primary">
  <th scope="row">Дерево</th>
  <td>O(n log n)</td>
  <td>O(n)</td>
  <td>неустойчив</td>
  <td>один из быстродействующих алгоритмов</td>
  <td>плохо работает при неудачных данных</td>
</tr>
<tr class="table-active">
  <th scope="row">Поразрядная</th>
  <td>O(nk)</td>
  <td>O(k)</td>
  <td>LSD-устойчив<br>
  MSD-неустойчив</td>
  <td>не основана на сравнениях</td>
  <td>узкая специализация</td>
</tr>
</tbody>
</table>

Вот данные, полученные в результате тестов с тысячью элементов массива:

<table class="MsoNormalTable" style="border: medium none ; border-collapse: collapse; top: 1230px; left: 232px; width: 879px; height: 311px;" border="1" cellpadding="0" cellspacing="0">
<tbody>
<tr style="height: 44.3pt;">
<td style="border: 1pt solid windowtext; padding: 0cm 5.4pt; width: 112.2pt; height: 44.3pt;" valign="top" width="150">
<p class="MsoNormal">1тыс. элементов</p>
<p class="MsoNormal"></p>
<p class="MsoNormal">миллисекунды<o:p></o:p></p>
</td>
<td style="border-style: solid solid solid none; border-color: windowtext windowtext windowtext -moz-use-text-color; border-width: 1pt 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 44.3pt;" valign="top" width="150">
<p class="MsoNormal">отсортирован<o:p></o:p></p>
<p class="MsoNormal">по возрастанию<o:p></o:p></p>
</td>
<td style="border-style: solid solid solid none; border-color: windowtext windowtext windowtext -moz-use-text-color; border-width: 1pt 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 44.3pt;" valign="top" width="150">
<p class="MsoNormal">случайный <o:p></o:p></p>
<p class="MsoNormal">порядок<o:p></o:p></p>
</td>
<td style="border-style: solid solid solid none; border-color: windowtext windowtext windowtext -moz-use-text-color; border-width: 1pt 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 44.3pt;" valign="top" width="150">
<p class="MsoNormal">отсортирован<o:p></o:p></p>
<p class="MsoNormal">по убыванию<o:p></o:p></p>
</td>
</tr>
<tr style="height: 15.6pt;">
<td colspan="4" style="border-style: none solid solid; border-color: -moz-use-text-color windowtext windowtext; border-width: medium 1pt 1pt; padding: 0cm 5.4pt; width: 448.8pt; height: 15.6pt;" valign="top" width="598">
<p class="MsoNormal" style="text-align: center;" align="center">простые<o:p></o:p></p>
</td>
</tr>
<tr style="height: 14.7pt;">
<td style="border-style: none solid solid; border-color: -moz-use-text-color windowtext windowtext; border-width: medium 1pt 1pt; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal">включение<o:p></o:p></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">003<o:p></o:p></span></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">003<o:p></o:p></span></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">007<o:p></o:p></span></p>
</td>
</tr>
<tr style="height: 14.7pt;">
<td style="border-style: none solid solid; border-color: -moz-use-text-color windowtext windowtext; border-width: medium 1pt 1pt; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal">выбор<o:p></o:p></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">003<o:p></o:p></span></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">003<o:p></o:p></span></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">003<o:p></o:p></span></p>
</td>
</tr>
<tr style="height: 14.7pt;">
<td style="border-style: none solid solid; border-color: -moz-use-text-color windowtext windowtext; border-width: medium 1pt 1pt; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal">обмен<o:p></o:p></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">004<o:p></o:p></span></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">009<o:p></o:p></span></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">011<o:p></o:p></span></p>
</td>
</tr>
<tr style="height: 14.7pt;">
<td colspan="4" style="border-style: none solid solid; border-color: -moz-use-text-color windowtext windowtext; border-width: medium 1pt 1pt; padding: 0cm 5.4pt; width: 448.8pt; height: 14.7pt;" valign="top" width="598">
<p class="MsoNormal" style="text-align: center;" align="center">сложные<o:p></o:p></p>
</td>
</tr>
<tr style="height: 14.7pt;">
<td style="border-style: none solid solid; border-color: -moz-use-text-color windowtext windowtext; border-width: medium 1pt 1pt; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal">шейкерная<o:p></o:p></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">005<o:p></o:p></span></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">009<o:p></o:p></span></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">012<o:p></o:p></span></p>
</td>
</tr>
<tr style="height: 14.7pt;">
<td style="border-style: none solid solid; border-color: -moz-use-text-color windowtext windowtext; border-width: medium 1pt 1pt; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal">быстрая<o:p></o:p></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">001<o:p></o:p></span></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">001<o:p></o:p></span></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">001<o:p></o:p></span></p>
</td>
</tr>
<tr style="height: 14.7pt;">
<td style="border-style: none solid solid; border-color: -moz-use-text-color windowtext windowtext; border-width: medium 1pt 1pt; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal">пирамидальная<o:p></o:p></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">002<o:p></o:p></span></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">002<o:p></o:p></span></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">002<o:p></o:p></span></p>
</td>
</tr>
<tr style="height: 14.7pt;">
<td style="border-style: none solid solid; border-color: -moz-use-text-color windowtext windowtext; border-width: medium 1pt 1pt; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">j-</span>сортировка<o:p></o:p></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">002<o:p></o:p></span></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">002<o:p></o:p></span></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">002<o:p></o:p></span></p>
</td>
</tr>
<tr style="height: 14.7pt;">
<td style="border-style: none solid solid; border-color: -moz-use-text-color windowtext windowtext; border-width: medium 1pt 1pt; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal">слиянием<o:p></o:p></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">002<o:p></o:p></span></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">002<o:p></o:p></span></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">002<o:p></o:p></span></p>
</td>
</tr>
<tr style="height: 14.7pt;">
<td style="border-style: none solid solid; border-color: -moz-use-text-color windowtext windowtext; border-width: medium 1pt 1pt; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal">дерево<o:p></o:p></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">002<o:p></o:p></span></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">002<o:p></o:p></span></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">002<o:p></o:p></span></p>
</td>
</tr>
<tr style="height: 15.6pt;">
<td style="border-style: none solid solid; border-color: -moz-use-text-color windowtext windowtext; border-width: medium 1pt 1pt; padding: 0cm 5.4pt; width: 112.2pt; height: 15.6pt;" valign="top" width="150">
<p class="MsoNormal">порязрядная<o:p></o:p></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 15.6pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">002<o:p></o:p></span></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 15.6pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">002<o:p></o:p></span></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 15.6pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">002<o:p></o:p></span></p>
</td>
</tr>
</tbody>
</table>

И с сотней тысяч элементов (миллион элементов сортируется простым методом более часа).

<table class="MsoNormalTable" style="border: medium none ; border-collapse: collapse; left: 232px; width: 877px;" border="1" cellpadding="0" cellspacing="0">
<tbody>
<tr style="height: 44.3pt;">
<td style="border: 1pt solid windowtext; padding: 0cm 5.4pt; width: 112.2pt; height: 44.3pt;" valign="top" width="150">
<p class="MsoNormal">1<span style="" lang="EN-US">00</span>тыс. элементов</p>
<p class="MsoNormal">мин:сек:мсек</p>
<p class="MsoNormal"></p>
</td>
<td style="border-style: solid solid solid none; border-color: windowtext windowtext windowtext -moz-use-text-color; border-width: 1pt 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 44.3pt;" valign="top" width="150">
<p class="MsoNormal">отсортирован<o:p></o:p></p>
<p class="MsoNormal">по возрастанию<o:p></o:p></p>
</td>
<td style="border-style: solid solid solid none; border-color: windowtext windowtext windowtext -moz-use-text-color; border-width: 1pt 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 44.3pt;" valign="top" width="150">
<p class="MsoNormal">случайный <o:p></o:p></p>
<p class="MsoNormal">порядок<o:p></o:p></p>
</td>
<td style="border-style: solid solid solid none; border-color: windowtext windowtext windowtext -moz-use-text-color; border-width: 1pt 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 44.3pt;" valign="top" width="150">
<p class="MsoNormal">отсортирован<o:p></o:p></p>
<p class="MsoNormal">по убыванию<o:p></o:p></p>
</td>
</tr>
<tr style="height: 15.6pt;">
<td colspan="4" style="border-style: none solid solid; border-color: -moz-use-text-color windowtext windowtext; border-width: medium 1pt 1pt; padding: 0cm 5.4pt; width: 448.8pt; height: 15.6pt;" valign="top" width="598">
<p class="MsoNormal" style="text-align: center;" align="center">простые<o:p></o:p></p>
</td>
</tr>
<tr style="height: 14.7pt;">
<td style="border-style: none solid solid; border-color: -moz-use-text-color windowtext windowtext; border-width: medium 1pt 1pt; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal">включение<o:p></o:p></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">39:783<o:p></o:p></span></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">34:078<o:p></o:p></span></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">1:03:885<o:p></o:p></span></p>
</td>
</tr>
<tr style="height: 14.7pt;">
<td style="border-style: none solid solid; border-color: -moz-use-text-color windowtext windowtext; border-width: medium 1pt 1pt; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal">выбор<o:p></o:p></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">39:719<o:p></o:p></span></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">39:786<o:p></o:p></span></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">40:903<o:p></o:p></span></p>
</td>
</tr>
<tr style="height: 14.7pt;">
<td style="border-style: none solid solid; border-color: -moz-use-text-color windowtext windowtext; border-width: medium 1pt 1pt; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal">обмен<o:p></o:p></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">40:856<o:p></o:p></span></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">1:36:197<o:p></o:p></span></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal">1<span style="" lang="EN-US">:47:388<o:p></o:p></span></p>
</td>
</tr>
<tr style="height: 14.7pt;">
<td colspan="4" style="border-style: none solid solid; border-color: -moz-use-text-color windowtext windowtext; border-width: medium 1pt 1pt; padding: 0cm 5.4pt; width: 448.8pt; height: 14.7pt;" valign="top" width="598">
<p class="MsoNormal" style="text-align: center;" align="center">сложные<o:p></o:p></p>
</td>
</tr>
<tr style="height: 14.7pt;">
<td style="border-style: none solid solid; border-color: -moz-use-text-color windowtext windowtext; border-width: medium 1pt 1pt; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal">шейкерная<o:p></o:p></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">40:995<o:p></o:p></span></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">1:25:540<o:p></o:p></span></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">1:44:262<o:p></o:p></span></p>
</td>
</tr>
<tr style="height: 14.7pt;">
<td style="border-style: none solid solid; border-color: -moz-use-text-color windowtext windowtext; border-width: medium 1pt 1pt; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal">быстрая<o:p></o:p></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">012<o:p></o:p></span></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">029<o:p></o:p></span></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">012<o:p></o:p></span></p>
</td>
</tr>
<tr style="height: 14.7pt;">
<td style="border-style: none solid solid; border-color: -moz-use-text-color windowtext windowtext; border-width: medium 1pt 1pt; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal">пирамидальная<o:p></o:p></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">063<o:p></o:p></span></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">068<o:p></o:p></span></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">058<o:p></o:p></span></p>
</td>
</tr>
<tr style="height: 14.7pt;">
<td style="border-style: none solid solid; border-color: -moz-use-text-color windowtext windowtext; border-width: medium 1pt 1pt; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">j-</span>сортировка<o:p></o:p></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">065<o:p></o:p></span></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">067<o:p></o:p></span></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">063<o:p></o:p></span></p>
</td>
</tr>
<tr style="height: 14.7pt;">
<td style="border-style: none solid solid; border-color: -moz-use-text-color windowtext windowtext; border-width: medium 1pt 1pt; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal">слиянием<o:p></o:p></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">1:157<o:p></o:p></span></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">1:208<o:p></o:p></span></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">1:178<o:p></o:p></span></p>
</td>
</tr>
<tr style="height: 14.7pt;">
<td style="border-style: none solid solid; border-color: -moz-use-text-color windowtext windowtext; border-width: medium 1pt 1pt; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal">дерево<o:p></o:p></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">063<o:p></o:p></span></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">065<o:p></o:p></span></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 14.7pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">060<o:p></o:p></span></p>
</td>
</tr>
<tr style="height: 15.6pt;">
<td style="border-style: none solid solid; border-color: -moz-use-text-color windowtext windowtext; border-width: medium 1pt 1pt; padding: 0cm 5.4pt; width: 112.2pt; height: 15.6pt;" valign="top" width="150">
<p class="MsoNormal">порязрядная<o:p></o:p></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 15.6pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">055<o:p></o:p></span></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 15.6pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">053<o:p></o:p></span></p>
</td>
<td style="border-style: none solid solid none; border-color: -moz-use-text-color windowtext windowtext -moz-use-text-color; border-width: medium 1pt 1pt medium; padding: 0cm 5.4pt; width: 112.2pt; height: 15.6pt;" valign="top" width="150">
<p class="MsoNormal"><span style="" lang="EN-US">058<o:p></o:p></span></p>
</td>
</tr>
</tbody>
</table>
