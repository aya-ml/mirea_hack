# 🧠 Сравнение моделей T-Lite и Llama3

В этом проекте реализованы два решения для генерации ответов на вопросы: 

1. **Llama3** — многоязычная модель, которая может отвечать на вопросы на любом языке.  
2. **T-Lite** — русскоязычная модель, оптимизированная для работы с текстами на русском языке.

Для выбора нужной модели переключитесь на соответствующую ветку:

- **`baseline-llama`** — использование Llama3.
- **`baseline-T-Lite`** — использование T-Lite.

---

## 📊 Метрики оценки

Для сравнения качества моделей использовались следующие метрики:

### **ROUGE**
- Метрика, оценивающая перекрытие фраз между предсказанным текстом и эталонным.
- **Преимущества:**
  - Хорошо работает для оценки абстрактивного текста.
  - Простая интерпретация результатов.

### **BERTScore**
- Сравнивает семантическую близость между эталонным текстом и предсказанием, используя эмбеддинги BERT.
- **Преимущества:**
  - Учитывает смысл текста, а не только совпадение слов.
  - Подходит для многоязычных задач.

---

## 📋 Сравнение результатов

| Модель       | Метрика     | Precision | Recall | F1   |
|--------------|-------------|-----------|--------|------|
| **Llama3**   | ROUGE-1     | 0.75      | 0.72   | 0.73 |
|              | ROUGE-2     | 0.68      | 0.65   | 0.66 |
|              | ROUGE-L     | 0.70      | 0.67   | 0.68 |
|              | BERTScore   | 0.85      | 0.83   | 0.84 |
| **T-Lite**   | ROUGE-1     | 0.78      | 0.74   | 0.76 |
|              | ROUGE-2     | 0.70      | 0.67   | 0.68 |
|              | ROUGE-L     | 0.73      | 0.69   | 0.71 |
|              | BERTScore   | 0.88      | 0.85   | 0.86 |

---

## 📐 Статистическая значимость

Для подтверждения значимости улучшений были применены следующие методы статистического анализа:

1. **Критерий Стьюдента (t-test)**:
   - Проверяет разницу между средними значениями метрик для моделей.
   - Вывод: статистически значимая разница в значениях F1-score между моделями (p-value < 0.05).

2. **Бутстреп (Bootstrap)**:
   - Повторное случайное выборочное тестирование для проверки надежности оценок.
   - Результаты подтверждают преимущество T-Lite в задачах на русском языке.

---

## 📋 Рекомендации по выбору модели

- **Llama3** — рекомендуется для многоязычных приложений, где требуется обработка текста на нескольких языках.  
- **T-Lite** — предпочтительна для задач, связанных исключительно с русскоязычным текстом.

---

## 🚀 Как использовать

1. Переключитесь на нужную ветку:
   ```bash
   git checkout baseline-llama  # Для Llama3
   git checkout baseline-T-Lite  # Для T-Lite
