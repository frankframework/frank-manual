.. _advancedDevelopmentDockerDevelAppServer:

Deploying as Docker image and orchestration
===========================================

This section continues where section :ref:`advancedDevelopmentDockerDevelBasics` ended. It provides more information about deploying Frank applications.

It is possible to distribute Frank applications as Docker images. These can then be started with ``docker compose`` or a more advanced tool for container orchestration like Kubernetes. Developers can create a Docker image by writing a Dockerfile. The Dockerfile should derive from image ``frankframework/frankframework`` (DockerHub) or ``nexus.frankframework.org/frankframework`` (server managed by maintainers of Frank!Framework). The new image should include the Frank configurations (can be plural in this case) being deployed in the ``/opt/frank/configurations`` directory. This directory can hold both packaged configurations and configurations as plain directory trees. This way, the production environment does not reference configurations from a volume anymore. In addition, the image should usually provide the database driver. See :ref:`deployingDatabaseDriver` to discover what driver you need for your database.

If a H2 database is used, there is no need for Frank developers to provide a database driver. The maintainers of the Frank!Framework have included the H2 database driver in their Docker image. This allows Frank developers to get started quickly, but a H2 database is not suited for production. Docker images used by real customers therefore need a database driver as stated above.

Here is an example Dockerfile:

.. literalinclude:: ../../../../srcSteps/Frank2Transactions/v480/Dockerfile

The version of the PostgreSQL driver is a parameter of this Dockerfile. It can be provided in a ``docker-compose.yml`` or similar. Here is an example ``docker-compose.yml``:

.. literalinclude:: ../../../../srcSteps/Frank2Transactions/v480/docker-compose.yml

There is no volume mapping for ``/opt/frank/configuration`` because that directory is filled in the image build by the Dockerfile. There is a volume mapping for ``/opt/frank/resources``. Here the system administrator of the customer can configure the deployment, for example by configuring the database.

.. NOTE::

   Directory ``/opt/frank/configurations`` can hold both packaged configurations and plain directory trees. In both cases, the Frank!Framework loads the configurations automatically when property ``configurations.directory.autoLoad`` is ``true``. This works from Frank!Framework version 9.3.0-20250806.042330 onwards. For earlier versions, it may be necessary to control the Java classloader used to load a configuration. See https://github.com/frankframework/frankframework/wiki/ClassLoaders#configuration-classloaders.

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
