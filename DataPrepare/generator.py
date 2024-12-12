from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

torch.manual_seed(42)

class AdvancedGenerator:
    def __init__(self, model_name="t-tech/T-lite-it-1.0"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float16,
            device_map="auto"
        )

    def generate_answer(self, query, context, max_new_tokens=256):
        messages = [
            {"role": "system", "content": "You are T-lite, a virtual assistant. Help the user find information and answer questions in the language in which the question is asked!"},
            {"role": "user", "content": f"Контекст: {context}"},
            {"role": "user", "content": f"Вопрос: {query}"}
        ]

        text = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )
        model_inputs = self.tokenizer([text], return_tensors="pt").to(self.model.device)

        generated_ids = self.model.generate(
            **model_inputs,
            max_new_tokens=max_new_tokens
        )
        generated_ids = [
            output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
        ]

        response = self.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
        return response