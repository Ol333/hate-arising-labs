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

Используя библиотеку Keras на Python мы будем обучать нейронную сеть, аппроксимирующую функцию $f(x) = sin(x)+sin( \sqrt{2} x)$, которая представлена на рис. ниже.

<div class="card border-primary mb-2" style="max-width: 30rem;">
    <div class="card-body">
    <img src="{{ site.baseurl }}/img/ANN_aperiod.jpg"
          alt="sin"  focusable="false" width="100%"
          class="d-block user-select-none" />
    </div>
  </div>

# Задание

## Шаг 1

* Создать набор данных на две колонки: $X$ от -20 до 20 с шагом 0.1 и $Y=f(x)$.
* Скопировать код:

``` python
# Разделить на обучающую и тестовую выборки.
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=13)

# Обучить с указанными параметрами.
model.compile(loss='mse', optimizer='rmsprop', metrics=['mae'])
model.fit(X_train, y_train, epochs=150, batch_size=10)

# Посчитать и вывести точность на обучающем и тестовом наборах данных.
_, accuracy = model.evaluate(X_train, y_train)
_, accuracy2 = model.evaluate(model.predict(X_test), y_test)
```

* Вывести график функции и точек предсказания нейронки на тестовом наборе.
* Сравнить с [рис.](#multihead) выше. Точность обучения - это `accuracy * 100`.
* **Подобрать наиболее простую архитектуру сети (количество слоев, количество нейронов в слоях, функции активации), которая обеспечивает близкую точность.**


## Шаг 2

Знание о периодичности нашей функции (одни и те же значения повторяются через каждые $2\pi$ единиц $x$) позволяет увидеть, как можно облегчить нейронной сети жизнь.

* Выделить из функции две переменные: номер периода ($T$) и смещение внутри периодически повторяющегося участка кривой ($\varphi$).
* Обучить сеть по двум входам ($T$, $\varphi$) предсказывать один выход ($Y$).
* Подобрать наиболее простую архитектуру сети, которая обеспечивает достаточную ($< 15$) точность. Сравнить с предыдущим вариантом.

## Шаг 3

То, что мы увидели периодичность и вручную выделили нужные переменные из исходной - это хорошо, но можно ли и эту часть обработки данных переложить на нейронную сеть?

* Обучить три сети и объединить:
  * Создать две отдельные сети, которые будут извлекать значения периода и смещения из исходной переменной. Первая сеть обучается по $x$ предсказывать $T$, вторая - $x$ → $\varphi$.
  * Подобрать архитектуры, хорошо обучить.
  * Объединить три предварительно обученные сети ($^1 x → T$, $^2 x → \varphi$, $^3 (T, \varphi) → Y=f(x)$) в [одну сложную](https://keras.io/api/layers/merging_layers/concatenate/){:target="_blank"}. Вывести результат.
* Сначала объединить три сети в одну сложную. Затем обучить. Вывести результат.
* Сравнить с предыдущими решениями.


Принимаются идеи улучшения, альтернативные решения, и объяснения, почему рассмотренное работает так, как оно работает.

<div class="row">
  <div class="col-lg-12">
    <ul class="list-unstyled">
      <li class="float-end">
        <button type="button" class="btn btn-outline-primary" onclick="window.location.href='#multihead';">Вверх</button>
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
