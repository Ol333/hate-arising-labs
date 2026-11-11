<ol class="breadcrumb">
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}">Главная</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/TIPiS/index.html">ТИПиС</a></li>
  <li class="breadcrumb-item active">ЛР №3</li>
</ol>

<nav>
  <ul></ul>
</nav>

# Экспертные оценки

Вам необходимо дерево решений с 6 листьями (конечными результатами) по варианту. Если вы не делали 2-ю лабораторную, см. пример ниже.

Для дерева решений собираем, удаляя повторы:
* множество $R$ вариантов результатов;
* множество $Q$ вопросов с ответами;
* множество $W$ вопросов c определенным ответом.

Если всего этого много, то удаляем ветви у дерева решений так, что бы осталось $W ≤ 8$ и $R ≤ 8$.

Разбираемся с расчетом оценки согласованности мнений экспертов (коэффициента конкордации) на [понятном сайте](http://cito-web.yspu.org/link1/metod/met90/node26.html){:target="_blank"}.
Про экспертные оценки можно почитать в [этом учебном пособии](https://studfile.net/preview/3816840/){:target="_blank"}.

Организуем форму для сбора экспертных оценок (эксперты должны проранжировать результаты $R$ по каждому из вопросов с ответами из $W$ – получится $w$ векторов длины $r$ от каждого эксперта).
Организуем автоматическую проверку согласованности для $n$ экспертов. Если несогласовано, то выбираем других экспертов.

Если все в порядке, модифицируем СППР (программу из 2-й лабы) следующим образом (или создаем новую):

* Добавляем второй вариант прохождения теста и оценки результата – использование БЗ (базы знаний) экспертных оценок;
* Чтобы получить обобщенную оценку (среднее от всех экспертов) каждого варианта результата, суммируем ранги и проставляем новый обобщенный ранг результатов для каждого вопроса. Сохраняем в виде какой-то структуры в теле программы или рядом файликом (*это будет вашей БД*);
* В этом варианте пользователю выводятся последовательно все вопросы из $Q$, после чего выводится первые несколько результатов из проранжированной последовательности $R$ всех возможных результатов.

Что использовать (на самостоятельный выбор, **но обработка данных и хранение знаний связаны**):

<div class="table-responsive">
<table class="table table-hover border-primary table-bordered">
  <tbody>
      <tr class="table-dark">
      <th scope="col" colspan="3">Сбор данных (как минимум 6 разных человек должны пройти ваш тест для экспертов)</th>
    </tr>
    <tr>
      <td>Гугл формы</td>
      <td>Веб-приложение</td>
      <td>Локальное приложение</td>
    </tr>
    <tr class="table-dark">
      <th scope="col" colspan="3">Обработка данных, полученных от экспертов</th>
    </tr>
    <tr>
      <td>Excel</td>
      <td colspan="2">Программа на любом языке</td>
    </tr>
    <tr class="table-dark">
      <th scope="col" colspan="3">Хранение знаний, полученных в результате анализа ответов экспертов</th>
    </tr>
    <tr>
      <td>Отдельный файл БД</td>
      <td colspan="2">-</td>
    </tr>
    <tr class="table-dark">
      <th scope="col" colspan="3">Итоговый тест</th>
    </tr>
    <tr>
      <td colspan="3">Программа на любом языке (не в Excel)</td>
    </tr>
   </tbody>
</table>
</div>

## Задание ✒️ 📕

* Подготовить дерево решений по варианту и множества $R$, $Q$, $W$.
* Подготовить форму для сбора экспертных оценок.
* Подготовить автоматическую проверку согласованности ответов экспертов (ожидаем, $W>0,7$).
* Провести опрос экспертов (как минимум 6 человек). Проверить согласованность. **Повторять пункт, пока ответы не будут согласованны.**
* Создать СППР с базой знаний экспертов. 



<div class="table-responsive">
<table class="table table-hover border-primary table-bordered">
  <thead>
    <tr class="table-dark">
      <th scope="col">№ варианта</th>
      <th scope="col">Тема</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">1</th>
      <td>Выбор направления обучения в университете</td>
    </tr>
    <tr>
      <th scope="row">2</th>
      <td>Диагностирование заболевания</td>
    </tr>
    <tr>
      <th scope="row">3</th>
      <td>Где провести отпуск</td>
    </tr>
    <tr>
      <th scope="row">4</th>
      <td>Выбор нового хобби</td>
    </tr>
    <tr>
      <th scope="row">5</th>
      <td>Выбор компьютерной игры / жанра</td>
    </tr>
    <tr>
      <th scope="row">6</th>
      <td>Диагностика неисправности компьютера</td>
    </tr>
    <tr>
      <th scope="row">7</th>
      <td>Рекомендация книги</td>
    </tr>
    <tr>
      <th scope="row">8</th>
      <td>Профориентация</td>
    </tr>
    <tr>
      <th scope="row">9</th>
      <td>Распознавание (определение вида) растения</td>
    </tr>
    <tr>
      <th scope="row">10</th>
      <td>Выбор музыки / жанра</td>
    </tr>
    <tr>
      <th scope="row">11</th>
      <td>Выбор уравнения для решения задачи по физике</td>
    </tr>
    <tr>
      <th scope="row">12</th>
      <td>Выбор головного убора</td>
    </tr>
   </tbody>
</table>
</div>

## Пример 🐣

<div class="card border-primary mb-2" style="max-width: 60rem;">
  <div class="card-body">
  <img src="{{ site.baseurl }}/img/tipis_lab3.svg"
        focusable="false" width="100%"
        class="d-block user-select-none" />
  </div>
</div>

<div class="table-responsive">
<table class="table table-hover border-primary table-bordered">
  <thead>
    <tr class="table-dark">
      <th scope="col">№w</th>
      <th scope="col">len(W) = 8</th>
      <th scope="col">№r</th>
      <th scope="col">len(R) = 6</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>w1</th>
      <td>Больше нравились обществознание или литература? Обществознание</td>
      <th>r1</th>
      <td>Бухгалтерия</td>
    </tr>
    <tr>
      <th>w2</th>
      <td>Больше нравились обществознание или литература? Литература</td>
      <th>r2</th>
      <td>Менеджмент</td>
    </tr>
    <tr>
      <th>w3</th>
      <td>Больше привлекает считать, руководить или работать с правами? Считать</td>
      <th>r3</th>
      <td>Юриспруденция</td>
    </tr>
    <tr>
      <th>w4</th>
      <td>Больше привлекает считать, руководить или работать с правами? Руководить</td>
      <th>r4</th>
      <td>Издательское дело</td>
    </tr>
    <tr>
      <th>w5</th>
      <td>Больше привлекает считать, руководить или работать с правами? Работать с правами</td>
      <th>r5</th>
      <td>Филология</td>
    </tr>
    <tr>
      <th>w6</th>
      <td>Больше привлекает работа с произведениями, изучать культуру или придумывание статей? Работа с произведениями</td>
      <th>r6</th>
      <td>Журналист</td>
    </tr>
    <tr>
      <th>w7</th>
      <td>Больше привлекает работа с произведениями, изучать культуру или придумывание статей? Изучать культуру</td>
      <th/>
      <td/>
    </tr>
    <tr>
      <th>w8</th>
      <td>Больше привлекает работа с произведениями, изучать культуру или придумывание статей? Придумывание статей</td>
      <th/>
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
<table class="table table-hover border-primary table-bordered">
<thead>
<tr class="table-dark">
      <th rowspan="2">Эксперты (m)</th>
      <th colspan="7">Профессии/направления обучения (n)</th>
    </tr>
    <tr class="table-dark">
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
    <tr>
      <th>1</th>
      <td>4</td>
      <td>3</td>
      <td>1</td>
      <td>5</td>
      <td>6</td>
      <td>2</td>
      <td>-</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>4</td>
      <td>1</td>
      <td>6</td>
      <td>5</td>
      <td>2</td>
      <td>-</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5</td>
      <td>3</td>
      <td>1</td>
      <td>4</td>
      <td>6</td>
      <td>2</td>
      <td>-</td>
    </tr>
    <tr>
      <th>Сумма рангов</th>
      <td>12</td>
      <td>10</td>
      <td>3</td>
      <td>15</td>
      <td>17</td>
      <td>6</td>
      <td>63</td>
    </tr>
    <tr>
      <th>Отклонение</th>
      <td>1,5</td>
      <td>-0,5</td>
      <td>-7,5</td>
      <td>4,5</td>
      <td>6,5</td>
      <td>-4,5</td>
      <td>-</td>
    </tr>
    <tr>
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
Достаточно согласовано ($> 0,7$).


Посчитаем обобщенную оценку экспертов в виде обобщенного ранга той или иной профессии по определенному результату (например, *Обществознание*) определенного вопроса (например, *Больше нравились обществознание или литература?*) (*формула в [учебном пособии](#экспертные-оценки) стр. 125*).

<div class="table-responsive">
<table class="table table-hover border-primary table-bordered">
<thead>
<tr class="table-dark">
      <th rowspan="2">W = 1</th>
      <th colspan="7">Профессии/направления обучения (n)</th>
    </tr>
    <tr class="table-dark">
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
    <tr>
      <th>Сумма рангов</th>
      <td>12</td>
      <td>10</td>
      <td>3</td>
      <td>15</td>
      <td>17</td>
      <td>6</td>
      <td>63</td>
    </tr>
    <tr>
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
<table class="table table-hover border-primary table-bordered">
<thead>
<tr class="table-dark">
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
    <tr>
      <th>1</th>
      <td>4</td>
      <td>3</td>
      <td>1</td>
      <td>5</td>
      <td>6</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6</td>
      <td>5</td>
      <td>4</td>
      <td>3</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>2</td>
      <td>5</td>
      <td>4</td>
      <td>6</td>
      <td>3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3</td>
      <td>1</td>
      <td>2</td>
      <td>4</td>
      <td>5</td>
      <td>6</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>2</td>
      <td>1</td>
      <td>4</td>
      <td>6</td>
      <td>3</td>
    </tr>
    <tr>
      <th>6</th>
      <td>5</td>
      <td>6</td>
      <td>2</td>
      <td>1</td>
      <td>3</td>
      <td>4</td>
    </tr>
    <tr>
      <th>7</th>
      <td>6</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>1</td>
    </tr>
    <tr>
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
<table class="table table-hover border-primary table-bordered">
  <tbody>
    <tr class="table-dark">
      <th>W</th>
      <th>1 (бух)</th>
      <th>2 (мен)</th>
      <th>3 (юр) </th>
      <th>4 (изд)</th>
      <th>5 (фил)</th>
      <th>6 (жур)</th>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>3</td>
      <td>1</td>
      <td>5</td>
      <td>6</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3</td>
      <td>1</td>
      <td>2</td>
      <td>4</td>
      <td>5</td>
      <td>6</td>
    </tr>
    <tr>
      <th>7</th>
      <td>6</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Сумма</th>
      <td>13</td>
      <td>6</td>
      <td>6</td>
      <td>13</td>
      <td>16</td>
      <td>9</td>
    </tr>
    <tr>
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

1. Филология.
2. Издательское дело.
3. Бухгалтерия.


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
