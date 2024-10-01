<ol class="breadcrumb">
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}">Главная</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/artificial-intelligence/index.html">ИИ</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/artificial-intelligence/ANN/index.html">ИНС</a></li>
  <li class="breadcrumb-item active">ЛР №4</li>
</ol>

<nav>
  <ul></ul>
</nav>

# Keras

Читаем [Шолле](https://codernet.ru/books/python/glubokoe_obuchenie_na_python_sholle_fransua/){:target="_blank"} стр. 81 – 119 и **реализуем то, что описывается**:
* стр. 92 – 102. Пример бинарной классификации (отзывы к фильмам);
* стр. 102 – 111. Пример многоклассивой классификации (новостные ленты);
* стр. 111 – 118. Пример регрессии (предсказание цен на дома).

## Задание 🔮

Используя библиотеку Keras на Python:

1. Обучить нейронку, аппроксимирующую функцию $f(x) = x$:
  * Создать набор данных на две колонки: $X$ от -20 до 20 с шагом 0.1 и $Y$.
  * Разделить на обучающую и тестовую выборки.
  * Обучить.
  * Вывести точность на обучающей выборке.
  * Вывести точность на тестовой выборке.
  * Вывести график функции и точек предсказания нейронки на тестовом наборе.
2. Обучить нейронку, аппроксимирующую функцию $f(x) = \vert x \vert $.
3. Обучить нейронку, аппроксимирующую окружность.
4. Обучить нейронку, аппроксимирующую функцию $f(x) = sin(x)$.
5. Найти на [Kaggle](https://www.kaggle.com/datasets){:target="_blank"} набор данных для классификации и обучить на нем модель. **Сохранить ссылку на набор данных, чтобы не потерять.**
6. Показать на графике, как меняется ошибка в процессе обучения (для одной из предыдущих НС).

## Пример вывода результата обучения

{% tabs ANN_4 %}

{% tab ANN_4 График %}
<div class="card border-primary mb-2" style="max-width: 30rem;">
  <div class="card-body">
    <img src="{{ site.baseurl }}/img/ANN_sin.jpg"
        alt="sin"  focusable="false" width="100%"
        class="d-block user-select-none" />
  </div>
</div>
{% endtab %}

{% tab ANN_4 Код для графика %}

``` python
#...
model.compile(loss='mse', optimizer='rmsprop', metrics=['mae'])
model.fit(X_train, y_train, epochs=param["epochs"], batch_size=param["batch_size"])
_, accuracy = model.evaluate(X_train, y_train)
_, accuracy2 = model.evaluate(model.predict(X_test), y_test)
predictions = model.predict(X_train)
plt.figure(figsize=(10., 10.))
title = str(list((str(dense[j]) +' '+ str(activation[j]) for j in range(len(param["layers"])))))
plt.title(title + "\nepochs="+str(param["epochs"])+" batch_size="+str(param["batch_size"])+"\nточность обучения %.2f, точность на тесте %.2f" % (accuracy*100, accuracy2*100))
for i in range(len(X_train)):
    plt.scatter((X_train)[i], predictions[i], c='red', label=('prediction' if i==0 else None))
plt.plot(x, y, c='blue', label=param["func_label"], marker='X')
plt.scatter(X_test, model.predict(X_test), c='green', label='тест')
plt.legend()
```
{% endtab %}

{% endtabs %}

<div class="row">
  <div class="col-lg-12">
    <ul class="list-unstyled">
      <li class="float-end">
        <button type="button" class="btn btn-outline-primary" onclick="window.location.href='#keras';">Вверх</button>
      </li>
      <li  class="float-end">
       <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/artificial-intelligence/ANN/labs/lab5.html';">ЛР №5 →</button>
     </li>
      <li>
        <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/artificial-intelligence/ANN/labs/lab3.html';">← ЛР №3</button>
      </li>
    </ul>
  </div>
</div>
