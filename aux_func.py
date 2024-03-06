import pickle

import numpy as np


def load_datasets(X_train_path, y_train_path):
    """
    Function to open the train dataset and answers
    """
    X_train = np.load(X_train_path, allow_pickle=True)
    y_train = np.load(y_train_path, allow_pickle=True)

    return X_train, y_train


def save_model(path, model):
    """
    Save trainde model to pkl file
    """
    with open(path, "wb") as f:
        pickle.dump(model, f)
