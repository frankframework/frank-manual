.. _helloTestPipeline:

Console Test Pipeline
=====================

In the previous section :ref:`helloIbis` , we examined the
Frank presented in the installation instructions
https://github.com/ibissource/docker4ibis/. We want
to test the pipeline while ignoring the receiver, allowing
us to enter test input more easily.

To do this, you can browse to "localhost/docker/iaf/gui". You see
a console to manage and test your Frank. Click "Testing".
The "Testing" link will expand to "Larva", "Ladybug",
"Test Pipeline" and "Test serviceListener". Click
"Test Pipeline". Select adapter "HelloDockerWorld" and enter some
arbitrary message in the Message field. Then Click
"Send". This results in the following screen:

.. image:: frankTestPipeline.png

The ``returnString`` you configured in the ``<FixedResultPipe>`` is printed
at the bottom. To the top, you see a green bar with
the word "success". "success" is the state you configured
in the ``<exit>`` tag.
