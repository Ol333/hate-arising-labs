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
    <svg xmlns="http://www.w3.org/2000/svg" width="841" height="166" viewBox="-.5 -.5 841 166"><defs><clipPath id="prefix__a"><path d="M4 31h212v26H4z"/></clipPath><clipPath id="prefix__b"><path d="M4 57h212v110H4z"/></clipPath><clipPath id="prefix__c"><path d="M314 31h212v26H314z"/></clipPath><clipPath id="prefix__d"><path d="M314 57h212v110H314z"/></clipPath><clipPath id="prefix__e"><path d="M624 31h212v26H624z"/></clipPath><clipPath id="prefix__f"><path d="M624 57h212v110H624z"/></clipPath></defs><g fill="none" stroke="currentColor" stroke-miterlimit="10"><path d="M0 26V0h220v26" pointer-events="all"/><path d="M0 26v136h220V26M0 26h220" pointer-events="none"/></g><text x="109.5" y="17.5" fill="currentColor" font-family="Helvetica" font-weight="bold" text-anchor="middle" font-size="12">ClassName1</text><path fill="none" stroke="currentColor" pointer-events="all" d="M0 26h220v26H0z"/><g fill="currentColor" font-family="Helvetica" clip-path="url(#prefix__a)" font-size="12"><text x="5.5" y="43.5">- privateImportantField: type</text></g><path fill="none" stroke="currentColor" pointer-events="all" d="M0 52h220v110H0z"/><g fill="currentColor" font-family="Helvetica" clip-path="url(#prefix__b)" font-size="12"><text x="5.5" y="69.5">+ method1(type): type</text><text x="5.5" y="97.5">+ ClassName1(): void</text><text x="5.5" y="111.5">+ ClassName1(type): void</text><text x="5.5" y="139.5">+ getPrivateImportantField(type): type</text><text x="5.5" y="153.5">- setPrivateImportantField(type): void</text></g><g fill="none" stroke="currentColor" stroke-miterlimit="10"><path d="M310 39h-71.88" pointer-events="stroke"/><path d="M221.12 39l17-8.5v17z" pointer-events="all"/></g><g fill="none" stroke="currentColor" stroke-miterlimit="10"><path d="M310 26V0h220v26" pointer-events="all"/><path d="M310 26v136h220V26M310 26h220" pointer-events="none"/></g><text x="419.5" y="17.5" fill="currentColor" font-family="Helvetica" font-weight="bold" text-anchor="middle" font-size="12">ClassName2</text><path fill="none" stroke="currentColor" pointer-events="all" d="M310 26h220v26H310z"/><g fill="currentColor" font-family="Helvetica" clip-path="url(#prefix__c)" font-size="12"><text x="315.5" y="43.5">- privateImportantField: type</text></g><path fill="none" stroke="currentColor" pointer-events="all" d="M310 52h220v110H310z"/><g fill="currentColor" font-family="Helvetica" clip-path="url(#prefix__d)" font-size="12"><text x="315.5" y="69.5">+ method2(type): type</text><text x="315.5" y="97.5">+ ClassName2(): void</text><text x="315.5" y="111.5">+ ClassName2(type): void</text><text x="315.5" y="139.5">+ getPrivateImportantField(type): type</text><text x="315.5" y="153.5">- setPrivateImportantField(type): void</text></g><g fill="none" stroke="currentColor" stroke-miterlimit="10"><path d="M620 26V0h220v26" pointer-events="all"/><path d="M620 26v136h220V26M620 26h220" pointer-events="none"/></g><text x="729.5" y="17.5" fill="currentColor" font-family="Helvetica" font-weight="bold" text-anchor="middle" font-size="12">ClassName3</text><path fill="none" stroke="currentColor" pointer-events="all" d="M620 26h220v26H620z"/><g fill="currentColor" font-family="Helvetica" clip-path="url(#prefix__e)" font-size="12"><text x="625.5" y="43.5">- privateImportantField: type</text></g><path fill="none" stroke="currentColor" pointer-events="all" d="M620 52h220v110H620z"/><g fill="currentColor" font-family="Helvetica" clip-path="url(#prefix__f)" font-size="12"><text x="625.5" y="69.5">+ method3(type): type</text><text x="625.5" y="97.5">+ ClassName3(): void</text><text x="625.5" y="111.5">+ ClassName3(type): void</text><text x="625.5" y="139.5">+ getPrivateImportantField(type): type</text><text x="625.5" y="153.5">- setPrivateImportantField(type): void</text></g><g fill="none" stroke="currentColor" stroke-miterlimit="10"><path d="M620 39h-71.88" pointer-events="stroke"/><path d="M531.12 39l17-8.5v17z" pointer-events="all"/></g></svg>
  </div>
</div>

# Задание

## Приемлемо

* Скачать [файл]({{ site.baseurl }}/img/uml1.svg), открыть в [draw.io](https://app.diagrams.net/){:target="_blank"}, изменить согласно варианту названия классов, полей и методов.
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
