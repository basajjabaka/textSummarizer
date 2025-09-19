from TextSummarizer.pipeline.stage01 import DataIngestionTrainingPipeline
from TextSummarizer.logging import logger
from TextSummarizer.pipeline.stage02 import DataValidationTrainingPipeline
from TextSummarizer.pipeline.stage03 import DataTransformationTrainingPipeline
from TextSummarizer.pipeline.stage04 import ModelTrainerPipeline

Stage = "Data Ingestion Stage"
try:
    logger.info(f">>>>>{Stage} started <<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> {Stage} completed!<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

Stage = "Data Validation Stage"
try:
    logger.info(f">>>>>{Stage} started <<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>> {Stage} completed!<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

Stage = "Data Transformation Stage"
try:
    logger.info(f">>>>>{Stage} started <<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>> {Stage} completed!<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

Stage = "Model Trainer Stage"
try:
    logger.info(f">>>>>{Stage} started <<<<<")
    model_trainer = ModelTrainerPipeline()
    model_trainer.main()
    logger.info(f">>>>> {Stage} completed!<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e