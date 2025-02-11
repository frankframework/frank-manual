.. _advancedDevelopmentDockerDevelBasics:

The basics
==========

Advantage of using Docker
-------------------------

Working with the Frank!Runner as was explained in :ref:`gettingStarted` is easy. The Frank!Runner handles a lot of details about starting your Frank configuration, for example:

* The Frank!Runner automatically downloads the Frank!Framework for you.
* It downloads Java.
* It downloads Apache Tomcat.
* It deploys the Frank!Framework, a Java webapplication, in Tomcat.
* It configures the Tomcat server, for example:

  * It sets properties such that the Frank!Framework can find your Frank configuration.
  * It sets ``dtap.stage=LOC`` in ``catalina.properties``.
  * It copies the ``context.xml`` you provide or it creates one that has a ``<Resource>`` tag for your database.
* It downloads ``FrankConfig.xsd``, a file you need to have syntax checking while editing Frank configurations.

You may want more insight into these details already during development. You can achieve this by using Docker (see https://hub.docker.com/). The maintainers of the Frank!Framework have created a Docker image that holds the Frank!Framework deployed inside the appropriate version of Apache Tomcat. This image can also be used in your production environment. If you do your development using Docker, your development environment is more similar to your production environment.

.. _advancedDevelopmentDockerDevelConfigureDocker:

About configuring Docker
------------------------

We assume in this section that you have Docker and docker-compose on your development device. This is not an issue for Linux users. For Windows users, Docker Desktop should work out-of-the-box.

If Docker Desktop does not work under Windows, you may have to configure it so that volumes can use your working directory. This can be done as follows:

1. Go to your Docker Desktop window and press the settings button:

   .. image:: dockerDesktopHighlightSettingsButton.jpg

#. Add your directory as a shared file resource:

   .. image:: setFileResource.jpg

Starting the FF! with docker-compose
------------------------------------

A Docker image named ``frankframework/frankframework`` is provided on DockerHub (https://hub.docker.com/r/frankframework/frankframework). It is suitable both for local and server use. DockerHub hosts images for millions of users and may remove images that are not downloaded, see https://www.docker.com/blog/scaling-dockers-business-to-serve-millions-more-developers-storage. For this reason, this image is saved on a proprietary Nexus server, https://nexus.frankframework.org, where images will be stored for as long as possible. In Docker Compose files, reference ``nexus.frankframework.org/frankframework`` to use this server. The source code of the image is available from the ``docker``-folder in the ``frankframework/frankframework`` GitHub repository.

The image runs Linux and contains Apache Tomcat with the Frank!Framework deployed. It configures the Frank!Framework to read configurations from directory ``/opt/frank/configurations``. The Frank!Framework is served under the root context on port 8080. The following ``docker-compose.yml`` is sufficient to get started:

.. literalinclude:: ../../../../srcSteps/Frank2DockerDevel/v500/docker-compose.yml
   :language: none

This defines service ``frank-docker-example`` from the mentioned FF! image. It exposes port 8080 of the container to port 8080 on your device. It creates a Docker volume that maps subdirectory ``configurations`` (relative to the project root) to ``/opt/frank/configurations``, allowing you to write your configurations in directory ``configurations`` on your device. Then it sets some necessary properties for the Frank!Framework, most notably ``instance.name`` and ``dtap.stage``. See :ref:`propertiesDeploymentEnvironment` about DTAP stages and :ref:`propertiesFramework` for an overview of all properties that change the behavior of the FF!.

You need one more file because the Frank!Framework expects that there is a database. Within Frank configurations, the database is referenced by a name. System administrators can then configure the application server of the deployment environment, such that the database name corresponds to a database. Application server Apache Tomcat expects a file ``context.xml`` for this. By default, the FF! uses a database with name ``jdbc/${instance.name.lc}`` with ``instance.name.lc`` the value of property ``instance.name`` converted to lower-case.

The Frank!Framework runs on multiple application servers, and therefore it supports a generic mechanism to reference resources. This can be accessed by Frank developers through a file ``resources.yml``. File ``docker-compose.yml`` creates an additional volume to put it in ``/opt/frank/resources``. To get started, you can use an in-memory H2 database by creating ``resources.yml`` as follows:

.. literalinclude:: ../../../../srcSteps/Frank2DockerDevel/v500/resources/resources.yml
   :language: none

.. WARNING::

   If you use an in-memory H2 database (which makes sense for local testing), it is recommended to include ``DB_CLOSE_ON_EXIT=FALSE`` in the URL. The Frank!Framework closes and opens database connections while working with the database. Without this text in the URL, the H2 database is cleared when the connection to the database is closed.

.. NOTE::

   It is also possible to create ``configurations/resources.yml`` instead of ``resources/resources.yml``. Doing so is not recommended because it makes it more difficult to deploy the product. See :ref:`advancedDevelopmentDockerDevelAppServer`.

.. NOTE::

   It is possible to boot the Frank!Framework without a database. If property ``jdbc.required`` is set to ``false``, the Frank!Framework does not check during the boot whether it can connect to databases. The Frank!Framework has a lot of functionality that requires a database however. If you boot with ``jdbc.required=false`` and if you do not configure a database, then the Frank!Framework will produce error message if it tries to do things that require a database.

Finally, a valid configuration is needed, for example in ``configurations/my-config/Configuration.xml``. If you are using this text as a tutorial, you can use the following example:

.. literalinclude:: ../../../../srcSteps/Frank2DockerDevel/v500/configurations/my-config/Configuration.xml
   :language: xml

And add ``configurations/my-config/Configuration_mine.xml``:

.. literalinclude:: ../../../../srcSteps/Frank2DockerDevel/v500/configurations/my-config/Configuration_mine.xml
   :language: xml

At this point, the development environment can be started using ``docker compose up``. It becomes available at http://localhost:8080.

.. NOTE::

   You may wonder why the shown URL starts with ``http`` instead of ``https`` - is your data safe within the Frank!Framework? The answer has to do with the DTAP stage. Only if ``dtap.stage=LOC`` then access through ``http`` is possible. Otherwise, access is only possible through ``https``. Service managers should check that security is taken care of in your app. The Frank!Framework allows Frank developers to protect the data.
