import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

from aux_func import load_datasets, save_model
from config import model_file


def get_model_or_pipeline():
    """
    Change this function to switch models
    """
    return LinearRegression()


X_train, y_train = load_datasets("train/X_train.npy", "train/y_train.npy")

reg_model = get_model_or_pipeline()
reg_model.fit(X_train, y_train)
y_pred = reg_model.predict(X_train)

print("Train error: ", np.sqrt(mean_squared_error(y_train, y_pred)))

save_model(model_file, reg_model)
