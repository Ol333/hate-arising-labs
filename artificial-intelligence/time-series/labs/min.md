<ol class="breadcrumb">
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}">Главная</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/artificial-intelligence/index.html">ИИ</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/artificial-intelligence/time-series/index.html">Временные ряды</a></li>
  <li class="breadcrumb-item active">Требования</li>
</ol>

## Требования для допуска к экзамену

Для допуска к экзамену по Временным рядам нужно:

* выполнить все лабораторные (7 шт. + 8шт. ИНС);
* посетить $>80 \%$ занятий по расписанию (из 24 шт.);
* выполнить диагностическое тестирование не менее, чем на 70%.

Посещение засчитывается, если есть:
* не меньше 60 мин присутствия на паре;
* одно из следующего:
  * сдача или попытка сдачи лабораторной;
  * описание текущего состояния работы (отличающегося от предыдущей пары) + осознанный вопрос, связанный с имеющимися затруднениями.

Если вы пропускаете занятие по неуважительной причине, то его нужно отработать (на консультации). Отработка засчитывается по тем же критериям, что и посещение.

Пропуск не нужно отрабатывать в двух случаях:
1. Наличие уважительной причины (см. пункты 4.6 и 4.7. [документа](https://www.surgu.ru/publish/document/tekKontrolDocLink/STO-2.12.5-17.pdf){:target="_blank"}).
2. К моменту пропуска были сданы все требуемые лабораторные работы.

___

## Посещения и сданные работы

<div class="table-responsive">
  <div id="gridContainer"></div>
</div>

<script>
  const url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQDPVi5ZgAjVwzEnZJVT9X5I6ZnfSCo5KHxleIYhQo957Xy84-GnepBWduPJ47QL01ZTq2j5hBELQfF/pubhtml?gid=0&amp;range=A1:AS13&amp;single=true&amp;widget=false&amp;chrome=false&amp;headers=false&amp";
  fetch(url)
    .then(res => res.text())
    .then(res => {
      const htmlString = "<table" + res.split('table')[2] + "table>"

      const parser = new DOMParser();
      const doc = parser.parseFromString(htmlString, 'text/html');
      const table = doc.querySelector('table');
      if (table) {
          function removeAttrs(element) {
              Array.from(element.attributes).forEach(attr => element.removeAttribute(attr.name));
              Array.from(element.children).forEach(child => removeAttrs(child));
          }
          removeAttrs(table);
      }
      const clean_table = doc.body.innerHTML;

      const out = clean_table.slice(0,6) + ' class="table table-hover border-primary table-bordered"' + clean_table.slice(6);
      console.log(out);

      document.getElementById("gridContainer").innerHTML = out;
    });

</script>


___




<!-- <div class="row">
  <div class="col-lg-12">
   <ul class="list-unstyled">
     <li class="float-end">
       <button type="button" class="btn btn-outline-primary" onclick="window.location.href='#вопросы-к-экзамену';">Вверх</button>
     </li>
     <li  class="float-end">
       <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/TIPiS/labs/lab10.html';">ЛР №10 →</button>
     </li>
     <li>
       <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/TIPiS/labs/lab8.html';">← ЛР №8</button>
     </li>
   </ul>
  </div>
</div> -->