from sentence_transformers import SentenceTransformer
import faiss

class VectorBase:
    def __init__(self, embedding_model_name="paraphrase-distilroberta-base-v1"):
        self.embedding_model = SentenceTransformer(embedding_model_name)
        self.index = None
        self.entries = []

    def fit(self, documents: list):
        if not documents:
            raise ValueError("Список документов пуст. Добавьте данные для индексации.")

        all_data = []
        for document in documents:
            all_data.extend(document)

        combined_data = [entry["text"] for entry in all_data]
        self.entries = all_data

        embeddings = self.embedding_model.encode(combined_data, convert_to_numpy=True)

        dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(embeddings)

    def add_documents(self, new_documents: list):
        if not self.index:
            raise ValueError("Индекс не инициализирован. Сначала выполните fit.")

        if not new_documents:
            raise ValueError("Список новых документов пуст. Добавьте данные для индексации.")

        new_data = []
        for document in new_documents:
            new_data.extend(document)

        combined_data = [entry["text"] for entry in new_data]
        new_embeddings = self.embedding_model.encode(combined_data, convert_to_numpy=True)

        self.entries.extend(new_data)
        self.index.add(new_embeddings)

    def search(self, query, top_k=5):
        if not self.index:
            raise ValueError("База данных пуста. Сначала добавьте данные.")

        query_embedding = self.embedding_model.encode([query], convert_to_numpy=True)
        distances, indices = self.index.search(query_embedding, top_k)

        results = []
        for i, d in zip(indices[0], distances[0]):
            if i < len(self.entries):
                results.append({
                    "text": self.entries[i]["text"],
                    "id": self.entries[i]["chunk_id"],
                    "distance": d
                })

        return results