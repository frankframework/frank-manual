If you do not administrator rights on your computer, you need some hacks to get your development environment ready. Martijn expects that Git and MinGW can easily be installed without administrator rights. If you have trouble installing these tools, please contact Martijn Dirkse or WeAreFrank! (https://www.wearefrank.nl). The remainder of this page focuses on Python and Pip. That installer requires administrator rights to run.

To install Python and Pip without a Windows installer, please do the following:

1. On the internet, find the "embedded" version of Python. It is a .zip. Extract it and put the result somewhere on your computer. This is your Python installation.
1. The following steps are a copy from StackOverflow. They are described there by  https://stackoverflow.com/users/4746438/oyon. His post is here: https://stackoverflow.com/questions/42666121/pip-with-embedded-python.

   1. Your Python installation has a file `python39._pth` or similar. Uncomment the import command. Result should look similar to this:

       ```
       python39.zip
       .
       import site
       ```

   1. Download `get-pip.py` from https://pip.pypa.io/en/stable/installation/ and put it in your Python installation directory.
   1. Run `get-pip.py`. This installs Pip into the `Scripts` directory:

      ```
      python get-pip.py
      ```

1. Run Pip to install packages `sphinx`, `sphinx_rtd_theme` and `pyyaml`. These are the same as documented in [CONTRIBUTING.md](./CONTRIBUTING.md).
1. Within your Python installation you should now heve `sphinx-build.exe`. Find the full path of this file. Create an environment variable `SPHINXBUILD` that has this path as its value.
1. From here, you should be able to run `generateAll.py` and `make.bat`. See [CONTRIBUTING.md](/CONTRIBUTING.md) for further instructions.