<ol class="breadcrumb">
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}">Главная</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/artificial-intelligence/index.html">ИИ</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/artificial-intelligence/ANN/index.html">ИНС</a></li>
  <li class="breadcrumb-item active">ЛР №5</li>
</ol>

<nav>
  <ul></ul>
</nav>

# Multihead

# Задание

Используя библиотеку Keras на Python выполнить следующее:

## Шаг 1

Обучить нейронку, аппроксимирующую функцию $f(x) = sin(x)+sin( \sqrt{2} x)$:

<ul>
<li>
  Создать набор данных на две колонки: $X$ от -20 до 20 с шагом 0.1 и $Y=f(x)$.
</li>
<li>
  Разделить на обучающую и тестовую выборки, как указано ниже:
  <pre><code class="lang-python">X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=13)</code></pre>
</li>
<li>
  Обучить с указанными ниже параметрами:
  <pre><code class="lang-python">model.compile(loss='mse', optimizer='rmsprop', metrics=['mae'])
model.fit(X_train, y_train, epochs=150, batch_size=10)</code></pre>
</li>
<li>
  Посчитать и вывести точность на обучающем и тестовом наборах данных.
  <pre><code class="lang-python">_, accuracy = model.evaluate(X_train, y_train)
_, accuracy2 = model.evaluate(model.predict(X_test), y_test)</code></pre>
</li>
<li>
  Вывести график функции и точек предсказания нейронки на тестовом наборе.
</li>
<li>
  Сравнить с рис. ниже. Точность обучения - это accuracy*100.

  <div class="card border-primary mb-2" style="max-width: 30rem;">
    <div class="card-body">
    <img src="{{ site.baseurl }}/img/ANN_aperiod.jpg"
          alt="sin"  focusable="false" width="100%"
          class="d-block user-select-none" />
    </div>
  </div>
</li>
<li>
  <b>Подобрать наиболее простую архитектуру сети (количество слоев, количество нейронов в слоях, функции активации), которая обеспечивает близкую точность.</b>
</li>
</ul>

## Шаг 2

Знание о периодичности нашей функции (одни и те же значения повторяются через каждые $2\pi$ единиц $x$) позволяет увидеть, как можно облегчить нейронной сети жизнь.

<ul>
<li>
  Выделить из функции две переменные: номер периода ($T$) и смещение внутри периодически повторяющегося участка кривой ($\varphi$).
</li>
<li>
  Обучить сеть на двух входах ($T$, $\varphi$) предсказывать один выход ($Y$).
</li>
<li>
  Подобрать наиболее простую архитектуру сети, которая обеспечивает достаточную ($< 15$) точность. Сравнить с предыдущим вариантом.
</li>
</ul>

## Шаг 3

То, что мы увидели периодичность и вручную выделили нужные переменные из исходной - это хорошо, но можно ли и эту часть обработки данных переложить на нейронную сеть?

<ul>
<li>
  Создать две отдельные сети, которые будут извлекать значения периода и смещения из исходной переменной. Первая сеть обучается по $x$ предсказывать $T$, вторая - по $x$ → $\varphi$.
</li>
<li>
  Подобрать архитектуры, хорошо обучить.
</li>
<li>
  Объединить предварительно обученные сети ($^1 x → T$, $^2 x → \varphi$, $^3 (T, \varphi) → Y=f(x)$) в одну сложную. Вывести результат.
</li>
<li>
  Сначала объединить сети в одну сложную. Затем обучить. Вывести результат.
</li>
<li>
  Сравнить с предыдущими решениями.
</li>
</ul>


Принимаются идеи улучшения, альтернативные решения, и объяснения, почему рассмотренное работает так, как оно работает.

<div class="row">
  <div class="col-lg-12">
    <ul class="list-unstyled">
      <li class="float-end">
        <button type="button" class="btn btn-outline-primary" onclick="window.location.href='#keras';">Вверх</button>
      </li>
      <li  class="float-end">
       <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/artificial-intelligence/ANN/labs/lab6.html';">ЛР №6 →</button>
     </li>
      <li>
        <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/artificial-intelligence/ANN/labs/lab4.html';">← ЛР №4</button>
      </li>
    </ul>
  </div>
</div>
