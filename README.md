## Setup Instructions

1. Install [pyenv](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation)
2. Set up virtualenv
```
pyenv install 3.12.0
pyenv virtualenv 3.12.0 midas
```
3. Activate virtualenv
```
pyenv activate midas
```
4. Download required python packages
```
pip install -r requirements.txt
```