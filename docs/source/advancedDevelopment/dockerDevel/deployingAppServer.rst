.. _advancedDevelopmentDockerDevelAppServer:

Additional information about deploying
======================================

This section continues where section :ref:`advancedDevelopmentDockerDevelBasics` ended. It provides more information about deploying Frank applications.

First, it is possible to distribute Frank applications as Docker images, as opposed to Frank configurations that still have to be deployed in an application server. Developers can create a Docker image by writing a Dockerfile. The Dockerfile should derive from image ``frankframework/frankframework`` (DockerHub) or ``nexus.frankframework.org/frankframework`` (server managed by maintainers of Frank!Framework). The new image should include the Frank configurations (can be plural in this case) being deployed in the ``/opt/frank/configurations`` directory. This directory can hold both packaged configurations and configurations as plain directory trees. This way, the production environment does not reference configurations from a volume anymore.

.. WARNING::

   From release 9.0 onwards, database libraries are no longer in the standard Docker image. See :ref:`deployingDatabaseDriver` for more explanation.

.. NOTE::

   The Frank!Framework Docker image expects libraries like database drivers in directory ``/opt/frank/drivers``.

.. NOTE::

   Directory ``/opt/frank/configurations`` can hold both packaged configurations and plain directory trees. In both cases, the Frank!Framework loads the configurations automatically when property ``configurations.directory.autoLoad`` is ``true``. This works from Frank!Framework version 9.3.0-20250806.042330 onwards. For earlier versions, it may be necessary to control the Java classloader used to load a configuration. See https://github.com/frankframework/frankframework/wiki/ClassLoaders#configuration-classloaders.

File ``resources.yml`` is usually mapped as a volume (in ``/opt/frank/resources``) to allow the customer to configure external resources. 

The maintainers of the Frank!Framework have done a lot of work to make image ``frankframework/frankframework`` reliable, and hence you are recommended not to interfere with the way it configures Apache Tomcat. For example, it is deprecated upon to provide some ``context.xml``. The image expects the following data in the following directories:

* **/opt/frank/configurations:** Strictly used for Frank configurations, possibly including .class files originating from configuration-specific custom Java code (see :ref:`advancedDevelopmentCustomCodeBackend`). Data for each configuration is hidden to other configurations.
* **/opt/frank/resources:** Data that is accessible to all configurations. Example files are ``resources.yml`` and application-level properties files (see :ref:`propertiesDeploymentEnvironment`).
* **/opt/frank/drivers:** Third-party libraries like database or queue drivers.

Detailed information about the image and how to use it can be found here: https://github.com/frankframework/frankframework/blob/master/Docker.md.

.. NOTE::

   It is possible to include ``resources.yml`` in the Docker image. In this case, all external resource descriptions for all DTAP stages have to be included. You probably need property ``jdbc.datasource.default``, which you can use to change the name of the default database. Using this property, you can use a different name for each DTAP stage. A drawback is that a new deployment is needed when the customer changes the external resources to be used. In most cases this is not a good way of working.

.. WARNING::

   When a configuration needs configuration-specific custom Java code, a property has to be set to allow this custom code to run. Set ``configurations.<configuration name>.allowCustomClasses`` as a system property to ``true``.

.. NOTE::

   About class loaders and custom Java code. It was said that configurations in ``/opt/frank/configurations`` are loaded when ``configurations.directory.autoLoad`` is ``true``. The Frank!Framework loads each subdirectory of ``/opt/frank/configurations`` using a ``DirectoryClassLoader`` and each .jar or .zip archive in ``/opt/frank/configurations`` using a ``JarFileClassLoader``. Custom Java code cannot be loaded with a ``DirectoryClassLoader``. This explains why configurations with custom Java code have to be packaged. As said, more information about classloaders is available at https://github.com/frankframework/frankframework/wiki/ClassLoaders#configuration-classloaders.
