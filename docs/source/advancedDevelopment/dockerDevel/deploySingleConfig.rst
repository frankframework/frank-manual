.. _advancedDevelopmentDockerDevelSingleConfig:

Packaging configurations
========================

In section :ref:`advancedDevelopmentDockerDevelBasics` it was explained how to run Frank configurations using Docker. Within the container derived from the Frank!Framework Docker image, a directory ``/opt/frank/configurations/my-config`` was created with ``Configuration.xml`` inside. This was fine to get started, but for real projects it is wise to package configurations in .zip or .jar files (extension does not matter, both work). There are two reasons for packaging configurations:

* When the customer manages his own deployment environment, Frank developers can deliver a single file to the customer when there is a new release.
* Without packaging, it is not possible to include Java .class files that are specific for the configuration.

Please follow the following rules when building the package:

* The name of each configuration should be different from the name of the instance (``${instance.name}``).
* A properties file ``BuildInfo.properties`` should be included with at least properties ``configuration.version`` and ``configuration.timestamp``.
* File ``Configuration.xml`` and other files of the configuration should live under a top-level directory. The name of the top-level directory is the name of the configuration.
* When frontend code is included as explained in :ref:`gettingStartedWebcontent`, it should live in a subdirectory ``<configuration name>/webcontent``.
* When there are Java .class files, their directory tree is a *brother* of the configuration's root directory.

Here is the contents of an example archive:

.. code-block:: none

   frank-mermaid-dashboard-config/BuildInfo.properties
   frank-mermaid-dashboard-config/Configuration.xml
   frank-mermaid-dashboard-config/Data.xml
   ...
   frank-mermaid-dashboard-config/webcontent/chunk-2D4RQQEM.js
   frank-mermaid-dashboard-config/webcontent/chunk-2VCO5H7P.js
   ...
   frank-mermaid-dashboard-config/webcontent/favicon.ico
   frank-mermaid-dashboard-config/webcontent/index.html
   frank-mermaid-dashboard-config/webcontent/main-2JFPUTB3.js
   ...
   frank-mermaid-dashboard-config/xsd/parsedTemplate.xsd
   ...
   frank-mermaid-dashboard-config/xsl/prepareDbLineStatusForJsonUI.xsl
   ...
   org/wearefrank/mermaid/dashboard/Analysis.class
   ...

File ``META-INF/MANIFEST.MF`` and other files in directory ``META-INF`` (not shown), which are typically created when building a Maven project, are optional. The maintainers of the Frank!Framework may eliminate the need for ``BuildInfo.properties`` in a future release of the Frank!Framework, its role being taken over by ``META-INF/MANIFEST.MF``.

Here is an example of ``BuildInfo.properties``:

.. literalinclude:: ../../../../src/frank-mermaid-dashboard/backend/src/main/configurations/frank-mermaid-dashboard-config/BuildInfo.properties

.. NOTE::

   Developers are encouraged to automate packaging (CI/CD). This can be done using Maven. If a ``pom.xml`` is added, Maven has access to a version number that can be easily substituted inside ``BuildInfo.properties`` during the build.

Exercise
--------

Try to package an example configuration and upload it in the Frank!Console. For instructions on uploading configurations see :ref:`frankConsoleConfigsUploading`.
