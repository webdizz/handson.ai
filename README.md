handson.ai
========================

## Work in Progress 

This is a repository to hold all related source code along with content for course on AI.
The goal of the course is to provide brief hands-on overview of actual state of AI field.

The course was inspired by the fact that in order to understand something in depth one needs to teach it to another one and different sources from the internet like [fast.ai](http://fast.ai), [Siraj Raval](https://www.youtube.com/channel/UCWN3xxRkmTPmbKwht9FuE5A) etc.

Prerequisite
------------------------

Understanding on Linear Algebra + some programming experience.

Usage
------------------------

Before to use source one needs to install [Anaconda](https://conda.io) and [Git](https://git-scm.com/).

When [Anaconda](https://conda.io) already installed clone repository and create an environment using next commands:

```sh
    git clone https://github.com/webdizz/handson.ai.git
    cd handson.ai # change directory to clone one
    conda env create # create conda environment from environment.yml file
    source activate handson.ai # activation of environment
    conda install -c conda-forge jupyter_contrib_nbextensions  # to install  additional extensions for Jupyter Notebook as a workaround because currently there is an issue with conda based installation
```

Open [Jupyter](https://github.com/jupyter/jupyter):

```sh
    jupyter notebook # will open browser at http://localhost:8888
```

On remote server we can start it using next command:

```sh
    nohup jupyter notebook --no-browser --ip=`hostname -I` &
    cat nohup.out # to obtain token for later authentication, for example,  http://localhost:8888/?token=5c78b5f97274301d71615d05a59660db07307498766758e0
```
