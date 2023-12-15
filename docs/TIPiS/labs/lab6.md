<ol class="breadcrumb">
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}">Главная</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/TIPiS/index.html">ТИПиС</a></li>
  <li class="breadcrumb-item active">ЛР №6</li>
</ol>

<nav>
  <ul></ul>
</nav>

# DFD

**Data flow diagrams** – диаграммы потоков данных.

Здесь нет строгой системы требований, как, например, в IDEF0 или BPMN, где нотации имеют жестко определенный синтаксис, так как они могут быть исполняемыми. Но все же определенных правил стоит придерживаться, чтобы не вносить путаницу при чтении DFD другими людьми.

Элементы диаграммы:

* *Процесс* (Process) – функция или последовательность действий, которые нужно предпринять, чтобы данные были обработаны (создание заказа, регистрация клиента и т.д.). В названиях процессов принято использовать глаголы, т.е. «Создать клиента» (а не «создание клиента»).

* *Внешние сущности* ( External Entity). Это любые объекты, которые не входят в саму систему, но являются для нее источником информации либо получателями какой-либо информации из системы после обработки данных (человек, внешняя система, какие-либо носители информации и хранилища данных).

* *Хранилище данных* (Data store). Внутреннее хранилище данных для процессов в системе. Поступившие данные перед обработкой и результат после обработки, а также промежуточные значения должны где-то храниться. Это и есть базы данных, таблицы или любой другой вариант организации и хранения данных.

* *Поток данных* (Data flow). стрелки, которые показывают, какая информация входит, а какая исходит из того или иного блока на диаграмме.

Используются две нотации: Йордана (Yourdon) и Гейна-Сарсон (Gane-Sarson), отличающиеся синтаксисом:

<div class="card border-primary mb-2" style="max-width: 30rem;">
  <div class="card-body">
  <img src="{{ site.baseurl }}/img/dfd.svg"
        alt="Синтаксис нотаций"  focusable="false" width="100%"
        class="d-block user-select-none" />
  </div>
</div>

## Задание

Проектирование информационной системы с помощью методологии DFD.

После сдачи предыдущей работы обратитесь к преподавателю.
Получите IDEF0 диаграмму информационной системы от одногрупника и сделайте по ней DFD диаграмму. Все, отраженное на исходной диаграмме, должно присутствовать на новой. При необходимости можно что-то добавлять, но не убирать.

<table class="table table-hover">
  <thead>
    <tr>
      <th scope="col">№ варианта</th>
      <th scope="col">Нотация</th>
    </tr>
  </thead>
  <tbody>
    <tr class="table-active">
      <th scope="row">Нечетные</th>
      <td>Йордана</td>
    </tr>
    <tr class="table-primary">
      <th scope="row">Четные</th>
      <td>Гейна-Сарсон</td>
    </tr>
    </tbody>
</table>

*Все элементы диаграммы должны иметь имена.*

Сайты, которые могут помочь:
* [красиво](https://www.lucidchart.com/pages/ru/%D0%B4%D0%B8%D0%B0%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B0-dfd){:target="_blank"}
* [вики](https://ru.wikipedia.org/wiki/DFD){:target="_blank"}
* [habr](https://habr.com/ru/articles/668684/){:target="_blank"}
* [познавательно](https://pcoding.ru/gost/dfd.pdf){:target="_blank"}

## Пример

*Информационная система анализа ходов игрока сёги.*

<div class="card border-primary mb-2" style="max-width: 40rem;">
  <div class="card-body">
  <img src="{{ site.baseurl }}/img/DFD_shogi.svg"
        alt="Синтаксис нотаций"  focusable="false" width="100%"
        class="d-block user-select-none" />
  </div>
</div>

<div class="row">
  <div class="col-lg-12">
   <ul class="list-unstyled">
     <li class="float-end">
       <button type="button" class="btn btn-outline-primary" onclick="window.location.href='#dfd';">Вверх</button>
     </li>
     <li  class="float-end">
       <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/TIPiS/labs/lab7.html';">ЛР №7 →</button>
     </li>
     <li>
       <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/TIPiS/labs/lab5.html';">← ЛР №5</button>
     </li>
   </ul>
  </div>
</div>