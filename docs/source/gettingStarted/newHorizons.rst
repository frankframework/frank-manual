.. _newHorizons:

Example: New Horizons
=====================

In the remaining sections of this Getting Started chapter, you will
be guided to build a Frank configuration yourself. Your configuration will serve an imaginary firm New Horizons. New Horizons allows 
travelers to book travels online, which constitute visits to 
hotels, apartments, campings or any other place where travelers 
can sleep. New Horizons makes traveling easier, because the 
traveler with a complex travel does not have to negotiate
with the individual hosts. New Horizons takes the responsibility
of paying them.

Of course New Horizons has many user stories. In the
:ref:`gettingStarted`, we focus on a very specific
task. A booking accepted by New Horizons, which can
constitute multiple visits, should be stored in a 
relational database for further processing.

To get started, please do the following:

#. In the ``franks`` directory you created in :ref:`frankRunnerInstallation`, add a new project directory ``Frank2Manual``. Within that directory, create ``configurations/NewHorizons`` for the configuration you are going to create.
#. In the ``NewHorizons`` directory, open a new file ``Configuration.xml``.
#. Give that file the following contents:

   .. literalinclude:: ../../../srcSteps/NewHorizons/v410/configurations/NewHorizons/Configuration.xml
      :language: xml

#. In directory ``Frank2Manual``, add file ``build.xml`` with the following contents:

   .. literalinclude:: ../../../srcSteps/NewHorizons/v410/build.xml
      :language: xml

   .. WARNING::

      This step should be sufficient to run your Frank configuration from within Visual Studio Code or Eclipse. However on March 24 2023 there is an issue with the Task Explorer plugin of Visual Studio Code. This motivates the next step that allows you to run your work using a Windows batch file. See https://github.com/ibissource/frank-runner for more information.

#. In directory ``Frank2Manual``, add file ``restart.bat`` with the following contents:

   .. literalinclude:: ../../../srcSteps/NewHorizons/v410/restart.bat
      :language: none

   .. WARNING::

      If you are working on Linux or on a Mac, you need ``restart.sh`` instead. See https://github.com/ibissource/frank-runner. Beware to call it as `./restart.sh` even if you are in the directory that holds this script (mind the `./`).

#. To check these steps, please start the Frank!Framework. To do this, run script ``restart.bat`` from a command prompt. You may have to change directory to the ``Frank2Manual`` directory before doing this.
#. When the Frank!Frame runs, go to the Adapter Status page. You should see a tab "NewHorizons".
#. Check that your directory ``Frank2Manual/configurations`` now contains ``FrankConfig.xsd``, the file referenced within ``Configuration.xml``. Placing this file is the job of the Frank!Runner.
#. The Frank!Runner should also create a ``.gitignore`` file that ignores ``FrankConfig.xsd`` for checkin. Please check that such a file has been created.

The details of what we want to build are in the next section.
