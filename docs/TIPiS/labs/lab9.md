<ol class="breadcrumb">
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}">Главная</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/TIPiS/index.html">ТИПиС</a></li>
  <li class="breadcrumb-item active">ЛР №9</li>
</ol>

<nav>
  <ul></ul>
</nav>

# Алгоритмы шифрования

## Код Хаффмана

Алгоритм для кодирования текста:
1.	Подсчитать частоту появления каждого символа в тексте. 
2.	Построить бинарное дерево, размещая в узлах символы (пошагово объединяя наименее вероятные). 
3.	Пройтись по дереву, сохраняя код для каждого символа.
4.	Закодировать текст. При этом в начале закодированного файла должно лежать дерево/коды символов, позволяющие в дальнейшем его раскодировать.

## LZ77

Идея – замена повторяющихся последовательностей ссылками на те позиции, где они уже встретились, при этом используется скользящее окно (размером в степень двойки).
В закодированном файле будут лежать тройки чисел: **(offset, length, next)**.

Пример

abacabacabadaca (с окном = 5)

<div class="card border-primary mb-2" style="max-width: 20rem;">
  <div class="card-body">
  <img src="{{ site.baseurl }}/img/lz77.svg"
        alt="Синтаксис нотаций"  focusable="false" width="100%"
        class="d-block user-select-none" />
  </div>
</div>


___

## Задание

<ol>
<li>Найти в Интернете текстовый файл, содержащий текст на одном из естественных языков или языке эсперанто. Длина текста – не менее 10 тыс. символов.
</li>
<li>Реализовать один из алгоритмов кодирования (Хаффман или LZ77):
как кодирование, так и декодирование.
После работы в папке с программой и исходным текстовым файлом должен появиться закодированный .bin файл и раскодированный .txt, совпадающий и исходным.
<br><b>Можно воспользоваться готовыми алгоритмами из библиотек, но в этом случае при сдаче придется подробно объяснить, как алгоритм работает. </b>
</li>
<li>Сжать файл. Оценить, на сколько уменьшился его объем: <br>
$ \Delta = (1 - \frac{n_{p1}}{n_p})*100% $,
где $n_{p1}$ – размер закодированного файла, $n_p$ – размер исходного файла.
<br><b>$\Delta$ должна быть $> 0$.</b>
</li>
</ol>

<div class="row">
  <div class="col-lg-12">
   <ul class="list-unstyled">
     <li class="float-end">
       <button type="button" class="btn btn-outline-primary" onclick="window.location.href='#алгоритмы-шифрования';">Вверх</button>
     </li>
     <!-- <li  class="float-end">
       <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/TIPiS/labs/lab10.html';">ЛР №10 →</button>
     </li> -->
     <li>
       <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/TIPiS/labs/lab8.html';">← ЛР №8</button>
     </li>
   </ul>
  </div>
</div>