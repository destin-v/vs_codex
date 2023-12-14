"""
Common functions that are executed when running Continuous Integration (CI) include:

* pytests: tests to verify code
* coverage: coverage of code given pytests
* profiling: profiling of certain functions
* autodocs: automatic documentation generation

"""
import os
import subprocess


def pytest():
    """Run pytests."""
    subprocess.run(["pytest"])


def coverage():
    """Run coverage of code based on pytests."""
    # Run coverage using pytest, then record results to docs.
    subprocess.run(["coverage", "run", "-m", "pytest"])
    subprocess.run(["coverage", "html", "-d", "save/coverage"])
    subprocess.run(["coverage", "report", "-m"])


def profile():
    """Profiles your selected code using scalene."""

    cwd = os.getcwd()
    subprocess.run(["mkdir", "-p", "save/profile"])

    # Profile the code.
    subprocess.run(
        [
            "scalene",
            "--outfile",
            f"{cwd}/save/profile/profile.html",
            "--html",
            "-m",
            "pytest",
        ],
        shell=True,
        env={
            "LINES": "25",
            "COLUMNS": "200",
        },
    )


def autodoc():
    """Generate automatic documentation."""

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


if __name__ == "__main__":
    # pytest()
    # coverage()
    profile()
    # autodoc()
