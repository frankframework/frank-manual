.. _advancedDevelopmentDockerDevelAppServer:

Deploying the full application
==============================

The previous page :ref:`advancedDevelopmentDockerDevelSingleConfig` explained one way to deploy: only distributing one Frank configuration. This has the advantage that system administrators of the customer have complete freedom to optimize the deployment environment. There are two drawbacks. First, deployment is not fully automated - there is a manual step to upload the configuration somewhere. A second drawback can be that Frank configurations need some control over the application server.

These issues can be addressed by distributing a Docker image. Developers can create it by writing a Dockerfile. The Dockerfile should derive from image ``frankframework/frankframework`` (if the desired application server is Apache Tomcat), which is available on Dockerhub and on a server owned by the maintainers of the Frank!Framework (see :ref:`advancedDevelopmentDockerDevelConfigureDocker`). The new image should include the Frank configurations (can be plural in this case) being deployed in the ``/opt/frank/configurations`` directory. The production environment does not reference them in a volume anymore.

.. WARNING::

   From release 9.0 onwards, database libraries are no longer in the standard Docker image. See :ref:`deployingDatabaseDriver` for more explanation. If you use the standard image to derive a customer-specific image, then add the library in ``/usr/local/tomcat/lib``. Keep in mind that this directory already contains other files, so do not make this directory a volume. You can also leave it to the customer to add the database driver. Make ``/opt/frank/resources`` a volume and have the library in that directory.
 
File ``resources.yml`` is still mapped as a volume (``/opt/frank/resources``) to allow the customer to configure external resources. This explains why it is useful not to put ``resources.yml`` in ``/opt/frank/configurations`` - doing so would make it more difficult to include configurations in a Docker image without doing so for ``resources.yml``.

The maintainers of the Frank!Framework have done a lot of work to make image ``frankframework/frankframework`` reliable, and hence you are recommended not to interfere with the way it configures Apache Tomcat. For example, it is deprecated upon to provide some ``context.xml``. Detailed information about this image and how to use it can be found here: https://github.com/frankframework/frankframework/blob/master/Docker.md.

.. NOTE::

   It is possible to include ``resources.yml`` in the Docker image. In this case, all external resource descriptions for all DTAP stages have to be included. You probably need property ``jdbc.datasource.default``, which you can use to change the JNDI name of the default database. Using this property, you can use a different JNDI name for each DTAP stage. A drawback is that a new deployment is needed when the customer changes the external resources to be used. In most cases this is not a good way of working.