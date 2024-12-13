from rouge import Rouge
from bert_score import score as bert_score

class EvaluationMetrics:
    def __init__(self):
        self.rouge = Rouge()

    def calculate_rouge(self, references, predictions):
        scores = self.rouge.get_scores(predictions, references, avg=True)
        return {
            "rouge-1": scores["rouge-1"],
            "rouge-2": scores["rouge-2"],
            "rouge-l": scores["rouge-l"]
        }

    def calculate_bertscore(self, references, predictions, model_type="distilbert-base-uncased"):
        P, R, F1 = bert_score(predictions, references, model_type=model_type, lang="en")
        return {
            "precision": P.mean().item(),
            "recall": R.mean().item(),
            "f1": F1.mean().item()
        }

    def evaluate(self, references, predictions):
        return {
            "rouge": self.calculate_rouge(references, predictions),
            "bertscore": self.calculate_bertscore(references, predictions)
        }