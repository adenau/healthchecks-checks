# healthchecks-checks
Collections of checks to be used with healthchecks.io


# Developper instructions

Create your virtual environment using 

  python3 -m venv env

To enter it

  source env/bin/activate

To install dependencies

  python -m pip install -r requirements.txt

To exit it

  deactivate

To save dependencies

  pip freeze > requirements.txt

To create packages

  python3 setup.py sdist bdist_wheel

To upload

  python3 -m twine upload --repository testpypi dist/*