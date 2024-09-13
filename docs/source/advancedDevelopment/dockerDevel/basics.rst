The basics
==========

Advantage of using docker
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

You may want more insight into these details already during development. You can achieve this by using Docker (see https://hub.docker.com/). We have created a Docker image that holds the Frank!Framework deployed inside the appropriate version of Apache Tomcat. This image can also be used in your production environment. If you do your development using Docker, your development environment is more similar to your production environment.

About configuring docker
------------------------

We assume in this section that you have docker and docker-compose on your development device. This is not an issue for Linux users. If you work with Windows and Docker Desktop, you have to configure it to allow volumes that use your working directory. Please do the following:

1. Go to your Docker Desktop window and press the settings button:

   .. image:: dockerDesktopHighlightSettingsButton.jpg

#. Add your directory as a shared file resource:

   .. image:: setFileResource.jpg

Starting the FF! with docker-compose
------------------------------------

Docker images are provided, suitable both for local and server use. Images are provided from the registry located at https://nexus.frankframework.org, where images will be stored for as long as possible. Specific nightly builds are made available on DockerHub ``frankframework/frankframework`` (https://hub.docker.com/r/frankframework/frankframework), but may only be available for 6 months (https://www.docker.com/blog/scaling-dockers-business-to-serve-millions-more-developers-storage). The source is available from the docker-folder in the ``frankframework/frankframework`` GitHub repository.

It runs Linux and contains Apache Tomcat with the Frank!Framework deployed. It configures the Frank!Framework to read configurations from directory ``/opt/frank/configurations``. The Frank!Framework is served under the root context on port 8080. The following ``docker-compose.yml`` is sufficient to get started:

.. literalinclude:: ../../../../srcSteps/Frank2DockerDevel/v500/docker-compose.yml
   :language: none

This defines service ``frank-docker-example`` from the mentioned FF! image. It exposes port 8080 of the container to port 8080 on your device. It creates a Docker volume that maps subdirectory ``configurations`` (relative to the project root) to ``/opt/frank/configurations``, allowing you to write your configurations in directory ``configurations`` on your device. Then it sets some necessary properties for the Frank!Framework, most notably ``instance.name`` and ``dtap.stage``. See :ref:`propertiesDeploymentEnvironment` about DTAP stages and :ref:`propertiesFramework` for an overview of all properties that change the behavior of the FF!.

You need one more file because the Frank!Framework expects that there is a database. Within Frank configurations, the database is referenced by a so-called JNDI name. System administrators can then configure the application server of the deployment environment, such that the JNDI name corresponds to a database. Application server Apache Tomcat expects a file ``context.xml`` for this. By default, the FF! uses a database with JNDI name ``jdbc/${instance.name.lc}`` with ``instance.name.lc`` the value of property ``instance.name`` converted to lower-case.

The Frank!Framework runs on multiple application servers, and therefore it supports a generic mechanism to reference resources. This can be accessed by Frank developers through a file ``resources.yml``. To get started, you can use an in-memory H2 database by creating ``configurations/resources.yml`` as follows:

.. literalinclude:: ../../../../srcSteps/Frank2DockerDevel/v500/configurations/resources.yml
   :language: none

.. WARNING::

   If you use an in-memory H2 database (which makes sense for local testing), it is recommended to include ``DB_CLOSE_ON_EXIT=FALSE`` in the URL. The Frank!Framework closes and opens database connections while working with the database. Without this text in the URL, the H2 database is cleared when the connection to the database is closed.

Finally, a valid configuration is needed, for example in ``configurations/my-config/Configuration.xml``. If you are using this text as a tutorial, you can use the following example:

.. literalinclude:: ../../../../srcSteps/Frank2DockerDevel/v500/configurations/my-config/Configuration.xml
   :language: xml

And add ``configurations/my-config/Configuration_mine.xml``:

.. literalinclude:: ../../../../srcSteps/Frank2DockerDevel/v500/configurations/my-config/Configuration_mine.xml
   :language: xml

At this point, the development environment can be started using ``docker compose up``. It becomes available at http://localhost:8080.

.. NOTE::

   You may wonder why the shown URL starts with ``http`` instead of ``https`` - is your data safe within the Frank!Framework? The answer has to do with the DTAP stage. Only if ``dtap.stage=LOC`` then access through ``http`` is possible. Otherwise, access is only possible through ``https``. Service managers should check that security is taken care of in your app. The Frank!Framework allows Frank developers to protect the data.
