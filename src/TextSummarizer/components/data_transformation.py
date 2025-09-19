import os
from TextSummarizer.logging import logger
from transformers import AutoTokenizer
from datasets import load_dataset, load_from_disk
from TextSummarizer.entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)

    def examples2features(self, exampleBatch):
        inputEncodings = self.tokenizer(exampleBatch['dialogue'], max_length=1024, truncation=True)

        with self.tokenizer.as_target_tokenizer():
            targetEncodings = self.tokenizer(exampleBatch['summary'], max_length=128, truncation=True)

        return{
            'input_ids': inputEncodings['input_ids'],
            'attention_mask': inputEncodings['attention_mask'],
            'labels': targetEncodings['input_ids']
        }

    def convert(self):
        dataset_samsum = load_from_disk(self.config.data_path)
        dataset_samsum_pt = dataset_samsum.map(self.examples2features, batched=True)
        dataset_samsum_pt.save_to_disk(os.path.join(self.config.root_dir, "samsum_dataset"))