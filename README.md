
# 🧠 Сравнение моделей T-Lite и Llama3

В этом проекте реализованы два решения для генерации ответов на вопросы. Если вы можете скачать модель Ollama с помощью предоставленного загрузчика или же по ссылке, то переходите в модель Llama3, иначе T-Lite: 

1. **Llama3** — многоязычная модель, которая может отвечать на вопросы на любом языке.  
2. **T-Lite** — универсальная модель, которая также может отвечать на вопросы на любом языке, но оптимизирована для работы с текстами на русском языке.

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
| **Llama3**   | ROUGE-1     | 1.00      | 1.00   | 1.00 |
|              | ROUGE-2     | 0.00      | 0.00   | 0.00 |
|              | ROUGE-L     | 1.00      | 1.00   | 1.00 |
|              | BERTScore   | 1.00      | 1.00   | 1.00 |
| **T-Lite**   | ROUGE-1     | 0.17      | 1.00   | 0.29 |
|              | ROUGE-2     | 0.14      | 1.00   | 0.25 |
|              | ROUGE-L     | 0.17      | 1.00   | 0.29 |
|              | BERTScore   | 0.51      | 0.89   | 0.65 |

---

## 📐 Статистическая значимость

Для подтверждения значимости улучшений были применены следующие методы статистического анализа:

1. **Критерий Стьюдента (t-test)**:
   - Проверяет разницу между средними значениями метрик для моделей.
   - **Вывод**: статистически значимая разница в значениях F1-score между моделями (p-value < 0.05).

2. **Тест Уилкоксона**:
   - **Вывод**: различие между метриками F1 для моделей Llama3 и T-Lite не является статистически значимым (p-value > 0.05).

При парсинге таблиц формат json дал небольшой прирост в метриках.

---

## 🚀 Как использовать

1. Переключитесь на нужную ветку:
   ```bash
   git checkout baseline-llama  # Для Llama3
   git checkout baseline-T-Lite  # Для T-Lite
   ```

2. **Для использования модели Llama3:**
   - Скачайте и установите модель из официального источника

3. **Для использования модели T-Lite:**
   - Модель уже встроена в проект и готова к использованию.

---
