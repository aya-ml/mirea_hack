# Text Generation, Metrics, and Data Preparation System with Llama3

Этот проект включает инструменты для генерации текста, оценки качества сгенерированного контента и подготовки данных для дальнейшего использования в системе поиска. Он использует цепочку RAG (Retrieval-Augmented Generation) и включает следующие компоненты:

- **Генерация ответов** с использованием модели `Llama3` в связке с RAG.
- **Оценка качества** с использованием метрик ROUGE и BERTScore.
- **Подготовка данных** с использованием FAISS для индексирования и поиска.

## Структура проекта

### 1. **Data Preparation**
Модуль для подготовки данных и создания векторного индекса с использованием FAISS и OllamaEmbeddings.

- **Индексирование данных с помощью FAISS**:
  Создание векторного индекса для документов с помощью эмбеддингов, полученных с использованием модели `nomic-embed-text`.

- **Поиск по индексу**:
  Выполнение поиска по индексированным данным с использованием подхода на основе схожести.

### 2. **Generator**
Модуль для генерации ответов на основе модели ChatOllama. Ответы генерируются с использованием контекста и заданного вопроса.

- **Метод `rag_chain.invoke(question)`**:
  Генерирует ответ на заданный вопрос с учетом контекста, используя модель `Llama3` в связке с RAG.

### 3. **Evaluation Metrics**
Модуль для оценки качества текста с помощью метрик ROUGE и BERTScore.

- **Метод `calculate_rouge(references, predictions)`**:
  Оценивает схожесть генерированного текста с эталонным текстом с использованием метрики ROUGE.

- **Метод `calculate_bertscore(references, predictions, model_type)`**:
  Оценивает схожесть текста с использованием метрики BERTScore.
