<ol class="breadcrumb">
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}">Главная</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/artificial-intelligence/index.html">ИИ</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/artificial-intelligence/ANN/index.html">ИНС</a></li>
  <li class="breadcrumb-item active">ЛР №1</li>
</ol>

<nav>
  <ul></ul>
</nav>

# Модель нейрона

Нейрон представляет собой единицу обработки информации в нейронной сети.

<div class="card border-primary mb-2" style="max-width: 30rem;">
  <div class="card-body">
  <img src="https://www.evkova.org/evkovaupload/job/113206/1.png"
        alt="Модель нейрона"  focusable="false" width="100%"
        class="d-block user-select-none" />
  </div>
</div>

Выше показана модель нейрона, лежащего в основе искусственных нейронных сетей. В этой модели можно выделить три основных элемента:

1. Набор **синапсов (*synapse*)** или **связей (*connecting link*)**, каждый из которых характеризуется своим **весом (*weight*)** или **силой (*strength*)**. В частности, сигнал $x_j$ на входе синапса $j$, связанного с нейроном $k$, умножается на вес $w_{kj}$. Важно обратить внимание на то, в каком порядке указаны индексы синаптического веса $w_{kj}$.Первый индекс относится к рассматриваемому нейрону, а второй – ко входному окончанию синапса, с которым связан данный вес. В отличие от синапсов мозга синаптический вес искусственного нейрона может иметь как положительные, так и отрицательные значения.
2. **Сумматор (*adder*)** складывает входные сигналы, взвешенные относительно соответствующих синапсов нейрона. Эту операцию можно описать как линейную комбинацию.
3. **Функция активации (*activation function*)** ограничивает амплитуду выходного сигнала нейрона. Эта функция также называется **функцией сжатия (*squashing function*)**. Обычно нормализованный диапазон амплитуд выхода нейрона лежит в интервале $[0, 1]$ или $[-1, 1]$.

В представленную модель нейрона включен **пороговый элемент (*bias*)**, который обозначен символом $b_k$. Эта величина отражает увеличение или уменьшение входного сигнала, подаваемого на функцию активации.

В математическом представлении функционирование нейрона $k$ можно описать следующей парой уравнений:

$u_k = \sum_{j=1}^m w_{kj} x_j$ <a id="eq_1" class="float-end">(1)</a>

$y_k=φ(u_k+b_k)$ <a id="eq_2" class="float-end">(2)</a>

### Типы функций активаций
Функции активации, представленные в формулах как $φ(v)$, определяют выходной сигнал нейрона в зависимости от индуцированного локального поля $v$. Можно выделить три основных типа функций активации.
<ol>
  <li><b>Функция единичного скачка</b>, или <b>пороговая функция (<i>threshold function</i>)</b>. Этот тип функции описывается следующим образом:

    $φ(v) = \begin{cases}
      1, & если \, v ≥ 0 \\\\
      0, & если \, v < 0
    \end{cases}$

  </li>
  <li><b>Кусочно-линейная функция (<i>piecewise-linear function</i>)</b>. Описывается следующим выражением:

  $φ(v) = \begin{cases}
    1, & если \, v≥ + \frac 12 \\\\
    |v|, & если \, -\frac 12 < v < +\frac 12 \\\\
    0, & если \, v ≤ -\frac 12
  \end{cases}$

  </li>
  <li><b>Сигмоидальная функция (<i>sigmoid function</i>)</b>. График напоминает букву S, функция является, пожалуй, самой распространенной функцией, используемой для создания искусственных нейроных сетей. Примером сигмоидальной функции может служить логистическая функция, задаваемая следующим выражением:

  $φ(v) = \frac{1}{1+exp⁡(-av)}$

  где $a$ – параметр наклона сигмоидальной функции.
  </li>
</ol>

## Задание

Реализовать искусственный нейрон описанный формулами [(1)](#eq_1) и [(2)](#eq_2) **в виде класса**.
Используя пороговую функцию активации, подобрать **веса ($w_{kj}$)** нейрона для решения задачи по варианту.

<div class="table-responsive">
<table class="table table-hover border-primary  table-bordered">
  <thead>
    <tr class="table-dark">
      <th scope="col">Вариант</th>
      <th scope="col">Входные данные</th>
      <th scope="col">Выходные данные</th>
      <th scope="col">Название булевой функции</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">1</th>
      <td>0 0 <br> 0 1 <br> 1 0 <br> 1 1</td>
      <td>0 <br> 0 <br> 0 <br> 1</td>
      <td>Коньюнкция</td>
    </tr>
    <tr>
      <th scope="row">2</th>
      <td>0 0 <br> 0 1 <br> 1 0 <br> 1 1</td>
      <td>1 <br> 0 <br> 1 <br> 1</td>
      <td>Обратная импликация</td>
    </tr>
    <tr>
      <th scope="row">3</th>
      <td>0 0 <br> 0 1 <br> 1 0 <br> 1 1</td>
      <td>1 <br> 1 <br> 0 <br> 1</td>
      <td>Импликация</td>
    </tr>
    <tr>
      <th scope="row">4</th>
      <td>0 0 <br> 0 1 <br> 1 0 <br> 1 1</td>
      <td>0 <br> 0 <br> 1 <br> 0</td>
      <td>Инверсия прямой импликации</td>
    </tr>
    <tr>
      <th scope="row">5</th>
      <td>0 0 <br> 0 1 <br> 1 0 <br> 1 1</td>
      <td>1 <br> 0 <br> 0 <br> 0</td>
      <td>Стрелка Пирса</td>
    </tr>
    <tr>
      <th scope="row">6</th>
      <td>0 0 <br> 0 1 <br> 1 0 <br> 1 1</td>
      <td>1 <br> 1 <br> 1 <br> 0</td>
      <td>Штрих Шеффера</td>
    </tr>
  </tbody>
</table>
</div>


## Пример
Дизъюнкция:

0 0 1 1 $x_1$     ($\overrightarrow{w_{11}=1}$)

$\,\,\,\,\,\,\,\,\,\,\,\,φ(v) = \begin{cases} 1 & если \, x>0 \\\\\\\\ 0 & если \, x≤0 \end{cases}\,\,\overrightarrow{w_{21}=1}\,\,$   y = 0 1 1 1

0 1 0 1 $x_2$      ($\overrightarrow{w_{12}=1}$)


 <div class="row">
   <div class="col-lg-12">
     <ul class="list-unstyled">
       <li class="float-end">
         <button type="button" class="btn btn-outline-primary" onclick="window.location.href='#модель-нейрона';">Вверх</button>
       </li>
       <li   class="float-end">
         <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/artificial-intelligence/ANN/labs/lab2.html';">ЛР №2 →</button>
       </li>
     </ul>
   </div>
 </div>