# textschema
analysing architecture lectures 

## TODO:

## Setup and Usage
To use the codebase, pip install all required packages in a virtual environment
```
# set up venv
python3 -m venv <name_of_virtualenv>
# activate venv
source <name_of_virtualenv>/bin/activate
# install requirements 
pip3 install requirements.txt
```
Preprocess the dataset (removes extraneous formatting, converts to utf-8 encoding, etc)
```
python3 datahandler.py
```
Now, you can experiment with models/visualizations within jupyter notebooks (or in
python). See `template.ipynb` in
`notebooks` for a simple example. 


## References
