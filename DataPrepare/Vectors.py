from sentence_transformers import SentenceTransformer
import faiss


class VectorDatabase:
    def __init__(self, model_name="paraphrase-distilroberta-base-v1"):
        self.model = SentenceTransformer(model_name)
        self.index = None
        self.entries = []  # Хранит элементы документа с их типами и текстом

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
