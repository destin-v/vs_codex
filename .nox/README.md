# 🧪 Nox
Nox is the spiritual successor to Tox for running scripts in controlled environments.

* **coverage**: provides code coverage analysis
* **pdoc**: basic documentation software
* **scalene**: profiler for evaluating performance
* **sphinx**: advance documentation software

The `noxfile.py` provides an example of how to run each of these:

```bash
    nox --list                 # Lists out all the available sessions
    nox -r -s pytest           # Run pytests
    nox -r -s pytest_cov       # Run pytests with coverage report
    nox -r -s coverage         # Run coverage (stand-alone)
    nox -r -s scalene          # Profile the code
    nox -r -s pdoc             # Generate documentation
    nox -r -s show_pdoc        # View HTML of pdoc
    nox -r -s show_sphinx      # View HTML of sphinx
```


For an explanation on how to properly setup multiple versions of Python to run with Nox see [**here**](https://sethmlarson.dev/nox-pyenv-all-python-versions).
