import os
import sys
from src.exception import CustomException
from src.logger import logging

import pandas as pd
import numpy as np
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

def save_object(file_path, obj):
    """
    Save the object to a file using pickle.
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys) from e 
    

def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    """
    Evaluate the performance of different regression models and return a report.
    """
    try:
        report = {}
        model_names = list(models.keys())
        for i in range(len(model_names)):
            model_name = model_names[i]
            model = models[model_name]
            para = param.get(model_name, {})
            gs = GridSearchCV(model, para, cv=3)   
            gs.fit(X_train, y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)

            y_train_pred = model.predict(X_test)
            y_test_pred = model.predict(X_test)
            train_model_score = r2_score(y_test, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)
            report[model_name] = test_model_score
        return report

    except Exception as e:
        raise CustomException(e, sys) from e
    

def load_object(file_path):
    try:
        with open(file_path, 'rb') as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        raise CustomException(e, sys)    
    