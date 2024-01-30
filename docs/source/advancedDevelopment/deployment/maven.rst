.. _advancedDevelopmentDeploymentMaven:

Maven
=====

The Frank!Framework is a Java webapplication that integrates other applications. The Frank!Framework needs to be configured with XML files that describe how messages are received, transformed and sent to their target systems. Chapter :ref:`gettingStarted` explained how to write these configuration files. The configurations were executed with the `Frank!Runner <https://github.com/wearefrank/frank-runner>`_, which was useful during development. The Frank!Runner was not designed however to deploy Frank configurations to a production environment.

Maven has been developed to build Java webapplications. The Frank!Framework is a Java webapplication. You can use Maven to package the Frank!Framework and one configuration into a single executable file. That file has extension ``.war``. It can be executed by an application server like `Apache Tomcat <https://tomcat.apache.org/>`_, `WildFly <https://www.wildfly.org/>`_, `JBoss EAP <https://developers.redhat.com/products/eap/overview>`_ or `WebSphere <https://www.ibm.com/cloud/websphere-application-server>`_. Maven projects can easily be tested and deployed within continuous delivery pipelines using for example `Jenkins <https://www.jenkins.io/>`_, `GitLab <https://about.gitlab.com/>`_  or `GitHub actions <https://github.com/features/actions>`_.

This subsection provides a basic understanding of Maven. After studying it, please study example Frank2Example4 within the Frank!Runner, see https://github.com/wearefrank/frank-runner.

.. toctree::
   :maxdepth: 1

   javaBasics
   mavenBasics
   executeJar
   mavenWebapp
