from joblib import load


def load_model(path):
    # Load the model from the file
    model = load(path)
    return model


xgb_clf = load('../model/xgb_model.joblib')


class _Classifier:
    def __init__(self, model=xgb_clf):
        self.model = model

    def classify(self, X_test):
        return self.model.predict(X_test)


clf = _Classifier()
