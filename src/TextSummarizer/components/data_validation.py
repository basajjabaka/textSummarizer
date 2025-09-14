import os
from TextSummarizer.logging import logger
import pathlib
from TextSummarizer.entity import DataValidationConfig


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

        # Create the status file if it doesn't exist
        status_file_path = pathlib.Path(self.config.STATUS_FILE)
        if not status_file_path.exists():
            status_file_path.parent.mkdir(parents=True, exist_ok=True)  # Ensure directory exists
            with open(self.config.STATUS_FILE, 'w') as f:
                f.write("Validation Status: Initialized\n")  # Initialize the file

    def validate_files_exist(self) -> bool:
        try:
            validation_status = None
            all_files = os.listdir(os.path.join("artifacts", "data_ingestion", "samsum_dataset"))

            for file in all_files:
                if file not in self.config.RQD_FILE:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation Status: {validation_status}\n")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation Status: {validation_status}\n")
            return validation_status
        except Exception as e:
            raise e