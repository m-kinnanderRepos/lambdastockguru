Basic working for lambda project.

Replicate what will run in lambda locally:

- Run this project in its own virtual environment. Look into venv or pyenv.
- You need to pip install -r requirements.txt.
- You will need to set up secrets in AWS.
  - I will eventually document what key/values are needed.
- Uncomment the imports in lambdaFolder/stock.py, lambdaFolder/stockGuru.py, and lambdaFolder/stock_classes.py and then run `python lambdaFolder/stockGuru`.
