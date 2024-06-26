<ol class="breadcrumb">
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}">Главная</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/artificial-intelligence/index.html">ИИ</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/artificial-intelligence/time-series/index.html">Временные ряды</a></li>
  <li class="breadcrumb-item active">ЛР №8</li>
</ol>

<nav>
  <ul></ul>
</nav>


# Динамические системы

[Лоскутов А.Ю. Анализ временных рядов. Курс лекций (2009)](https://chaos.phys.msu.ru/loskutov/PDF/Lectures_time_series_analysis.pdf){:target="_blank"}

Статистические методы обработки временных рядов предполагают, что изучаемый ряд стохастический. Это не всегда верно. Помимо случайных процессов, описываемых статистикой и теорией вероятности, существует хаос.
Обычно критерием отличия хаотических систем является **не**устойчивость к малым возмущениям.

*Сосредоточенные* системы, с которыми мы обычно работаем, имеют конечное число степеней свободы (система автоматического управления температурой котла) и для них мы можем использовать уравнения/модели. Трудности - вычислительные, состоят в нахождении значений показателей для подстановки в известные формулы.

Фазовое пространство *распределенных* систем (атмосфера), которых в природе большинство, является **бесконечномерным**. Большинство таких систем диссипативны: с течением времени все фазовые траектории стягиваются к некоторому подмножеству исходно бесконечномерного пространства. Как правило, это подмножество конечномерно и описывается каким-то конечным набором переменных. Следовательно, рассматривая это подмножество, можно изучить динамику исходной системы.

Наименьшее число независимых переменных, однозначно определяющих установившееся движение исходной диссипативной распределенной системы, называют **размерностью вложения** и обозначают $d_e$ (от embedding).

Подмножество, к которому стягиваются траектории системы, - это **аттрактор** (attract - притягивать).

**Точка бифуркации**, точка в фазовом пространстве, от которой могут исходить несколько решений (устойчивых и неустойчивых).

___

При анализе временных рядов главной задачей является реконструкция породившей этот ряд динамической системы.

В соответствии с теорией Такенса–Мане приемлемое описание фазового пространства динамической системы можно получить, если взять вместо реальных переменных системы (которые могут быть неизвестны вообще!) $k$–мерные векторы задержек, составленные из значений ряда в последовательные моменты времени.

При выполнении условия $k >= 2 d_e + 1$, где $d_e$ - размерность вложения, возможно реконструировать фазовое пространство системы.
При условии *стационарности* временного ряда на базе этой реконструкции
строится прогноз его дальнейшей динамики.

Методы определения $k$:
* Алгоритм Грассбергера-Прокаччиа.
* функциональный метод.

В рамках нелинейной динамики были разработаны практические методики:
* сингулярный спектральный анализ (SSA), который является глобальным методом;
* многоканальный анализ сингулярного спектра (MSSA), как расширенная форма SSA;
* локальная аппроксимация (LA);
* сочетание SSA–LA.


## Задание

* Сделать предсказание для сигнала из [ЛР5]({{ site.baseurl }}/artificial-intelligence/time-series/labs/lab5.html){:target="_blank"} одним из методов выше (методы не должны повторяться в подгруппе).


<div class="row">
  <div class="col-lg-12">
    <ul class="list-unstyled">
      <li class="float-end">
        <button type="button" class="btn btn-outline-primary" onclick="window.location.href='#динамические-системы';">Вверх</button>
      </li>
      <!-- <li  class="float-end">
       <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/artificial-intelligence/time-series/labs/lab9.html';">ЛР №9 →</button>
     </li> -->
      <li>
        <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/artificial-intelligence/time-series/labs/lab7.html';">← ЛР №7</button>
      </li>
    </ul>
  </div>
</div>
