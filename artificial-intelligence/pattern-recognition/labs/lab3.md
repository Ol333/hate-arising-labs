<ol class="breadcrumb">
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}">Главная</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/artificial-intelligence/index.html">ИИ</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/artificial-intelligence/pattern-recognition/index.html">Распознавание образов</a></li>
  <li class="breadcrumb-item active">ЛР №3</li>
</ol>

<nav>
  <ul></ul>
</nav>

# Опознание объекта, но быстрее

Обнаружение объекта требует выделения на изображении области, где предположительно может быть объект и классификации этого фрагмента изображения.

[*](https://libeldoc.bsuir.by/bitstream/123456789/43782/1/Verkhov_Metody.pdf)
Методы обнаружения объектов, как правило, основаны либо на машинном обучении, либо на глубоком обучении.

Для методов, основанных на машинном обучении, сначала требуется определить особенности объекта, перед тем как классифицировать его. Далее, с помощью техник схожих с методом опорных векторов, осуществляется классификация объекта.

Примеры методов с использованием машинного обучения:
* алгоритм Виолы-Джонса, основанный на признаках Хаара;
* масштабно-инвариантная трансформация признаков;
* гистограмма направленных градиентов.


Для методов, основанных на глубоком обучении, свойственно использование сверточных нейронных сетей, которые позволяют осуществлять обнаружение объекта без использования списка специфических особенностей данного объекта.

Примеры методов с использованием глубокого обучения:
* Region Proposals (с использованием различных региональных сверточных нейронных сетей: R-CNN, Fast R-CNN, Faster R-CNN, cascade R-CNN);
* SSD (Single-Shot MultiBox Detector);
* YOLO (You Only Look Once);
* RetinaNet;
* RefineDet (Single-Shot Refinement Neural Network for Object Detection);
* Deformable ConvNets (Deformable convolutional networks).

Данные методы базируются на сверточных нейронных сетях, основной идеей которых является чередование сверточных и субдискретизирующих слоев, а также наличие операции свертки, в процессе которой на матрицу свертки поэлементно умножается каждый фрагмент изображения, суммируется и записывается в соответствующую позицию в выходном изображении.




### YOLO

Суть данного метода заключается в первоначальном разделении изображения на сетку ячеек.
Каждая ячейка отвечает за расположение области объекта на изображении, если центр данной
области находится в пределах ячейки. Для каждой области определяются координаты x и y, ши-
рина и высота области, а также коэффициент уверенности, который показывает вероятность
наличия в данной области какого-либо объекта. Кроме того, каждая клетка определяет класс
объекта в области, которая относится к этой клетке.

Старая, но доходчивая статья про [YOLO v3](https://proglib.io/p/raspoznavanie-obektov-s-pomoshchyu-yolo-v3-na-tensorflow-2-0-2020-11-08).

Все более выстрые версии, предлагаются различными исследователями довольно часто: [9-я](https://viso.ai/computer-vision/yolov9/) в феврале 2024, [10-я](https://blog.roboflow.com/deploy-yolov10-model/) в мае, [11-я](https://www.ultralytics.com/ru/blog/ultralytics-yolo11-has-arrived-redefine-whats-possible-in-ai) в сентябре.

С помощью библиотеки `ultralytics` (ставится через `pip`, но долго) можно поработать с моделью YOLO v11.
Ниже простой пример использования (***удобно каждую строчку поместить в отдельную ячейку jupyter notebook***)[*](https://docs.ultralytics.com/quickstart/#use-ultralytics-with-python):

```python
from ultralytics import YOLO

# Построить новую модель
model = YOLO("yolo11n.yaml")
# Загрузить предобученную модель (рекомендуется для дальнейшего обучения)
model = YOLO("yolo11n.pt")
# Обучить модель на данных датасета небольшого COCO8
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)

# Продемонстрировать обнаружение объекта на изображенях из папки с прошлой лабы
results = model(["recog_2/10.jpg", "recog_2/9.jpg"])
for result in results:
  result.show()
```

Обучение этой модели происходило на датасете COCO, который является относительно небольшим.
Если попробовать дообучить модель на более обширном датасете VOC (заменив в методе `train`  только источник данных с `"coco8.yaml"` на `"VOC.yaml"`), то потребуется ~ 3.5 ч * 100 эпох в Goggle Colab (если опустить время, пока датасет скачается).

## Задание 1

Для модели YOLO сравните точность обнаружения в случаях:
1. Новой модели, которую обучили.
1. Предобученной модели без дообучения.
1. Предобученной модели, которую дообучили.

## Задание 2

* Посмотреть страничку с описанием модели обнаружения объекта по варианту.
* Посмотреть все упоминавшиеся источники и найти дополнительную  информацию о модели самостоятельно.
* Улучшить описание модели в файле `markdown`. Можно расписать понятнее, добавить картинки, схемы, формулы, примеры работы, примеры с другими реализациями/библиотеками и т.д. 
* Прислать файл преподавателю на почту (bobrovskaya_op@surgu.ru) или сделать pull request в [репозиторий](https://github.com/Ol333/hate-arising-labs).
* Чтобы сдать лабораторную необходимо 1 из 2:
  1. Знать как работает модель (разобраться с архитектурой);
  2. Знать как использовать (запустить модель).

[Справка по markdown](https://doka.guide/tools/markdown/)

[Пример отчета, размещенного на github](https://github.com/still-coding/report_demo)

[Одно из расширений VSCode для превью .md](https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced)


<div class="table-responsive">
<table class="table table-hover border-primary  table-bordered ">
  <thead>
    <tr class="table-dark">
      <th scope="col">№ варианта</th>
      <th scope="col">Тема</th>
      <th scope="col">Страничка</th>
      <th scope="col">Скачать</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">1</th>
      <td>SSD</td>
      <td><a href="{{ site.baseurl }}/artificial-intelligence/pattern-recognition/labs/lab3_data/SSD.html" target="_blank">SSD</a></td>
      <td><a href="{{ site.baseurl }}/artificial-intelligence/pattern-recognition/labs/lab3_data/SSD.md" download>↓</a></td>
    </tr>
    <tr>
      <th scope="row">2</th>
      <td>RefineDet</td>
      <td><a href="{{ site.baseurl }}/artificial-intelligence/pattern-recognition/labs/lab3_data/RefineDet.html" target="_blank">RefineDet</a></td>
      <td><a href="{{ site.baseurl }}/artificial-intelligence/pattern-recognition/labs/lab3_data/RefineDet.md" download>↓</a></td>
    </tr>
    <tr>
      <th scope="row">3</th>
      <td>Deformable ConvNets</td>
      <td><a href="{{ site.baseurl }}/artificial-intelligence/pattern-recognition/labs/lab3_data/DCN.html" target="_blank">Deformable ConvNets</a></td>
      <td><a href="{{ site.baseurl }}/artificial-intelligence/pattern-recognition/labs/lab3_data/DCN.md" download>↓</a></td>
    </tr>
    <tr>
      <th scope="row">4</th>
      <td>RetinaNet</td>
      <td><a href="{{ site.baseurl }}/artificial-intelligence/pattern-recognition/labs/lab3_data/RetinaNet.html" target="_blank">RetinaNet</a></td>
      <td><a href="{{ site.baseurl }}/artificial-intelligence/pattern-recognition/labs/lab3_data/RetinaNet.md" download>↓</a></td>
    </tr>
    <tr>
      <th scope="row">5</th>
      <td>Faster R-CNN</td>
      <td><a href="{{ site.baseurl }}/artificial-intelligence/pattern-recognition/labs/lab3_data/FasterRCNN.html" target="_blank">Faster R-CNN</a></td>
      <td><a href="{{ site.baseurl }}/artificial-intelligence/pattern-recognition/labs/lab3_data/FasterRCNN.md" download>↓</a></td>
    </tr>
    <tr>
      <th scope="row">6</th>
      <td>CenterNet</td>
      <td><a href="{{ site.baseurl }}/artificial-intelligence/pattern-recognition/labs/lab3_data/CenterNet.html" target="_blank">CenterNet</a></td>
      <td><a href="{{ site.baseurl }}/artificial-intelligence/pattern-recognition/labs/lab3_data/CenterNet.md" download>↓</a></td>
    </tr>
   </tbody>
</table>
</div>

<div class="row">
  <div class="col-lg-12">
    <ul class="list-unstyled">
      <li class="float-end">
        <button type="button" class="btn btn-outline-primary" onclick="window.location.href='#опознание-объекта-но-быстрее';">Вверх</button>
      </li>
      <li  class="float-end">
       <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/artificial-intelligence/pattern-recognition/labs/lab4.html';">ЛР №4 →</button>
     </li>
      <li>
        <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/artificial-intelligence/pattern-recognition/labs/lab2.html';">← ЛР №2</button>
      </li>
    </ul>
  </div>
</div>