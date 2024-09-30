FROM ubuntu:24.04
SHELL ["/bin/bash", "-e", "-u", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /usr/local/bin/

ENV BL_PYTHON_VERSION=3.12

RUN apt-get update \
    && apt-get install -y --no-install-recommends software-properties-common \
    && add-apt-repository ppa:deadsnakes/ppa -y \
    && apt-get install -y --no-install-recommends \
    "python${BL_PYTHON_VERSION}-dev" \
    "python${BL_PYTHON_VERSION}-venv" \
    python3-pip \
    gcc \
    git \
    sudo \
    openssh-client \
    \
    && apt-get remove --purge -y software-properties-common \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV BL_VENV_PATH=/home/ubuntu/sample-virtual-env \
    BL_PIP_VERSION=24.2

ENV PATH="${BL_VENV_PATH}/bin:$PATH"

RUN python3 -m venv "${BL_VENV_PATH}" \
    && source activate \
    \
    && pip3 install --no-cache-dir "pip==${BL_PIP_VERSION}"

RUN pip3 install --no-cache-dir "Django==4.2.16" --no-input

USER ubuntu
WORKDIR /home/ubuntu/sample-django-project