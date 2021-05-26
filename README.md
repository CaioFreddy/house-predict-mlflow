# Exemplo de projeto com mlflow

## Instalar dependencias
- pip install -r requirements.txt

## Treino do modelo
- python src/models/train_model.py --learning-rate [valor do learning rate] --max-depth [valor maximo de profundidade]
- python src/models/train_model.py --learning-rate 0.3 --max-depth 5

## Execucao via script
### Editar dentro do script o caminho e id do modelo treinado
- python src/models/predict_model.py 

## Execucao no terminal
- mlflow models predict -m [id-da-execucao] -i [base-de-entrada] -t [formato] -o [arquivo-saída]
- mlflow models predict -m 'runs:/c10dfb69dd0a472b82e32d905dd9171e/model' -i 'data/processed/casas_X.csv' -t 'csv' -o 'data/output/precos2.csv'

## Execucao na api
- mlflow models serve -m [id-da-execução] -p [porta]
- mlflow models serve -m 'runs:/c10dfb69dd0a472b82e32d905dd9171e/model' -p 5001

- Request POST no endereço [url]/invocations
```json
{
    "columns": ["tamanho", "ano", "garagem"],
    "data": [
        [150, 2003, 2],
        [80, 2010, 3]
    ]
}
```
