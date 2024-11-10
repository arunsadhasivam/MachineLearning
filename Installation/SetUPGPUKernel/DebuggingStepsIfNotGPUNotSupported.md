To ensure CUDA and cuDNN are properly set up and detected on your system, let's break the process down step by step with a focus on installation paths
and the necessary environment variables for your CUDA v12.6 and cuDNN installation.
Step-by-Step Guide for Installing and Configuring CUDA, cuDNN, and Setting up Environment Variables

Step 1: Verify Your GPU Driver Installation
============================================

    Verify that your GPU is detected by NVIDIA:
        Open Command Prompt and run:

            nvidia-smi

        This will show if the GPU is being detected. If it's not detected, you'll need to reinstall the NVIDIA drivers from the NVIDIA driver download page.

Step 2: Install CUDA
======================

You mentioned you have installed CUDA v12.6. The default installation directory for CUDA is:

C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.6

Step 3: Install cuDNN
======================

After installing CUDA, you will need to install cuDNN. Here's how you do it:

CUDA PATH = C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.6\bin,C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.6\lib

CUDA_CNN = C:\Program Files\NVIDIA\CUDNN\v9.5\bin, C:\Program Files\NVIDIA\CUDNN\v9.5\lib


VERY IMPORTANT:
================

      after installatin of cudacnn make sure copy all C:\Program Files\NVIDIA\CUDNN\v9.5\lib, bin,include 
      to C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.6\lib,bin include.




  Download cuDNN:
  ==============
      Go to the NVIDIA cuDNN page and download the version of cuDNN that matches your installed version of CUDA (in your case, CUDA 12.6).

  Install cuDNN:
  ===============
      Once downloaded, extract the contents of the cuDNN ZIP file.
      Copy the bin, include, and lib folders from the extracted cuDNN directory into the respective CUDA directories.

  Default paths to copy cuDNN files:
  ==================================
  
      bin: Copy cudnn64_8.dll to C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.6\bin
      include: Copy cudnn.h to C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.6\include
      lib: Copy cudnn.lib to C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.6\lib\x64

Step 4: Set Environment Variables

After installing CUDA and cuDNN, you need to set the environment variables correctly to make sure the system can locate them.

    Set CUDA_HOME: This will point to the CUDA installation directory. For your case, the default path is:

C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.6

Steps to add this variable:

    Right-click This PC > Properties > Advanced system settings > Environment Variables.
    Under System variables, click New and create a variable called CUDA_HOME and set the value to:

    C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.6

Add CUDA to the PATH: You need to add the following directories to your PATH environment variable:

    C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.6\bin
    C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.6\libnvvp

To add to PATH:

    Under System variables in the Environment Variables window, find and select the Path variable, then click Edit.
    Click New and add each of the paths mentioned above.

Set CUDNN_INCLUDE_DIR and CUDNN_LIB_DIR (optional):

    CUDNN_INCLUDE_DIR should be set to the include folder where cudnn.h is located:

C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.6\include

CUDNN_LIB_DIR should be set to the lib\x64 folder where cudnn.lib is located:

        C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.6\lib\x64

    These are not strictly required for Python libraries like PyTorch or TensorFlow, but they can be useful for compiling custom CUDA code.

Step 5: Verify CUDA and cuDNN Installation

    Check CUDA:
        Open a Command Prompt and run:

        nvcc --version

        This should print the version of CUDA installed (in your case, CUDA 12.6).

    Check cuDNN: To verify that cuDNN is installed correctly, you can check if the cudnn64_8.dll file exists in the C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.6\bin directory.

Step 6: Test GPU Access in Python

    For PyTorch: To verify if PyTorch can detect your GPU, run the following code in Python:

import torch
print(torch.cuda.is_available())  # Should print True if GPU is available
print(torch.cuda.get_device_name(0))  # Should print the name of your GPU

For TensorFlow: To verify if TensorFlow can detect your GPU, run the following code in Python:

    import tensorflow as tf
    print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

    If both frameworks show that your GPU is available, you're ready to use the GPU for computations.

Step 7: Troubleshooting

    No GPU Detected:
        If your GPU is still not being detected, check if the NVIDIA Driver is properly installed and the GPU is functioning correctly using nvidia-smi as described in Step 1.
        Ensure you have installed the appropriate versions of CUDA and cuDNN compatible with each other and with the Python libraries you're using (PyTorch, TensorFlow).

    Reinstall CUDA and cuDNN: If you continue to face issues, it might be helpful to completely uninstall CUDA, cuDNN, and your GPU drivers and then reinstall them following the steps above.

Conclusion

By ensuring your CUDA_HOME, PATH, and cuDNN paths are set correctly, and verifying the installations with simple tests in Python, your GPU should be detected for use with frameworks like PyTorch or TensorFlow. Let me know if you encounter any issues!
