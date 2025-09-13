import os
import urllib.request as request
import zipfile
from TextSummarizer.logging import logger
from TextSummarizer.utils.common import getSize
from pathlib import Path 
from TextSummarizer.entity import DataIngestionConfig  # Import Path if not already imported

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        # Create the directory if it doesn't exist
        download_dir = Path(self.config.local_data_file).parent
        os.makedirs(download_dir, exist_ok=True)  # Create directory

        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} downloaded! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {getSize(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        """
        zip_file_path: str
        extracts zip file into data directory
        function returns nothing
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)