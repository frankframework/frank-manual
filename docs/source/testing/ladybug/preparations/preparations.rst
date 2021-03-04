.. _preparations:

Preparations
============

As said in :ref:`introduction`, this subsection walks you through
setting up your environment. You need this environment to follow
the instructions of the proceeding sections. Feel free not
to follow the instructions and just read along. In that case,
you do not need this environment and you can skip this section.

Here are the instructions:

#. If you already did tutorial :ref:`gettingStarted`, proceed to step 6. Your instance directory is ``Frank2Manual`` in this case and your configurations come in ``Frank2Manual/configurations``.
#. Otherwise, install the Frank!Framework using the Frank!Runner, see https://github.com/ibissource/frank-runner.
#. Create a directory for your instance. The last component of the path will be the instance name. Instance names should begin with ``Frank2``, expressing that you are frank, open about your work. The word coming after ``Frank2`` should begin with a capital.
#. Within your ``frank-runner`` directory, create file ``build.properties``. Fill it like explained in the README file of the Frank!Runner to reference your instance.
#. Give your instance directory a subdirectory ``configurations``.
#. Download :download:`ladybug <../../../downloads/ladybug.zip>`.
#. Unzip this file into your configurations directory. Your files should appear in a directory ``configurations/ladybug``. Here is the directory tree you should have now: ::

     Frank2Manual
     |- configurations
        |- ladybug
           |- Configuration.xml
           ...

#. When you work under Windows (the only possibility right now, but this will change), you need Postman. Install it from https://www.getpostman.com/downloads/. Note that only one of the proceeding subsections requires you to use Postman. You can do the rest of this tutorial without.
#. When you work under Linux, you need curl. If you do not have curl, there is one section you cannot do. The other sections do not require curl.
