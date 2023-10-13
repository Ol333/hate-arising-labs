<ol class="breadcrumb">
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}">Главная</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/artificial-intelligence/index.html">ИИ</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/artificial-intelligence/ANN/index.html">ИНС</a></li>
  <li class="breadcrumb-item active">ЛР №3</li>
</ol>

<nav>
  <ul></ul>
</nav>

# Обратное распространение ошибки

**Читаем** cтр. 219 – 241 у [Хайкина](https://palchevsky.ru/uploads/books/1.pdf){:target="_blank"}.

Или кратко стр. 241 – 243.

## Алгоритм:

<ul>
<li>
<b>Инициализация.</b>
Генерируем небольшие случайные веса.
</li>
<li>
<b>Предъявление примеров обучения.</b>
В сеть подаются образцы из обучающего множества (эпохи).
</li>
<li>
<b>Прямой проход.</b>
Вычисляем по слоям выходы нейронов. Сигнал до активации будет:
<br>
$ v_i^k = \sum_{i=0}^m ω_{ij}^k y_{ij}^{k-1}$,
<br>Выходной сигнал будет равен:<br>
$ y_{ij}^{k} = f_i(v_i^k)$, <a id="eq_1">(1)</a>
<br>
где $k$ – номер слоя, $i$ – номер нейрона в слое, $j$ – номер синаптической связи от нейрона предыдущего слоя, $f_i$ – функция активации i-го нейрона, $m$ – количество нейронов в слое, $y_{ij}^{k-1}$ – выходной сигнал $i$-го нейрона на предыдущем слое $k-1$.
<br>Если нейрон находится в первом скрытом слое, то для него выходы предыдущего слоя – входы $x$.
<br>Вычисляем ошибку:
<br>
$ e_i^{k} = Y_i - y_i^K$, <a id="eq_2">(2)</a>
<br>
где $k$ – номер слоя, $i$ – номер нейрона в выходном слое, $m$ – количество слоев, $ Y_i$ – ожидаемый выходной сигнал $i$-го нейрона.
</li>
<li>
<b>Обратный проход.</b>
Вычисляем локальные градиенты узлов сети:
<br>
$\delta_i^k = f'_i(v_i^k) \sum_{q=0}^m (\delta_q^{t+1} \delta_{qi}^{t+1}) $,	<a id="eq_3">(3)</a>
<br>где $f'_i()$ – дифференцирование по аргументу
<br>Изменяем веса сети:
<br>
$ω_{ij}^k(n+1) = ω_{ij}^k(n) + α (\delta_i^k y_i^{k-1} ) $,	<a id="eq_4">(4)</a>
<br>где $α$ – параметр скорости обучения.
</li>
<li>
<b>Итерации.</b>
Если не достигнут критерий останова, возвращаемся к п.2.
</li>
</ul>

# Задание

Изменить код однослойной сети (2-й лабораторной), добавив слои.

Реализовать обратное распространение ошибки.

Протестировать на [наборе данных]().

При сдаче работы ответить на вопросы.

<div class="row">
  <div class="col-lg-12">
    <ul class="list-unstyled">
      <li class="float-end">
        <button type="button" class="btn btn-outline-primary" onclick="window.location.href='#обратное-распространение-ошибки';">Вверх</button>
      </li>
      <li  class="float-end">
       <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/artificial-intelligence/ANN/labs/lab4.html';">Лабораторная работа №4 →</button>
     </li>
      <li>
        <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/artificial-intelligence/ANN/labs/lab2.html';">← Лабораторная работа №2</button>
      </li>
    </ul>
  </div>
</div>
