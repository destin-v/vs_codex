<p align="center">
  <a href="https://github.com/destin-v">
    <img src="https://drive.google.com/uc?export=view&id=1yFte-RASCcF1ahkYg1Jybavi-gWje8kp" alt="drawing" width="500"/>
  </a>
</p>

# 📒 Description
<p align="center">
  <img src="docs/pics/program_logo.png" alt="drawing" width="150"/>
</p>

<p align="center">
  <a href="https://devguide.python.org/versions/">              <img alt="" src="https://img.shields.io/badge/python-^3.10-blue?logo=python&logoColor=white"></a>
  <a href="https://docs.github.com/en/actions/quickstart">      <img alt="" src="https://img.shields.io/badge/CI-github-blue?logo=github&logoColor=white"></a>
  <a href="https://black.readthedocs.io/en/stable/index.html">  <img alt="" src="https://img.shields.io/badge/code%20style-black-blue"></a>
</p>

<p align="center">
  <a href="https://github.com/destin-v/vs_codex/actions/workflows/pre-commit.yml">  <img alt="pre-commit" src="https://github.com/destin-v/vs_codex/actions/workflows/pre-commit.yml/badge.svg"></a>
  <a href="https://github.com/destin-v/vs_codex/actions/workflows/pdoc.yml">        <img alt="pdoc" src="https://github.com/destin-v/vs_codex/actions/workflows/pdoc.yml/badge.svg"></a>
  <a href="https://github.com/destin-v/vs_codex/actions/workflows/pytest.yml">      <img alt="pytest" src="https://github.com/destin-v/vs_codex/actions/workflows/pytest.yml/badge.svg"></a>
</p>

This is a development template designed with VsCode configurations, development containers, testing/profiling utilities, and automatic documentation.  The code is designed to run with Black to perform automatic formatting and uses pre-commit to check all commits.

# 📦 VsCode Recommended Extensions


<details>
  <summary>Code</summary>

  * [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
</details>

<details>
  <summary>Documentation</summary>

  * [Automatic Doc String](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring)
  * [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)
  * [Markdown Extended](https://marketplace.visualstudio.com/items?itemName=jebbs.markdown-extended)
</details>

<details>
  <summary>Linting / Formatting</summary>

  * [Black](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter)
  * [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
</details>

<details>
  <summary>Testing</summary>

  * [Python Test Explorer for Visual Studio](https://marketplace.visualstudio.com/items?itemName=LittleFoxTeam.vscode-python-test-adapter)
  * [Test Explorer UI](https://marketplace.visualstudio.com/items?itemName=hbenl.vscode-test-explorer)
</details>

<details>
  <summary>Configuration Control</summary>

  * [Git Graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph)
</details>

<details>
  <summary>Containers</summary>

  * [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
  * [Docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)
</details>

<details>
  <summary>Remote</summary>

  * [Remote - SSH](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh)
  * [Remote - SSH: Editing Configuration Files](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh)
  * [Remote Explorer](https://marketplace.visualstudio.com/items?itemName=ms-vscode.remote-explorer)
</details>

<details>
  <summary>Misc</summary>

  * [Back & Forth](https://marketplace.visualstudio.com/items?itemName=nick-rudenko.back-n-forth)
  * [Chronicler](https://marketplace.visualstudio.com/items?itemName=arcsine.chronicler)
  * [Material Icon Theme](https://marketplace.visualstudio.com/items?itemName=PKief.material-icon-theme)
  </details>

# 🅿 Pre-commit
Always install/update your pre-commit to use the latest versions prior to starting a project.

```bash
pre-commit install
pre-commit autoupdate
```

# 🎯 Version Control
The `pyproject.toml` defines a set of packages with the allowable ranges that you expect to install.  However, poetry builds a `poetry.lock` that defines the specific versions used by your project.  If you want to ensure everyone on your team installs the same version you will need to commit the `poetry.lock` file to your repo.

# 🅰 Font
You will need to install [**Nerd Fonts**]([containers/README.md](https://www.nerdfonts.com/)) MesloLGLDZ Nerd Font.  This will be used to display glyphs and icons for all of your terminals.

# ✨ Theme
To customize your themes you need to set them in your settings.json file.  To identify items you want to change in the editor, you will have to use the inspector:

**Cmd-Shift-P › Inspect Editor Tokens and Scopes**

This feature allows you to view the settings and scope of any item in your editor.  Once you have identified the item you want to change, go to the `settings.json` and make the desired modifications.

### References:
* https://stackoverflow.com/questions/57024732/how-can-i-customize-python-syntax-highlighting-in-vs-code
* https://www.alveeakand.com/how-to-modify-themes-in-vscode/

# 🐚 Remote Development
To generate your SSH keys, type the following command:

```bash
ssh-keygen
ssh-copy-id <user_id>@<host_ip>   # Copy the SSH keys to the host
ssh <user_id>@<host_ip>           # Log into the host
```

# 🐳 Container Development
An example Dockerfile is included in the [**.devcontainer**](.devcontainer/README.md) folder.  An Apptainer template is included in the [**containers**](containers/README.md) folder.  Containerization is essential if you plan on deploying your software.  As such, it is **strongly** recommended that you use containerization via [**Docker**](https://www.docker.com) or [**Apptainer**](https://apptainer.org).


## Scripts
Several CI tools have been included with this codex:

* **coverage**: provides code coverage analysis
* **pdoc**: automatic documentation software
* **scalene**: profiler for evaluating performance

The `noxfile.py` provides an example of how to run each of these.  The `src/ci` folder contains common CI modules.  For an explaination on how to properly setup multiple versions of Python to run with Nox see [**here**](https://sethmlarson.dev/nox-pyenv-all-python-versions).

All of the CI tools listed above can generate a `HTML` website.  You can upload the folders to a temporary website to view its contents:

```bash
smokeshow upload path/to/folder  # this will generate a tempoary html link
```

# 🧸 Misc
## Tab Removal
In general you should never need to have tabs.  Vscode provides an ordered list of all files and windows you have opened sorted alphabetically.  This is a much better way of accessing files.

* **Cmd-P** # shows all tabs
* Settings › Workbench › Editor: Show Tabs [OFF]

# 🔧 Troubleshooting

<details>
<summary>TestExplorer UI</summary>
To have TestExplorer UI properly detect your tests by pressing and selecting:

* **Shift-Cmd-P** › Python: Configure Tests › Pytests › <target_dir>

For a full explaination on how to properly setup the TestExplorer UI see [**here**](https://graycode.ie/blog/how-to-set-up-testing-explorer-with-python-pytest-in-vscode/).
</details>

<details>
<summary>SSH FileLocking</summary>
If performing remote development you may need to configure your file locking parameters depending on whether it is allowed on the host:

* Settings › Remote.SSH: Lockfiles In Tmp [ON]
* Settings › Remote.SSH: useFlock [OFF]
* **Cmd-Shift-P** › Remote-SSH: Kill VS Code Server on Host...

This will disable file locking and restart the remote VS Code host.  You will have to download all of your extensions once it reconnects with the server.

</details>

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
