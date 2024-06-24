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
<img src ="https://github.com/DanilaAkh/retinopathy_of_prematurity/assets/147710292/e0d238ef-5e5a-4faf-8c53-bb31a89d6847.jpg" width="600">

Метрики обучения на датасете 2
<img src ="https://github.com/DanilaAkh/retinopathy_of_prematurity/assets/147710292/11486f62-8dfd-4ae5-97de-262df0986f81.jpg" width="600">

## Примеры ошибок модели ResNet
Примеры ошибок на датасете 1
<img src ="https://github.com/DanilaAkh/retinopathy_of_prematurity/assets/147710292/8893e663-2058-43f0-a887-1d83132cd7ca.jpg" width="600">
 (0 – Здоров, 1 – Нездоров)

Примеры ошибок на датасете 2
<img src ="https://github.com/DanilaAkh/retinopathy_of_prematurity/assets/147710292/a11faea6-8ecd-434c-b476-6b01a5de35c7.jpg" width="600">
(0 – Здоров, 1 – Стадия 2-3, 2 – Плюс болезнь)

# Модель EfficientNet
Модель EfficientNet загружалась с предобученными весами на наборе данных IMAGENET1K_V1.

Метрики обучения на датасете 1
<img src ="https://github.com/DanilaAkh/retinopathy_of_prematurity/assets/147710292/6da2cda2-4bdd-4617-97fa-b544327b5087.jpg" width="600">

Метрики обучения на датасете 2
<img src ="https://github.com/DanilaAkh/retinopathy_of_prematurity/assets/147710292/523fff93-8134-4201-a7a2-27ba8683e1ce.jpg" width="600">

## Примеры ошибок модели ResNet
Примеры ошибок на датасете 1
<img src ="https://github.com/DanilaAkh/retinopathy_of_prematurity/assets/147710292/94bb5fd0-45d1-4b89-94e7-75d5bab7907e.jpg" width="300">
 (0 – Здоров, 1 – Нездоров)

Примеры ошибок на датасете 2
<img src ="https://github.com/DanilaAkh/retinopathy_of_prematurity/assets/147710292/a11faea6-8ecd-434c-b476-6b01a5de35c7.jpg" width="600">
(0 – Здоров, 1 – Стадия 2-3, 2 – Плюс болезнь)

