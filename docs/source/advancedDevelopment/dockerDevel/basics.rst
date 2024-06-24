The basics
==========

About configuring docker
------------------------

We assume in this section that you have docker and docker-compose on your development device. If you work with Windows and Docker Desktop, you have to configure it to allow volumes that use your working directory. Please do the following:

1. Go to your Docker Desktop window and press the settings button:

   .. image:: dockerDesktopHighlightSettingsButton.jpg

#. Add your directory as a shared file resource:

   .. image:: setFileResource.jpg

Starting the FF! with docker-compose
------------------------------------

WeAreFrank! maintains Docker image ``frankframework/frankframework`` on Dockerhub. It runs Linux and contains Apache Tomcat with the Frank!Framework deployed. It configures the Frank!Framework to read configurations from directory ``/opt/frank/configurations``. The Frank!Framework is served under the root context on port 8080. The following ``docker-compose.yml`` is sufficient to get started:

.. literalinclude:: ../../../../srcSteps/Frank2dockerDevel/v500/docker-compose.yml

This defines service ``frank-docker-example`` from the mentioned FF! image. It exposes port 8080 of the container to port 8080 on your device. It creates a Docker volume that maps subdirectory ``configurations`` (relative to the project root) to ``/opt/frank/configurations``, allowing you to write your configurations in directory ``configurations`` on your device. Then it sets some necessary properties for the Frank!Framework, most notably ``instance.name`` and ``dtap.stage``. See :ref:`propertiesDeploymentEnvironment` about DTAP stages and :ref:`propertiesFramework` for an overview of all properties that change the behavior of the FF!.

You need one more file because the Frank!Framework expects that there is a database with JNDI name ``jdbc/${instance.name.lc}`` with ``instance.name.lc`` the value of property ``instance.name`` converted to lower-case. To get started, you can use an in-memory H2 database. To do this, create file ``configurations/resources.yml`` with the following contents:

.. literalinclude:: ../../../../srcSteps/Frank2dockerDevel/v500/configurations/resources.yml

If you also provide a valid configuration in ``configurations/Configuration.xml``, you can start your work using ``docker-compose up``. You can see it on http://localhost:8080.

.. NOTE::

   You may wonder why the shown URL starts with `http` instead of `https` - is your data safe within the Frank!Framework? The answer has to do with the DTAP stage. Only if `dtap.stage=LOC` then access through `http` is possible. Otherwise, access is only possible through `https`. As a service manager, you should check that security is taken care of in your app. The Frank!Framework allows Frank developers to protect the data.
