# Description
This is a development template designed with VsCode configurations, development containers, testing/profiling utilities, and automatic documentation.  The code is designed to run with Black to perform automatic formatting and uses pre-commit to check all commits.

# VsCode Recommended Extensions
* [autoDocstring](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring)
* [Black](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter)
* [Chronicler](https://marketplace.visualstudio.com/items?itemName=arcsine.chronicler)
* [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
* [Docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)
* [Git Graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph)
* [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)
* [Material Icon Theme](https://marketplace.visualstudio.com/items?itemName=PKief.material-icon-theme)
* [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
* [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
* [Python Test Explorer for Visual Studio](https://marketplace.visualstudio.com/items?itemName=LittleFoxTeam.vscode-python-test-adapter)
* [Remote - SSH](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh)
* [Remote - SSH: Editing Configuration Files](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh)
* [Remote Explorer](https://marketplace.visualstudio.com/items?itemName=ms-vscode.remote-explorer)
* [Test Explorer UI](https://marketplace.visualstudio.com/items?itemName=hbenl.vscode-test-explorer)

# TestExplorer UI
To have TestExplorer UI properly detect your tests by pressing **Shift-Cmd-P** and selecting:

* **Python: Configure Tests** --> **Pytests** --> **<target_dir>**

Set  `PYTHONPATH` in `.vscode/.env` to point to your test directory.

```
PYTHONPATH="/Users/projects/custom_python_library/"
```

For a full explaination on how to properly setup the TestExplorer UI refer to this [post](https://graycode.ie/blog/how-to-set-up-testing-explorer-with-python-pytest-in-vscode/).

# Remote Development
## SSH Keys
To generate your SSH keys, type the following command:

```console
ssh-keygen
```

Copy the SSH keys to the host:
```console
ssh-copy-id <user_id>@<host_ip>
```

Log into the host:
```console
ssh <user_id>@<host_ip>
```

## Troubleshooting
If performing remote development you may need to configure your file locking parameters depending on whether it is allowed on the host:

* **Settings** -> Remote.SSH: Lockfiles In Tmp [ON]
* **Settings** -> Remote.SSH: useFlock=False [OFF]
* **Cmd-Shift-P** -> Remote-SSH: Kill VS Code Server on Host...

This will disable file locking and restart the remote VS Code host.  You will have to download all of your extensions once it reconnects with the server.
