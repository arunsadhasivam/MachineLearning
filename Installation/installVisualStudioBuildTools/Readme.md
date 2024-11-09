Visual Studio Dependency for python:
====================================

Error:
======

from langchain.memory import ConversationBufferMemory unable to install langchain 

WARNING: Failed to activate VS environment: Could not find C:\Program Files (x86)\Microsoft Visual Studio\Installer\vswhere.exe

Instead of installing whole visual studio just install Visual Studio Build Tools.

Solution:
=========

Compiling C++ Extensions: Some Python libraries (especially those with C++ bindings, like numpy, tensorflow, or scikit-learn)
may require a C++ compiler to build from source on Windows. 
In these cases, the Visual Studio Build Tools or the full Visual Studio IDE is necessary.


Visual Studio Build Tools:
==========================

https://visualstudio.microsoft.com/visual-cpp-build-tools/
