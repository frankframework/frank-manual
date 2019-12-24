.. _propertiesDeploymentEnvironment:

Deployment Environment Characteristics
======================================

The introduction of this chapter introduced properties as the communication mechanism between a Frank and its deployment environment. The previous subsection introduced properties with a short tutorial in which you defined and referenced properties. In this subsection, we link properties to characteristics of your deployment environment.

Infrastructure
--------------

The figure below presents a general overview of the infrastructure used to deploy the Frank!Framework:

.. image:: deploymentLayers.jpg

The bottom layer shows the operating system of your server. On top of that you need an application server, typically Apache Tomcat, JBoss Application Server (recently renamed to WildFly) or WebSphere Application Server. The application server makes the Frank!Framework a web application.

On top of the application server the Frank!Framework is deployed. The Frank!Framework is a Java application. Java programs are compiled into byte code that is executed by the Java Virtual Machine. The application server runs the JVM and places deployed applications on the classpath. The classpath not only holds the byte code of the Frank!Framework, but it can also hold additional binaries and data, which is shown with the word "classes" next to the Frank!Framework. For the application server there is no distinction between the Frank!Framework and the extra data shown as "classes". When the Frank!Framework starts, it looks for additional Frank configurations outside the classpath. This is shown as the top layer, "Configurations".

Please remember that a Frank configuration consists of three directories ``classes``, ``configurations`` and ``tests`` (see section :ref:`horizonsMultipleFiles`). The directory ``classes`` has this name because its contents is put on the Java classpath. The contents of ``configurations`` and ``tests`` belongs to the top layer, "Configurations", because it does not appear on the classpath. For more information on how to deploy a Frank configuration, see chapter :ref:`deploying`.

This stack is relevant for Frank developers because it limits the way properties can be used. When the application server is started, it gets property definitions from the operating system and from command-line arguments (system properties). The application server then boots the Frank!Framework. During this process, properties are read from the classpath. Next, the Frank!Framework reads configurations from outside the classpath and reads properties from them (configuration properties).

Some properties can only be defined as system properties. An example is property ``log.dir``, the directory in which the Frank!Framework should store log files. When it is defined as classpath property, it will not work: the value is not applied by the Frank!Framework to store log information, but references to it in Frank configurations do produce the configured value. There are also properties that only work as system property or classpath property, but not as configuration property. See subsection :ref:`propertiesFramework` for more examples. This limitation can only apply to properties that are interpreted by the Frank!Framework. Other properties (e.g. ``my.hello`` in subsection :ref:`propertiesReference`) can be freely defined as configuration properties, classpath properties or system properties.

The Frank!Framework detects the type of application server used to host it. This information appears in property ``application.server.type``. The following table shows for each application server the resulting value of ``application.server.type``:

==========================  ======================================
   application.server.type     Application server
--------------------------  --------------------------------------
   WAS                         WebSphere Application Server.
   TOMCAT                      Apache Tomcat.
   TOMCAT                      WeAreFrank! Quick Docker Installer.
   JBOSS                       JBoss Application Server
   TIBCOAMX                    Tibco AMX
==========================  ======================================

Logical characteristics
-----------------------

There are also logical characteristics of your deployment environment. These are not related to the infrastructure being used, but they reflect information about the way the deployment is used.

First, it is wise to differentiate between test environments and production environments. In general, an enterprise application is first tested by the development team on a development environment (D). If the development team considers a release, the application is deployed and tested on a test environment (T). If these tests are successful, the application is delivered to the customer. The customer deploys the application on a test environment for acceptance testing (A). Only when the acceptance tests succeed, the application is deployed on the production environment (P). This story explains the meaning of the DTAP acronym. At WeAreFrank!, we add the L (Local) for development testing on the laptop of an individual developer.

The Frank!Framework expects that the deployer sets property ``otap.stage`` to one of the following values: ``LOC``, ``DEV``, ``TST``, ``ACC`` or ``PRD``. Details on how to do this are in chapter :ref:`deploying`.

.. NOTE::

   OTAP is the Dutch version of the DTAP acronym. 


Second, the customer may have multiple departments or networks, each requiring its own fine-tuning. You can make your Frank configurable by using the property ``otap.side``. The default value of this property is ``xxx``. The system administrator deploying your Frank can freely choose a value for this property.

The three properties ``otap.stage``, ``application.server.type`` and ``otap.side`` influence the way that other property values are initialized. This is explained in the next subsection.
