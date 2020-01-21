.. _gettingStartedLadyBug:

Console Ladybug
===============

The Frank!Framework offers a strong debugger called Ladybug.
It gives detailed insight of how your message is processed,
because the input and the output of every pipe is shown.

Please do the following:

#. Click the link "Testing" shown below. Then click "Ladybug".

   .. image:: frankConsoleFindTestTools.jpg

#. You see you are in Ladybug (number 1 in the picture below). Click "Refresh" (number 2) to see the report of running your adapter.

   .. image:: ladybugAnnotated.jpg

#. In the table of adapter runs, select the report you want to examine (number 3). The tree view to the bottom left then shows what happened when the adapter executed.
#. Select the second "Pipeline" node (number 4). To the bottom right, you see the dummy message you entered (number 5).
#. Select the bottom "Pipeline" node, with the arrow pointing left (number 1 in the picture below).

   .. image:: ladybugAnnotated2.jpg

#. Now you see the output message (number 2).

.. NOTE::

   In the tree view you see session keys. These are used to
   store information that complements the incoming message, for
   example tsReceived for the time that the input message was
   received (timezone UTC!).

If you want to learn more about Ladybug, you can study section :ref:`ladybug`. This tool also has features to automate testing.
