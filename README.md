# TP-ml-prod
Репозиторий с домашними заданиями по курсу "Машинное обучение в продакшене"

Installation: 
~~~
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
~~~
Logistic regression:
~~~
python src/train_pipeline.py configs/train_config_log_reg.yaml
~~~
Random forest:
~~~
python src/train_pipeline.py configs/train_config_random_forest.yaml
~~~

Test:
~~~
pytest tests/
~~~

Project Organization
------------

    ├── LICENSE
    ├── README.md               <- Описание проекта.
    ├── data
    │   ├── predicted           <- Предстазанные метки.
    │   └── raw                 <- Исходные данные.
    │
    ├── models                  <- Модели, трансформеры, метрики.
    │
    ├── notebooks               <- Jupyter notebooks. Предварительный анализ данных.
    │
    ├── requirements.txt        <- Необходимые пакеты для запуска обучения и предсказния.
    │
    ├── setup.py                <- Возможность установки проекта через pip.
    │
    ├── src                     <- Код для запуска пайплана.
    │   ├── __init__.py         <- src в Python модуль.
    │   │
    │   ├── data                <- Работа с данными.
    │   │
    │   ├── entity              <- Структуры и параметры для работы модели.
    │   │
    │   ├── features            <- Преобразование "сырых" данных к признакам модели.
    │   │
    │   ├── models              <- Код для обучения моделей и использование обученных модели для реализации.
    │   │
    │   ├── predict_pipeline.py <- Пайплайн для прогноза.
    │   │
    │   ├── train_pipeline.py   <- Пайплайн для тренировки.
    │
    ├── tests                   <- Тесты

--------