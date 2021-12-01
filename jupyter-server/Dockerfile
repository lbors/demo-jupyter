ARG OWNER=jupyter
ARG BASE_CONTAINER=$OWNER/minimal-notebook
FROM $BASE_CONTAINER

#LABEL maintainer="Jupyter Project <jupyter@googlegroups.com>"

COPY dockerpy_remote_exec.ipynb work/

USER root

# Install all OS dependencies for fully functional notebook server
RUN apt-get update --yes && \
    apt-get install --yes --no-install-recommends \
    openssh-server \
    ssh \
    net-tools && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

USER ${NB_UID}

RUN pip install docker

RUN pip install -U sshkernel && \
    python -m sshkernel install --user

RUN pip install -U bash_kernel && \
    python -m bash_kernel.install

RUN pip install -U sos-notebook sos-papermill sos-r && \
    python -m sos_notebook.install
RUN jupyter labextension install transient-display-data
RUN jupyter labextension install jupyterlab-sos

# Create alternative for nano -> nano-tiny
#RUN update-alternatives --install /usr/bin/nano nano /bin/nano-tiny 10

# Switch back to jovyan to avoid accidental container runs as root
#USER ${NB_UID}


RUN mkdir $HOME/.ssh/
RUN ssh-keygen -b 2048 -t rsa -f $HOME/.ssh/id_rsa -q -N ""
