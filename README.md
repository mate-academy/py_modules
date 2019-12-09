# py_modules

Split the code from the py_tasktracker task into modules: one class in one module. Create the appropriate tests and commands to call linters.

To deploy project on your local machine create new virtual environment and execute this command:

`pip install -r requirements.txt`

To run all style checkers and tests use commands:

`pytest `

`flake8 log worker task linked_list`

`pylint log worker task linked_list`

`mypy --ignore-missing-imports .`
