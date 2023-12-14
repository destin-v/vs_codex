# :ledger: Description
## :whale: Docker
* Primary method for building and maintaining **un-secure** containers.
* Must have root access in order to work.
* Deployable to any machine.
* [Additional Information](#🐳-docker-notes)

## :owl: Apptainer
* Primary method for building and maintaining **secure** containers.
* Used primarily in settings where root access is not possible.
* Deployable to any machine.
* [Additional Information](#🦉-apptainer-notes)

## :package: Packages
The default development containers will these packages by default.  Only the essentials are included.

* [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/) 
* [Oh My Bash](https://github.com/ohmybash/oh-my-bash)
* [Oh My Zsh](https://ohmyz.sh)
* [Precommit](https://pre-commit.com)

# :whale: Docker Notes

## :musical_score:  Docker Compose
* Allows you to create multiple different builds using different Docker files.
* The context directory can be set from the `docker_compose.yml` file.
* More options than a standard Docker file.

## :athletic_shoe: Running Commands
* In Docker each `RUN` command is treated as a new shell instance.  This means that commands cannot persist across different RUN commands.

```Docker
RUN command1    # this command is run in its own shell!
RUN command2    # this command is run in its own shell!
```

## :card_file_box: Copying Folders/Files
* If you need to copy files or directories into the Docker container, first put them in an **artifacts** directory that can be seen from the context directory.

```Docker
COPY <artifact_directory> <container_path>
```
## :open_file_folder: Context Directory

* By default Dockerfiles are only aware of what is in their **context directory**.  A context directory is the directory where a Dockerfile is located in.  It cannot access any files outside of the context directory.

* The context directory can be set from the command line or from a `docker_compose.yml` file.

* It is recommended that all folders/files be copied be placed in an **artifacts** directory that is under the context directory.

## :floppy_disk: Out of Memory
* Occasionally you will need to clean your docker images and docker volumes in order to recover memory.

```console
docker volume prune
docker image prune
docker container prune
```

# :owl: Apptainer Notes
