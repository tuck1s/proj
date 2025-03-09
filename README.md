# Python Project Template

[![ci](https://github.com/tuck1s/proj/actions/workflows/ci.yaml/badge.svg)](https://github.com/tuck1s/proj/actions/workflows/ci.yaml)

This is a simple Python project structure with source files that build into a single command-line tool.

`pip` is used to install project dependencies. To avoid running this as root, the container runs as user `vscode`.

## Tests
`pytest` tests are included, these can be opened and run locally or in a Docker container.

The tests can be run from the vscode [testing menu](https://code.visualstudio.com/docs/python/testing#_configure-tests), or from a terminal.

```
pytest
===================================================== test session starts ======================================================
platform linux -- Python 3.12.9, pytest-8.3.5, pluggy-1.5.0
rootdir: /workspaces/proj
configfile: pytest.ini
plugins: cov-6.0.0
collected 4 items                                                                                                              

tests/test_cli.py ..                                                                                                     [ 50%]
tests/test_module1.py .                                                                                                  [ 75%]
tests/test_module2.py .                                                                                                  [100%]

====================================================== 4 passed in 0.07s =======================================================
```

In [test_cli.py](.tests/test_cli.py)
* `unittest.mock.patch` is used to mock * `argparse.ArgumentParser.parse_args` to simulate different command-line arguments.
`patch('builtins.print')` is used to mock the print function to verify the output.

## Code coverage

"Run test with Coverage" can be used from the VS code test explorer menu, which uses `pytest-cov`.
The popular [Coverage Gutters](https://marketplace.visualstudio.com/items?itemName=ryanluker.vscode-coverage-gutters) extension shows the results visually. This is installed into the container.


## CI with Github Actions

The tests are also run via Github Actions on checkin.
