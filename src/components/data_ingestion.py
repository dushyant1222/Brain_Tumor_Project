import sys
import os
import numpy as np
import pandas as pd
from zipfile import Path
from pymongo import MongoClient
from src.constant import *
from src.exception import CustomException
from src.logger import logging
from src.utils import main_utils
from dataclasses import dataclass
import upload_data



@dataclass
class DataIngestionConfig:
    artifact_folder: str = os.path.join(artifact_folder)
    
class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.utils = main_utils()
        
    def export_datacollection_as_dataframe(self, collection_name, database_name):
        try:
            mongo_client = MongoClient(MONGO_DB_URL)
            
            collection = mongo_client(database_name, collection_name)
            
            df = pd.DataFrame(list(collection.find()))
            
            if "_id" in df.columns.to_list():
                df = df.drop(columns=['id'], axis=1)
                
            df.replace({"na": np.nan}, inplace=True)
            return df
        except Exception as e:
            raise CustomException(e, sys)
            