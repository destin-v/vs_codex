# 👨‍🔬 PyTests
Tests should include both `unit testing` and `integration testing`.  Prior to developing a feature, the tests should be written to verify that the function behaves as expected.  Once the verification function has been written, the function to perform the task should be written.

```bash
pytest # run all tests
pytest pytest src/tests/basic_test.py # run tests in module
pytest src/tests/basic_test.py::test_hello_world # run a specific test
```

PyTest provides additional features such as [parameter sweeping](https://docs.pytest.org/en/7.1.x/example/parametrize.html), [fixtures](https://docs.pytest.org/en/7.1.x/explanation/fixtures.html?highlight=fixtures), and [logging](https://docs.pytest.org/en/7.1.x/how-to/logging.html?highlight=fixtures).  These should be applied depending on the test requirements.

## Coverage
PyTests offers `coverage` support.  When running PyTests with Coverage, it will generate a HTML that show which parts of your repo have not been traced using PyTests.  This lets you know which areas of your code still need to be tested.

```console
pytest --cov=<repo_path> --cov-report=html:<target_output>
```
## Design Pattern
Placed a `tests` folder underneath every `module` that you want to create tests for.  A top level `tests` folder can be included for integration tests that span multiple modules.

```
project
└───src
│   └───tests
│       └─── __init__.py
│       └─── unit_test.py
└───tests
    └─── __init__.py
    └─── integration_test.py
```
