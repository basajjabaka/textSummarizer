import os
from box.exceptions import BoxValueError
from box import ConfigBox
import yaml
from pathlib import Path
import logging
from typing import Any
from TextSummarizer.logging import logger
from ensure import ensure_annotations

@ensure_annotations
def read_yaml(yamlPath: Path) -> ConfigBox:
    """Reads a yaml file with 

    Args:
        yamlPath (str): Path to the yaml file

    Raises:
        ValueError: If yaml file is empty
        e: Empty file 

    Returns:
        ConfigBox: ConfigBox object containing the yaml file contents
    """

    try:
        with open(yamlPath, "r") as yamlFile:
            content = yaml.safe_load(yamlFile)
            logger.info(f"yaml file: {yamlPath} loaded successfully")
            return ConfigBox(content)
    except BoxValueError as e:
        raise ValueError(f"yaml file: {yamlPath} is empty: {e}")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(pathToDirectories: list, verbose=True):
    """Creates a list of directories

    Args:
        pathToDirectories (list): List of paths to create
        ignoreLog (bool, optional): ignore if multiple directories are created. Defaults to false
    """
    for path in pathToDirectories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")

@ensure_annotations
def getSize(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): Path of the file

    Returns:
        str: size in KB
    """
    sizeInKB = round(os.path.getsize(path)/1024)
    return f"~ {sizeInKB} KB"