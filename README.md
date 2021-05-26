# Exemplo de projeto com mlflow

## Instalar dependencias
- pip install -r requirements.txt

## Executar o mlflow ui
- mlflow ui

## Executar o mlflow ui armazenando os artefatos no banco SQLite
- mlflow server --backend-store-uri sqlite:///[nome do artefato] --default-artifact-root [destino] --host [host]
- mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./artifacts --host 0.0.0.0


## Treino do modelo
- python src/models/train_model.py --learning-rate [valor do learning rate] --max-depth [valor maximo de profundidade]
- python src/models/train_model.py --learning-rate 0.3 --max-depth 5

## Execucao via script
### Editar dentro do script o caminho e id do modelo treinado
- python src/models/predict_model.py 

## Execucao no terminal
- mlflow models predict -m [id-da-execucao] -i [base-de-entrada] -t [formato] -o [arquivo-saída]
- mlflow models predict -m 'runs:/c10dfb69dd0a472b82e32d905dd9171e/model' -i 'data/processed/casas_X.csv' -t 'csv' -o 'data/output/precos2.csv'

## Execucao na api usando id da execução
- mlflow models serve -m [id-da-execução] -p [porta]
- mlflow models serve -m 'runs:/c10dfb69dd0a472b82e32d905dd9171e/model' -p 5001

## Execucao na api usando o model salvo
- export MLFLOW_TRACKING_URI=http://127.0.0.1:5000
- mlflow models serve -m [modelo] -p 5001
- mlflow models serve -m 'models:/House Prices/Production' -p 5001

## Criacao da api em imagem docker
- export MLFLOW_TRACKING_URI=http://127.0.0.1:5000
- mlflow models build-docker -m [modelo] -n [nome-imagem]
- mlflow models build-docker -m 'models:/House Prices/Production' -n 'house-prices'

## Iniciar api docker
- docker run -p [porta externa]:[porta interna] [nome-imagem]
- docker run -p 5001:8080 "house-prices"
## Consumir api REST
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

