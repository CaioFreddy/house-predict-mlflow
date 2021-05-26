# Exemplo de projeto com mlflow

## Instalar dependencias
- pip install -r requirements.txt

## Treino do modelo
- python src/models/train_model.py --learning-rate [valor do learning rate] --max-depth [valor maximo de profundidade]

## Execucao via script
- python src/models/predict_model.py 

## Execucao no terminal
- mlflow models predict -m [id-da-execucao] -i [base-de-entrada] -t [formato] -o [arquivo-saída]

## Execucao na api
- mlflow models serve -m [id-da-execução]
- Request POST no endereço [url]/invocations
```json
{
    'columns': ['tamanho', 'ano', 'garagem'],
    'data': [
        [150, 2003, 2],
        [80, 2010, 3]
    ]
}
```
