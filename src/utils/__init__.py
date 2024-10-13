import sys
import os
import pickle
import yaml
import boto3
import pandas as pd  # If needed for your project, else can be removed

from src.constant import *
from src.exception import CustomException
from src.logger import logging


class MainUtils:
    def __init__(self) -> None:
        pass

    def read_yaml_file(self, filename: str) -> dict:
        """Reads a YAML file and returns its contents as a dictionary."""
        try:
            with open(filename, "r") as yaml_file:  # Open as text
                return yaml.safe_load(yaml_file)
        except Exception as e:
            raise CustomException(e, sys) from e

    def read_schema_config_file(self) -> dict:
        """Reads the schema configuration file."""
        try:
            schema_config = self.read_yaml_file(os.path.join("config", "schema.yaml"))
            return schema_config
        except Exception as e:
            raise CustomException(e, sys) from e

    @staticmethod
    def save_object(file_path: str, obj: object) -> None:
        """Saves an object to a file using pickle."""
        logging.info("Entered the save_object method of MainUtils class")
        try:
            with open(file_path, "wb") as file_obj:
                pickle.dump(obj, file_obj)
            logging.info("Exited the save_object method of MainUtils class")
        except Exception as e:
            raise CustomException(e, sys) from e

    @staticmethod
    def load_object(file_path: str) -> object:
        """Loads an object from a file using pickle."""
        logging.info("Entered the load_object method of MainUtils class")
        try:
            with open(file_path, "rb") as file_obj:
                obj = pickle.load(file_obj)
            logging.info("Exited the load_object method of MainUtils class")
            return obj
        except Exception as e:
            logging.info('Exception occurred in load_object function of MainUtils class')
            raise CustomException(e, sys) from e
