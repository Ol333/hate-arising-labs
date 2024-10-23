# SSD: Single Shot MultiBox Detector

## Кто предложил

Liu, W. et al. (2016). SSD: Single Shot MultiBox Detector. In: Leibe, B., Matas, J., Sebe, N., Welling, M. (eds) Computer Vision – ECCV 2016. ECCV 2016. Lecture Notes in Computer Science(), vol. 9905. Springer, Cham. DOI: [10.1007/978-3-319-46448-0_2](https://doi.org/10.1007/978-3-319-46448-0_2){:target="_blank"}. URL: [https://arxiv.org/abs/1512.02325](https://arxiv.org/abs/1512.02325){:target="_blank"}.

## Описание модели

![architecture]({{ site.baseurl }}/artificial-intelligence/pattern-recognition/labs/lab3_data/SSD_architecture.svg)

Мы представляем метод обнаружения объектов на изображениях с использованием одной глубокой нейронной сети. Наш подход, названный SSD, дискретизирует выходное пространство ограничивающих рамок в набор рамок по умолчанию с различными соотношениями сторон и масштабами для каждого местоположения карты признаков. Во время прогнозирования сеть генерирует оценки наличия каждой категории объектов в каждой рамке по умолчанию и вносит корректировки в рамку для лучшего соответствия форме объекта. Кроме того, сеть объединяет прогнозы из нескольких карт признаков с различными разрешениями для естественной обработки объектов различных размеров. Наша модель SSD проста по сравнению с методами, требующими предложений объектов, поскольку она полностью исключает генерацию предложений и последующую стадию повторной выборки пикселей или признаков и инкапсулирует все вычисления в одной сети. Это делает SSD простым в обучении и простым в интеграции в системы, требующие компонента обнаружения. Экспериментальные результаты на наборах данных PASCAL VOC, MS COCO и ILSVRC подтверждают, что SSD имеет сопоставимую точность с методами, которые используют дополнительный шаг предложения объектов, и намного быстрее, обеспечивая при этом единую структуру как для обучения, так и для вывода. По сравнению с другими одноступенчатыми методами, SSD имеет гораздо лучшую точность, даже при меньшем размере входного изображения. Для входного изображения 300×300 SSD достигает 72,1% mAP на тесте VOC2007 при 58 FPS на Nvidia Titan X, а для входного изображения 500×500 SSD достигает 75,1% mAP, превосходя сопоставимую современную модель Faster R-CNN.


## Фреймворк размещенный авторами на GitHub 

[исходники](https://github.com/weiliu89/caffe/tree/ssd)

## Пример работы

...