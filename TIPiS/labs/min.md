<ol class="breadcrumb">
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}">Главная</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/TIPiS/index.html">ТИПиС</a></li>
  <li class="breadcrumb-item active">Требования</li>
</ol>

<nav>
  <ul></ul>
</nav>

# Начисление баллов

Принятая лабораторная дает ```+5``` баллов.

Пропуск любой пары по расписанию (лекция или практика) ```-1``` балл.

## Дополнительные баллы

До декабря принимаются:
* возражения по стоимости.
* соревнования для добавления в таблицу.

<div class="table-responsive">
<table class="table table-hover border-primary table-bordered">
  <thead>
  <tr class="table-dark">
      <th scope="col" colspan="4">Считается участие в течение текущего семестра и решение ненулевого количества заданий<br>Призовое место - x2</th>
    </tr>
    <tr class="table-dark">
      <th scope="col">1 балл</th>
      <th scope="col">2 балл</th>
      <th scope="col">5 балл</th>
      <th scope="col">100500 баллов</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="https://sp.urfu.ru/qf/" target="_blank">Квалификация ICPC</a>, <br><a href="https://foncode.ru/" target="_blank">Регулярные Соревнования по спортивному программированию FONCODE</a></td>
      <td><a href="https://yandex.ru/cup/" target="_blank">Yandex Cup</a>, <br><a href="https://rucode.net/" target="_blank">RUCODE festival</a>, <br>VK Cup</td>
      <td><a href="https://sp.urfu.ru/qf/" target="_blank">Четвертьфинал ICPC</a></td>
      <td>Полуфинал или финал ICPC</td>
    </tr>
    <tr>
      <td>Местный Хакатон: surgu.ai, <a href="https://leader-id.ru/events/247747" target="_blank">Digital Challenge</a></td>
      <td>Окружной Хакатон, <a href="https://www.it-innohack.ru/" target="_blank">IT INNO HACK</a>, <a href="https://moretech.vtb.ru/">VTB</a>, <a href="грантгубернатор.рф">грант губернатора ЮГРЫ</a>, <a href="https://mik.2035.university/">доп образование от university2035</a></td>
      <td><a href="https://www.хакатоны.рф/" target="_blank">Оффлайн хакатон за пределами ХМАО</a></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td><a href="https://ctfnews.ru/news/1900" target="_blank">SurCTF</a></td>
      <td><a href="https://ctfnews.ru/" target="_blank">Оффлайн CTF за пределами ХМАО</a></td>
      <td></td>
    </tr>
    <tr>
      <td>Месяц работы системным администратором</td>
      <td>Месяц работы системным аналитиком или программистом</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>
</div>

___

<div class="table-responsive">
  <div id="gridContainer"></div>
</div>
 
<script>
  const url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSdmZTJfKmtWBaQvhjsvgDtvTsN1mIAPjqI_4G6h-DUXeteWdkZkcDxnIXILr9rn2Vjqv2mwOFfELW9/pub?gid=0&amp;range=A1:AR38&amp;single=true&amp;widget=false&amp;chrome=false&amp;headers=false&amp&output=csv";
  fetch(url)
    .then(res => res.text())
    .then(res => {
      const rows = res.split('\n');
        let html = '<table class="table table-hover border-primary table-bordered">';
        
        rows.forEach((row, index) => {
            const cells = row.split(',');
            html += '<tr>';
            cells.forEach(cell => {
                if (index === 0) {
                    html += `<th>${cell}</th>`;
                } else {
                    html += `<td>${cell}</td>`;
                }
            });
            html += '</tr>';
        });
        
        html += '</table>';
        document.getElementById("gridContainer").innerHTML = html;
    })
    .catch(error => {
        console.error('Ошибка:', error);
    });
</script>


___

## Требования для допуска к экзамену

Для допуска к экзамену по ТИПиС нужно:

* выполнить не менее 1 лабораторной из каждого раздела (МФПС, МАИС, Информационные процессы);
* набрать ```13``` баллов;
* выполнить диагностическое тестирование не менее, чем на 70%;
* посетить *(или выполнить тест в moddle по теме занятия)* не менее 70% лекционных занятий.

___

```25``` баллов обеспечит получение оценки “удовлетворительно” по дисциплине.

Для получения более высокой оценки необходимо ответить на 2 теоретических вопроса из билета.

___

```32``` баллов обеспечит получение оценки "хорошо" по дисциплине.

Для получения более высокой оценки необходимо ответить на 1 теоретический вопрос из двух в билете.

___

```49``` баллов обеспечит получение оценки "отлично" по дисциплине.


____

## Пересдача 🎠

Пересдача экзамена принимается при условии выполнения 80% лабораторных работ. Оценка на один балл ниже, чем средняя оценка ответов на два вопроса билета.


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