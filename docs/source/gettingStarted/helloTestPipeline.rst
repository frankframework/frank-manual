.. _helloTestPipeline:

Console Test Pipeline
=====================

In the previous section :ref:`helloIbis` , we examined the
Frank presented in the installation instructions
https://github.com/ibissource/docker4ibis/. We want
to test the pipeline while ignoring the receiver, allowing
us to enter test input more easily.

After following the instructions of :ref:`helloIbis`, please proceed as follows:

#. Start the Frank!Framework. This is different for Windows and for Linux.
 using the command prompt (Windows) or a Linux shell (Linux). Go to directory ``franks/docker4ibis`` and do: ::

   * On Windows, open a command prompt. Go to directory ``franks\docker4ibis``. Run the following command: ::

       franks\docker4ibis> docker4ibis.bat Ibis4DockerExample

   * On Linux, open a shell. Go to directory ``franks\docker4ibis``. Run the following command: ::
       franks/docker4ibis> docker4ibis.sh Ibis4DockerExample

#. Browse to http://localhost/docker/iaf/gui. You see the Frank!Console as shown below. Click "Testing". The "Testing" link will expand to "Larva", "Ladybug", "Test Pipeline" and "Test serviceListener".

   .. image:: frankConsoleFindTestTools.jpg

#. Click "Test Pipeline". Select adapter "HelloDockerWorld" (number 1 in the picture below). Enter some
arbitrary message in the Message field (number 2). Then Click "Send" (number 3). 

   .. image:: frankTestPipeline.jpg

#. The ``returnString`` you configured in the ``<FixedResultPipe>`` is printed
at the bottom (number 4). To the top, you see a green bar with
the word "success" (number 5). "success" is the state you configured
in the ``<Exit>`` tag.
