# Docker workshop

This repository contains tasks that are intended to give you some hands-on experience with Docker by building images and running containers.

Each task has its own README with instructions.

Solutions can be found in the corresponding solution folder for each task.

## Prerequisites

Each task assumes that you have Docker installed.

### Windows / macOS
On Windows and macOS you can install [Docker Desktop](https://www.docker.com/products/docker-desktop)

#### Setup on Windows
On Windows we need to do some more setup before we are ready.

##### Switch between Windows and Linux containers
On Windows you can toggle which daemon (Linux or Windows) the Docker CLI talks to. The default is supposed to be Linux, but that seems to not always be the case, so make sure it's switched to Linux containers before starting with the tasks.

Right-click the Docker tray icon -> "Switch to Linux containers...".

If you get the option to "Switch to Windows containers..." you are already using Linux containers.

##### Enable file sharing
File sharing is required for mounting volumes when running Linux containers on Windows, so you need to enable the local directories you’d like to share with your Linux containers.

Right-click the Docker tray icon -> Settings -> Shared Drives -> Select the drives you want to share.

In order to solve all the tasks you need to share the drive you cloned this repository to.

### Linux
On Linux (Ubuntu) you can follow [this](https://docs.docker.com/install/linux/docker-ce/ubuntu/) guide.

On Linux it's suggested to create a `docker` group and add your user to it in order to run Docker commands as non-root. See instructions on how to do this here: https://docs.docker.com/install/linux/linux-postinstall/

## Tasks

Each task will ask you to edit some files and run some commands. Make sure this is done in the task folder and not the root folder for this repository.

1) [Hosting a static website](01_static_website)
2) [Fetching content from an API](02_dynamic_website)
3) [Connecting to a PostgreSQL database](03_database)
4) [Data Science using a Jupyter notebook](04_jupyter_notebook)
