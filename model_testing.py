import pickle

import numpy as np
from sklearn.metrics import mean_squared_error

from aux_func import load_datasets
from config import model_file

# load TEST DATA
X_test, y_test = load_datasets("test/X_test.npy", "test/y_test.npy")


with open(model_file, "rb") as f:
    reg_model = pickle.load(f)

y_pred = reg_model.predict(X_test)
np.sqrt(mean_squared_error(y_test, y_pred))

print(f"Model error: {reg_model.score(X_test, y_test)}")
