.. _gettingStartedWebcontent:

Web content
===========

Java applications may consist of front-end and backend code.
The backend code executes on the server. When a user
visits the application, the browser downloads the front-end code and
executes it. Front-end code typically has HTML files, stylesheets (CSS files)
and JavaScript code. 

Frank configurations can have front-end code like ordinary Java
applications. To add front-end code to a Frank configuration,
add a folder named ``webcontent`` and put the HTML files, CSS
files and JavaScript files there. These files will be available
at URL ``webcontent/name-of-configuration``.

This can be illustrated by adding a welcome page to the NewHorizons
configuration developed in this chapter. Please do the following:

1. In the ``NewHorizons`` folder, add a subfolder ``webcontent``.
#. In folder ``webcontent``, add a file ``index.html`` with the following contents:

   .. literalinclude:: ../../../srcSteps/NewHorizons/v510/configurations/NewHorizons/webcontent/index.html
      :language: html

#. Start the configuration using the Frank!Runner. Then browse to http://localhost/webcontent/NewHorizons. The browser should show the text "Welcome to New Horizons!".

.. NOTE::

   The requested URL did not contain the text ``index.html``, but the Frank!Framework nevertheless served that file. When the Frank!Framework gets a HTTP request
   ``webcontent/name-of-a-configuration``, it is automatically interpreted as a request for the welcome file: the ``index.html`` file in folder ``webcontent`` of the referenced configuration.

.. NOTE::

   Each configuration in a Frank application can have a ``webcontent`` folder with front-end code. Each configuration has a different name and has its front-end code served at a different URL ``webcontent/name-of-configuration``.

.. NOTE::

   Each configuration can have a ``webcontent`` folder no matter the class loader type (property ``configurations.MyConfig.classLoaderType``), see subsection :ref:`propertiesFramework`.