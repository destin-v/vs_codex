import os
import sys

# You will need to append paths to sys.path if you want Sphinx to be able to import them.
sys.path.insert(0, os.path.abspath(".."))
sys.path.insert(0, os.path.abspath("../.."))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project: str = "vs_codex"
copyright: str = "2024, W. Li"
author: str = "W. Li"
release: str = "1.00"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions: list[str] = [
    "sphinx_design",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "myst_parser",
    "sphinx.ext.viewcode",
]

source_suffix: dict = {".rst": "restructuredtext"}

# Setting options
autosummary_generate: bool = True
autosummary_imported_members: bool = True
autosummary_generate_overwrite: bool = True
exclude_patterns: list[str] = []
myst_enable_extensions: list[str] = ["colon_fence"]
pygments_style: str = "dracula"
templates_path: list[str] = ["_templates"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = "vs_codex"
html_theme: str = "sphinx_book_theme"
html_static_path: list[str] = ["_static"]
# html_logo: str = "../pics/program_logo.png"
html_theme_options: dict = {
    "use_sidenotes": True,  # allow Edward Tufte style side-nodes
    "repository_url": "https://github.com/destin-v/vs_codex",  # repo link
    "use_repository_button": True,
}
