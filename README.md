# Python Project Template

[![ci](https://github.com/tuck1s/proj/actions/workflows/ci.yaml/badge.svg)](https://github.com/tuck1s/proj/actions/workflows/ci.yaml)

This is a simple Python project structure with source files that build into a single command-line tool.

`pip` is used to install project dependencies. To avoid running this as root, the container runs as user `vscode`.

## Tests
`pytest` tests are included, these can be opened and run locally or in a Docker container.

The tests can be run from the vscode [testing menu](https://code.visualstudio.com/docs/python/testing#_configure-tests), or from a terminal.

```bash
scode@330fc421df1c:/workspaces/proj$ pytest

===================================================== test session starts ======================================================
platform linux -- Python 3.12.9, pytest-8.3.5, pluggy-1.5.0
rootdir: /workspaces/proj
configfile: pytest.ini
collected 2 items                                                                                                              

tests/test_module1.py .                                                                                                  [ 50%]
tests/test_module2.py .                                                                                                  [100%]

====================================================== 2 passed in 0.01s =======================================================
```

## CI with Github Actions

The tests are also run via Github Actions on checkin.
