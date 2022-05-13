.. _advancedDevelopmentDeploymentMaven:

Maven
=====

The Frank!Framework is a Java webapplication that integrates other applications. The Frank!Framework needs to be configured with XML files that describe how messages are received, transformed and sent to their target systems. Chapter :ref:`gettingStarted` explained how to write these configuration files. The configurations were executed with WeAreFrank!'s `Frank!Runner <https://github.com/ibissource/frank-runner>`_, which was useful during development. The Frank!Runner was not designed however to deploy Frank configurations to a production environment.

Maven has been developed to build Java webapplications. The Frank!Framework is a Java webapplication. You can use Maven to package the Frank!Framework and one configuration into a single executable file. That file has extension ``.war``. It can be executed by an application server like `Apache Tomcat <https://tomcat.apache.org/>`_, `WildFly <https://www.wildfly.org/>`_, `JBoss EAP <https://developers.redhat.com/products/eap/overview>`_ or `WebSphere <https://www.ibm.com/cloud/websphere-application-server>`_. Maven projects can easily be tested and deployed within continuous delivery pipelines using for example `Jenkins <https://www.jenkins.io/>`_, `GitLab <https://about.gitlab.com/>`_  or `GitHub actions <https://github.com/features/actions>`_.

A basic understanding of Maven is needed before it can be leveraged in Frank projects successfully. This introduction appears in subsections :ref:`advancedDevelopmentDeploymentMavenJavaBasics`, :ref:`advancedDevelopmentDeploymentMavenMavenBasics`, :ref:`advancedDevelopmentDeploymentMavenExecuteJar` and :ref:`advancedDevelopmentDeploymentMavenMavenWebapp`. Subsections :ref:`advancedDevelopmentDeploymentMavenBasicFrankWebapp`, :ref:`advancedDevelopmentDeploymentMavenFrankFrontend` and :ref:`advancedDevelopmentDeploymentMavenLarva` explain how to use Maven within a Frank development project. By the end of subsection :ref:`advancedDevelopmentDeploymentMavenLarva`, you will have a Maven project that you can use as a template for your own Frank project. Here is the :download:`download <../../downloads/configurations/Frank2Webapp.zip>`.

The project setup of :ref:`advancedDevelopmentDeploymentMavenLarva` has some drawbacks. These can be addressed by using the Frank!Runner, which can work with Frank projects structured as a Maven project. This is demonstrated in example "Frank2Example4" of the `Frank!Runner <https://github.com/ibissource/frank-runner>`_. This is explained in more detail in subsection :ref:`advancedDevelopmentDeploymentMavenUsingFrankRunner`.

.. toctree::
   :maxdepth: 1

   javaBasics
   mavenBasics
   executeJar
   mavenWebapp
   basicFrankWebapp
   frankFrontend
   larva
   usingFrankRunner