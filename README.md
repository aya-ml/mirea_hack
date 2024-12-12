# Advanced Text Generation and Search System

Этот проект представляет собой комплексную систему для генерации текстов и поиска информации с использованием современных методов обработки естественного языка. Включает в себя:

- **Парсинг документов в формате DOCX** для извлечения текста.
- **Поиск по векторному индексу** с использованием FAISS и моделей для эмбеддингов (Sentence Transformers).
- **Генерацию ответов** с помощью модели T-lite.
- **Оценку качества генерации** с помощью метрик ROUGE и BERTScore.

## Структура проекта

### 1. **Docx Parser**
Модуль для парсинга DOCX документов. Разделяет текст на части (чанки) и добавляет их в базу данных для последующего поиска.

- **Метод `parse_docx(file_path, document_id)`**:
  Извлекает текст из документа DOCX и разбивает его на части для индексации.

### 2. **Vector Base**
Модуль для создания и работы с векторным индексом с использованием FAISS для поиска информации.

- **Метод `fit(documents)`**:
  Индексирует документы с помощью эмбеддингов, полученных из модели SentenceTransformer.
  
- **Метод `add_documents(new_documents)`**:
  Добавляет новые документы в уже существующий индекс.

- **Метод `search(query, top_k)`**:
  Выполняет поиск по запросу, возвращая топ-k наиболее релевантных документов.

### 3. **Advanced Generator**
Модуль для генерации ответов на основе модели языковой модели с предобученными параметрами. Использует библиотеку HuggingFace `transformers`.

- **Метод `generate_answer(query, context, max_new_tokens)`**:
  Генерирует ответ на основе запроса и контекста, используя модель T-lite.

### 4. **Evaluation Metrics**
Модуль для оценки качества генерации текста с помощью метрик ROUGE и BERTScore.

- **Метод `calculate_rouge(references, predictions)`**:
  Оценивает схожесть генерированного текста с эталонным текстом с использованием метрики ROUGE.

- **Метод `calculate_bertscore(references, predictions, model_type)`**:
  Оценивает схожесть с использованием метрики BERTScore.

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/aya-ml/mirea_hack.git
   cd advanced-text-generation
   ```

2. Переключитесь на ветку baseline-T-Lite:
   ```bash
   git checkout baseline-T-Lite
   ```

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

4. Для работы с моделями HuggingFace и FAISS потребуется GPU (если доступно).

## Использование

### Парсинг DOCX

```python
from docx_parser import DocxParser

parser = DocxParser(chunk_size=100)
chunks = parser.parse_docx("path/to/document.docx", document_id="doc_1")
print(chunks)
```

### Индексирование и поиск

```python
from vector_base import VectorBase

# Инициализация поиска
vector_base = VectorBase(embedding_model_name="paraphrase-distilroberta-base-v1")

# Индексирование документов
documents = [{"text": "Документ 1 текст."}, {"text": "Документ 2 текст."}]
vector_base.fit(documents)

# Поиск по запросу
results = vector_base.search("Поиск текста", top_k=3)
for result in results:
    print(result)
```

### Генерация ответов

```python
from generator import AdvancedGenerator

generator = AdvancedGenerator(model_name="t-tech/T-lite-it-1.0")
response = generator.generate_answer("Какой прогноз погоды?", "Сегодня в Москве облачно и дождливо.")
print(response)
```

### Оценка качества

```python
from evaluation_metrics import EvaluationMetrics

metrics = EvaluationMetrics()
references = ["Это эталонный текст."]
predictions = ["Это сгенерированный текст."]
evaluation = metrics.evaluate(references, predictions)
print(evaluation)
```
