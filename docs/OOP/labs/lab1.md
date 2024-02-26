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
        alt="Синтаксис нотаций"  focusable="false" width="100%"
        class="d-block user-select-none" />
  </div>
</div>

# Задание

## Приемлемо

* Скачать файл .svg (картинка выше), изменить согласно варианту названия классов, полей и методов.
* Реализовать иерархию классов в коде. Геттер и сеттер для приватного поля реализовать:
  * для ClassName1 через методы;
  * для ClassName2 через свойство;
  * для ClassName3 через автосвойство.
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
<table class="table table-hover">
  <thead>
    <tr>
      <th scope="col">№ варианта</th>
      <th scope="col">ClassName1</th>
      <th scope="col">ClassName2</th>
      <th scope="col">ClassName3</th>
    </tr>
  </thead>
  <tbody>
    <tr class="table-active">
      <th scope="row">1</th>
      <td>Человек</td>
      <td>Студент</td>
      <td>Первокурсник</td>
    </tr>
    <tr class="table-primary">
      <th scope="row">2</th>
      <td>Человек</td>
      <td>Служащий</td>
      <td>Инженер</td>
    </tr>
    <tr class="table-active">
      <th scope="row">3</th>
      <td>Изделие</td>
      <td>Механизм</td>
      <td>Деталь</td>
    </tr>
    <tr class="table-primary">
      <th scope="row">4</th>
      <td>Печатное издание</td>
      <td>Книга</td>
      <td>Учебник</td>
    </tr>
    <tr class="table-active">
      <th scope="row">5</th>
      <td>Испытание</td>
      <td>Экзамен</td>
      <td>Тест</td>
    </tr>
    <tr class="table-primary">
      <th scope="row">6</th>
      <td>Товар</td>
      <td>Продукт питания</td>
      <td>Молоко</td>
    </tr>
    <tr class="table-active">
      <th scope="row">7</th>
      <td>Транспортное средство</td>
      <td>Поезд</td>
      <td>Экспресс</td>
    </tr>
    <tr class="table-primary">
      <th scope="row">8</th>
      <td>Двигатель</td>
      <td>Двигатель внутреннего сгорания</td>
      <td>Дизельный двигатель</td>
    </tr>
    <tr class="table-active">
      <th scope="row">9</th>
      <td>Животное</td>
      <td>Птица</td>
      <td>Сокол</td>
    </tr>
    <tr class="table-primary">
      <th scope="row">10</th>
      <td>Товар</td>
      <td>Велосипед</td>
      <td>Горный велосипед</td>
    </tr>
    <tr class="table-active">
      <th scope="row">11</th>
      <td>Человек</td>
      <td>Музыкант</td>
      <td>Барабанщик</td>
    </tr>
    <tr class="table-primary">
      <th scope="row">12</th>
      <td>Товар</td>
      <td>Инструмент</td>
      <td>Молоток</td>
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
       <li   class="float-end">
         <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/OOP/labs/lab2.html';">ЛР №2 →</button>
       </li>
     </ul>
   </div>
 </div>
