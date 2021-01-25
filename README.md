```
python3 -m venv _python
source _python/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python -m ipykernel install --user --name walk-tracker-kernel --display-name "walk-tracker"
jupyter nbextension enable --py --sys-prefix ipyleaflet
```
