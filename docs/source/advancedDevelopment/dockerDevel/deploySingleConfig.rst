*Work in progress.*

.. _advancedDevelopmentDockerDevelSingleConfig:

Deploying a single configuration
================================

As said in :ref:`advancedDevelopmentDockerDevel`, the development environment has characteristics that are not desirable for production. There are two ways to deploy Frank configurations. One way is to only deliver a single configuration to the customer. The customer is then responsible for maintaining an application server, uploading the configuration and configuring access to the external resources required by the configuration. Enterprises usually have specialized staff who have been trained well for these tasks.

Deploying a configuration like this is done as follows:

* Add a file ``BuildInfo.properties`` inside the configuration. In the example developed here this is ``configurations/my-config/BuildInfo.properties``. A minimal example is:

  .. literalinclude:: ../../../../srcSteps/Frank2DockerDevel/v515/configurations/my-config/BuildInfo.properties

* Zip the directory of the configuration. In this example ``configurations/my-config``. For the Frank!Framework it does not matter whether the file extension becomes ``.zip`` or ``.jar``.
* Provide the archive to the customer.

.. NOTE::

   Developers are encouraged to automate these steps (CI/CD). This can be done using Maven. If a ``pom.xml`` is added, Maven has access to a version number that can be easily substituted inside ``BuildInfo.properties`` during the build.


Exercise
--------

Try to upload the example configuration developed here within the Frank!Console. For instructions on uploading configurations see :ref:`frankConsoleConfigsUploading`.
