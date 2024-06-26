<ol class="breadcrumb">
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}">Главная</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/artificial-intelligence/index.html">ИИ</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/artificial-intelligence/ANN/index.html">ИНС</a></li>
  <li class="breadcrumb-item active">ЛР №7</li>
</ol>

<nav>
  <ul></ul>
</nav>

# Рекуррентная сеть

Базовая архитектура - *полностью рекуррентная сеть* (fully recurrent neural network - FRNN).

<div class="card border-primary mb-2" style="max-width: 15rem;">
  <div class="card-body">
    <img src="{{ site.baseurl }}/img/RNN_0.svg"
        alt="RNN" focusable="false" width="100%"
        class="d-block user-select-none" />
  </div>
</div>

Здесь $x$ - входные данные, $y$ - выходные данные, $h$ - скрытое состояние, которое рассчитывается на основе предыдущего скрытого состояния и входных данных.

В развернутом виде один шаг по времени будет выглядеть так:

<div class="card border-primary mb-2" style="max-width: 30rem;">
  <div class="card-body">
    <img src="{{ site.baseurl }}/img/RNN_1.svg"
        alt="RNN" focusable="false" width="100%"
        class="d-block user-select-none" />
  </div>
</div>

Здесь $t$ - текущий момент времени, $t-1$ - предыдущий момент времени.

Три набора весов - матрицы

* $W$ размера $k$ на $n$, связывает $x_t$ и $h_t$;
* $U$ размера k на k, связывает $h_{t-1}$ и $h_t$;
* $V$ размера m на k, связывает $h_t$ и $y_t$;

и два смещения - вектор-столбцы:

* $b_h$ размера h, добавляется при расчете $h_t$;
* $b_y$ размера m, добавляется при расчете $y_t$.

Итого, работа FRNN описывается следующими уравнениями:

$ h_t = \tanh(Wx_t + Uh_{t-1} + b_h) $

$ y_t = Vh_t + b_y $

Чтобы реализовать прямое распространение нужно еще только в нулевой момент времени объявить вектор $h$ и заполнить его нулями.

### Backward pass

В случаем бинарной классификации удобно использовать функцию потерь перекрестной энтропии, как [здесь](https://python-scripts.com/recurrent-neural-network).

$L = -\ln(p_c)$

Предыдущий рисунок в компактном виде:

<div class="card border-primary mb-2" style="max-width: 20rem;">
  <div class="card-body">
    <img src="{{ site.baseurl }}/img/RNN_2.svg"
        alt="RNN" focusable="false" width="100%"
        class="d-block user-select-none" />
  </div>
</div>

Заметим, что $y^1$ и $y^2$ никак не используются в простейшем случае, поэтому не будем их учитывать при расчете ошибки.

BPTT (Packpropagation Through Time) из [Хайкин](https://palchevsky.ru/uploads/books/1.pdf){:target="_blank"} 942/1101:

Пусть множество данных, используемое для обучения реккурентной сети, разбито на независимые эпохи, каждая из которых представляет интересующий отрезок времени. Пусть $n_0$ - время начала эпохи; $n_1$ - время ее окончания. Рассматривая такую эпоху, можно определить следующую функцию стоимости:

$ E_{общ.}(n_0,n_1) = \frac12 \sum_{n=n_0}^{n_1} \sum_{j \in A} e_j^2(n) $

где $A$ - множество индексов $j$, относящееся к тем нейронам сети, для которых определены желаемые отклики; $e_j(n)$ - сигнал ошибки на выходе этих нейронов, измеренный по отношению к некоторому желаемому отклику. Требуется вычислить чувствительность этой сети, т.е. частные производные функции стоимости $E_{общ.}(n_0,n_1)$ по синаптическим весам сети.

Алгоритм обучения по эпохам:

* Сначала осуществляется прямая передача данных по сети на интервале времени $(n_0, n_1)$. Для записи входных данных состояние сети (т.е. ее синаптические веса) и желаемый отклик для этого интервала времени *сохраняются*.

* Для вычисления значений локальных градиентов выполняется единичная обратная передача через последнюю запись:

$ \delta_j(n) = - \frac{\partial E_{общ.}(n_0, n_1)}{\partial v_j(n)} $

для всех $ j \in A $ и $n_0 < n \le n_1 $. Это вычисление выполняется с помощью формулы

<div class="table-responsive">
$ \delta_j(n) = \begin{cases}
  	\phi '(v_j(n)) e_j(n), & n = n_1 \\
  	\phi '(v_j(n)) [e_j(n) + \sum_{k \in A}w_{jk}\delta_k(n+1)], & n_0 < n \le n_1
  \end{cases}$ <a id="eq_1" class="float-end">(1)</a>
</div>

где $\phi \'(\cdot)$ - производная функции активации по своему агрументу; $v_j(n)$ - сигнала нейрона $j$ до применения функции активации. Предполагается, что все нейроны сети имеют одну и ту же функцию активации $\phi \'(\cdot)$. Вычисления [(1)](#eq_1) повторяются с момента времени $n_1$, шаг за шагом, пока не будет достигнут момент $n_0$. Количество выполняемых шагов равно количеству шагов времени в данной эпохе.

* После выполнения вычислений по методу обратного распростанения до момента времени $n_0+1$ к синаптическим весам $w_{ji}$ нейрона $j$ применяется следующая коррекция:

<div class="table-responsive">
$ \Delta w_{ji} = -\eta \frac{\partial E_{общ.}(n_0, n_1)}{\partial w_{ji}} = \eta \sum_{n=n_0+1}^{n_1} \delta_j(n)x_i(n-1)$
</div>

где $\eta$ - параметр скорости обучения; $x_i(n-1)$ - входной сигнал, поданный на $i$-й синапс $j$-го нейрона в момент времени $n-1$.


### Обучение

Особенность подготовки данных для рекуррентных сетей в том, что мы работаем с последовательностями.
Поэтому порядок следования элементов в наборе данных важен: вместо выдергивания элементов со случайных позиций, в данном случае, мы выделяем для обучающего и тестового набора последовательные непересекающиеся связные наборы (в простейшем виде, первые 70% записей в обучающую выборку, последние 30% - тестовую).

## Задание 1

* Создать однослойную реккуррентную сеть своими руками.
* Найти и подготовить данные.
* Обучить сеть и решить задачу.

# Keras готовые блоки

Популярные рекуррентные сети уже реализованы в библиотеке Keras:

**Сеть с долговременной и кратковременной памятью (LSTM)**. Сеть состоит из нескольких ячеек, в которых собраны рекуррентные слои и вентили (gate), обеспечивающие механизм "забывания".

**Управляемый рекуррентный блок (GRU)**. Упрощенная версия предыдущей идеи, облегчающая обучение, но обладающая чуть меньшими возможностями.

**Двунаправленные рекуррентные нейронные сети (biRNN)**. Объединяет разнонаправленные слои (например, LSTM, GRU), что обеспечивает учет не только предыдущих элементов последовательности, но и последующих.

## Задание 2

* Создать рекуррентную сеть с помощью keras.
* Решить с помощью нее задачу.
* Знать принцип работы.

# Keras возможности для расширения

Не столь популярные рекуррентные сети не реализованы, но есть все возможности, чтобы их доделать до необходимого.

## Задание 3

* Дособрать сеть из того, что представлено в keras. Или воспользоваться TensorFlow, Theano и проч.
* Решить задачу.
* Знать принцип работы сети.

<div class="table-responsive">
<table class="table table-hover border-primary table-bordered ">
  <thead>
    <tr class="table-dark">
      <th scope="col">№ варианта</th>
      <th scope="col">1. Задача</th>
      <th scope="col">2. Тип сети</th>
      <th scope="col">2. Задача</th>
      <th scope="col">3. Тип сети</th>
      <th scope="col">3. Задача</th>
    </tr>
  </thead>
  <tbody>
  <tr>
      <th scope="row">1</th>
      <td>-</td>
      <td>GRU</td>
      <td>Генерация тестовых отзывов</td>
      <td>seq2seq</td>
      <td>Генерация аннотации по тексту научной статьи<a class="link-dark" href="https://cyberleninka.ru/" target="_blank">*</a> (можно заголовка по аннотации)<a class="link-dark" href="https://www.kaggle.com/datasets/Cornell-University/arxiv" target="_blank">*</a></td>
    </tr>
    <tr>
      <th scope="row">2</th>
      <td>Предсказание 4-го слова по контексту из первых трех</td>
      <td>LSTM</td>
      <td>Генерация похожей музыки<a class="link-dark" href="https://www.kaggle.com/datasets/ac0hik/moroccan-music-data" target="_blank">*</a></td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <th scope="row">3</th>
      <td>-</td>
      <td>biRNN</td>
      <td>Перевод текста с английского на русский<a class="link-dark" href="https://www.kaggle.com/datasets/rexhaif/rus-eng-bible" target="_blank">*</a></td>
      <td>Сеть Хопфилда</td>
      <td>Запомнить несколько изображений и восстанавливать их искаженные фрагменты</td>
    </tr>
    <tr>
      <th scope="row">4</th>
      <td>Предсказание 4-го кадра анимации по трем предыдущим</td>
      <td>LSTM</td>
      <td>Бинарная классификация текстовых отзывов на рестораны</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <th scope="row">5</th>
      <td>-</td>
      <td>GRU</td>
      <td>Бинарная классификация текстовых отзывов на фильмы</td>
      <td>Сеть Элмана</td>
      <td>Классификация изображений с наложенными фильтрами (в тестовом наборе)</td>
    </tr>
    <tr>
      <th scope="row">6</th>
      <td>Предсказание 4-го значения температуры по трем предыдущим</td>
      <td>biRNN</td>
      <td>Перевод текста с русского на английский<a class="link-dark" href="https://www.kaggle.com/datasets/rexhaif/rus-eng-bible" target="_blank">*</a></td>
      <td>-</td>
      <td>-</td>
    </tr>
  </tbody>
</table>
</div>

\* - примеры датасетов. По желанию можете найти самостоятельно.




<div class="row">
  <div class="col-lg-12">
    <ul class="list-unstyled">
      <li class="float-end">
        <button type="button" class="btn btn-outline-primary" onclick="window.location.href='#рекуррентная-сеть';">Вверх</button>
      </li>
      <li  class="float-end">
       <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/artificial-intelligence/ANN/labs/lab8.html';">ЛР №8 →</button>
     </li>
      <li>
        <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/artificial-intelligence/ANN/labs/lab6.html';">← ЛР №6</button>
      </li>
    </ul>
  </div>
</div>
