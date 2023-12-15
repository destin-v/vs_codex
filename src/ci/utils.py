"""
Common functions that are executed when running Continuous Integration (CI) include:

* pytests: tests to verify code
* coverage: coverage of code given pytests
* profiling: profiling of certain functions
* autodocs: automatic documentation generation

"""
import os
import subprocess
import webbrowser


def coverage(browser: str = "chrome", local_path: str = "save/coverage"):
    """Run coverage of code based on pytests."""

    # Run coverage using pytest, then record results to docs.
    subprocess.run(["coverage", "run", "-m", "pytest"])
    subprocess.run(["coverage", "html", "-d", local_path])
    subprocess.run(["coverage", "report", "-m"])

    # Open in a browser and view results
    cwd = os.getcwd()
    url = f"file://{cwd}/{local_path}/index.html"
    webbrowser.get(browser).open(url)


def profile():
    """Profiles your selected code using scalene."""

    subprocess.run(["scalene", "-m", "pytest"])


def autodoc(browser: str = "chrome", local_path: str = "save/pdocs"):
    """Generate automatic documentation."""

    subprocess.run(["mkdir", "-p", f"{local_path}/docs"])
    subprocess.run(["cp", "-rf", "docs/pics", f"{local_path}/docs/"])
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
            local_path,
            "src",
        ]
    )

    # Open in a browser and view results
    cwd = os.getcwd()
    url = f"file://{cwd}/{local_path}/index.html"
    webbrowser.get(browser).open(url)
