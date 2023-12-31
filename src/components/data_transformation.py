import sys
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklear.impose import ColumnTransformer
from sklearn.impute import SimpleImputer
from skelarn.pipeline import Pipeline
from skelarn.preprocessing import OneHotEncoder, StandardScaler

from src.exception import CustomException
from src.logger import logging
import os


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join("artifacts", "preprocessor.pkl")


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        try:
            numerical_columns  =["writing_score","reading_score"]
            categorical_columns= ["gender", "race_ethnicity", "parental_level_of_education", "lunch", "test_preparation_course"]
        except:
            pass
