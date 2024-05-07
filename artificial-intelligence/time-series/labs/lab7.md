<ol class="breadcrumb">
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}">Главная</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/artificial-intelligence/index.html">ИИ</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/artificial-intelligence/time-series/index.html">Временные ряды</a></li>
  <li class="breadcrumb-item active">ЛР №7</li>
</ol>

<nav>
  <ul></ul>
</nav>


# Вейвлет-преобразование

[Астафьева Н. М. Вейвлет-анализ: основы теории и примеры применения](https://www.mathnet.ru/php/archive.phtml?wshow=paper&jrnid=ufn&paperid=1260&option_lang=rus){:target="_blank"} :

Вейвлет - "маленькая волна".
Вейвлет-преобразование одномерного сигнала состоит в его разложении по базису, сконструированному из обладающей определенными свойствами солитоноподобной функции (вейвлета), посредством масштабных преобразований и переносов.

Вейвлет-преобразование обеспечивает двумерную развертку (в отличие от одномерной преобразования Фурье) исследуемого одномерного сигнала, при этом частота ($a$) и координата ($b$) рассматриваются как независимые переменные.

Простейший пример ортогонального вейвлета - HAAR-вейвлет, определяемый соотношением

$ \psi^H(t) = \begin{cases}
  	1, & 0 \le t < 1/2 \\\\\\\\
    -1, & 1/2 \le t < 1 \\\\\\\\
  	0, & t < 0, t \ge 1.
  \end{cases} $

[ещё формулы](https://habrastorage.org/webt/il/en/mn/ilenmnay4yq-grlce3q3puycguc.png){:target="_blank"}

Признаки вейвлета: локализация, нулевое среднее, ограниченность, автомодальность базиса.

Вейвлет-преобразование - это интегральное преобразование, представляющее собой свертку вейвлет-функции с сигналом.

### Непрерывное вейвлет-преобразование

Прямое вейвлет-преобразование сигнала $f(t)$:

$ W_f(a,b) = \vert a \vert ^{-1/2} \int_{-\infty}^{\infty} f(t) \psi^* (\frac{t-b}{a}) dt $

Если для порождающего вейвлета $\psi (t)$ выполняется равенство $ C_{\psi} = \int_{-\infty}^{\infty} \frac{\vert \Psi(\Omega) \vert ^2}{\Omega} d \Omega < \infty $, то возможно обратное преобразование:

$ f(t) = \frac{1}{C_{\psi}} \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} W_f(a,b) \psi_{ab}(t) \frac{da db}{a^2} .$

Здесь $\Psi(\Omega)$ - преобразование Фурье функции $\psi(t)$ .

Вейвлет-преобразование может быть записано также через образы Фурье сигнала $\widehat f(w)$ и вейвлета $\widehat \psi (w)$. 

В результате вейвлет-преобразования комплексного одномерного сигнала получаются двуменые массивы значений модуля коэффициентов и фазы: $ W(a,b) = \vert W(a,b) \vert exp [i \Phi (a,b)] $

Спектр $W(a,b)$ однмерного сигнала представляет собой поверхность в трехмерном пространстве.
Ее можно представить в виде проекции на плоскость $ab$ с изолиниями или изоуровнями или картину линий локальных экстремумов этих поверхностей ("sceleton").

### Дискретное вейвлет-преобразование

При исследовании сигналов полезно их представление в виде совокупности последовательных приближений грубой (аппроксимирующей) $A_{j_0}(t)$ и уточненной (детализирующей) $D_j(t)$ составляющих:

$f(t) = A_{j_0}(t) + \sum_{j=1}^{j_0} D_j(t)$

с последующим их уточнением итерационным методом. Каждый
шаг уточнения соответствует определенному масштабу, то есть
уровню $j_0$ анализа (декомпозиции) и синтеза (реконструкции)
сигнала.

Коэффициенты аппроксимации (`cA`) представляют выход фильтра нижних частот  (фильтра усреднения) [DWT](https://pywavelets.readthedocs.io/en/latest/ref/dwt-discrete-wavelet-transform.html){:target="_blank"}. Коэффициенты детализации (`cD`) представляют  выход фильтра высоких частот (разностного фильтра) DWT.


<div class="card border-primary mb-2" style="max-width: 30rem;">
  <div class="card-body">
    <img src="https://masters.donntu.ru/2005/kita/stoyanovsky/diss/photo11.gif"
        alt="Банк фильтров"  focusable="false" width="100%"
        class="d-block user-select-none" />
  </div>
</div>

DWT всегда реализуется как банк фильтров в виде каскада высокочастотных и низкочастотных фильтров. Банки фильтров являются очень эффективным способом разделения сигнала на несколько частотных поддиапазонов.

На первом этапе с малым масштабом анализируется высокочастотное поведение сигнала. На втором этапе шкала увеличивается с коэффициентом два (частота уменьшается с коэффициентом два), и мы анализируем поведение около половины максимальной частоты. На третьем этапе масштабный фактор равен четырем, и мы анализируем частотное поведение около четверти максимальной частоты. И это продолжается до тех пор, пока мы не достигнем максимального уровня разложения.



## Задание 1

* Построить график произвольной функции из `pywt.data`.
* Построить скейлограмму.
* Построить трехмерную поверхность двухпараметрического спектра $W(a,b)$. Как [здесь](https://habr.com/ru/articles/449646/).
* Построить плоскость $ab$ с цветовыми областями вейвлет-преобразования.
* Построить сечения вейвлет-спектра $W(a,b)$ по нескольким произвольным значениям $a$ и $b$.
* Построить скелетон - линии локальных экстремумов.


## Задание 2

* Добавить к сигналу из [ЛР5]({{ site.baseurl }}/artificial-intelligence/time-series/labs/lab5.html){:target="_blank"} белый гауссовский шум с нулевым математическим ожиданием и произвольно выбранной дисперсией.
* Вычисление прямого дискретного вейвлет-преобразования с пошаговым выводом графиков коеффициентов (что-то [такое](https://www.wolfram.com/mathematica/new-in-8/wavelet-analysis/HTMLImages.ru/lifting-wavelet-transform-(lwt)/O_10.png){:target="_blank"}).
* Вычисление обратного дискретного вейвлет-преобразования.
* Сравнение исходного сигнала (без шума) с сигналом, прошедшим через фильтр. $MSE = \frac{1}{N} \sum_{k=0}^{N-1} (f(k) - \widehat f(k))^2 $, где $f(k)$ - эталонный сигнал, $\widehat f(k)$ - восстановленный сигнал.

* Поменять вейвлет на произвольный неуказанный в вариантах и повторить все пункты выше.



<div class="table-responsive">
<table class="table table-hover border-primary">
   <thead>
     <tr class="table-dark">
       <th scope="col">№ варианта</th>
       <th scope="col">Вейвлет</th>
       <th scope="col">Название в PyWavelets</th>
     </tr>
   </thead>
   <tbody>
     <tr>
       <th scope="row">1</th>
       <td>Gaussian</td>
       <td>"gausP", где P - число от 1 до 8</td>
     </tr>
     <tr>
       <th scope="row">2</th>
       <td>Haar</td>
       <td>"haar"</td>
     </tr>
     <tr>
       <th scope="row">3</th>
       <td>Complex Gaussian</td>
       <td>"cgauP", где P - число от 1 до 8</td>
     </tr>
     <tr>
       <th scope="row">4</th>
       <td>Morlet</td>
       <td>"morl"</td>
     </tr>
     <tr>
       <th scope="row">5</th>
       <td>MHAT</td>
       <td>"mexh"</td>
     </tr>
     <tr>
       <th scope="row">6</th>
       <td>Shannon</td>
       <td>"shanB-C", где вещественные числа B - ширина полосы, C - центральная частота</td>
     </tr>
    </tbody>
</table>
</div>

<div class="row">
  <div class="col-lg-12">
    <ul class="list-unstyled">
      <li class="float-end">
        <button type="button" class="btn btn-outline-primary" onclick="window.location.href='#keras';">Вверх</button>
      </li>
      <li  class="float-end">
       <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/artificial-intelligence/time-series/labs/lab8.html';">(доп.) ЛР №8 →</button>
     </li>
      <li>
        <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/artificial-intelligence/time-series/labs/lab6.html';">← ЛР №6</button>
      </li>
    </ul>
  </div>
</div>
