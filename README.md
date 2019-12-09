# py_modules

Split the code from the py_tasktracker task into modules: one class in one module. Create the appropriate tests and commands to call linters.

To deploy project on your local machine create new virtual environment and execute this command:

`pip install -r requirements.txt`

'pytest'

'flake8 .'

'pylint log register worker task test_modules'

'mypy --ignore-missing-imports .'