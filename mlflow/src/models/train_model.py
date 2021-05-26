import argparse
import math
import mlflow
import pandas as pd
import xgboost
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


def parse_args():
    parser = argparse.ArgumentParser(description='House Prices ML')
    parser.add_argument(
        '--learning-rate',
        type=float,
        default=0.3,
        help='taxa de aprendizado para atualizar tamanho de cada passo do boosting'
    )
    parser.add_argument(
        '--max-depth',
        type=int,
        default=6,
        help='profundidade maxima das arvores'
    )
    return parser.parse_args()


df = pd.read_csv('data/processed/casas.csv')
X = df.drop('preco', axis=1)
y = df['preco'].copy()

X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.3,
                                                    random_state=42)

dtrain = xgboost.DMatrix(X_train, label=y_train)
dtest = xgboost.DMatrix(X_test, label=y_test)


def main():
    args = parse_args()
    xgb_params = {'learning_rate': args.learning_rate,
                  'max_depth': args.max_depth, 'seed': 42}

    mlflow.set_tracking_uri('http://localhost:5000')
    mlflow.set_experiment('house_prices_script')
    with mlflow.start_run():
        mlflow.xgboost.autolog()
        xgb = xgboost.train(xgb_params, dtrain, evals=[(dtrain, 'train')])

        xgb_pred = xgb.predict(dtest)

        mse = mean_squared_error(y_test, xgb_pred)  # erro quadrado médio
        rmse = math.sqrt(mse)  # raiz erro quadrado medio
        r2 = r2_score(y_test, xgb_pred)

        mlflow.log_metrics({'mse': mse, 'rmse': rmse, 'r2': r2})


if __name__ == '__main__':
    main()
