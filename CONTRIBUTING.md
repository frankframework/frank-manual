# CONTRIBUTING

This file explains how to contribute to this project.

## Building the Manual

The manual is built automatically by http://readthedocs.io. The formatted manual can
be found at http://ibis4manual.readthedocs.io. This is the official version, but
when you work on this manual you also need to build it on your laptop. This is done
using the script `make` (Linux) or the script `make.bat` (Windows). Before these
scripts work, you need Python 2.7 and Pip. Information on how to install these is available
on the internet.

In addition, you need to install the following packages using pip:
* `pip install sphinx`
* `pip install sphinx_rtd_theme`

Then you can build the manual on your laptop using `make html` (Linux) or `make.bat html` (Windows).

