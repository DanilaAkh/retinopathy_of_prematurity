# Расширение возможностей медицинских учреждений здравоохранения Свердловской области в диагностике ретинопатии недоношенных с помощью проекта компьютерного зрения

## Команда:
Ахаимов Д.И,
Гребнев Н.А,
Кашкин А.В,
Масленников В.М,
Рихарди С,
Романова В.Б.

## Цель:
Создание системы компьютерного зрения, способной автоматически классифицировать снимки глазного дна недоношенных детей по стадиям ретинопатии недоношенных (РН).

## Значимость:
Разработанная система может быть использована для скрининга РН у недоношенных детей. Система может помочь врачам в постановке диагноза и выборе оптимальной схемы лечения. Раннее выявление и лечение РН позволит предотвратить развитие слепоты и других осложнений у недоношенных детей. Снижение риска развития слепоты и других осложнений РН позволит повысить социальную адаптацию недоношенных детей.

## Набор данных:
Изображения глазного дна, предоставленные МКМЦ "Бонум". 
<img src="https://github.com/DanilaAkh/retinopathy_of_prematurity/assets/147710292/ed87c4b1-a690-40c3-9cb2-049720076802.jpg" width="500">

## Визуализация датасета 1

<img src ="https://github.com/DanilaAkh/retinopathy_of_prematurity/assets/147710292/f011feb7-90a3-4aa8-80b2-f818bd63f8a2.jpg" width="600">

## Визуализация датасета 2
<img src ="https://github.com/DanilaAkh/retinopathy_of_prematurity/assets/147710292/c7aa26ad-55ee-48f4-bed7-a8054cfb82ea.jpg" width="600">

## Обучение
Для обучения был изменен размер изображения на 224х224, применена нормализация, аугментация.

Гипер-параметры модели:

•	Функция потерь: CrossEntropyLoss.

•	Количество эпох обучения: 50.

•	Размер batch: 32.

•	Скорость обучения: 0.001, 0.005, 0.010, 0.020, 0.030, 0.050, 0.08.

# Модель ResNet
Метрики обучения на датасете 1
<img src ="https://github.com/DanilaAkh/retinopathy_of_prematurity/assets/147710292/17354e2c-da59-4382-9a25-8a69a7a54945.jpg" width="600">

Метрики обучения на датасете 2
<img src ="https://github.com/DanilaAkh/retinopathy_of_prematurity/assets/147710292/0a6194dc-ae9a-40d9-a073-d6ea170159d5.jpg" width="600">

## Примеры ошибок модели ResNet
Примеры ошибок на датасете 1
<img src ="https://github.com/DanilaAkh/retinopathy_of_prematurity/assets/147710292/8893e663-2058-43f0-a887-1d83132cd7ca.jpg" width="600">

 (0 – Здоров, 1 – Нездоров)

Примеры ошибок на датасете 2
<img src ="https://github.com/DanilaAkh/retinopathy_of_prematurity/assets/147710292/2d77ea19-67c3-459a-b62c-989c25226de0.jpg" width="600">

(0 – Здоров, 1 – Стадия 2-3, 2 – Плюс болезнь)

# Модель EfficientNet
Модель EfficientNet загружалась с предобученными весами на наборе данных IMAGENET1K_V1.

Метрики обучения на датасете 1
<img src ="https://github.com/DanilaAkh/retinopathy_of_prematurity/assets/147710292/6da2cda2-4bdd-4617-97fa-b544327b5087.jpg" width="600">

Метрики обучения на датасете 2
<img src ="https://github.com/DanilaAkh/retinopathy_of_prematurity/assets/147710292/523fff93-8134-4201-a7a2-27ba8683e1ce.jpg" width="600">

## Примеры ошибок модели EfficientNet
Примеры ошибок на датасете 1

<img src ="https://github.com/DanilaAkh/retinopathy_of_prematurity/assets/147710292/94bb5fd0-45d1-4b89-94e7-75d5bab7907e.jpg" width="300">

(0 – Здоров, 1 – Нездоров)


## Метрики обучение с примененной аугментацией
Датасет 1

<img src ="https://github.com/DanilaAkh/retinopathy_of_prematurity/assets/147710292/d3adb774-6584-4b85-97a9-979dcd9f08e7.jpg" width="600">

Итоговое соотношение классов для датасета №1: 42,7% : 57,3%.


Датасет 2

<img src ="https://github.com/DanilaAkh/retinopathy_of_prematurity/assets/147710292/b1b99939-ed9a-4a48-bf30-3f23420c8fb3.jpg" width="600">

Итоговое соотношение классов для датасета №2: 51,9% : 14,3% : 33,8%.

## Облачное приложение для классификации степени заболевания
Ссылка на облачное приложение

Сейчас приложение определяет 3 класса: Здоров, Стадия 2-3, Плюс болезнь. 
```
[https://goo.su/TDcn](http://188.73.168.175:8501/#7f2902ec)
```

## Пример изображения для загрузки
<img src="https://github.com/soulvi/Retinopathy/assets/147710292/8603f8b6-1556-464e-bbd6-dc80204be915.jpg" width="400">




