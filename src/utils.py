import os
import sys
from src.exception import CustomException
from src.logger import logging

import pandas as pd
import numpy as np
import pickle
from sklearn.metrics import r2_score


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
    

def evaluate_models(X_train, y_train, X_test, y_test, models):
    """
    Evaluate the performance of different regression models and return a report.
    """
    try:
        report = {}
        for i in range(len(list(models))):
            model = list(models.values())[i]
            model.fit(X_train, y_train)
            y_train_pred = model.predict(X_test)
            y_test_pred = model.predict(X_test)
            train_model_score = r2_score(y_test, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)
            report[list(models.keys())[i]] = test_model_score
        return report

    except Exception as e:
        raise CustomException(e, sys) from e