"""
Nox creates a new virtual environment for each individual test.  Thus, it is important for to install all the packages needed for testing.  When using Nox, it will by default grab the current python version available in your environment and run testing with it.

Useful commands:

```console
nox --list              # Lists out all the available sessions
nox -r -s pytest           # Run pytests
nox -r -s pytest_cov       # Run pytests with coverage report
nox -r -s coverage         # Run coverage (stand-alone)
nox -r -s scalene          # Profile the code
nox -r -s pdoc             # Generate documentation

nox                     # Run all sessions
```

"""
import nox

from src.ci.utils import pdoc as ci_pdoc
from src.ci.utils import coverage as ci_coverage
from src.ci.utils import pytest_cov as ci_pytest_cov


@nox.session
def pytest(session):
    """Run PyTests."""

    session.run("poetry", "install", "--with=dev", external=True)
    session.run("pytest", "-v")


@nox.session
def pytest_cov(session):
    """Run PyTests with coverage.  This generates a HTML report."""

    session.run("poetry", "install", "--with=dev", external=True)
    ci_pytest_cov(html=True)


@nox.session
def coverage(session):
    """Runs coverage pytests"""

    session.run("poetry", "install", "--with=dev", external=True)
    ci_coverage(html=True)


@nox.session
def scalene(session):
    """Profiles your selected code using scalene."""

    session.run("poetry", "install", "--with=dev", external=True)
    session.run("scalene", "-m", "pytest")


@nox.session
def pdoc(session):
    """Generate pdocs."""

    session.run("poetry", "install", "--with=dev", external=True)
    ci_pdoc(html=True)


@nox.session
def deploy_pdoc(session):
    """This process is designed to generate a set of artifacts for deployment.  It is designed to operate with Github actions."""

    session.run("poetry", "install", "--with=dev", external=True)
    ci_pdoc(html=False)
