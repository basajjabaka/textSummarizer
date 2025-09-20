from TextSummarizer.config.configuration import ConfigManager
from transformers import AutoTokenizer, pipeline

class PredictionPipeline:
    def __init__(self):
        self.config = ConfigManager().get_model_eval_config()

    def predict(self, text: str):
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        gen_kwargs = {
            "length_penalty": 0.8,
            "num_beams": 8,
            "max_length": 128
        }
        pipe = pipeline("summarization", model=self.config.model_path, tokenizer=tokenizer)

        print("Dialogue: ", text)

        output = pipe(text, **gen_kwargs)[0]["summary_text"]
        print("Model Summary: ", output)

        return output
