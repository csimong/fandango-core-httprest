# Commands

## Conda environment
```
conda create -n core-httprest python=3.11
conda activate core-httprest
pip install -r requirements.txt
```

## Run app
```
python app.py
```

# Paths and enpoints
## Swagger documentation
http://127.0.0.1:5000/
http://127.0.0.1:5000/swagger.json

## FandanGO commands
```
python execute.py createproject --id 123
python execute.py deleteproject --id 123
python execute.py copydata --plugin irods --id 456 --rawdata path/to/rawdata

```
