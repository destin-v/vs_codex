"""
Common functions that are executed when running Continuous Integration (CI) include:

* `pytests`: tests to verify code
* `pytest_cov`: pytest with coverage of code
* `coverage`: coverage of code given pytests
* `pdoc`: automatic documentation generation
"""
import os
import subprocess
import webbrowser


def pytest_cov(browser: str | None = None, local_path: str = "save/pytest-cov", html: bool = True):
    """Run pytest with coverage report.

    Args:
        browser (str | None, optional): Possible arguments include `Chrome`, `Firefox`, `Safari`.  If no browser is specified it will open using your system's default browser. Defaults to None.
        local_path (str, optional): The local path to save the files. Defaults to "save/pytest-cov".
        html (bool, optional): Option for viewing as HTML. Defaults to True.
    """
    subprocess.run(["pytest", "--cov=./", f"--cov-report=html:{local_path}"])

    if html:
        # Open in a browser and view results
        cwd = os.getcwd()
        url = f"file://{cwd}/{local_path}/index.html"
        webbrowser.get(browser).open(url)

def coverage(browser: str | None = None, local_path: str = "save/coverage", html: bool = True):
    """Run coverage of code based on pytests.

    Args:
        browser (str | None, optional): Possible arguments include `Chrome`, `Firefox`, `Safari`.  If no browser is specified it will open using your system's default browser. Defaults to None.
        local_path (str, optional): The local path to save the files. Defaults to "save/coverage".
        html (bool, optional): Option for viewing as HTML. Defaults to True.
    """
    # Run coverage using pytest, then record results to docs.
    subprocess.run(["coverage", "run", "-m", "pytest"])
    subprocess.run(["coverage", "html", "-d", local_path])
    subprocess.run(["coverage", "report", "-m"])

    if html:
        # Open in a browser and view results
        cwd = os.getcwd()
        url = f"file://{cwd}/{local_path}/index.html"
        webbrowser.get(browser).open(url)
    


def pdoc(browser: str | None = None, local_path: str = "save/pdocs", html: bool = True):
    """Generate automatic documentation.

    Args:
        browser (str | None, optional): Possible arguments include `Chrome`, `Firefox`, `Safari`.  If no browser is specified it will open using your system's default browser. Defaults to None.
        local_path (str, optional): The local path to save the files. Defaults to "save/pdocs".
        html (bool, optional): Option for viewing as HTML. Defaults to True.
    """

    subprocess.run(["mkdir", "-p", f"{local_path}/docs"])
    subprocess.run(["cp", "-rf", "docs/pics", f"{local_path}/docs/"])
    subprocess.run(
        [
            "pdoc",
            "-d",
            "google",
            "--logo",
            "https://github.com/destin-v/vs_codex/blob/main/docs/pics/program_logo.png?raw=true",
            "--logo-link",
            "https://github.com/destin-v/vs_codex",
            "--math",
            "--footer-text",
            "Author: W. Li",
            "--output-directory",
            local_path,
            "src",
        ]
    )

    if html:
        # Open in a browser and view results
        cwd = os.getcwd()
        url = f"file://{cwd}/{local_path}/index.html"
        webbrowser.get(browser).open(url)
