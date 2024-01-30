<ol class="breadcrumb">
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}">Главная</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/artificial-intelligence/index.html">ИИ</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/artificial-intelligence/time-series/index.html">Временные ряды</a></li>
  <li class="breadcrumb-item active">ЛР №1</li>
</ol>

<nav>
  <ul></ul>
</nav>

# Статистический анализ

[Нильсон, Э. Практический анализ временных рядов (2021)](https://vk.com/doc565756056_616232540?hash=qzp7VWbZG3MsVOx1djYaqBAzzkf1IaOOS83a6IqjswT&dl=KT3lOyVMVxRtOI2XnfvtZzZ2OVqYzPUj7YzrmvXcVw0) со стр. 106.

## Задание 1

Скачиваем [датасет](https://github.com/vincentarelbundock/Rdatasets/blob/master/csv/datasets/EuStockMarkets.csv) о ежедневных ценах закрытия четырех основных европейских фондовых индексов, указанных с 1991 по 1998 год.

* Существуют ли в наборе данных взаимосвязанные столбцы?
* Вывести среднее значение изучаемой величины и дисперсию.
* Изменяется ли диапазон доступных значений с изменением временного
периода или другой подвергаемой анализу характеристики?
* Являются ли данные однородными и логически взаимосвязанными или же
предполагают временные изменения в способах измерения или в поведении?
* Построить гистограмму абсолютных значений и гистограмму разностей. Сделать выводы.
* Построить две диаграммы рассеяния: для определения взаимосвязи между ценами двух акций в отдельные моменты времени и для отслеживания их временных изменений.
* Посчитать ковариацию для двух индексов. Вывести ковариационную матрицу.
* Прочитать про ложную корреляцию стр. 135 - 137. Найти и продемонстрировать интересную ложную корреляцию на упомянутом сайте.

# Авторегрессия 

Стационарный временной ряд - это ряд, который характеризуется неизменными во времени статистическими показателями, в частности средним значением и дисперсией.

Имеется ряд $y_n$ и шум (последовательность некоррелирующих и одинаково распределенных случайных величин $\xi_i$ с нулевым средним):

$y_n = F(y_{n-1}, ..., y_{n-m}, \xi_n, ..., \xi_{n-k})$

## Задание 2



# Cкользящее среднее

(сравнить с разными окнами)

## Задание 3

# ARMA

Линейные модели типа ARMA (Auto Regression Moving Average - авторегрессия скользящего среднего):

$y_i = a_0 + \sum_{j=1}^m a_i y_{i-j} + \sum_{j=0}^k b_j \xi_{i-j}$

В качестве прогнозируемой величины обычно используют среднее значение:

$\hat y_i = a_0 + \sum_{j=1}^m a_i y_{i-j}$

Нелинейные модели NARMA:
* параметрические: функция $F(\vec y, \vec \xi, \vec a)$ одна и та же для всех $\vec y$ и $\vec  \xi$. Несколько параметров $\vec a = \{a_1, ..., a_k \}$ находятся по временному ряду.
* непараметрические: набор $\{ \vec y, \vec \xi \}$, в окрестности которого используется локальная аппроксимация.

## Задание 4

<div class="row">
  <div class="col-lg-12">
    <ul class="list-unstyled">
      <li class="float-end">
        <button type="button" class="btn btn-outline-primary" onclick="window.location.href='#keras';">Вверх</button>
      </li>
      <li  class="float-end">
       <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/artificial-intelligence/time-series/labs/lab2.html';">ЛР №2 →</button>
     </li>
      <!-- <li>
        <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/artificial-intelligence/time-series/labs/lab5.html';">← ЛР №5</button>
      </li> -->
    </ul>
  </div>
</div>
