import numpy as np
from joblib import load

_xgb_clf = load('../model/xgb_model.joblib')
_scaler = load('../model/scaler.joblib')


class _Classifier:
    def __init__(self, model=_xgb_clf, scaler=_scaler):
        self._model = model
        self._scaler = scaler

    def classify(self, x_test: tuple):
        X_test = np.array([x_test])
        X_test_scaled = self._scaler.transform(X_test)
        return int(self._model.predict(X_test_scaled)[0])


clf = _Classifier()
