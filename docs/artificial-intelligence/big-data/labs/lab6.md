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

Для этого вам потребуется настроить виртуальное окружение, установить библиотеку `jupyter`, запустить сервер `jupyter notebook`, и установить библиотеки необходимые для работы вашего кода.

* Могу посоветовать `pipenv` и [Pipfile]({{ site.baseurl }}/files/AI-big-data/Pipfile) и [Pipfile.lock]({{ site.baseurl }}/files/AI-big-data/Pipfile.lock) для него.

* Если хотите воспользоваться `venv`, а выходит ошибка с предложением команды `apt-get install python-venv`, обратитесь к преподавателю.

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