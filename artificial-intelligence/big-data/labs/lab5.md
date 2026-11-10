<ol class="breadcrumb">
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}">Главная</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/artificial-intelligence/index.html">ИИ</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/artificial-intelligence/big-data/index.html">Обработка данных</a></li>
  <li class="breadcrumb-item active">ЛР №5</li>
</ol>

# Ансамбли

Линейные модели хороши, но умеют ловить только линейные зависимости. Решающие деревья решают проблему нелинейности, а их композиции — случайные леса и градиентный бустинг — до сих пор входят в число самых сильных универсальных методов ML. Кстати, ранжирование поиска Яндекса (MatrixNet) построено именно на бустинге над деревьями. Это не «академическая экзотика», а то, что вы будете использовать на работе.

![](https://avatars.mds.yandex.net/i?id=9fac8e288b243a2a1f3efda99d302192_l-5233330-images-thumbs&n=13&n=13&w=690&h=460)

#### Решающие деревья (л.7)

*Суть:* дерево — это набор вопросов вида «признак $x_j < t$?», по которому объект «катится» от корня к листу, где лежит ответ. Как Алгоритм «Кредит/отказ» в банке: возраст < 18? → зарплата < 50к? → стаж? → другие кредиты? Именно так и работают решающие деревья. 

**Дерево строится жадно**: в каждой вершине перебираем признаки $j$ и пороги $t$, выбираем разбиение, которое максимизирует функционал качества $Q$, и рекурсивно повторяем в поддеревьях. Найти оптимальное дерево целиком — NP-полная задача, поэтому все методы жадные и эвристичные.

**Критерии информативности** — мера «чистоты» вершины. Для регрессии это дисперсия ответов; для классификации — ошибка классификации (грубая), критерий Джини $H(R)=\sum_k p_k(1−p_k)$ или энтропийный критерий $H(R)=−\sum_k p_k \log⁡p_k$. 

**Критерии останова**: максимальная глубина, минимальное число объектов в листе, требование улучшения качества на заданный процент. Подбираются кросс-валидацией.

**Стрижка (pruning)**: альтернатива раннему останову — строим переобученное дерево, потом удаляем вершины. Есть метод cost-complexity pruning: минимизируем $R_α(T)=R(T)+α∣T∣$, балансируя качество и размер. По исследованиям работает лучше раннего останова, но в библиотеках почти не реализован — потому что сами по себе деревья слабы, а в композициях они либо должны быть переобучены (леса), либо неглубокими (бустинг). 

**Пропуски и категориальные признаки**: объект с пропуском можно вести в оба поддерева с весами или использовать суррогатные предикаты. Категориальный признак для бинарной классификации и регрессии можно упорядочить по доле положительных ответов (или среднему ответу) — и получить то же разбиение, что при полном переборе $2^{q−1}−1$ вариантов. Так делает Spark MLlib.

Дерево — это линейная модель над бинарными признаками «попал в область $J_j$». То есть дерево само «находит» полезные признаки, а потом строит над ними линейную модель. Многие нелинейные методы ML — это линейные модели + хитрое порождение признаков.

#### Бэггинг, случайные леса и bias-variance (л.8)

#### Градиентный бустинг (л.9)

#### XGBoost и стекинг (л.10)

___
Теория: [лекция 1]({{ site.baseurl }}/files/AI-big-data/lecture07-trees.pdf){:target="_blank"}, [лекция 2]({{ site.baseurl }}/files/AI-big-data/lecture08-ensembles.pdf){:target="_blank"}, [лекция 3]({{ site.baseurl }}/files/AI-big-data/lecture09-ensembles.pdf){:target="_blank"}, [лекция 4]({{ site.baseurl }}/files/AI-big-data/lecture10-ensembles.pdf){:target="_blank"}.

Задание в [блокноте]({{ site.baseurl }}/files/AI-big-data/homework-practice-03-ensembles.ipynb).

Может оказаться полезным посмотреть блокноты [1](https://github.com/esokolov/ml-course-hse/blob/master/2016-fall/seminars/sem07-trees.ipynb){:target="_blank"}, [2](https://github.com/esokolov/ml-course-hse/blob/master/2016-fall/seminars/sem08-ensembles.pdf){:target="_blank"}, [3](https://github.com/esokolov/ml-course-hse/blob/master/2016-fall/seminars/sem09-ensembles.pdf){:target="_blank"}, [4](https://github.com/esokolov/ml-course-hse/blob/master/2016-fall/seminars/sem10-ensembles.ipynb){:target="_blank"}, потому что там есть картинки, хорошие объяснения и примеры кода.

Успехов!


<div class="row">
  <div class="col-lg-12">
    <ul class="list-unstyled">
      <li class="float-end">
        <button type="button" class="btn btn-outline-primary" onclick="window.location.href='#ансамбли';">Вверх</button>
      </li>
      <li  class="float-end">
       <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/artificial-intelligence/big-data/labs/lab6.html';">ЛР №6 →</button>
     </li>
      <li>
        <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/artificial-intelligence/big-data/labs/lab4.html';">← ЛР №4</button>
      </li>
    </ul>
  </div>
</div>
