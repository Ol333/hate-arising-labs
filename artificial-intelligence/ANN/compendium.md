<ol class="breadcrumb">
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}">Главная</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/artificial-intelligence/index.html">ИИ</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/artificial-intelligence/ANN/index.html">ИНС</a></li>
  <li class="breadcrumb-item active">Памятка</li>
</ol>

# ИНС. Обучение с учителем

Если у вас нет каких-то важных причин отступать от следующего плана, то придерживайтесь его. Во всяком случае будет неплохо с него начать.

<ol>
<li>
  Определиться с набором данных $X$ и целевой переменной $Y=f(x)$. Целевая переменная может быть одна (значение - в регрессии, класс - в классификации), или их может быть несколько (массив значений вероятности для множества классов).
  <div class="table-responsive">
    <table class="table table-bordered">
        <tbody>
            <tr class="table-active">
                <td>$X_1$</td>
                <td>$X_2$</td>
                <td>..</td>
                <td>$X_n$</td>
                <td>$Y$</td>
            </tr>
            <tr>
                <td colspan="4" align="center">1 объект</td>
                <td>цель 1</td>
            </tr>
            <tr>
                <td colspan="4" align="center">2 объект</td>
                <td>цель 1</td>
            </tr>
            <tr>
                <td colspan="4" align="center">..</td>
                <td>..</td>
            </tr>
            <tr>
                <td colspan="4" align="center">m-ый объект</td>
                <td>цель m</td>
            </tr>
        </tbody>
    </table>
  </div>
</li>
<li>
  Предобработка данных <i>(приведение типов, повороты и растяжения. удаление пропусков)</i>. Все преобразования производятся над данными до их разделения на выборки. Для удобства последующего использования модели с новыми данными, стоит оформить обработку как функцию <code class="lang-python">def</code>.
</li>
<li>
  Разделить данные ($X, Y$) на обучающую и тестовую выборки
  <pre><code class="lang-python">from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.25, random_state=13)</code></pre>
</li>
<li>
  Создать модель. Накидать слоёв (в соответствии с вашими целями).
</li>
<li>
  Собрать модель, подобрав нужные для конкретного типа задачи функцию потерь и проч. аргументы
  <pre><code class="lang-python">model.compile(loss='?', optimizer='?', metrics=['?'])</code></pre>
</li>
<li>
  Обучить нейросеть, чтобы она, получая на вход <code class="lang-python">X_train</code>, предсказывала значения <code class="lang-python">y_train</code>. От аргументов <code class="lang-python">epochs</code> и <code class="lang-python">batch_size</code> будет зависеть время обучения и точность модели на обучающей выборке
  <pre><code class="lang-python">model.fit(X_train, y_train, epochs=?, batch_size=?)</code></pre>
</li>
<li>
  Посчитать и вывести точность на тестовом наборе данных (который не участвовал в обучении).
  <pre><code class="lang-python">_, accuracy = model.evaluate(model.predict(X_test), y_test)</code></pre>
</li>
<li>
  Если позволяет задача, вывести график с данными и предсказаниями нейронки на тестовом наборе. Проверить, что сделанное совпадает с задуманным.
</li>
<li>
  Поэкспериментировать с архитектурой сети (количество слоев, количество нейронов в слоях, функции активации), попытаться улучшить точность и упростить архитектуру.
</li>
</ol>


<div class="row">
  <div class="col-lg-12">
    <ul class="list-unstyled">
      <li class="float-end">
        <button type="button" class="btn btn-outline-primary" onclick="window.location.href='#инс-обучение-с-учителем';">Вверх</button>
      </li>
      <!-- <li  class="float-end">
       <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/artificial-intelligence/ANN/labs/lab7.html';">ЛР №7 →</button>
     </li>
      <li>
        <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/artificial-intelligence/ANN/labs/lab5.html';">← ЛР №5</button>
      </li> -->
    </ul>
  </div>
</div>