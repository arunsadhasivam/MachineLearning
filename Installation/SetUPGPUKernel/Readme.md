
To set up and use a GPU kernel for deep learning with frameworks like TensorFlow or PyTorch, follow these steps:

Step 1: 
======
Install NVIDIA Drivers

Ensure your GPU drivers are correctly installed and up-to-date. You can download the drivers from the NVIDIA website.

    Check if your GPU is recognized:

        nvidia-smi

    This command should display information about your GPU, including the driver version.

    Install the appropriate driver if needed, following NVIDIA's installation instructions.

Step 2: Install CUDA Toolkit and cuDNN
=======================================

CUDA and cuDNN are required to enable GPU support for deep learning libraries.

    Install CUDA:
    --------------
        Download and install the CUDA Toolkit from the NVIDIA CUDA website.
        Select the version compatible with the deep learning framework you intend to use (TensorFlow, PyTorch, etc.). Each framework may require specific CUDA versions, so refer to its documentation.

    Install cuDNN:
    --------------
    
        Download cuDNN from the NVIDIA cuDNN website.
        Unzip and copy the files to the CUDA directory (typically /usr/local/cuda/ on Linux). Follow NVIDIA’s installation instructions for your operating system.

    Add CUDA to Path:
    -----------------
    
        Make sure CUDA binaries are in your path. Add the following to your shell profile (~/.bashrc, ~/.zshrc, etc.):

    export PATH=/usr/local/cuda/bin:$PATH
    export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH

Verify CUDA and cuDNN installation:
====================================

    To check that CUDA is installed correctly:

        nvcc --version

        TensorFlow and PyTorch will automatically detect CUDA if it’s correctly installed.

Step 3: Set Up an Anaconda Environment with GPU Support
=======================================================

Using Anaconda simplifies setting up a GPU-compatible environment for TensorFlow or PyTorch.

Create a new Conda environment:
=================================

     conda create --name gpu_env python=3.8

Replace 3.8 with the Python version you want to use.

Activate the environment:
=========================

      conda activate gpu_env

Install GPU-Compatible Libraries:
=================================

    For TensorFlow:

        conda install tensorflow-gpu

For PyTorch: You can install PyTorch with GPU support by specifying the CUDA version. For example, if using CUDA 11.8:

        conda install pytorch torchvision torchaudio cudatoolkit=11.8 -c pytorch

Step 4: Verify GPU Support in Python
=====================================

Once you’ve installed your deep learning framework, verify that the GPU is detected.

    TensorFlow:

import tensorflow as tf
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

This should list the number of GPUs available. If it returns a number greater than 0, TensorFlow has detected the GPU.

PyTorch:
========

    import torch
    print("CUDA Available: ", torch.cuda.is_available())

    This should return True if PyTorch detects the GPU.

Step 5: Set Up and Run a GPU-Compatible Kernel in Jupyter Notebook
===================================================================

If you’re using Jupyter Notebook, you can set up a kernel that uses your Conda environment.

Install Jupyter in the Conda Environment:
=========================================

  conda install jupyter

Install ipykernel:
==================

      conda install ipykernel
      python -m ipykernel install --user --name=gpu_env


Start Jupyter Notebook:
=======================

    jupyter notebook

    In the Jupyter interface, you can select your new gpu_env kernel, which has GPU support.

Summary

You now have a Conda environment with a GPU-compatible Jupyter kernel. You can run deep learning code in Jupyter Notebook, and it will automatically use the GPU if available.
