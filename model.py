import pandas as pd
from sklearn.model_selection import train_test_split
from lightgbm import LGBMRegressor
import dill as pickle
import warnings

warnings.filterwarnings("ignore")


def build_and_train():
    df = pd.read_csv('ML_models/dataset.csv')
    # параметры модели
    model = LGBMRegressor(max_depth=101,
                          min_child_samples=20,
                          num_leaves=11,
                          n_estimators=300,
                          random_state=47,
                          force_row_wise=True)

    df = df.drop(['Unnamed: 0'], axis=1)
    X = df.drop(['price_doc'], axis=1)
    y = df['price_doc']

    (X_train, X_test,
     y_train, y_test) = train_test_split(X, y, train_size=0.8, random_state=42)
    # обучение модели
    model.fit(X_train, y_train)
    return model


if __name__ == '__main__':
    model = build_and_train()

    filename = 'model_v1.pk'
    with open(filename, 'wb') as file:
        pickle.dump(model, file)
