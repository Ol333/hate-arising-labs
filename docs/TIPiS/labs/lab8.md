<ol class="breadcrumb">
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}">Главная</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/TIPiS/index.html">ТИПиС</a></li>
  <li class="breadcrumb-item active">ЛР №8</li>
</ol>

<nav>
  <ul></ul>
</nav>

# Исследование избыточности источника информации

___

## Избыточность 

Коэффициент избыточности показывает, какая часть реального сообщения является излишней и могла бы не передаваться, если бы сообщение было организовано оптимально. Коэффициент избыточности выражается формулами: 

$ φ = \frac{n_p - n_0}{n_p} = 1 - \frac{n_0}{n_p} ,$

$ φ = \frac{H_p - H_0}{H_p} = 1 - \frac{H_0}{H_p} ,$

где $n_p$ и $H_p$ - длина и энтропия реального сообщения, $n_0$ и $H_0$ – длина и энтропия оптимального сообщения.

Сообщение будет оптимальным тогда, когда все символы алфавита равновероятны.
Энтропия такого сообщения максимальна и равна $log_2m$, где $m$ – мощность алфавита.

Энтропия реального сообщения при условии независимости символов сообщения вычисляется по формуле:

$ H = - \sum_{i=1}^m p_i \log_2 p_i ,$

где $p_i$ – вероятность появления $i$-го символа. 

Справочно: для русского языка значение реальной энтропии равно 4.36 бит на символ, для английского языка – 4.04, для французского – 3.96, для немецкого – 4.10, для испанского – 3.98.

___

## RLE

Run-length encoding – кодирование длин серий.

Идея – заменяем последовательность одинаковых символов на символ и количество его повторений.

Пример с буквами:

АААААБББССД → 5А3Б2С1Д

Пример с числами (исходник "00000042044448802221" – 20 байт):

<div class="table-responsive">
<table class="table table-bordered">
  <tbody>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>4</td>
    <td>2</td>
    <td>0</td>
    <td>4</td>
    <td>4</td>
    <td>4</td>
    <td>4</td>
    <td>8</td>
    <td>8</td>
    <td>0</td>
    <td>2</td>
    <td>2</td>
    <td>2</td>
    <td>1</td>
  </tbody>
</table>
</div>

↓

<div class="table-responsive">
<table class="table table-bordered">
  <tbody>
    <td>6</td>
    <td>0</td>
    <td>1</td>
    <td>4</td>
    <td>1</td>
    <td>2</td>
    <td>1</td>
    <td>0</td>
    <td>4</td>
    <td>4</td>
    <td>2</td>
    <td>8</td>
    <td>1</td>
    <td>0</td>
    <td>3</td>
    <td>2</td>
    <td>1</td>
    <td>1</td>
  </tbody>
</table>
</div>

Сжалось до 18 байт.

Можно сделать чуть умнее. В байте, уходящем на кодирование количества повторов, первый бит отдать на флаг повтора, а остальные 7 – на количество символов (до 128), к которому этот флаг относится. На предыдущем примере это будет выглядеть так:

<div class="table-responsive">
<table class="table table-bordered">
  <tbody>
    <td>1|6</td>
    <td>0</td>
    <td>0|3</td>
    <td>420</td>
    <td>1|4</td>
    <td>4</td>
    <td>1|2</td>
    <td>8</td>
    <td>0|1</td>
    <td>0</td>
    <td>1|3</td>
    <td>2</td>
    <td>0|1</td>
    <td>1</td>
  </tbody>
</table>
</div>

Получилось сжать до 16 байт.

При этом, можно уменьшить числа, обозначающие количество повторов, для повторов на 2, а для уникальных – на 1:

<div class="table-responsive">
<table class="table table-bordered">
  <tbody>
    <td>1|4</td>
    <td>0</td>
    <td>0|2</td>
    <td>420</td>
    <td>1|2</td>
    <td>4</td>
    <td>1|0</td>
    <td>8</td>
    <td>0|0</td>
    <td>0</td>
    <td>1|1</td>
    <td>2</td>
    <td>0|0</td>
    <td>1</td>
  </tbody>
</table>
</div>

Размер – 16 байт.

___

## Задание

<ol>
  <li>Реализовать алгоритм декодирования файла, сжатого с помощью RLE.</li>
  <li>Раскодировать файл по номеру варианта и записать результат в файл .txt.</li>
  <li>Рассчитать оптимальную энтропию (если бы символы использовались равновероятно) для раскодированного сообщения.
  $ H_0  =n \log_2  m $, где $n$ – количество символов в тексте, $m$ – мощность алфавита.
  </li>
  <li>Экспериментально определить реальную энтропию раскодированного сообщения при условии независимости символов.
  $ H_P  = - \sum_{i=1}^m p_i \log_2 p_i $ , где где $p_i$ – вероятность появления $i$-го символа (или частота символа). 
  </li>
  <li>Рассчитать избыточность раскодированного сообщения при условии независимости символов алфавита.
  $ φ = \frac{H_p -H_0}{H_p} = 1 - \frac{H_0}{H_p}  $
  </li>
  <li>Рассчитать насколько уменьшилась избыточность сообщения в результате кодирования. 
  $ μ = \frac{n_{p1}}{n_p}$, где $n_{p1}$ – размер закодированного файла, $n_p$ – размер раскодированного файла.
  </li>
</ol>

<table class="table table-hover">
   <thead>
     <tr>
       <th scope="col">№ варианта</th>
       <th scope="col">Задача</th>
     </tr>
   </thead>
   <tbody>
     <tr class="table-active">
       <th scope="row">1</th>
       <td><a href="{{ site.baseurl }}/files/TIPiS/rle1.bin">Файл</a></td>
     </tr>
     <tr class="table-primary">
       <th scope="row">2</th>
       <td><a class="link-dark" href="{{ site.baseurl }}/files/TIPiS/rle2.bin">Файл</a></td>
     </tr>
     <tr class="table-active">
       <th scope="row">3</th>
       <td><a href="{{ site.baseurl }}/files/TIPiS/rle3.bin">Файл</a></td>
     </tr>
     <tr class="table-primary">
       <th scope="row">4</th>
       <td><a class="link-dark" href="{{ site.baseurl }}/files/TIPiS/rle4.bin">Файл</a></td>
     </tr>
     <tr class="table-active">
       <th scope="row">5</th>
       <td><a href="{{ site.baseurl }}/files/TIPiS/rle5.bin">Файл</a></td>
     </tr>
     <tr class="table-primary">
       <th scope="row">6</th>
       <td><a class="link-dark" href="{{ site.baseurl }}/files/TIPiS/rle6.bin">Файл</a></td>
     </tr>
     <tr class="table-active">
       <th scope="row">7</th>
       <td><a href="{{ site.baseurl }}/files/TIPiS/rle7.bin">Файл</a></td>
     </tr>
     <tr class="table-primary">
       <th scope="row">8</th>
       <td><a class="link-dark" href="{{ site.baseurl }}/files/TIPiS/rle8.bin">Файл</a></td>
     </tr>
     <tr class="table-active">
       <th scope="row">9</th>
       <td><a href="{{ site.baseurl }}/files/TIPiS/rle9.bin">Файл</a></td>
     </tr>
     <tr class="table-primary">
       <th scope="row">10</th>
       <td><a class="link-dark" href="{{ site.baseurl }}/files/TIPiS/rle10.bin">Файл</a></td>
     </tr>
     <tr class="table-active">
       <th scope="row">11</th>
       <td><a href="{{ site.baseurl }}/files/TIPiS/rle11.bin">Файл</a></td>
     </tr>
     <tr class="table-primary">
       <th scope="row">12</th>
       <td><a class="link-dark" href="{{ site.baseurl }}/files/TIPiS/rle12.bin">Файл</a></td>
     </tr>
    </tbody>
</table>

<br>

<div class="row">
  <div class="col-lg-12">
   <ul class="list-unstyled">
     <li class="float-end">
       <button type="button" class="btn btn-outline-primary" onclick="window.location.href='#исследование-избыточности-источника-информации';">Вверх</button>
     </li>
     <!-- <li  class="float-end">
       <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/TIPiS/labs/lab9.html';">ЛР №9 →</button>
     </li> -->
     <li>
       <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/TIPiS/labs/lab7.html';">← ЛР №7</button>
     </li>
   </ul>
  </div>
</div>