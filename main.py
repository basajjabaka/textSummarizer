from TextSummarizer.pipeline.stage01 import DataIngestionTrainingPipeline
from TextSummarizer.logging import logger

Stage = "Data Ingestion Stage"
try:
    logger.info(f">>>>>{Stage} started <<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> {Stage} completed!<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e