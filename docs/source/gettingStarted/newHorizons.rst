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

#. You will put your work for NewHorizons in a dedicated Frank configuration. You will store it in the directory ``franks/Frank2Manual/configurations/NewHorizons`` (see subsection :ref:`horizonsMultipleFilesSetUpYourInstance` about the directory tree). In that ``NewHorizons`` directory, open a new file ``Configuration.xml``.
#. Give that file the following contents:

   .. literalinclude:: ../../../srcSteps/NewHorizons/v390/configurations/NewHorizons/Configuration.xml
      :language: xml

#. To check this step, please start the Frank!Framework.
#. Go to the Adapter Status page. You should see a tab "NewHorizons".

The details of what we want to build are in the next section.
