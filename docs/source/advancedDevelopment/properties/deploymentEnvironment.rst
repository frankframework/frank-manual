.. _propertiesDeploymentEnvironment:

Deployment Environment Characteristics
======================================

The introduction of this chapter introduced properties as the communication mechanism between a Frank and its deployment environment. In this subsection, we examine characteristics of this deployment environment.

First, it is wise to differentiate between test environments and production environments. In general, an enterprise application is first tested by the development team on a development environment (D). If the development team considers a release, the application is deployed and tested on a test environment (T). If these tests are successful, the application is delivered to the customer. The customer deploys the application on a test environment for acceptance testing (A). Only when the acceptance tests succeed, the application is deployed on the production environment (P). This story explains the meaning of the DTAP acronym. At WeAreFrank!, we add the L (Local) for development testing on the laptop of an individual developer.

The Frank!Framework expects that the deployer sets property ``otap.stage`` to one of the following values: ``LOC``, ``DEV``, ``TST``, ``ACC`` or ``PRD``. Details on how to do this are in chapter :ref:`deploying`.

.. NOTE::

   OTAP is the Dutch version of the DTAP acronym. 

Second, you can deploy the Frank!Framework on multiple application servers like Apache Tomcat, JBoss Application Server (recently renamed to WildFly) or WebSphere Application Server. The Frank!Framework automatically sets property ``application.server.type``. The following table shows for each application server the resulting value of ``application.server.type``:

==========================  ======================================
   application.server.type     Application server
--------------------------  --------------------------------------
   WAS                         WebSphere Application Server.
   TOMCAT                      Apache Tomcat.
   TOMCAT                      WeAreFrank! Quick Docker Installer.
   JBOSS                       JBoss Application Server
   TIBCOAMX                    Tibco AMX
==========================  ======================================

Third, the customer may have multiple departments or networks, each requiring its own fine-tuning. You can make your Frank configurable by using the property ``otap.side``. The default value of this property is ``xxx``. The system administrator deploying your Frank can freely choose a value for this property.

The three properties ``otap.stage``, ``application.server.type`` and ``otap.side`` influence the way that other property values are initialized. This is explained in the next subsection.
