from TextSummarizer.pipeline.stage01 import DataIngestionTrainingPipeline
from TextSummarizer.logging import logger
from TextSummarizer.pipeline.stage02 import DataValidationTrainingPipeline

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