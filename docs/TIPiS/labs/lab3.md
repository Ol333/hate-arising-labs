<ol class="breadcrumb">
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}">Главная</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/TIPiS/index.html">ТИПиС</a></li>
  <li class="breadcrumb-item active">ЛР №3</li>
</ol>

<nav>
  <ul></ul>
</nav>

# Экспертные оценки

## Задание

Берем свою 2-ю лабораторную.

Собираем множество $R$ вариантов результатов, удаляя повторы.

Собираем множество $Q$ вопросов с ответами, удаляя повторы.

Собираем множество $W$ вопросов c определенным ответом.

Если всего этого много, то удаляем ветви у дерева решений так, что бы осталось $W ≤ 8$ и $R ≤ 8$.

Разбираемся с расчетом оценки согласованности мнений экспертов (коэффициента конкордации) на [понятном сайте](http://cito-web.yspu.org/link1/metod/met90/node26.html).

В [этом учебном пособии](https://www.researchgate.net/publication/265964844_Metody_ekspertnyh_ocenok) можно почитать про экспертные оценки.

Организуем форму для сбора экспертных оценок (эксперты должны проранжировать результаты $R$ по каждому из вопросов с ответами из $W$ – получится $w$ векторов длины $r$ от каждого эксперта).
Организуем автоматическую проверку согласованности для $n$ экспертов. Если несогласовано, то выбираем других экспертов.

Если все в порядке, модифицируем СППР (приложение 2-й лабы) следующим образом:

* Добавляем второй вариант прохождения теста и оценки результата – использование БЗ (базы знаний) экспертных оценок;
* Чтобы получить обобщенную оценку (среднее от всех экспертов) каждого варианта результата, суммируем ранги и проставляем новый обобщенный ранг результатов для каждого вопроса. Сохраняем в виде какой-то структуры в теле программы или рядом файликом (*это будет вашей БД*);
* В этом варианте пользователю выводятся последовательно все вопросы из $Q$, после чего выводится первые несколько результатов из проранжированной последовательности $R$ всех возможных результатов.

Что использовать (на выбор (самостоятельный)):

<table class="table table-hover">
  <thead>
    <tr>
      <th scope="col">Сбор данных</th>
      <th scope="col">Обработка данных</th>
    </tr>
  </thead>
  <tbody>
    <tr class="table-light">
      <td>Гугл формы</td>
      <td>Excel</td>
    </tr>
    <tr class="table-info">
      <td>Консольный ввод</td>
      <td>Python</td>
    </tr>
    <tr class="table-light">
      <td>Собственный граф интерфейс</td>
      <td>C++</td>
    </tr>
    <tr class="table-info">
      <td>Веб</td>
      <td>C#</td>
    </tr>
   </tbody>
</table>

## Пример

<div class="card border-primary mb-2" style="max-width: 60rem;">
  <div class="card-body">
  <img src="{{ site.baseurl }}/img/tipis_lab3.svg"
        focusable="false" width="100%"
        class="d-block user-select-none" />
  </div>
</div>

<div class="table-responsive">
<table class="table table-hover">
  <thead>
    <tr>
      <th scope="col">№w</th>
      <th scope="col">len(W) = 8</th>
      <th scope="col">№r</th>
      <th scope="col">len(R) = 6</th>
    </tr>
  </thead>
  <tbody>
    <tr class="table-active">
      <td>w1</td>
      <td>Больше нравились обществознание или литература? Обществознание</td>
      <td>r1</td>
      <td>Бухгалтерия</td>
    </tr>
    <tr class="table-primary">
      <td>w2</td>
      <td>Больше нравились обществознание или литература? Литература</td>
      <td>r2</td>
      <td>Менеджмент</td>
    </tr>
    <tr class="table-active">
      <td>w3</td>
      <td>Больше привлекает считать, руководить или работать с правами? Считать</td>
      <td>r3</td>
      <td>Юриспруденция</td>
    </tr>
    <tr class="table-primary">
      <td>w4</td>
      <td>Больше привлекает считать, руководить или работать с правами? Руководить</td>
      <td>r4</td>
      <td>Издательское дело</td>
    </tr>
    <tr class="table-active">
      <td>w5</td>
      <td>Больше привлекает считать, руководить или работать с правами? Работать с правами</td>
      <td>r5</td>
      <td>Филология</td>
    </tr>
    <tr class="table-primary">
      <td>w6</td>
      <td>Больше привлекает работа с произведениями, изучать культуру или придумывание статей? Работа с произведениями</td>
      <td>r6</td>
      <td>Журналист</td>
    </tr>
    <tr class="table-active">
      <td>w7</td>
      <td>Больше привлекает работа с произведениями, изучать культуру или придумывание статей? Изучать культуру</td>
      <td/>
      <td/>
    </tr>
    <tr class="table-primary">
      <td>w8</td>
      <td>Больше привлекает работа с произведениями, изучать культуру или придумывание статей? Придумывание статей</td>
      <td/>
      <td/>
    </tr>
   </tbody>
</table>
</div>

Эксперту нужно для каждого из 8 вариантов ответов на 3 вопроса проранжировать 6 вариантов.

Для первого $w$: *«Больше нравились обществознание или литература? Обществознание.»* ответ первого эксперта -  `362145` в порядке убывания вероятности.

От еще 2-х экспертов на этот вопрос получим `361254` и `362415`.

Посчитаем согласованность (ссылка на понятный сайт [выше](#экспертные-оценки)).

<div class="table-responsive">
<table class="table table-hover">
<thead>
<tr class="table-info">
      <th rowspan="2">Эксперты (m)</th>
      <th colspan="7">Профессии/направления обучения (n)</th>
    </tr>
    <tr class="table-info">
      <th>1 (бух)</th>
      <th>2 (мен)</th>
      <th>3 (юр) </th>
      <th>4 (изд)</th>
      <th>5 (фил)</th>
      <th>6 (жур)</th>
      <th>итого</th>
    </tr>
  </thead>
  <tbody>
    <tr class="table-light">
      <th>1</th>
      <td>4</td>
      <td>3</td>
      <td>1</td>
      <td>5</td>
      <td>6</td>
      <td>2</td>
      <td>-</td>
    </tr>
    <tr class="table-active">
      <th>2</th>
      <td>3</td>
      <td>4</td>
      <td>1</td>
      <td>6</td>
      <td>5</td>
      <td>2</td>
      <td>-</td>
    </tr>
    <tr class="table-light">
      <th>3</th>
      <td>5</td>
      <td>3</td>
      <td>1</td>
      <td>4</td>
      <td>6</td>
      <td>2</td>
      <td>-</td>
    </tr>
    <tr class="table-light">
      <th>Сумма рангов</th>
      <td>12</td>
      <td>10</td>
      <td>3</td>
      <td>15</td>
      <td>17</td>
      <td>6</td>
      <td>63</td>
    </tr>
    <tr class="table-active">
      <th>Отклонение</th>
      <td>1,5</td>
      <td>-0,5</td>
      <td>-7,5</td>
      <td>4,5</td>
      <td>6,5</td>
      <td>-4,5</td>
      <td>-</td>
    </tr>
    <tr class="table-light">
      <th>Квадраты отклонений</th>
      <td>2,25</td>
      <td>0,25</td>
      <td>56,25</td>
      <td>20,25</td>
      <td>42,25</td>
      <td>20,25</td>
      <td>141,5</td>
    </tr>
   </tbody>
</table>
</div>

Коэффициент конкордации:

```python
a = 12 * 141.5
b = 3**2 * (6**3 - 6)
print(a/b)
```

```console
0.8984126984126984
```
Достаточно согласовано ($> 0,5$).


Посчитаем обобщенную оценку экспертов в виде обобщенного ранга той или иной профессии по данному результату (*Обществознание*) данного вопроса (*Больше нравились обществознание или литература?*) (*формула в [учебном пособии](#экспертные-оценки) стр. 125*).

<div class="table-responsive">
<table class="table table-hover">
<thead>
<tr class="table-info">
      <th rowspan="2">W = 1</th>
      <th colspan="7">Профессии/направления обучения (n)</th>
    </tr>
    <tr class="table-info">
      <th>1 (бух)</th>
      <th>2 (мен)</th>
      <th>3 (юр) </th>
      <th>4 (изд)</th>
      <th>5 (фил)</th>
      <th>6 (жур)</th>
      <th>итого</th>
    </tr>
  </thead>
  <tbody>
    <tr class="table-light">
      <th>Сумма рангов</th>
      <td>12</td>
      <td>10</td>
      <td>3</td>
      <td>15</td>
      <td>17</td>
      <td>6</td>
      <td>63</td>
    </tr>
    <tr class="table-active">
      <th>Обобщенный ранг</th>
      <td>4</td>
      <td>3</td>
      <td>1</td>
      <td>5</td>
      <td>6</td>
      <td>2</td>
      <td></td>
    </tr>
   </tbody>
</table>
</div>

То же самое для еще 7 $w$ из $W$.
Получится набор ранжирований для того или иного результата каждого из вариантов каждого вопроса, основанные на экспертных оценках.

Пускай, получится что-то такое:

<div class="table-responsive">
<table class="table table-hover">
<thead>
<tr class="table-info">
      <th>W</th>
      <th>1 (бух)</th>
      <th>2 (мен)</th>
      <th>3 (юр) </th>
      <th>4 (изд)</th>
      <th>5 (фил)</th>
      <th>6 (жур)</th>
    </tr>
  </thead>
  <tbody>
    <tr class="table-light">
      <th>1</th>
      <td>4</td>
      <td>3</td>
      <td>1</td>
      <td>5</td>
      <td>6</td>
      <td>2</td>
    </tr>
    <tr class="table-active">
      <th>2</th>
      <td>6</td>
      <td>5</td>
      <td>4</td>
      <td>3</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr class="table-light">
      <th>3</th>
      <td>1</td>
      <td>2</td>
      <td>5</td>
      <td>4</td>
      <td>6</td>
      <td>3</td>
    </tr>
    <tr class="table-active">
      <th>4</th>
      <td>3</td>
      <td>1</td>
      <td>2</td>
      <td>4</td>
      <td>5</td>
      <td>6</td>
    </tr>
    <tr class="table-light">
      <th>5</th>
      <td>5</td>
      <td>2</td>
      <td>1</td>
      <td>4</td>
      <td>6</td>
      <td>3</td>
    </tr>
    <tr class="table-active">
      <th>6</th>
      <td>5</td>
      <td>6</td>
      <td>2</td>
      <td>1</td>
      <td>3</td>
      <td>4</td>
    </tr>
    <tr class="table-light">
      <th>7</th>
      <td>6</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>1</td>
    </tr>
    <tr class="table-active">
      <th>8</th>
      <td>5</td>
      <td>3</td>
      <td>2</td>
      <td>4</td>
      <td>6</td>
      <td>1</td>
    </tr>
   </tbody>
</table>
</div>

Добавить второй вариант прохождения опросника, когда ответы даются на все вопросы $Q$ (*даже те, что, по идее, находятся в ветви, которую мы обрезаем, выбирая одно из двух*). Т.е. в нашем примере надо будет ответить на вопросы:

1. Больше нравились обществознание или литература?
2. Больше привлекает считать, руководить или работать с правами?
3. Больше привлекает работа с произведениями, изучать культуру или придумывание статей?

Пускай, ответы будут: обществознание, работать с правами, изучать культуру.
Это $w1$, $w4$, $w7$.
Для них:

<div class="table-responsive">
<table class="table table-hover">
  <tbody>
    <tr class="table-info">
      <th>W</th>
      <th>1 (бух)</th>
      <th>2 (мен)</th>
      <th>3 (юр) </th>
      <th>4 (изд)</th>
      <th>5 (фил)</th>
      <th>6 (жур)</th>
    </tr>
    <tr class="table-light">
      <th>1</th>
      <td>4</td>
      <td>3</td>
      <td>1</td>
      <td>5</td>
      <td>6</td>
      <td>2</td>
    </tr>
    <tr class="table-active">
      <th>4</th>
      <td>3</td>
      <td>1</td>
      <td>2</td>
      <td>4</td>
      <td>5</td>
      <td>6</td>
    </tr>
    <tr class="table-light">
      <th>7</th>
      <td>6</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>1</td>
    </tr>
    <tr class="table-active">
      <th>Сумма</th>
      <td>13</td>
      <td>6</td>
      <td>6</td>
      <td>13</td>
      <td>16</td>
      <td>9</td>
    </tr>
    <tr class="table-light">
      <th>Ранг</th>
      <td>2</td>
      <td>5</td>
      <td>5</td>
      <td>2</td>
      <td>1</td>
      <td>4</td>
    </tr>
   </tbody>
</table>
</div>

Выписываем в результат первые 3 варианта. Это будут:

1. филология,
2. издательское дело,
3. бухгалтерия.


<div class="row">
  <div class="col-lg-12">
   <ul class="list-unstyled">
     <li class="float-end">
       <button type="button" class="btn btn-outline-primary" onclick="window.location.href='#экспертные-оценки';">Вверх</button>
     </li>
     <li  class="float-end">
       <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/TIPiS/labs/lab4.html';">ЛР №4 →</button>
     </li>
     <li>
       <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/TIPiS/labs/lab2.html';">← ЛР №2</button>
     </li>
   </ul>
  </div>
</div>
