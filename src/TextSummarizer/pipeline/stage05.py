from TextSummarizer.components.model_evaluation import ModelEvaluation
from TextSummarizer.config.configuration import ConfigManager
from TextSummarizer.logging import logger

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
            config = ConfigManager()
            model_eval_config = config.get_model_eval_config()
            model_evaluator = ModelEvaluation(config=model_eval_config)
            model_evaluator.evaluate()