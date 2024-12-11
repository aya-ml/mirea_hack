from transformers import T5ForConditionalGeneration, T5Tokenizer
from sentence_transformers import SentenceTransformer
import faiss

class BaseGenerator:
    def __init__(self, model_name="paraphrase-distilroberta-base-v1"):
        self.model = SentenceTransformer(model_name)
        self.index = None
        self.entries = []

        self.text_generation_model = T5ForConditionalGeneration.from_pretrained("t5-large")
        self.tokenizer = T5Tokenizer.from_pretrained("t5-large")

    def fit(self, documents: list):
        all_data = []

        for document in documents:
            all_data.extend(document)

        combined_data = [entry["text"] for entry in all_data]
        self.entries = all_data

        embeddings = self.model.encode(combined_data, convert_to_numpy=True)

        dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(embeddings)

    def add_documents(self, new_documents: list):
        if not self.index:
            raise ValueError("Индекс не инициализирован. Сначала выполните fit.")

        new_data = []
        for document in new_documents:
            new_data.extend(document)

        combined_data = [entry["text"] for entry in new_data]
        new_embeddings = self.model.encode(combined_data, convert_to_numpy=True)

        self.entries.extend(new_data)
        self.index.add(new_embeddings)

    def search(self, query, top_k=5):
        if not self.index:
            raise ValueError("База данных пуста. Сначала добавьте данные.")

        query_embedding = self.model.encode([query], convert_to_numpy=True)
        distances, indices = self.index.search(query_embedding, top_k)

        results = [
            {
                "type": self.entries[i]["type"],
                "text": self.entries[i]["text"],
                "distance": d
            }
            for i, d in zip(indices[0], distances[0])
        ]
        return results

    def generate_answer(self, query, context, max_length=350):
        input_text = f"question: {query} context: {context}"

        inputs = self.tokenizer(input_text, return_tensors="pt", truncation=True, padding=True, max_length=512)
        outputs = self.text_generation_model.generate(**inputs, max_length=max_length, num_beams=5, early_stopping=True)

        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
