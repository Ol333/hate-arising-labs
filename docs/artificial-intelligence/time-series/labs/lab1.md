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

[Нильсон, Э. Практический анализ временных рядов (2021)](https://vk.com/doc565756056_616232540?hash=qzp7VWbZG3MsVOx1djYaqBAzzkf1IaOOS83a6IqjswT&dl=KT3lOyVMVxRtOI2XnfvtZzZ2OVqYzPUj7YzrmvXcVw0){:target="_blank"} со стр. 106.

## Задание 1

Скачиваем [датасет](https://github.com/vincentarelbundock/Rdatasets/blob/master/csv/datasets/EuStockMarkets.csv){:target="_blank"} о ежедневных ценах закрытия четырех основных европейских фондовых индексов, указанных с 1991 по 1998 год.

* Существуют ли в наборе данных взаимосвязанные столбцы?
* Вывести среднее значение изучаемой величины и дисперсию.
* Изменяется ли диапазон доступных значений с изменением временного
периода или другой подвергаемой анализу характеристики?
* Являются ли данные однородными и логически взаимосвязанными или же
предполагают временные изменения в способах измерения или в поведении?
* Построить гистограмму абсолютных значений и гистограмму разностей. Сделать выводы.
* Построить две диаграммы рассеяния: для определения взаимосвязи между ценами двух акций в отдельные моменты времени и для отслеживания их временных изменений.
* Посчитать ковариацию для двух индексов. Вывести граффик ковариационной матрицы.
* Прочитать про ложную корреляцию стр. 135 - 137. Найти и продемонстрировать интересную ложную корреляцию на упомянутом сайте.

# Авторегрессия 

**Стационарный временной ряд** характеризуется неизменными во времени статистическими показателями, в частности средним значением и дисперсией.

Его можно представить в виде ряда $X_n$ и шума (последовательности некоррелирующих и одинаково распределенных случайных величин $\varepsilon_i$ с нулевым средним):

$X_t = F(X_{t-1}, ..., X_{t-p}, \varepsilon_t, ..., \varepsilon_{t-k})$

В **авторегрессионной модели** (AR) значения временного ряда в данный момент линейно зависят от предыдущих $p$ значений этого же ряда:

$X_t = a_0 + \sum_{i=1}^p a_t X_{t-i} + \varepsilon_t $

## Задание 2

* Найти стационарный ряд в [этих данных](https://archive.ics.uci.edu/dataset/360/air+quality){:target="_blank"}. Или привести ряд к стационарному.
* Использовать модель авторегрессии (AR) для предсказания следующих значений ряда (могу порекомендовать использовать библиотеку `statsmodels`):
  * Определить лаг с помощью графика частичной автокорреляционной функции.
  * Создать и обучить модель AR.
  * Построить график.

# Cкользящее среднее

**Cкользящее среднее** - функция, значения которой в каждой точке равно некоторому среднему значению исходной функции за предыдущий период.

**Модель скользящего среднего** (Moving Average - MA) предназначена для описания процессов, в которых значение в каждой отдельной временной точке является функцией недавних компонентов "ошибок", каждая из которых не зависит от других:

$X_t = \sum_{i=0}^q b_i \varepsilon_{t-i}$


## Задание 3

* Использовать тот же временной ряд, что и в предыдущем задании. Апроксимировать функцию скользящим средним с окнами 3, 5, 10, 50. Построить график.
* Построить график предсказания с помощью модели скользящего среднего (MA).

# ARMA

Линейные модели типа ARMA (Auto Regression Moving Average - авторегрессия скользящего среднего):

$X_t = a_0 + \sum_{i=1}^p a_t X_{t-i} + \sum_{i=0}^q b_i \varepsilon_{t-i}$

## Задание 4

* Используя модель авторегрессии скользящего среднего (ARMA) или ее интегрированного варианта (ARIMA) сделать предсказание.
* По вариантам реализовать одну из задач построения или предсказания $n$ значений временного ряда **самостоятельно** *(не используя для этого готовые высокоуровневые библиотеки)*.

<table class="table table-hover">
  <thead>
    <tr>
      <th scope="col">№ варианта</th>
      <th scope="col">Реализовать</th>
    </tr>
  </thead>
  <tbody>
    <tr class="table-active">
      <th scope="row">1</th>
      <td>Построение модели AR(p)</td>
    </tr>
    <tr class="table-primary">
      <th scope="row">2</th>
      <td>Предсказание моделью AR(p)</td>
    </tr>
    <tr class="table-active">
      <th scope="row">3</th>
      <td>Построение модели MA(q)</td>
    </tr>
    <tr class="table-primary">
      <th scope="row">4</th>
      <td>Предсказание моделью MA(q)</td>
    </tr>
    <tr class="table-active">
      <th scope="row">5</th>
      <td>Построение модели ARMA(p,q)</td>
    </tr>
    <tr class="table-primary">
      <th scope="row">6</th>
      <td>Предсказание моделью ARMA(p,q)</td>
    </tr>
  </tbody>
</table>

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
