<ol class="breadcrumb">
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}">Главная</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/artificial-intelligence/index.html">ИИ</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/artificial-intelligence/time-series/index.html">Временные ряды</a></li>
  <li class="breadcrumb-item active">ЛР №3</li>
</ol>

# Необычные временные ряды

Имеются данные, предсталенные в виде текстового файла.
В нем есть 5 колонок, содержащих информацию об изменении сердечного ритма во время прослушивания определенного типа музыки:

<div class="table-responsive">
<table class="table table-bordered">
  <tbody>
    <tr>
      <td>Ничего</td>
      <td>Агрессивная</td>
      <td>Белый шум</td>
      <td>Классическая</td>
      <td>Ритмичная</td>
    </tr>
    <tr>
      <td>..</td>
      <td>..</td>
      <td>..</td>
      <td>..</td>
      <td>..</td>
    </tr>
  </tbody>
</table>
</div>

Числовые значения - это интервалы времени между ударами сердца в мс. Показания регистрировались в течении, приблизительно, 5 мин.

Удар сердца можете принять за условную 1, отсутствие удара за 0. 

## Задание

Преобразовать данные во временной ряд и визуализировать.


<div class="table-responsive">
<table class="table table-hover border-primary table-bordered">
   <thead>
     <tr>
       <th scope="col">№ варианта</th>
       <th scope="col">Данные</th>
     </tr>
   </thead>
   <tbody>
     <tr>
       <th scope="row">1</th>
       <td><a href="https://disk.yandex.ru/d/gx5pmlWUvQJTkw" target="_blank">Файл</a></td>
     </tr>
     <tr>
       <th scope="row">2</th>
       <td><a class="link-dark" href="https://disk.yandex.ru/d/P2rpxR0wvdC5gg" target="_blank">Файл</a></td>
     </tr>
     <tr>
       <th scope="row">3</th>
       <td><a href="https://disk.yandex.ru/d/t4_xfXjEs25ebw" target="_blank">Файл</a></td>
     </tr>
     <tr>
       <th scope="row">4</th>
       <td><a class="link-dark" href="https://disk.yandex.ru/d/k_vWrR3x3QbLSA" target="_blank">Файл</a></td>
     </tr>
     <tr>
       <th scope="row">5</th>
       <td><a href="https://disk.yandex.ru/d/m5WxScQK5g18Ww" target="_blank">Файл</a></td>
     </tr>
     <tr>
       <th scope="row">6</th>
       <td><a class="link-dark" href="https://disk.yandex.ru/d/wEmNrzXTfShEjw" target="_blank">Файл</a></td>
     </tr>
    </tbody>
</table>
</div>



<div class="row">
  <div class="col-lg-12">
    <ul class="list-unstyled">
      <li class="float-end">
        <button type="button" class="btn btn-outline-primary" onclick="window.location.href='#необычные-временные-ряды';">Вверх</button>
      </li>
      <li  class="float-end">
       <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/artificial-intelligence/time-series/labs/lab4.html';">ЛР №4 →</button>
     </li>
      <li>
        <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/artificial-intelligence/time-series/labs/lab2.html';">← ЛР №2</button>
      </li>
    </ul>
  </div>
</div>
