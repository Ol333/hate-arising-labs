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

* *Процесс* (Process) – функция или последовательность действий, которые необходимо предпринять, чтобы данные были обработаны (создание заказа, регистрация клиента и т.д.). В названиях процессов принято использовать глаголы, т.е. «Создать клиента» (а не «создание клиента»).

* *Внешние сущности* ( External Entity). Это любые объекты, которые не входят в саму систему, но являются для нее источником информации либо получателями какой-либо информации из системы после обработки данных (человек, внешняя система, какие-либо носители информации и хранилища данных).

* *Хранилище данных* (Data store). Внутреннее хранилище данных для процессов в системе. Поступившие данные перед обработкой и результат после обработки, а также промежуточные значения должны где-то храниться. Это и есть базы данных, таблицы или любой другой вариант организации и хранения данных.

* *Поток данных* (Data flow). Стрелки, которые показывают, какая информация входит, а какая исходит из того или иного блока на диаграмме.

Используются две нотации: Йордана (Yourdon) и Гейна-Сарсон (Gane-Sarson), отличающиеся синтаксисом:

<div class="card border-primary mb-2" style="max-width: 20rem;">
  <div class="card-body">
  <img src="{{ site.baseurl }}/img/dfd.svg"
        alt="Синтаксис нотаций"  focusable="false" width="100%"
        class="d-block user-select-none" />
  </div>
</div>

Правила и советы по построению диаграмм DFD:

* Каждый процесс должен сопровождаться как минимум одним входным и одним выходным потоком.
* В каждое хранилище должен впадать как минимум один поток данных и как минимум один — вытекать.
* Данные, хранимые в системе, должны проходить через процесс.
* Каждый процесс диаграммы DFD должен вести либо к другому процессу, либо к хранилищу данных.
* Все элементы диаграммы должны иметь имена.
* Стрелки не могут связывать напрямую хранилища данных, все связи идут через процессы.


## Задание ⌛

* В [папке](https://disk.yandex.ru/d/JEIWmrYomuTjqQ){:target="_blank"} взять **незанятую** (*проверить файл "отмечаемся здесь.xlsx"*) диаграмму IDEF0 по теме, не совпадающей с вашим вариантом 5-й лабораторной.
* По этой диаграмме сделать диаграмму DFD.
  * Все, отраженное на исходной диаграмме, должно присутствовать на новой. При необходимости можно что-то добавлять, но не убирать.


<div class="table-responsive">
<table class="table table-hover border-primary table-bordered">
  <thead>
    <tr>
      <th scope="col">№ варианта</th>
      <th scope="col">Нотация</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">Нечетный</th>
      <td>Йордана</td>
    </tr>
    <tr>
      <th scope="row">Четный</th>
      <td>Гейна-Сарсон</td>
    </tr>
    </tbody>
</table>
</div>



## Пример информационной системы

*Информационная система анализа ходов игрока сёги в нотации Йордана.*

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