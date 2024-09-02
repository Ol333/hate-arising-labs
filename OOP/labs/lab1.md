<ol class="breadcrumb">
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}">Главная</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/OOP/index.html">ООП</a></li>
  <li class="breadcrumb-item active">ЛР №1</li>
</ol>

# Классы, объекты, инкапсуляция, наследование

Дана UML диаграмма классов. У каждого класса есть приватное поле (`privateImportantField`), конструктор без параметров и один перегруженный конструктор с параметром, значение которого передается в упомянутое поле.

Необходимо придумать осмысленные поле и метод для каждого из классов (осмысленные и для его наследников). По желанию можно сделать классы более конкретными.

<div class="card border-primary mb-2" style="max-width: 60rem;">
  <div class="card-body">
    <img src="{{ site.baseurl }}/img/uml1.svg"
        alt="Диаграмма классов"  focusable="false" width="100%"
        class="d-block user-select-none" />
  </div>
</div>

# Задание

## Приемлемо

* Скачать [файл]({{ site.baseurl }}/img/uml1.svg), открыть в [draw.io](https://app.diagrams.net/){:target="_blank"}, изменить согласно варианту названия классов, полей и методов.
* Реализовать иерархию классов в коде. Геттер и сеттер для приватного поля реализовать:
  * для ClassName1 через методы (как на диаграмме);
  * для ClassName2 через [свойство](https://metanit.com/sharp/tutorial/3.4.php);
  * для ClassName3 через [автосвойство](https://metanit.com/sharp/tutorial/3.4.php).
* В основном теле программы создать экземпляры классов разными способами, продемонстрировать доступные и недоступные способы работы с ними.

___

## Выше ожидаемого

* Использовать в методах значения полей родительских классов.
* Перегрузить в классах наследниках методы родительских классов.

___

## Превосходно

Осмысленно перегрузить для ClassName3 операторы:
* `+`
* `>` и `<`
* `==` и `!=`
* `++`

<div class="table-responsive">
<table class="table table-hover border-primary  table-bordered">
  <thead>
    <tr class="table-dark">
      <th scope="col">№ варианта</th>
      <th scope="col">ClassName1</th>
      <th scope="col">ClassName2</th>
      <th scope="col">ClassName3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">1</th>
      <td>Сортировка</td>
      <td>Простая (квадратичная) сортировка $O(n^2)$</td>
      <td>Сортировка пузырьком</td>
    </tr>
    <tr>
      <th scope="row">2</th>
      <td>Веб-сервис</td>
      <td>Сервис прогноза погоды</td>
      <td>Gismeteo</td>
    </tr>
    <tr>
      <th scope="row">3</th>
      <td>Элемент графического интерфейса</td>
      <td>Виджет</td>
      <td>TextBox</td>
    </tr>
    <tr>
      <th scope="row">4</th>
      <td>Компилятор</td>
      <td>Компилятор для языка Си</td>
      <td>GCC</td>
    </tr>
    <tr>
      <th scope="row">5</th>
      <td>Игровой движок</td>
      <td>Шахматный движок</td>
      <td>Stockfish</td>
    </tr>
    <tr>
      <th scope="row">6</th>
      <td>Коллекция объектов</td>
      <td>Список</td>
      <td>Двусвязный список</td>
    </tr>
    <tr>
      <th scope="row">7</th>
      <td>Веб-сервис</td>
      <td>Сервис прогноза погоды</td>
      <td>wttr.in</td>
    </tr>
    <tr>
      <th scope="row">8</th>
      <td>Коллекция объектов</td>
      <td>Список</td>
      <td>Кольцевой список</td>
    </tr>
    <tr>
      <th scope="row">9</th>
      <td>Элемент графического интерфейса</td>
      <td>Виджет</td>
      <td>Кнопка</td>
    </tr>
    <tr>
      <th scope="row">10</th>
      <td>Компилятор</td>
      <td>Компилятор для языка C#</td>
      <td>csc.exe</td>
    </tr>
    <tr>
      <th scope="row">11</th>
      <td>Сортировка</td>
      <td>Сложная сортировка $O(n \log n)$</td>
      <td>Быстрая сортировка</td>
    </tr>
    <tr>
      <th scope="row">12</th>
      <td>Генератор</td>
      <td>Генератор случайных чисел</td>
      <td>Генератор случайных чисел с нормальным распределением</td>
    </tr>
   </tbody>
</table>
</div>


<div class="row">
  <div class="col-lg-12">
   <ul class="list-unstyled">
     <li class="float-end">
       <button type="button" class="btn btn-outline-primary" onclick="window.location.href='#задание';">Вверх</button>
     </li>
     <li  class="float-end">
       <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/OOP/labs/lab2.html';">ЛР №2 →</button>
     </li>
     <li>
       <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/OOP/labs/lab0.html';">← ЛР №0</button>
     </li>
   </ul>
  </div>
</div>