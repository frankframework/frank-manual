.. _advancedDevelopmentDockerDevel:

Developing with docker instead of Frank!Runner
==============================================

In :ref:`gettingStarted`, you learned the basics of developing Frank configurations. You used the Frank!Runner (https://github.com/wearefrank/frank-runner) to run them. Working with the Frank!Runner is easy because it handles a lot of details about starting your Frank configuration, for example:

* The Frank!Runner automatically downloads the Frank!Framework for you.
* It downloads Java.
* It downloads Apache Tomcat.
* It deploys the Frank!Framework, a Java webapplication, in Tomcat.
* It configures the Tomcat server, for example:
  * It sets properties such that the Frank!Framework can find your Frank configuration.
  * It sets `dtap.stage=LOC` in `catalina.properties`.
  * It copies the `context.xml` you provide or it creates one that has a `<Resource>` tag for your database.

You may want more insight into these details already during development. You can achieve this by using Docker (see https://hub.docker.com/). WeAreFrank! has created a Docker image that holds the Frank!Framework deployed inside the appropriate version of Apache Tomcat. This image can also be used in your production environment. If you do your development using Docker, your development environment is more similar to your production environment. This page focuses on development, however, not on deployment on a production environment.

This section has the following sub-sections:

.. toctree::
   :maxdepth: 3

   basics
   frankflow