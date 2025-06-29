import os
import sys
from src.exception import CustomException
from src.logger import logging

import pandas as pd
import numpy as np
import pickle


def save_object(file_path, obj):
    """
    Save the object to a file using pickle.
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            import pickle
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys) from e