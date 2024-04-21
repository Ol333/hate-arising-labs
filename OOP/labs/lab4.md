<ol class="breadcrumb">
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}">Главная</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/OOP/index.html">ООП</a></li>
  <li class="breadcrumb-item active">ЛР №4</li>
</ol>

# Объектно-ориентированное проектирование 2

Проектируем мини-ИС.
Нужно будет обеспечить сохранение введенной пользователем информации и состояния системы между запусками программы.

У основного объекта (подчеркнутого в задаче) должно быть как минимум **5 полей**.


Учитывайте, что проект, который вы создадите, нужно будет реализовать.

# Задание

## Приемлемо

Согласно варианту разработать 2 диаграммы UML:
* Описать функциональную задачу с помощью *диаграммы прецедентов*.
* Составить *диаграмму классов*, используя заданный паттерн.

___

## Выше ожидаемого

* При проектировании использовать 2 паттерна.
* Составить 3-ю UML *диаграмму на ваш выбор*.

___

## Превосходно

* При проектировании использовать SOLID принципы.


<div class="table-responsive">
<table class="table table-hover border-primary  table-bordered ">
  <thead>
    <tr class="table-dark">
      <th scope="col">№ варианта</th>
      <th scope="col">Задача</th>
      <th scope="col">Паттерн</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">1</th>
      <td>ИС склада: прием <u>товара</u> на временное хранение и размещение его на складе</td>
      <td><a class="link-dark" href="https://metanit.com/sharp/patterns/3.6.php" target="_blank">Состояние (State)</a></td>
    </tr>
    <tr>
      <th scope="row">2</th>
      <td>ИС службы заказа такси: поиск <u>такси</u> для клиента из множества работающих в данных момент</td>
      <td><a class="link-dark" href="https://metanit.com/sharp/patterns/3.2.php" target="_blank">Наблюдатель (Observer)</a></td>
    </tr>
    <tr>
      <th scope="row">3</th>
      <td>ИС службы доставки еды: выдать пользователю доступные для заказа <u>блюда</u>, собранные от нескольких ресторанов, в единообразном виде</td>
      <td><a class="link-dark" href="https://metanit.com/sharp/patterns/4.2.php" target="_blank">Адаптер (Adapter)</a></td>
    </tr>
    <tr>
      <th scope="row">4</th>
      <td>ИС выдачи музыкальных рекомендаций: обеспечить сбор данных о <u>музыкальных композициях</u> с какого-либо сайта и выдачу списка композиций, удовлетворяющих критерию запроса</td>
      <td><a class="link-dark" href="https://metanit.com/sharp/patterns/4.3.php" target="_blank">Фасад (Facade)</a></td>
    </tr>
    <tr>
      <th scope="row">5</th>
      <td>ИС фирмы проката автомобилей: выбор <u>автомобиля</u> для проката и просмотр приблизительной стоимости и характеристик</td>
      <td><a class="link-dark" href="https://metanit.com/sharp/patterns/4.5.php" target="_blank">Заместитель (Proxy)</a></td>
    </tr>
    <tr>
      <th scope="row">6</th>
      <td>ИС частной поликлиники: расчет стоимости приема <u>врача</u> с учетом обязательных услуг</td>
      <td><a class="link-dark" href="https://metanit.com/sharp/patterns/4.1.php" target="_blank">Декоратор (Decorator)</a></td>
    </tr>
    <tr>
      <th scope="row">7</th>
      <td>ИС кредитной компании: создать кредитный план по желаниям, возможностям и кредитной истории <u>клиента</u></td>
      <td><a class="link-dark" href="https://metanit.com/sharp/patterns/2.5.php" target="_blank">Строитель (Builder)</a></td>
    </tr>
    <tr>
      <th scope="row">8</th>
      <td>ИС приемной компании в университете: создать список <u>студентов</u> (сделать список самостоятельно без использования List&lt;T&gt; из System.Collections.Generic)</td>
      <td><a class="link-dark" href="https://metanit.com/sharp/patterns/3.5.php" target="_blank">Итератор (Iterator)</a></td>
    </tr>
    <tr>
      <th scope="row">9</th>
      <td>ИС документооборота: генерация нескольких видов <u>документов</u> по шаблонам</td>
      <td><a class="link-dark" href="https://metanit.com/sharp/patterns/3.3.php" target="_blank">Команда (Command)</a></td>
    </tr>
    <tr>
      <th scope="row">10</th>
      <td>ИС сборочного производства: заполнить помещение несколькими видами <u>станков</u> с учетом заданной площади помещения и требуемой интенсивности производства</td>
      <td><a class="link-dark" href="https://metanit.com/sharp/patterns/2.4.php" target="_blank">Прототип (Prototype)</a></td>
    </tr>
    <tr>
      <th scope="row">11</th>
      <td>ИС ресторана: распределение заказанных <u>бизнес-ланчей</u> между поварами</td>
      <td><a class="link-dark" href="https://metanit.com/sharp/patterns/2.2.php" target="_blank">Абстрактная фабрика (abstract factory)</a></td>
    </tr>
    <tr>
      <th scope="row">12</th>
      <td>ИС психолога: обработка <u>ответов пациента на психологический тест</u> и вывод результатов</td>
      <td><a class="link-dark" href="https://metanit.com/sharp/patterns/3.1.php" target="_blank">Стратегия (Strategy)</a></td>
    </tr>
   </tbody>
</table>
</div>

<div class="row">
  <div class="col-lg-12">
   <ul class="list-unstyled">
     <li class="float-end">
       <button type="button" class="btn btn-outline-primary" onclick="window.location.href='#объектно-ориентированное-проектирование-2';">Вверх</button>
     </li>
     <li  class="float-end">
       <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/OOP/labs/lab5.html';">ЛР №5 →</button>
     </li>
     <li>
       <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/OOP/labs/lab3.html';">← ЛР №3</button>
     </li>
   </ul>
  </div>
</div>
