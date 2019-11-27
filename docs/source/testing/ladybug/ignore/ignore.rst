.. _ignore:

Ignore Elements
===============

In subsection :ref:`capture`, you learned how to capture reports into test scripts. You saw how these tests could be run, allowing you to do regression tests of your system. In :ref:`edit`, you saw examples of failing tests. A test fails if there is any difference between the output captured in the past and the current output. This is not always what you want. As an example, your adapter may return the current time in some XML element. The output will then be different each time your System Under Test is run, but these differences do not indicate failures.

This subsection demonstrates how to ignore specific differences between the expected result of your test script and the actual result. These ignores can be configured globally for all tests, or locally for a specific test script. Both options are presented here.

This is a large subsection. Therefore it is divided in sub-subsections as shown in the following table-of-contents:

.. toctree::
   :maxdepth: 3

   preparations
   global
   testSpecific
