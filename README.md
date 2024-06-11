<p align="center">
  <a href="https://github.com/destin-v">
    <img src="https://camo.githubusercontent.com/8a5a84adae2071b1d131af237bc0a15253b91bb86b2761bbd62ed3c3ac7aabea/68747470733a2f2f64726976652e676f6f676c652e636f6d2f75633f6578706f72743d766965772669643d31794674652d5241534363463161686b5967314a79626176692d67576a65386b70" alt="drawing" width="500"/>
  </a>
</p>

# 📒 Description
<p align="center">
  <img src="docs/pics/program_logo.png" alt="drawing" width="150"/>
</p>

<p align="center">
  <a href="https://devguide.python.org/versions/">                <img alt="" src="https://img.shields.io/badge/python-^3.10-blue?logo=python&logoColor=white"></a>
  <a href="https://github.com/pre-commit/pre-commit">             <img alt="" src="https://img.shields.io/badge/pre--commit-enabled-blue?logo=pre-commit"></a>
  <a href="https://docs.pytest.org/en/7.1.x/getting-started.html"><img alt="" src="https://img.shields.io/badge/pytest-enabled-blue?logo=pytest&logoColor=white"></a>
  <a href="https://sphinx-book-theme.readthedocs.io/en/stable/">  <img alt="" src="https://img.shields.io/badge/Sphinx-^1.1.2-blue?logo=sphinx&logoColor=white"></a>
  <a href="https://black.readthedocs.io/en/stable/index.html">    <img alt="" src="https://img.shields.io/badge/code%20style-black-blue?logo=stylelint&logoColor=white"></a>
</p>

<p align="center">
  <a href="https://docs.github.com/en/actions/quickstart">                          <img alt="" src="https://img.shields.io/badge/CI-github-brightgreen?logo=github&logoColor=white"></a>
  <a href="https://github.com/destin-v/vs_codex/actions/workflows/pre-commit.yml">  <img alt="pre-commit" src="https://github.com/destin-v/vs_codex/actions/workflows/pre-commit.yml/badge.svg"></a>
  <a href="https://github.com/destin-v/vs_codex/actions/workflows/sphinx.yml">      <img alt="sphinx" src="https://github.com/destin-v/vs_codex/actions/workflows/sphinx.yml/badge.svg"></a>
  <a href="https://github.com/destin-v/vs_codex/actions/workflows/pytest.yml">      <img alt="pytest" src="https://github.com/destin-v/vs_codex/actions/workflows/pytest.yml/badge.svg"></a>
</p>

This is a development template designed with VSCode configurations, development containers, testing/profiling utilities, and automatic documentation.  The code is designed to run with Black to perform automatic formatting and uses pre-commit to check all commits.

# 🌎 Global Config

Make sure to replace the following keywords in this repo:

<center>

| Variable | User Defined |
| -------- | ------------ |
| vs_codex | project name |
| destin-v | GitHub name  |
| W. Li    | author name  |

</center>

# ⚙️ [VSCode Settings](.vscode/README.md)

# 🧪 [Nox](.nox/README.md)

# ♾️ [CI/CD](.github/workflows/README.md)
# 🅿 Pre-commit
Always install/update your pre-commit to use the latest versions prior to starting a project.

```bash
pre-commit install
pre-commit autoupdate
```

# 🎯 Version Control
The `pyproject.toml` defines a set of packages with the allowable ranges that you expect to install.  However, poetry builds a `poetry.lock` that defines the specific versions used by your project.  If you want to ensure everyone on your team installs the same version you will need to commit the `poetry.lock` file to your repo.



# 🐚 Remote Development
To generate your SSH keys, type the following command:

```bash
ssh-keygen
ssh-copy-id <user_id>@<host_ip>   # Copy the SSH keys to the host
ssh <user_id>@<host_ip>           # Log into the host
```

# 🐳 Container Development
* [**Docker**](containers/docker/README.md)
* [**Apptainer**](containers/apptainer/README.md)

## Smokeshow
All `HTML` files can be hosted on a website.

```bash
smokeshow upload path/to/folder  # this will generate a temporary html link
```

# 🔧 Troubleshooting

<details>
<summary>Reducing Git Size</summary>

To remove large files from a Git repo use [**BFG**](https://rtyley.github.io/bfg-repo-cleaner/).

```bash
# Remove the unwanted data from Git
brew install bfg                                        # installs everything you need
git clone --mirror git://example.com/some-big-repo.git  # clone a fresh copy of repo using --mirror
bfg --strip-blobs-bigger-than 1M some-big-repo.git      # remove files larger than a set size

# Now remove the untracked data
cd some-big-repo.git
git reflog expire --expire=now --all && git gc --prune=now --aggressive
git push
```
</details>

<details>
<summary>Smokeshow</summary>
If you are unable to utilize smokeshow make sure you are not behind a proxy.
</details>
