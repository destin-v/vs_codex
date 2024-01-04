<figure>
    <p align="center">
    <img src="https://drive.google.com/uc?export=view&id=1yFte-RASCcF1ahkYg1Jybavi-gWje8kp" alt="drawing" width="600"/>
    </p>
</figure>

# 📒 Description
<figure>
    <p align="center">
      <img src="docs/pics/program_logo.png" alt="drawing" width="150"/>
    </p>
</figure>

<p align="center">
  <a href="https://devguide.python.org/versions/">              <img alt="" src="https://img.shields.io/badge/python-^3.10-blue?logo=python&logoColor=white"></a>
  <a href="https://docs.github.com/en/actions/quickstart">      <img alt="" src="https://img.shields.io/badge/CI-github-blue?logo=github&logoColor=white"></a>
  <a href="https://black.readthedocs.io/en/stable/index.html">  <img alt="" src="https://img.shields.io/badge/code%20style-black-blue"></a>
  <a href="https://pre-commit.com">                             <img alt="" src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit"></a>
  <a href="https://pytest.org">                                 <img alt="" src="https://img.shields.io/badge/pytest-enabled-brightgreen?logo=pytest&logoColor=white"></a>
  <a href="https://pdoc.dev">                                   <img alt="" src="https://img.shields.io/badge/pdoc-enabled-brightgreen?logo=googledocs&logoColor=white"></a>
  <a href="">                                                   <img alt="" src="https://img.shields.io/badge/license-mit-mediumturquoise"></a>
</p>

This is a development template designed with VsCode configurations, development containers, testing/profiling utilities, and automatic documentation.  The code is designed to run with Black to perform automatic formatting and uses pre-commit to check all commits.

# 📦 VsCode Recommended Extensions
* [autoDocstring](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring)
* [Back & Forth](https://marketplace.visualstudio.com/items?itemName=nick-rudenko.back-n-forth)
* [Black](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter)
* [Chronicler](https://marketplace.visualstudio.com/items?itemName=arcsine.chronicler)
* [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
* [Docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)
* [Git Graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph)
* [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)
* [Markdown Extended](https://marketplace.visualstudio.com/items?itemName=jebbs.markdown-extended)
* [Material Icon Theme](https://marketplace.visualstudio.com/items?itemName=PKief.material-icon-theme)
* [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
* [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
* [Python Test Explorer for Visual Studio](https://marketplace.visualstudio.com/items?itemName=LittleFoxTeam.vscode-python-test-adapter)
* [Remote - SSH](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh)
* [Remote - SSH: Editing Configuration Files](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh)
* [Remote Explorer](https://marketplace.visualstudio.com/items?itemName=ms-vscode.remote-explorer)
* [Test Explorer UI](https://marketplace.visualstudio.com/items?itemName=hbenl.vscode-test-explorer)

# 🅿 Pre-commit
Always update your pre-commit to use the latest versions prior to starting a project.

```console
pre-commit autoupdate
```

# ✨ Theme
To customize your themes you need to set them in your settings.json file.  To identify items you want to change in the editor, you will have to use the inspector:

**Cmd-Shift-P › Inspect Editor Tokens and Scopes**

This feature allows you to view the settings and scope of any item in your editor.  Once you have identified the item you want to change, go to the `settings.json` and make the desired modifications.

References:
* https://stackoverflow.com/questions/57024732/how-can-i-customize-python-syntax-highlighting-in-vs-code
* https://www.alveeakand.com/how-to-modify-themes-in-vscode/

# 🐚 Remote Development
To generate your SSH keys, type the following command:

```console
ssh-keygen
ssh-copy-id <user_id>@<host_ip>   # Copy the SSH keys to the host
ssh <user_id>@<host_ip>           # Log into the host
```

# 🐳 Container Development
An example Dockerfile is included in the `.devcontainer` [**folder**](.devcontainer/README.md).  Containerization is essential if you plan on deploying your software.  As such, it is **strongly** recommended that you use containerization via [Docker](https://www.docker.com) or [Apptainer](https://apptainer.org).


# ♾️ Continuous Integration (CI) Tools
Several CI tools have been included with this codex:

* **coverage**: provides code coverage analysis
* **pdoc**: automatic documentation software
* **scalene**: profiler for evaluating performance

The `noxfile.py` provides an example of how to run each of these.  The `src/ci` folder contains common CI modules.  For an explaination on how to properly setup multiple versions of Python to run with Nox see [here](https://sethmlarson.dev/nox-pyenv-all-python-versions).

# 🧸 Misc
## Tab Removal
In general you should never need to have tabs.  Vscode provides an ordered list of all files and windows you have opened sorted alphabetically.  This is a much better way of accessing files.

* **Cmd-P** # shows all tabs
* Settings › Workbench › Editor: Show Tabs [OFF]

# 🔧 Troubleshooting

## TestExplorer UI
To have TestExplorer UI properly detect your tests by pressing and selecting:

* **Shift-Cmd-P** › Python: Configure Tests › Pytests › <target_dir>

For a full explaination on how to properly setup the TestExplorer UI see [here](https://graycode.ie/blog/how-to-set-up-testing-explorer-with-python-pytest-in-vscode/).

## SSH FileLocking
If performing remote development you may need to configure your file locking parameters depending on whether it is allowed on the host:

* Settings › Remote.SSH: Lockfiles In Tmp [ON]
* Settings › Remote.SSH: useFlock [OFF]
* **Cmd-Shift-P** › Remote-SSH: Kill VS Code Server on Host...

This will disable file locking and restart the remote VS Code host.  You will have to download all of your extensions once it reconnects with the server.

## Reducing Git Size

To remove large files from a Git repo use [BFG](https://rtyley.github.io/bfg-repo-cleaner/).

```console
# Remove the unwanted data from Git
brew install bfg                                        # installs everything you need
git clone --mirror git://example.com/some-big-repo.git  # clone a fresh copy of repo using --mirror
bfg --strip-blobs-bigger-than 1M some-big-repo.git      # remove files larger than a set size

# Now remove the untracked data
cd some-big-repo.git
git reflog expire --expire=now --all && git gc --prune=now --aggressive
git push
```

To repack git to be the smallest size possible while retaining the history use the command:
```console
 git repack -a -d --depth=250 --window=250
 ```
