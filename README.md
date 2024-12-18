# Конвертация из json в маску

Этот репозиторий содержит Python-скрипт для преобразования аннотированных JSON-файлов в маски изображений с использованием библиотеки Pillow. Скрипт обрабатывает полигоны, описанные в JSON, и создаёт изображения размером 900x900 пикселей с заливкой полигонов белым цветом на чёрном фоне.

## Возможности

- **Чтение JSON**: Считывает данные аннотаций из JSON-файла.
- **Преобразование полигонов**: Преобразует относительные координаты полигонов в абсолютные значения для холста 900x900 пикселей.
- **Создание масок**: Генерирует изображения масок в указанной выходной папке.
- **Пакетная обработка**: Обрабатывает несколько групп аннотаций из одного JSON-файла.

## Требования

- Python 3.7+
- Pillow (Python Imaging Library)

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/yourusername/jsonToMask.git
   ```
2. Перейдите в директорию репозитория:
   ```bash
   cd jsonToMask
   ```
3. Установите необходимые зависимости:
   ```bash
   pip install pillow
   ```

## Использование

1. Поместите ваш JSON-файл в директорию `json` и убедитесь, что он соответствует указанному формату (см. ниже).
2. Запустите скрипт:
   ```bash
   python jsonToMask.py
   ```
3. Сгенерированные маски изображений будут сохранены в папке `json_to_mask`.

## Формат JSON

JSON-файл должен быть структурирован следующим образом:

```json
[
  {
    "annotations": [
      {
        "result": [
          {
            "type": "polygonlabels",
            "value": {
              "points": [[10, 20], [30, 40], [50, 60]]
            }
          }
        ]
      }
    ]
  }
]
```
- `points` должен быть массивом относительных координат (в процентах), представляющих вершины полигона.

## Результат

Для каждой группы в JSON-файле создаётся изображение маски, которое сохраняется в папке `json_to_mask`. Изображения называются последовательно, например: `output_image_1.png`, `output_image_2.png` и т.д.

## Пример

### Входной JSON:

```json
[
  {
    "annotations": [
      {
        "result": [
          {
            "type": "polygonlabels",
            "value": {
              "points": [[10, 10], [20, 20], [30, 10]]
            }
          }
        ]
      }
    ]
  }
]
```

### Сгенерированная маска:

Изображение размером 900x900 пикселей с указанным полигоном, залитым белым цветом.



