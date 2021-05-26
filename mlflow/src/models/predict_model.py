import pandas as pd
import mlflow
logged_model = 'file:///home/kyle/Projetos/house-predict-mlflow/mlflow/mlflow/mlruns/1/9f7fa08a8d2b485699d8ad5dba01ecbf/artifacts/model'

# Load model as a PyFuncModel.
loaded_model = mlflow.pyfunc.load_model(logged_model)

# Predict on a Pandas DataFrame.
data = pd.read_csv('data/processed/casas_X.csv')
predicted = loaded_model.predict(data)

data['predicted'] = predicted
data.to_csv('data/output/precos.csv', index=False)
