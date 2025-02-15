Create kernal envionment for gpu:
=================================

    C:\Users\aruns>python -m venv CUDA-GPU

Activate
========

  C:\Users\aruns>source CUDA-GPU activate

Pip Wheels
============ 

NVIDIA provides Python Wheels for installing CUDA through pip, primarily for using CUDA with Python. These packages are intended for runtime use and do not currently include developer tools (these can be installed separately).

Please note that with this installation method, CUDA installation environment is managed via pip and additional care must be taken to set up your host environment to use CUDA outside the pip environment.

Prerequisites:
===============

To install Wheels, you must first install the nvidia-pyindex package, which is required in order to set up your pip installation to fetch additional Python modules from the NVIDIA NGC PyPI repo. If your pip and setuptools Python modules are not up-to-date, then use the following command to upgrade these Python modules. If these Python modules are out-of-date then the commands which follow later in this section may fail.

    py -m pip install --upgrade setuptools pip wheel

You should now be able to install the nvidia-pyindex module.

    py -m pip install nvidia-pyindex


Procedure
===========

Install the CUDA runtime package:
===================================

    py -m pip install nvidia-cuda-runtime-cu12

Optionally, install additional packages as listed below using the following command:
====================================================================================


    py -m pip install nvidia-<library>

install torch:
================

    pip install torch==2.2.0 torchvision==0.17.0 torchaudio==2.2.0 --extra-index-url https://download.pytorch.org/whl/cu121

install from wheel files directly:
======================================


Go to https://download.pytorch.org/whl/torch_stable.html
Find the appropriate wheel file for your:

Python version (e.g., cp39 for Python 3.9)
Windows version (win_amd64)
CUDA version (cu121 for CUDA 12.1)
    https://download.pytorch.org/whl/torch_stable.html
