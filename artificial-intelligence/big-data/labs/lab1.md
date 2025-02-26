<ol class="breadcrumb">
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}">Главная</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/artificial-intelligence/index.html">ИИ</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/artificial-intelligence/big-data/index.html">Обработка данных</a></li>
  <li class="breadcrumb-item active">ЛР №1</li>
</ol>

<nav>
  <ul></ul>
</nav>

# Предварительная обработка данных для машинного обучения

Цель предварительной обработки данных — сделать исходные данные пригодными для машинного обучения. Сюда входят векторизация, нормализация, обработка недостающих значений и извлечение признаков.

## Векторизация
Мешок слов (bag of words) - упрощенное представление текста, которое показывает, какие слова встретились в тексте, но при этом не учитывает их порядок.

Представление мешка слов — это таблица с числами, в которой столбцы таблицы — уникальные слова, а строки — документы коллекции. В ячейках таблицы находится число вхождений слова в документ. Значит, в каждой строке получится набор чисел (он же вектор), характеризующий состав документа.

Пусть у нас есть два текста: «Это были лучшие времена» и «Это было худшее время» (ниже пример на английском, потому что библиотека работает с английским). В обоих предложениях встречается суммарно 5 различных слов, если привести к начальным формам: «Это», «Быть», «Лучший», «Худший», «Время». Это будет наш словарь.

Выделим встреченные слова из словаря в текстах: в первом встретились `[«Это», «Быть», «Лучший», «Время»]`, а во втором — `[«Это», «Быть», «Худший», «Время»]`.

Векторное представление мешка слов для первого текста будет `[1 1 1 0 1]`, где нолик стоит на месте элемента «Худший», так как оно не встретилось в нем, а для второго — `[1 1 0 1 1]`, где нолик на месте слова «Лучший». Так мы перешли к упрощенному машиночитаемому представлению двух текстов.
```python
import numpy as np

s1 = 'It was a good time'
s2 = 'It was a worst time'
s3 = [s1, s2]
words = list(set((s1+' '+s2).split()))
print(words)

results = np.zeros((len(s3), len(words)))

for i, sequence in enumerate(s3):
    for j in sequence.split():
        results[i, words.index(j)] = 1.

print(results)
```
### Задание 1
Данные - текстовые отзывы на фильмы, разделенные на негативные и позитивные. Что мы собираемся с ними сделать:

1.	Выделить отдельные слова, привести из к единому виду (убрав словоформы);
2.	Построить вектор из всех слов, а потом для каждого сообщения заполнить вектор такой же длины нулями или единицами в зависимости от того, было ли слово в тексте;
3.	Объединить все, разделить данные на обучающую и тестовую выборки;
4.	Создать классификатор и обучить его.

В папке с лабораторной скачайте файл [data.zip](https://disk.yandex.ru/d/173dgm63uNffpA).

В цикле считайте из папки neg txt'шники в `list` строк. В тот же `list` добавьте строки из папки pos. Параллельно создайте `list` со значениями `0` для негативных отзывов и `1` – для положительных.

Выполнить прямое кодирование списков слов в векторы нулей и единиц (в numpy массив). Это может означать, например, преобразование последовательности [good, day] в 10 000-мерный вектор, все элементы которого содержат нули, кроме элементов с индексами 3 и 5 (номеров этих слов в словаре), которые содержат единицы. Затем их можно передать на вход модели машинного обучения.

> В реальных задачах все сложнее. Чтобы не мусорить в таблице, из текста убирают служебные слова. Слова приводят не обязательно к начальной форме (см. «лемматизация»), но иногда и обрезают, оставляя только грамматическую основу. (см. «стемминг»). Поэтому правильнее называть их уже не словами, а «токенами». Иногда столбцы обозначают не отдельные слова, а пары подряд идущих слов (биграммы) или тройки (триграммы).
Чаще всего в ячейках пишут не абсолютный показатель «слово встретилось 15 раз», а относительный показатель из статистики: он называется tf-idf и описывает важность слова для классификации текста.

**Стемминг** – это грубый эвристический процесс, который отрезает «лишнее» от корня слов, часто это приводит к потере словообразовательных суффиксов.

**Лемматизация** – это более тонкий процесс, который использует словарь и морфологический анализ, чтобы в итоге привести слово к его канонической форме – лемме.

После векторизации нужно разбить выборку на обучающую и тестовую.
```python
from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(train_data_features,
                                                    emotion,
                                                    test_size=0.2,
                                                    random_state=0)
```
Создать и обучить классификатор
```python
from sklearn.naive_bayes import BernoulliNB

clf = BernoulliNB()
clf.fit()
```
Посмотреть, что выдает классификатор на тестовой выборке и сравнить с правильными значениями.
```python
from sklearn import metrics

print(metrics.accuracy_score(clf.predict(x_test),y_test))
```


## Нормализация
Чтобы упростить обучение сети, данные должны обладать следующими характеристиками:

*	принимать небольшие значения — как правило, значения должны находиться в диапазоне 0–1;
*	быть однородными — то есть все признаки должны принимать значения из примерно одного и того же диапазона.

Кроме того, может оказаться полезной следующая практика нормализации, хотя она не всегда необходима (например, мы не использовали нормализацию в примере классификации цифр):
*	нормализация каждого признака независимо, чтобы его среднее значение было равно 0;
*	нормализация каждого признака независимо, чтобы его стандартное отклонение было равно 1.

Это легко реализуется с применением массивов Numpy:
```python
x -= x.mean(axis=0)
x /= x.std(axis=0)
```
Предполагается, что x — это двумерная матрица данных с формой (образцы, свойства).

### Задание 2

Прочитать [Шолле Ф. Глубокое обучение на Python (2018)](https://codernet.ru/books/python/glubokoe_obuchenie_na_python_sholle_fransua/):

<ins>от стр.111.</ins> 3.6. Предсказание цен на дома: пример регрессии

<ins>до стр.112.</ins> 3.6.2. Подготовка данных (*Конструирование сети – не нужно*).

После подготовки данных, обучить модель Ridge и вывести значение среднеквадратичной ошибки.
```python
from sklearn.linear_model import Ridge
```
**Обобщенная модель обучения при использовании чужих библиотек *(будь то ML или нейронки)*:**
```python
model = ModelName()
model.fit(X_train, Y_train)
metrics_check_name(model.predict(x_test), y_test)
```
Если ругается на прошлый вариант оценки точности, можно так:
```python
print(model.score(test_data, test_targets))
```

## Обработка недостающих значений
Иногда в исходных данных могут отсутствовать некоторые значения. Так, в примере с предсказанием цен на дома первым признаком (столбец с индексом 0 в данных) был уровень преступности на душу населения. Как быть, если этот признак определен не во всех образцах? Если оставить все как есть, у нас будет недоставать значений в тренировочных или в контрольных данных.

Можно заменить недостающие входные значения нулями, при условии, что 0 не является осмысленным значением. Обратите внимание на то, что, если в контрольных данных имеются отсутствующие значения, но модель была обучена без них, ваша модель не будет распознавать отсутствующие значения! В этой ситуации следует искусственно сгенерировать тренировочные экземпляры с отсутствующими признаками: скопируйте несколько тренировочных образцов и отбросьте в них некоторые признаки, которые, как ожидается, не определены в контрольных данных.


## Конструирование признаков
Конструирование признаков — это процесс использования ваших собственных знаний о данных и алгоритме машинного обучения, чтобы улучшить эффективность алгоритма применением предопределенных преобразований к данным перед передачей их в модель. Во многих случаях не следует ожидать, что модель машинного обучения сможет обучиться на полностью произвольных данных. Данные должны передаваться в модель в виде, облегчающем ее работу.

Рассмотрим простой пример. Допустим, нам нужно разработать модель, принимающую изображение циферблата часов со стрелками и возвращающую время:

<div class="table-responsive">
<table class="table table-hover border-primary  table-bordered ">
  <thead>
    <tr class="table-dark">
      <th scope="col">Исходные данные: сетка с пикселами</th>
      <th scope="col" colspan="2">🕒</th>
      <th scope="col" colspan="2">🕙</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row" rowspan="2">Более удачные признаки: координаты стрелок</th>
      <td>$x_1 = 0.0$</td>
      <td>$x_2 = 0.5$</td>
      <td>$x_1 = -0.7$</td>
      <td>$x_2 = 0.0$</td>
    </tr>
    <tr>
      <td>$y_1 = 1.0$</td>
      <td>$y_2 = 0.0$</td>
      <td>$y_1 = 0.7$</td>
      <td>$y_2 = 1.0$</td>
    </tr>
    <tr>
      <th scope="row">Еще более удачные признаки: углы отклонения стрелок</th>
      <td>$\theta_1 = 0$</td>
      <td>$\theta_2 = 45$</td>
      <td>$\theta_1 = 90$</td>
      <td>$\theta_2 = 135$</td>
    </tr>
   </tbody>
</table>
</div>

Если в качестве входных данных использовать пикселы исходных изображений, вы столкнетесь со сложной задачей машинного обучения. Для ее решения вам потребуется сконструировать сверточную сеть и потратить большой объем вычислительных ресурсов на ее обучение.

Однако, понимая задачу на высоком уровне (как человек определяет время по циферблату часов), можно сконструировать гораздо более удачные входные признаки для алгоритма машинного обучения: например, можно с легкостью написать пять строк кода на Python, которые проследуют по черным пикселам стрелок и вернут координаты (x, y) конца каждой стрелки. Тогда простой алгоритм машинного обучения сможет обучиться связывать эти координаты с соответствующим временем дня.

Можно пойти еще дальше: преобразовать координаты (x, y) в полярные координаты относительно центра изображения. В этом случае на вход будут подаваться углы отклонения стрелок. Полученные в результате признаки делают задачу настолько простой, что для ее решения не требуется применять методику машинного обучения; простой операции округления и поиска в словаре вполне достаточно, чтобы получить приближенное значение времени дня.

В этом суть конструирования признаков: упростить задачу и сделать возможным ее решение более простыми средствами. Обычно для этого требуется глубокое понимание задачи.

До глубокого обучения конструирование признаков играло важную роль, поскольку классические поверхностные алгоритмы не имели пространств гипотез, достаточно богатых, чтобы выявить полезные признаки самостоятельно. Форма данных, передаваемых алгоритму, имела решающее значение для успеха.

К счастью, современные технологии глубокого обучения в большинстве случаев избавляют от необходимости конструировать признаки, потому что нейронные сети способны автоматически извлекать полезные признаки из исходных данных. Означает ли это, что вы не должны беспокоиться о конструировании признаков при использовании глубоких нейронных сетей? Нет, и вот почему:

* Хорошие признаки позволяют решать задачи более элегантно и с меньшими затратами ресурсов. Например, было бы смешно решать проблему чтения показаний с циферблата часов с привлечением сверточной нейронной сети.
* Хорошие признаки позволяют решать задачи, имея намного меньший объем исходных данных. Способность моделей глубокого обучения самостоятельно выделять признаки зависит от наличия большого объема исходных данных; если у вас всего несколько образцов, информационная ценность их признаков приобретает определяющее значение.

<div class="row">
  <div class="col-lg-12">
    <ul class="list-unstyled">
      <li class="float-end">
        <button type="button" class="btn btn-outline-primary" onclick="window.location.href='#предварительная-обработка-данных-для-машинного-обучения';">Вверх</button>
      </li>
      <li  class="float-end">
       <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/artificial-intelligence/big-data/labs/lab2.html';">ЛР №2 →</button>
     </li>
    </ul>
  </div>
</div>