.. _newHorizons:

Example: New Horizons
=====================

In the remaining sections of :ref:`gettingStarted` , we consider a
more interesting example than outputting a fixed string.

We consider an imaginary firm New Horizons. New Horizons allows 
travelers to book travels online, which constitute visits to 
hotels, apartments, campings or any other place where travelers 
can sleep. New Horizons makes traveling easier, because the 
traveler with a complex travel does not have to negotiate
with the individual hosts. New Horizons takes the responsibility
of paying them.

Of course New Horizons has many user stories. In the
:ref:`gettingStarted` , we focus on a very specific
task. A booking accepted by New Horizons, which can
constitute multiple visits, should be stored in a 
relational database for further processing.

To get started, please do the following:

#. In the ``franks`` directory you created in :ref:`frankRunnerInstallation`, add a new project directory ``Frank2Manual``. Within that directory, create ``configurations/NewHorizons`` for the configuration you are going to create.
#. In the ``NewHorizons`` directory, open a new file ``Configuration.xml``.
#. Give that file the following contents:

   .. literalinclude:: ../../../srcSteps/NewHorizons/v390/configurations/NewHorizons/Configuration.xml
      :language: xml

Please take your time to configure your development environment. The `GitHub page of the Frank!Runner <https://github.com/ibissource/frank-runner>`_ contains all the information you need. You will use the non-Maven directory structure that is explained there. You can see how to work with ``FrankConfig.xsd`` and the code completion and syntax checking that it supports. You can also see how you can easily start the Frank!Runner during development.

4. To check these steps, please start the Frank!Framework and go to the Adapter Status page. You should see a tab "NewHorizons".

The details of what we want to build are in the next section.
