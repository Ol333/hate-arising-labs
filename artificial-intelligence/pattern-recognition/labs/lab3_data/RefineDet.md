# RefineDet

## Кто предложил

S. Zhang, L. Wen, X. Bian, Z. Lei and S. Z. Li, "Single-Shot Refinement Neural Network for Object Detection," 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition, Salt Lake City, UT, USA, 2018, pp. 4203-4212, doi: 10.1109/CVPR.2018.00442. URL: [https://arxiv.org/abs/1711.06897](https://arxiv.org/abs/1711.06897)

## Описание модели

Для обнаружения объектов двухэтапный подход (например, Faster R-CNN) обеспечивает наивысшую точность, тогда как одноэтапный подход (например, SSD) имеет преимущество в виде высокой эффективности. Чтобы унаследовать достоинства обоих методов, преодолевая их недостатки, в этой статье мы предлагаем новый детектор на основе однократного срабатывания, называемый RefineDet, который достигает лучшей точности, чем двухэтапные методы, и сохраняет сопоставимую эффективность одноэтапных методов. RefineDet состоит из двух взаимосвязанных модулей, а именно, модуля уточнения якорей и модуля обнаружения объектов. В частности, первый нацелен на (1) фильтрацию отрицательных якорей для сокращения пространства поиска для классификатора и (2) грубую настройку местоположений и размеров якорей для обеспечения лучшей инициализации для последующего регрессора. Последний модуль принимает уточненные якоря в качестве входных данных из первого для дальнейшего улучшения регрессии и прогнозирования многоклассовой метки. Между тем, мы проектируем блок передачи соединения для передачи признаков в модуле уточнения якоря для прогнозирования местоположений, размеров и меток классов объектов в модуле обнаружения объектов. Функция многозадачных потерь позволяет нам обучать всю сеть сквозным способом. Обширные эксперименты на PASCAL VOC 2007, PASCAL VOC 2012 и MS COCO демонстрируют, что RefineDet достигает точности обнаружения на самом современном уровне с высокой эффективностью.


## Страничка авторов на GitHub 

[исходники](https://github.com/sfzhang15/RefineDet)

## Пример работы

...