.. _frankConsoleEnvironmentVariables:

Environment Variables
=====================

In the previous section :ref:`frankConsoleLadybug`, you saw how a Frank config can be debugged with Ladybug. If an error happens on your production site, you typically cooperate with a Frank developer to fix the issue. A Frank developer may ask you about system variables or system properties. This short section helps you to answer these questions.

As an example, suppose that you are asked about property "configurations.names". Please do the following to find the value of this property:

#. Start the Frank!Framework as explained in section :ref:`frankConsolePreparations`.
#. In the main menu, select "Environment Variables" as shown below:

   .. image:: mainMenuEnvironmentVariables.jpg

#. Use ctrl-f to search on the current browser page. Search for ``configurations.names``. You should see the following:

   .. image:: environmentVariablesSearchResult.jpg

#. You see a key "configurations.names" (number 1), which is selected because you are searching for this string. To the right, you see the value: "NewHorizons" (number 2).

   .. NOTE::

      Property "configurations.names" defines which Frank!Configs should be loaded by the Frank!Framework. The property has been calculated by the Frank!Runner, which has provided it to the Frank!Framework.