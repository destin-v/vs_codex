"""
Nox creates a new virtual environment for each individual test.  Thus, it is important for to install all the packages needed for testing.  When using Nox, it will by default grab the current python version available in your environment and run testing with it.

Useful commands:

```console
nox --list              # Lists out all the available sessions
nox -s pytest           # Run pytests
nox -s coverage         # Run coverage
nox -s profile          # Profile the code
nox -s documentation    # Generate documentation

nox                     # Run all sessions
```

"""
import subprocess

import nox


@nox.session(python=["3.8", "3.9", "3.10"])
def pytest(session):
    """Run PyTests."""

    session.run("poetry", "install")
    session.install("pytest")
    session.run("pytest", "-v")


@nox.session
def coverage(session):
    """Runs coverage pytests"""

    session.run("poetry", "install")
    session.run("coverage", "run", "-m", "pytest")
    session.run("coverage", "html", "-d", "save/coverage")
    session.run("coverage", "report", "-m")


@nox.session
def profile(session):
    """Profiles your selected code using scalene."""

    session.run("poetry", "install")
    session.run("mkdir", "-p", "save/profile")
    session.run(
        "scalene",
        "--outfile",
        "save/profile/profile.html",
        "--html",
        "-m",
        "pytest",
        env={"LINES": "25", "COLUMNS": "200"},
    )


@nox.session
def autodoc(session):
    """Generate automatic documentation."""

    session.run("pip", "install", "pdoc")
    subprocess.run(["mkdir", "-p", "html/docs"])
    subprocess.run(["cp", "-rf", "docs/pics", "html/docs/"])

    subprocess.run(
        [
            "pdoc",
            "--logo",
            "https://github.com/destin-v/vs_codex/blob/main/docs/pics/program_logo.png?raw=true",
            "--logo-link",
            "https://github.com/destin-v/vs_codex",
            "--footer-text",
            "Author: W. Li",
            "--output-directory",
            "html",
            "src",
        ]
    )
