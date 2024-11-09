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

![image](https://github.com/user-attachments/assets/0584f594-1761-4632-b309-59c4a03a3b93)

Fixed:
======

after installation from langchain.memory import ConversationBufferMemory  error goes away

ERROR Before VC++ Installation:
==============================

    Collecting langchain
      Using cached langchain-0.3.7-py3-none-any.whl.metadata (7.1 kB)
    Requirement already satisfied: PyYAML>=5.3 in c:\arun\python\python313\lib\site-packages (from langchain) (6.0.2)
    Collecting SQLAlchemy<3,>=1.4 (from langchain)
      Using cached SQLAlchemy-2.0.36-cp313-cp313-win_amd64.whl.metadata (9.9 kB)
    Collecting aiohttp<4.0.0,>=3.8.3 (from langchain)
      Using cached aiohttp-3.10.10-cp313-cp313-win_amd64.whl.metadata (7.8 kB)
    Collecting langchain-core<0.4.0,>=0.3.15 (from langchain)
      Using cached langchain_core-0.3.15-py3-none-any.whl.metadata (6.3 kB)
    Collecting langchain-text-splitters<0.4.0,>=0.3.0 (from langchain)
      Using cached langchain_text_splitters-0.3.2-py3-none-any.whl.metadata (2.3 kB)
    Requirement already satisfied: langsmith<0.2.0,>=0.1.17 in c:\arun\python\python313\lib\site-packages (from langchain) (0.1.142)
    Collecting numpy<2.0.0,>=1.26.0 (from langchain)
      Using cached numpy-1.26.4.tar.gz (15.8 MB)
      Installing build dependencies ... done
      Getting requirements to build wheel ... done
      Installing backend dependencies ... done
      Preparing metadata (pyproject.toml) ... error



 

 After Installation of VC++ Installation:
 ==========================================



     Collecting langchain
      Using cached langchain-0.3.7-py3-none-any.whl.metadata (7.1 kB)
    Requirement already satisfied: PyYAML>=5.3 in c:\arun\python\python313\lib\site-packages (from langchain) (6.0.2)
    Collecting SQLAlchemy<3,>=1.4 (from langchain)
      Using cached SQLAlchemy-2.0.36-cp313-cp313-win_amd64.whl.metadata (9.9 kB)
    Collecting aiohttp<4.0.0,>=3.8.3 (from langchain)
      Using cached aiohttp-3.10.10-cp313-cp313-win_amd64.whl.metadata (7.8 kB)
    Collecting langchain-core<0.4.0,>=0.3.15 (from langchain)
      Using cached langchain_core-0.3.15-py3-none-any.whl.metadata (6.3 kB)
    Collecting langchain-text-splitters<0.4.0,>=0.3.0 (from langchain)
      Using cached langchain_text_splitters-0.3.2-py3-none-any.whl.metadata (2.3 kB)
    Requirement already satisfied: langsmith<0.2.0,>=0.1.17 in c:\arun\python\python313\lib\site-packages (from langchain) (0.1.142)
    Collecting numpy<2.0.0,>=1.26.0 (from langchain)
      Using cached numpy-1.26.4.tar.gz (15.8 MB)
      Installing build dependencies ... done
      Getting requirements to build wheel ... done
      Installing backend dependencies ... done
      Preparing metadata (pyproject.toml) ... done
    Requirement already satisfied: pydantic<3.0.0,>=2.7.4 in c:\arun\python\python313\lib\site-packages (from langchain) (2.9.2)
    Requirement already satisfied: requests<3,>=2 in c:\arun\python\python313\lib\site-packages (from langchain) (2.32.3)
    Requirement already satisfied: tenacity!=8.4.0,<10,>=8.1.0 in c:\arun\python\python313\lib\site-packages (from langchain) (8.5.0)

Reason why vc++ required:
=========================

You need to install the Visual Studio C++ Build Tools from the following link to build the **langchain-0.3.7-py3-none-any.whl**:
Visual Studio C++ Build Tools

Then, you need to select Desktop Development with C++ in the Visual Studio C++ Build Tools Installer and install it.

After, installing the Desktop Development with C++ in the Visual Studio C++ Build Tools installer. Run the following command again:
pip install -r requirements.txt

Visual Studio Build Tools:
==========================

https://visualstudio.microsoft.com/visual-cpp-build-tools/
