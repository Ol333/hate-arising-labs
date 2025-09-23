<ol class="breadcrumb">
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}">Главная</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/artificial-intelligence/index.html">ИИ</a></li>
  <li class="breadcrumb-item"><a href="{{ site.baseurl }}/artificial-intelligence/pattern-recognition/index.html">Распознавание образов</a></li>
  <li class="breadcrumb-item active">ЛР №5</li>
</ol>

<nav>
  <ul></ul>
</nav>


# Отслеживание объекта

До этого мы занимались обработкой изображений. Во многих из рассмотренных методов акцентировалось внимание на скорости работы (один проход, два прохода). Это не особо важно для обработки одного изображения, но становится важным при работе с видео (последовательностью множества изображений) и еще важнее, если обработка идет в реальном времени.

Отслеживание объекта в видеопотоке подразумевает решение задачи обнаружения объекта на каждом последовательном изображении и идентификацию этого объекта, т.е. определения, что на новом кадре это все тот же объект.

Знакомая нам модель YOLO может справиться с отслеживанием объектов, на которых она обучалась. Попробуем научить ее отслеживать новый, незнакомый ей объект.

## План

**Объект** - монетка.

**Модель** - YOLO 8.

#### Шаг 0. Сбор данных

* Снять несколько 10 сек видео, где объект перемещается в кадре. Будет легче, если:
  * объект четко выделяется на фоне;
  * положение камеры и освещение фиксированы;
  * качество съемки может быть плохим.

<div class="card border-primary mb-2" style="max-width: 15rem;">
  <div class="card-body">
    <img src="{{ site.baseurl }}/img/track_1.gif"
        alt="test video" focusable="false" width="100%"
        class="d-block user-select-none" />
  </div>
</div>

Проверяем, что yolo не отслеживает монетки:

___

{% tabs recog_track_1 %}

{% tab recog_track_1 Код %}

``` python
from ultralytics import YOLO

# Загрузка предобученной модели YOLOv8
model = YOLO("yolov8n.pt")

# Путь к вашему видео
video_path = "/content/VID_20230408_143103.mp4"

# Выполнение предсказаний
model.predict(source=video_path, show=True, save=True, save_txt=True)
```
{% endtab %}

{% tab recog_track_1 Результат %}
<div class="card border-primary mb-2" style="max-width: 15rem;">
  <div class="card-body">
    <img src="{{ site.baseurl }}/img/track_2.gif"
        alt="test video" focusable="false" width="100%"
        class="d-block user-select-none" />
  </div>
</div>
{% endtab %}

{% endtabs %}

___

Модель отслеживает объект, но класс, который она ему присваивает - не верный.

#### Шаг 1. Предобработка данных

* Здесь можно было бы наложить ч/б  фильтр или изменить размер картинки, но мы этого делать не будем ***(и очень зря, ведь очистка и аугментация данных могут повысить скорость обучения и точность модели)***.

#### Шаг 2. Разметка данных

* Разметить данные: на каждом кадре видео заключить объект в рамку *bounding boxes*.
* Сохранить аннотации в формате, совместимом с выбранной моделью.

Используя [LabelStudio](https://labelstud.io/guide/get_started.html){:target="_blank"}, выделим на видео объект монетки.

<div class="card border-primary mb-2" style="max-width: 50rem;">
  <div class="card-body">
    <img src="{{ site.baseurl }}/img/label-studio_2.png"
        alt="test video" focusable="false" width="100%"
        class="d-block user-select-none" />
  </div>
</div>

Поскольку экспортировать вышло только json, а не то, что ожидает модель YOLO, нужно доработать:
  * Разбить видео на фреймы и для каждого получившегося изображения создать текстовый файл с метками (номер класса объекта, координаты x, y, ширина и высота рамки).


#### Шаг 3. Подготовка данных

* Поскольку мы пропустили подготовку данных, будем делать это сейчас (*лучше бы раньше, но раньше уже закончилось*):
  * Уменьшить размер изображений до 640x640. Это уменьшит размер датасета и ускорит обучение модели.

* Разбить данные на обучающую, тестовую и валидационную выборки.

Получится следующая структура :

```bash
dataset/
    images/
        train/
        val/
        test/
    labels/
        train/
        val/
        test/
```

#### Шаг 4. (До)Обучение

* Создаем файл data.yaml с описанием датасета, который необходим модели YOLO:

```python
train: /content/dataset/images/train  # Путь к обучающим изображениям
val: /content/dataset/images/val      # Путь к валидационным изображениям

nc: 1                        # Количество классов
names: ['Coin']              # Имена классов
```

* Используем предобученную модель.

```python
model = YOLO("yolov8n.pt")
results = model.train(data="data.yaml", epochs=5, imgsz=640)
```

Интересные метрики, приведены в таблице ниже. В процессе обучения уменьшаются потери ***box_loss*** (координаты ограничивающих рамок), ***cls_loss*** (классы объектов).

<div class="table-responsive">
<table class="table table-hover border-primary table-bordered">
  <thead>
    <tr class="table-dark">
      <th scope="col"></th>
      <th scope="col">box_loss</th>
      <th scope="col">cls_loss</th>
      <th scope="col">mAP50</th>
      <th scope="col">mAP50-95</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">1 эпоха</th>
      <td>1.403</td>
      <td>0.47</td>
      <td>0.604</td>
      <td>0.464</td>
    </tr>
    <tr>
      <th scope="row">50 эпоха</th>
      <td>3.013</td>
      <td>0.53</td>
      <td>0.634</td>
      <td>0.896</td>
    </tr>
   </tbody>
</table>
</div>

*mAP (Mean Average Precision)* показывает, насколько хорошо модель обнаруживает объекты и классифицирует их. *mAP50* — это среднее значение точности для всех классов объектов при пороге IoU (Intersection over Union) 0.5.

$IoU=\frac{\text{Area of Overlap}}{\text{Area of Union}}$ — метрика, которая измеряет пересечение предсказанной и истинной ограничивающей рамки относительно их объединения. Когда IoU равен 0.5, это означает, что пересечение предсказанной и истинной рамки составляет 50% от их объединения. mAP50 учитывает только те предсказания, у которых IoU больше или равен 0.5.

*mAP50-95* — это среднее значение точности для всех классов объектов при различных порогах IoU от 0.5 до 0.95 с шагом 0.05. Это более строгая метрика, которая учитывает предсказания с различными уровнями точности. mAP50-95 вычисляется как среднее значение точности для всех этих порогов.

В общем случае, значения `mAP50` $> 0.7$ и `mAP50-95` $> 0.5$ считаются хорошими.

#### Шаг 5. Тестирование

* Отслеживание объекта (если вы не повторяли прилежно все шаги выше, можете взять [веса]({{ site.baseurl }}/files/AI-recognition/best.pt) и [файл](https://disk.yandex.ru/i/83iGOLjla31X7A){:target="_blank"}):

___

{% tabs recog_track_2 %}

{% tab recog_track_2 Код %}
```python
# Загрузка обученной модели
model = YOLO("/content/runs/detect/train/weights/best.pt")

# Обработка видео
video_path = "/content/dataset/videos/d7577ff4-VID_20230408_143103.mp4"
model.predict(source=video_path, show=True, save=True)
```
{% endtab %}

{% tab recog_track_2 Результат %}
<div class="card border-primary mb-2" style="max-width: 15rem;">
  <div class="card-body">
    <img src="{{ site.baseurl }}/img/track_3.gif"
        alt="test video" focusable="false" width="100%"
        class="d-block user-select-none" />
  </div>
</div>
{% endtab %}

{% endtabs %}

___


Как видите, модель неплохо работает даже с учетом того, что обучалась на сжатых данных 640x640, а тестируется на оригинальном формате 1920x1080 (или сжатой версии 640x360).

Можно проверить, как она обработает сжатое (деформированное) изображение, которое потом будет преобразовано обратно с пропорциональным растяжением метки.

___

{% tabs recog_track_3 %}

{% tab recog_track_3 Результат %}
<div class="card border-primary mb-2" style="max-width: 15rem;">
  <div class="card-body">
    <img src="{{ site.baseurl }}/img/track_4.gif"
        alt="test video" focusable="false" width="100%"
        class="d-block user-select-none" />
  </div>
</div>
{% endtab %}

{% tab recog_track_3 Код %}
```python
import cv2

# Путь к обученной модели
model = YOLO("/content/runs/detect/train/weights/best.pt")

# Путь к видео
video_path = "/content/d7577ff4-VID_20230408_143103.mp4"
output_video_path = "output_video.mp4"

# Открываем видео
cap = cv2.VideoCapture(video_path)
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Сжимаем кадр до 640x640
    resized_frame = cv2.resize(frame, (640, 640))

    # Обрабатываем кадр моделью
    results = model(resized_frame)

    # Масштабируем результаты обратно в 1080x1920
    for result in results:
        for box in result.boxes.xyxy:
            x1, y1, x2, y2 = box[:4]
            x1 = int(x1 * (width / 640))
            x2 = int(x2 * (width / 640))
            y1 = int(y1 * (height / 640))
            y2 = int(y2 * (height / 640))

            # Рисуем прямоугольник на исходном кадре
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Сохраняем обработанный кадр
    out.write(frame)

cap.release()
out.release()
print("Обработка видео завершена.")
```
{% endtab %}

{% endtabs %}

___

#### Шаг 6. Отслеживание

Для отслеживания объектов на видео нужен алгоритм отслеживания, который сопостовляет обнаруженные объекты на текущем кадре с объектами на предыдущих кадрах.

Используем DeepSORT для трекинга из библиотеки `deep_sort_realtime`.

___

{% tabs recog_track_4 %}

{% tab recog_track_4 Результат %}
<div class="card border-primary mb-2" style="max-width: 15rem;">
  <div class="card-body">
    <img src="{{ site.baseurl }}/img/track_5.gif"
        alt="test video" focusable="false" width="100%"
        class="d-block user-select-none" />
  </div>
</div>
{% endtab %}

{% tab recog_track_4 Код %}
```python
from deep_sort_realtime.deepsort_tracker import DeepSort

# Инициализация YOLO модели
model_path = "/content/runs/detect/train2/weights/best.pt"  # Укажите путь к вашей модели
model = YOLO(model_path)

# Инициализация трекера DeepSORT
tracker = DeepSort(max_age=70, n_init=5, max_cosine_distance=0.7, nn_budget=None)

# Открываем видео
video_path = "/content/dcf73189-VID_20230408_143121.mp4"
output_path = "output_video_3.mp4"
cap = cv2.VideoCapture(video_path)

# Получаем информацию о разрешении и FPS видео
fps = int(cap.get(cv2.CAP_PROP_FPS))
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Сжимаем кадр для обработки YOLO
    resized_frame = cv2.resize(frame, (640, 640))

    # Обработка кадра моделью YOLO
    results = model(resized_frame, conf=0.6, iou=0.5)

    detections = []
    for result in results:
        if len(result.boxes.xyxy) > 0:
            # Преобразуем tензор в numpy для удобства
            boxes = result.boxes.xyxy.cpu().numpy()  # Преобразуем в numpy массив
            conf = float(result.boxes.conf.cpu().numpy()[0])  # Уверенность модели
            cls = int(result.boxes.cls.cpu().numpy()[0])  # Класс объекта
            for box in boxes:
                x1, y1, x2, y2 = box[:4]
                # Масштабируем координаты обратно в оригинальное разрешение
                x1 = int(x1 * (frame_width / 640))
                x2 = int(x2 * (frame_width / 640))
                y1 = int(y1 * (frame_height / 640))
                y2 = int(y2 * (frame_height / 640))
                # Формат для трекера: [x1, y1, width, height, confidence, class_id]
                detections.append([[x1, y1, x2 - x1, y2 - y1], conf, cls])

    # Обновляем трекер
    tracks = tracker.update_tracks(detections, frame=frame)

    # Отображаем треки на кадре
    for track in tracks:
        if not track.is_confirmed():
            continue

        track_id = track.track_id
        ltrb = track.to_ltrb()
        x1, y1, x2, y2 = map(int, ltrb)

        # Рисуем прямоугольник и ID трека
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        label = f"ID {track_id}"
        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Сохраняем обработанный кадр
    out.write(frame)

cap.release()
out.release()
print(f"Обработка завершена, результат сохранён в {output_path}")
```
{% endtab %}

{% endtabs %}

___

Как видим, после того, как рука закрывает монету на продолжительное время, модель перестает отслеживать объект, и когда видит его вновь, то считает за новый. Зато успешно справляется с тем, чтобы следить за объектом, если его никто не перекрывает.

Можно попробовать изменять значения conf, iou для YOLO и max_age, n_init, max_cosine_distance для DeepSORT, чтобы улучшить отслеживание.

### Полезные источники:

* [Обучение модели обнаружения объектов YOLO на пользовательском наборе данных (2020)](https://proglib.io/p/obuchenie-modeli-obnaruzheniya-obektov-yolo-na-polzovatelskom-nabore-dannyh-2020-01-21){:target="_blank"}
* [Обучите YOLOv8 на пользовательском наборе данных (2023)](https://habr.com/ru/articles/714232/){:target="_blank"}
* [Как обнаруживать объекты, используя YOLO, OpenCV и PyTorch в Python (2021)](https://waksoft.susu.ru/2021/05/19/kak-vypolnit-obnaruzhenie-obektov-yolo-s-pomoshhyu-opencv-i-pytorch-v-python/){:target="_blank"}
* [Современные технологии трекинга объектов на видео (2020)](https://recog.ru/%D1%81%D0%BE%D0%B2%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%BD%D1%8B%D0%B5-%D1%82%D0%B5%D1%85%D0%BD%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D0%B8-%D1%82%D1%80%D0%B5%D0%BA%D0%B8%D0%BD%D0%B3%D0%B0-%D0%BE%D0%B1%D1%8A/){:target="_blank"}

## Задание 🌇

* Самостоятельно снять несколько коротких видео с передвижением некоторого объекта.
  * Проверить (продемонстрировать), что используемая вами предобученная модель не в состоянии отслеживать те объекты, что вы хотите.
* Заменить один из шагов (или больше) по варианту. Можно изменить используемый инструмент на другой, на свою реализацию, свернуть несколько шагов в один альтернативный. **Результирующий набор использованных инструментов не должен совпадать в группе.** Можно добавить потоковую обработку видео.
* Реализовать программу, отслеживающую объект на видео.
* Если сдаете в течение пар семестра, то продемонстрировать работу модели. Если после - прислать на почту преподавателя подробный отчет о работе до экзамена.

<div class="table-responsive">
<table class="table table-hover border-primary table-bordered ">
  <thead>
    <tr class="table-dark">
      <th scope="col">№ варианта</th>
      <th scope="col">Шаг</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">1</th>
      <td>1</td>
    </tr>
    <tr>
      <th scope="row">2</th>
      <td>2</td>
    </tr>
    <tr>
      <th scope="row">3</th>
      <td>3</td>
    </tr>
    <tr>
      <th scope="row">4</th>
      <td>4</td>
    </tr>
    <tr>
      <th scope="row">5</th>
      <td>5</td>
    </tr>
    <tr>
      <th scope="row">6</th>
      <td>6</td>
    </tr>
   </tbody>
</table>
</div>


<div class="row">
  <div class="col-lg-12">
    <ul class="list-unstyled">
      <li class="float-end">
        <button type="button" class="btn btn-outline-primary" onclick="window.location.href='#отслеживание-объекта';">Вверх</button>
      </li>
      <!-- <li  class="float-end">
       <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/artificial-intelligence/pattern-recognition/labs/lab6.html';">ЛР №6 →</button>
     </li> -->
      <li>
        <button type="button" class="btn btn-primary" onclick="window.location.href='{{ site.baseurl }}/artificial-intelligence/pattern-recognition/labs/lab4.html';">← ЛР №4</button>
      </li>
    </ul>
  </div>
</div>