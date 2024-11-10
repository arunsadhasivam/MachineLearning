Certainly! Using the standard Python kernel with GPU support is possible by setting up the necessary libraries 
(like CUDA, cuDNN, and a compatible deep learning framework such as TensorFlow or PyTorch). Here are the steps:

Step 1: Install NVIDIA Drivers
===============================

    Install the NVIDIA driver compatible with your GPU. You can download the drivers from the NVIDIA website.
    Verify the installation:

        nvidia-smi

    This should show your GPU details if the driver is installed correctly.

Step 2: Install CUDA and cuDNN
===============================

CUDA and cuDNN are essential libraries that enable deep learning frameworks to use the GPU.

  Install CUDA:
  =============
      Download the CUDA Toolkit from NVIDIA’s CUDA download page.
      Install the version that is compatible with your deep learning framework (e.g., TensorFlow, PyTorch).
      Follow the installation steps provided by NVIDIA.


  Method 1: Check Environment Variables
  =====================================

    If CUDA is added to your environment variables, you can check its path this way:

   
On Windows:
==========

 Open Command Prompt or PowerShell and type:

        echo %CUDA_PATH%

  Install cuDNN:
  ==============
      Download cuDNN from NVIDIA cuDNN (requires registration).
      Follow the instructions to copy the files to your CUDA installation directory (usually /usr/local/cuda/ on Linux).

    Set environment variables: Add CUDA paths to your shell configuration (~/.bashrc, ~/.zshrc, etc.):

export PATH=/usr/local/cuda/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH

Verify installation:
====================

    Check if CUDA is installed correctly:

            nvcc --version

        Your deep learning framework will automatically detect CUDA if installed correctly.

Step 3: Install Required Libraries with pip
============================================

Now that CUDA and cuDNN are installed, you can set up your Python environment to use GPU-supported libraries directly without Anaconda.

    Set up a virtual environment (optional):

        python3 -m venv gpu_env
        source gpu_env/bin/activate

Note: It’s best to work within a virtual environment to keep dependencies isolated.

Install the GPU-compatible libraries:
=====================================


NOTE:
=====

tensorflow does not support latest python, 
currently, TensorFlow does not support Python 3.13, as it's a relatively new release, and many libraries, including TensorFlow, 
may not yet be compatible. Here’s what you can do to install TensorFlow:

Solution: Use Python 3.8 - 3.10
================================

For TensorFlow with GPU support:

        pip install tensorflow

TensorFlow will automatically detect and use the GPU if CUDA is correctly installed.

For PyTorch with GPU support: Visit the PyTorch website to find the appropriate installation command based on your CUDA version. For example:
==============================================================================================================================================

        pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu118

Step 4: Verify GPU Support in Python
=====================================

After installing the libraries, verify that your setup can detect the GPU.

For TensorFlow:
==============

    import tensorflow as tf
    print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

For PyTorch:
============

    import torch
    print("CUDA Available: ", torch.cuda.is_available())

If these commands detect a GPU, your setup is complete.

Step 5: Using the GPU with Jupyter Notebook (Optional)
=======================================================

If you want to use this environment in Jupyter Notebook with GPU support:

    Install Jupyter Notebook in your environment:

    pip install jupyter
    
    Install ipykernel:
    
    pip install ipykernel
    python -m ipykernel install --user --name=gpu_env --display-name "Python (GPU)"

Start Jupyter Notebook:
=======================

    jupyter notebook

    Open a new notebook, and select the "Python (GPU)" kernel.

Your Python environment should now be set up to leverage GPU acceleration for any supported deep learning tasks.
