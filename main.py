from TextSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from TextSummarizer.logging import logger

STAGE_NAME = "data_ingestion_training"
try:
    logger.info(f">>>>>> stage{STAGE_NAME} started<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage{STAGE_NAME} finished<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e