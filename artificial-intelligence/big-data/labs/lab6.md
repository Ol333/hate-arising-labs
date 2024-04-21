<ol class="breadcrumb">
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}">Главная</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/artificial-intelligence/index.html">ИИ</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/artificial-intelligence/big-data/index.html">Обработка данных</a></li>
  <li class="breadcrumb-item active">ЛР №6</li>
</ol>

# Кластеризация

Теория: [лекция]({{ site.baseurl }}/files/AI-big-data/lecture12-unsupervised.pdf){:target="_blank"}.

Может оказаться полезным посмотреть блокнот [1](https://github.com/esokolov/ml-course-hse/blob/master/2016-fall/seminars/sem13-pca.ipynb){:target="_blank"}, потому что там есть картинки, хорошие объяснения и примеры кода.

___

Задание в [блокноте]({{ site.baseurl }}/files/AI-big-data/homework-practice-04-unsupervised.ipynb).
Чтобы сдать лабораторную, нужно продемонстрировать работу блокнота **на университетском компьютере** (У801).

Для этого вам потребуется настроить виртуальное окружение (любое, на ваш выбор). Распространенные варианты:
<ul>
  <li><b>pipenv</b>
  <pre><code class="console">pip3 install pipenv
pipenv --python 3.11  </code></pre> 
  Заменяете созданные Pipfile и Pipfile.lock на <a href="{{ site.baseurl }}/files/AI-big-data/Pipfile">Pipfile</a> и <a href="{{ site.baseurl }}/files/AI-big-data/Pipfile.lock">Pipfile.lock</a>.
  <pre><code class="console">pipenv install --dev
pipenv shell
jupyter notebook  </code></pre> 
  </li>
  <li><b>venv</b>
  <pre><code class="console">python3.11 -m venv your_env_name</code></pre>
  Если выходит ошибка с предложением команды <code class="console">apt-get install python-venv</code>, обратитесь к преподавателю.
  <pre><code class="console">source your_env_name/bin/activate
pip install jupyter
pip install ..</code></pre> 
  </li>
</ul>

<div class="row">
  <div class="col-lg-12">
    <ul class="list-unstyled">
      <li class="float-end">
        <button type="button" class="btn btn-outline-primary" onclick="window.location.href='#кластеризация';">Вверх</button>
      </li>
      <li>
        <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/artificial-intelligence/big-data/labs/lab5.html';">← ЛР №5</button>
      </li>
    </ul>
  </div>
</div>