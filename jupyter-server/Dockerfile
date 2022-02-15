FROM jupyter/minimal-notebook

COPY requirements.txt /temp/requirements.txt
RUN python3 -m pip install --no-cache-dir -r /temp/requirements.txt

RUN python3 -m bash_kernel.install
RUN python3 -m sos_notebook.install
RUN python3 -m sshkernel install --user
RUN jupyter labextension install transient-display-data
RUN jupyter labextension install jupyterlab-sos

# Change user name
# Install all OS dependencies for fully functional notebook server

USER root
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    openssh-server \
    ssh \
    net-tools && \
    apt-get clean && rm -rf /var/lib/apt/lists/*


ENV NEW_NB_USER=user
ENV HOME=/home/$NEW_NB_USER
RUN usermod --login $NEW_NB_USER --move-home --home $HOME $NB_USER
WORKDIR $HOME/work
ENV CHOWN_EXTRA=WORKDIR
ENV CHOWN_EXTRA_OPTS=-R
ENV GRANT_SUDO=yes

# Create alternative for nano -> nano-tiny
#RUN update-alternatives --install /usr/bin/nano nano /bin/nano-tiny 10

# Switch back to jovyan to avoid accidental container runs as root
USER ${NEW_NB_USER}

RUN mkdir $HOME/.ssh/
RUN ssh-keygen -b 2048 -t rsa -f $HOME/.ssh/id_rsa -q -N ""
COPY config $HOME/.ssh/

RUN git clone https://github.com/lbors/demo-jupyter.git
