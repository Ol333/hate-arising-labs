<ol class="breadcrumb">
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}">Главная</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/artificial-intelligence/index.html">ИИ</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/artificial-intelligence/time-series/index.html">Временные ряды</a></li>
  <li class="breadcrumb-item active">ЛР №2</li>
</ol>

<nav>
  <ul></ul>
</nav>

# Свёртка

Операцию свёртки можно интерпретировать как «схожесть» одной функции с отражённой и сдвинутой копией другой. 

$ w(t)=\int_{\tau =0}^{t} f(\tau )g(t-\tau )d\tau $

В дискретном случае свёртка соответствует сумме значений $f$ с коэффициентами, соответствующими смещённым значениям $g$, то есть 

$ (f*g) (x) = f(1) g(x-1) + f(2) g(x-2) + f(3) g(x-3) + \dots $


## Задание 1

<ol>
<li>
Реализовать по формуле выше свёртку двух ступенчатых сигналов:

$f(x) = \begin{cases}
  	1, & если \, 0 < x < 1 \\\\
  	0, & иначе
  \end{cases}$

Построить график.
</li>
<li>
То же самое, но с использованием готовых библиотек.
</li>
</ol>

# Взаимнокорреляционная функция

В общем случае, для непрерывных функций $f(t)$ и $g(t)$ взаимная корреляция определяется как

$ (f \star g)(t) \overset{def}= \int_{- \infty}^{+ \infty} f^*(\tau) g(t+\tau) d\tau $

где верхний индекс в виде звёздочки означает комплексное сопряжение.

Взаимная корреляция двух рядов $f$ и $g$ определяется по формуле:

$ (f \star g)_i \overset{def}= \sum_j f_j^* g _{i+j} $

где $i$ - сдвиг между последовательностями относительно друг друга.

## Задание 2

* Выбрать 5 функций из [учебника](https://go.11klasov.net/7805-spravochnik-po-matematicheskim-formulam-i-grafikam-funkcij-dlja-studentov-starkov-sn.html){:target="_blank"}. **Ваши функции не должны повторяться внутри подгруппы.**
* Для каждой пары функций из набора построить график, содержащий две функции и их взаимнокорреляционную функцию.



<div class="row">
  <div class="col-lg-12">
    <ul class="list-unstyled">
      <li class="float-end">
        <button type="button" class="btn btn-outline-primary" onclick="window.location.href='#свёртка';">Вверх</button>
      </li>
      <li  class="float-end">
       <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/artificial-intelligence/time-series/labs/lab3.html';">ЛР №3 →</button>
     </li>
      <li>
        <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/artificial-intelligence/time-series/labs/lab1.html';">← ЛР №1</button>
      </li>
    </ul>
  </div>
</div>
