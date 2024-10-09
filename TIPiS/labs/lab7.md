<ol class="breadcrumb">
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}">Главная</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/TIPiS/index.html">ТИПиС</a></li>
  <li class="breadcrumb-item active">ЛР №7</li>
</ol>

<nav>
  <ul></ul>
</nav>

# Баесовский вывод

$P(A/B) = \frac{P(A)*P(B/A)}{P(B)}$ 

$P(B)$ может быть вычислено по формуле полной вероятности:

$P(B) = \sum_{i=1}^N{P(A_i)*P(B/A_i)},$

где $N=2$ (событие $A$ может наступить или не наступить).


## Задание 🏂

* Провести опрос своей группы (не менее 15 человек):
  * В опросе 2 вопроса в вариантами ответа да/нет.
  * Из опроса вы можете рассчитать статистические оценки: $P(A)$ - вероятность наступления события $A$, $P(B)$- вероятность наступления события $B$, $P(B/A)$ - вероятность наступления события $B$ при условии, что наступило событие $A$.
* Осуществить расчеты, чтобы выяснить $P(A/B)$.

<div class="table-responsive">
<table class="table table-hover border-primary table-bordered">
  <thead>
    <tr class="table-dark">
      <th scope="col">№ варианта</th>
      <th scope="col">$A$</th>
      <th scope="col">$B$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">1</th>
      <td>Знаете больше 3 языков программирования.</td>
      <td>Пьете от одной и больше чашек кофе в день</td>
    </tr>
    <tr>
      <th scope="row">2</th>
      <td>Удовлетворительная оценка по теор. вер.</td>
      <td>Удовлетворительная оценка по мат. анализу</td>
    </tr>
    <tr>
      <th scope="row">3</th>
      <td>Есть стипендия</td>
      <td>Большую часть времени на парах с собой есть свой ноутбук</td>
    </tr>
    <tr>
      <th scope="row">4</th>
      <td>Есть/была работа (с офиц. трудоустройством)</td>
      <td>Работали когда-либо с VirtulBox</td>
    </tr>
    <tr>
      <th scope="row">5</th>
      <td>Ходите в универ пешком</td>
      <td>Баллы при поступлении $>220$ (ЕГЭ или вступительные)</td>
    </tr>
    <tr>
      <th scope="row">6</th>
      <td>Планируете получать повышенную степендию со след. семестра</td>
      <td>Пользуетесь ИИ чаще 1 раза в неделю</td>
    </tr>
    <tr>
      <th scope="row">7</th>
      <td>Проходили практику на кафедре</td>
      <td>Участвовали в Хакатонах</td>
    </tr>
    <tr>
      <th scope="row">8</th>
      <td>Количество долгов $>5$</td>
      <td>Приезжаете в универ на машине</td>
    </tr>
    <tr>
      <th scope="row">9</th>
      <td>Хорошо разбираетесь в Excel</td>
      <td>Удовлетворительная оценка "Алгоритмы и языки программирования"</td>
    </tr>
    <tr>
      <th scope="row">10</th>
      <td>Перепоступали/брали академ/переводились на курс ниже</td>
      <td>Работали с Linux</td>
    </tr>
    <tr>
      <th scope="row">11</th>
      <td>Планируете работать по специальности</td>
      <td>В детстве (до 10 лет) разбирали системный блок на части</td>
    </tr>
    <tr>
      <th scope="row">12</th>
      <td>Вы можете назвать 3 сортировки и реализовать одну по памяти</td>
      <td>На вашем ноутбуке/домашнем ПК есть наклейки</td>
    </tr>
   </tbody>
</table>
</div>


<div class="row">
  <div class="col-lg-12">
   <ul class="list-unstyled">
     <li class="float-end">
       <button type="button" class="btn btn-outline-primary" onclick="window.location.href='#баесовский-вывод';">Вверх</button>
     </li>
     <li  class="float-end">
       <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/TIPiS/labs/lab8.html';">ЛР №8 →</button>
     </li>
     <li>
       <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/TIPiS/labs/lab6.html';">← ЛР №6</button>
     </li>
   </ul>
  </div>
</div>
