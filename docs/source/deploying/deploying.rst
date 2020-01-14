.. _deploying:

Deployment
==========

In :ref:`globalIntroduction` it was said that the Frank!Framework is a solution to quickly build enterprise applications, called Franks. A Frank consists of the Frank!Framework that is combined with Frank configurations. Frank configurations configure the Frank!Framework to provide the services you need. They are written as XML documents and property files. The chapters :ref:`gettingStarted` and :ref:`advancedDevelopment` explain how to write Frank configurations. This chapter can be studied independently from :ref:`gettingStarted`. It is not about writing Frank configurations, but focuses on deployment. How can a given Frank configuration be deployed on the IT infrastructure you want?

The Frank!Framework is a Java web application that has to be served by an application server. The Frank!Framework can be deployed on many types of application servers, for example Apache Tomcat, JBoss Application Server (recently renamed to WildFly) or WebSphere Application Server. These application server types require different procedures for deploying the Frank!Framework. The present version of this manual only covers deployment on Apache Tomcat. If you want to deploy on a different type of application server, please contact `WeAreFrank! <https://www.integrationpartners.nl>`_ .

If you want to install a Frank on your existing IT infrastructure, you should know how to manually deploy the Frank!Framework on your application server and you should know how to add your Frank configuration. This is covered in section :ref:`deploymentTomcat` in case you are using Apache Tomcat. There are also two projects that automate deploying and running a Frank, see sections :ref:`deploymentTomcat4Frank` and :ref:`deploymentDocker4Frank`.

Here is the table of contents of this chapter:

.. toctree::
   :maxdepth: 3

   tomcat4frank
   docker4frank
   tomcat
 