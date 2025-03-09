# Python Project Template

[![ci](https://github.com/tuck1s/proj/actions/workflows/ci.yaml/badge.svg)](https://github.com/tuck1s/proj/actions/workflows/ci.yaml)

This is a simple Python project template, with source files that build a single command-line tool.

`pip` is used to install project dependencies. The container runs as user `vscode`.

## Tests
`pytest` and example unit tests are included.

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

Command-line arguments are exercised by [test_cli.py](.tests/test_cli.py):
* `unittest.mock.patch` simulates different command-line arguments (`argparse.ArgumentParser.parse_args`).
* `patch('builtins.print')` is mocks the print function to verify the output.

## Code coverage and visual display

"Run test with Coverage" (using `pytest-cov`) can be used from the VS code test explorer menu.
The popular [Coverage Gutters](https://marketplace.visualstudio.com/items?itemName=ryanluker.vscode-coverage-gutters) extension shows the results visually. This is installed into the container.


## CI with Github Actions

The tests are also run via Github Actions on checkin.
