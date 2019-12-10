# py_modules

Split the code from the py_tasktracker task into modules: one class in one module. Create the appropriate tests and commands to call linters.

To deploy project on your local machine create new virtual environment and execute this command:

`pip install -r requirements.txt`

To run all style checkers and tests use commands:

pytest

flake8 .

pylint test_modules.py

pylint log.py

pylint tasks.py

pylint day_plan.py

pylint worker.py

mypy --ignore-missing-imports .
