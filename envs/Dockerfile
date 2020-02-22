FROM continuumio/anaconda3:2019.10

USER root

RUN apt-get update && apt-get install -yq --no-install-recommends \
    curl \
    dpkg \
    grep \
    sed \
    libsm6 \
    libxrender1 \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep -o "/v.*\"" | sed 's:^..\(.*\).$:\1:'` && \
    curl -L "https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb" > tini.deb && \
    dpkg -i tini.deb && \
    rm tini.deb && \
    rm -rf /var/lib/apt/lists/*
# "

RUN mkdir -p /home/data_science && \
mkdir -p ~/.jupyter && { \
echo "c.NotebookApp.allow_root = True"; \
echo "c.NotebookApp.ip = '0.0.0.0'"; \
echo "c.NotebookApp.token = ''"; \
echo "c.NotebookApp.open_browser = False"; \
echo "c.JupyterLabTemplates.include_default = True"; \
echo "c.NotebookApp.notebook_dir = '/home/data_science'"; \
echo "c.JupyterLabTemplates.template_dirs = ['list', 'of', 'template', 'directories']"; \
} | tee ~/.jupyter/jupyter_notebook_config.py

ENV CONDA_DIR=/opt/conda

SHELL ["/bin/bash", "-c"]
RUN $CONDA_DIR/bin/conda config --system --prepend channels conda-forge

RUN apt-get update && apt-get install -yq --no-install-recommends \
    build-essential \
    zsh \
    fonts-ipaexfont \
    fonts-noto-cjk \
    git \
    inkscape \
    libgl1-mesa-dev \
    pandoc \
    texlive-fonts-extra \
    texlive-fonts-recommended \
    texlive-generic-recommended \
    texlive-latex-base \
    texlive-latex-extra \
    unzip \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY /experiments/base.yaml /tmp
RUN $CONDA_DIR/bin/conda env update -f /tmp/base.yaml && \
    rm /tmp/base.yaml && \
    conda clean --all -f -y

EXPOSE 9999
ENTRYPOINT [ "/usr/bin/tini", "--" ]
