from dataclasses import dataclass

import nox

from src.ci.utils import view_html


@dataclass
class config:
    """Nox creates a new virtual environment for each individual test.  Thus, it is important for to install all the packages needed for testing.  When using Nox, it will by default grab the current python version available in your environment and run testing with it."""

    coverage_pytest_path: str = "docs/source/_static/pytest-cov"
    coverage_module_path: str = "docs/source/_static/coverage"
    pdoc_path: str = "docs/source/_static/pdocs"
    scalene_path: str = "docs/source/_static/scalene"
    sphinx_path: str = "docs/build/html"


@nox.session
def pytest(session: nox.Session):
    """Run PyTests.

    Args:
        session (nox.Session): The current Nox session.
    """

    session.run("poetry", "install", "--with=dev", "--no-root")
    session.run("pytest", "-v")


@nox.session
def pytest_cov(session: nox.Session):
    """Run PyTest coverage.

    Args:
        session (nox.Session): The current Nox session.
    """

    session.run("poetry", "install", "--with=dev", "--no-root")
    session.run("pytest", "--cov=./", f"--cov-report=html:{config.coverage_pytest_path}")


@nox.session
def coverage(session: nox.Session):
    """Runs coverage only on specific module.

    Args:
        session (nox.Session): The current Nox session.
    """

    session.run("poetry", "install", "--with=dev", "--no-root")
    session.run("coverage", "run", "-m", "pytest")
    session.run("coverage", "html", "-d", config.coverage_module_path)
    session.run("coverage", "report", "-m")
    session.run("mv", ".coverage", config.coverage_module_path)


@nox.session
def scalene(session: nox.Session):
    """Profiles your selected code using scalene.

    Args:
        session (nox.Session): The current Nox session.
    """

    session.run("poetry", "install", "--with=dev", "--no-root")
    session.run("scalene", "-m", "pytest")
    session.run("mkdir", "-p", f"{config.scalene_path}")
    session.run("mv", "profile.html", f"{config.scalene_path}/profile.html")
    session.run("mv", "profile.json", f"{config.scalene_path}/profile.json")


@nox.session
def pdoc(session: nox.Session):
    """Generate pdocs.

    Args:
        session (nox.Session): The current Nox session.
    """

    session.run("poetry", "install", "--with=dev", "--no-root")
    session.run("mkdir", "-p", f"{config.pdoc_path}/docs")
    session.run("cp", "-rf", "docs/pics", f"{config.pdoc_path}/docs/")
    session.run(
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
        config.pdoc_path,
        "src",
    )


@nox.session
def sphinx(session: nox.Session):
    """Generate Sphinx documentation.

    Args:
        session (nox.Session): The current Nox session.
    """
    session.run("poetry", "install", "--with=dev", "--no-root")

    # Build Sphinx
    session.run("sphinx-apidoc", "-o", "docs/source/pages/api", "src")
    session.chdir("docs")
    session.run("make", "clean", external=True)
    session.run("make", "html", external=True)
    session.chdir("../")


@nox.session
def show_pytest_cov(session: nox.Session):
    """Show pytest coverage in HTML.

    Args:
        session (nox.Session): The current Nox session.
    """

    pytest_cov(session)
    view_html(config.coverage_pytest_path)


@nox.session
def show_pdoc(session: nox.Session):
    """Show pdoc in HTML.

    Args:
        session (nox.Session): The current Nox session.
    """

    pdoc(session)
    view_html(config.pdoc_path)


@nox.session
def show_sphinx(session: nox.Session):
    """Show Sphinx in HTML.

    Args:
        session (nox.Session): The current Nox session.
    """

    sphinx(session)
    view_html(config.sphinx_path)


@nox.session
def build(session: nox.Session):
    """Build all artifacts.

    Args:
        session (nox.Session): The current Nox session.
    """

    # Build external docs
    coverage(session)
    pdoc(session)
    pytest_cov(session)
    scalene(session)
    sphinx(session)
