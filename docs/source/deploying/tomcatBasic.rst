.. _deploymentTomcatBasic:

Deploying with a H2 database
============================

Preparations
------------

.. highlight: none

This subsection is the first tutorial about manually deploying a Frank on an Apache Tomcat application server. It uses an in-memory H2 database. In this tutorial we do not set up an external database.

As a starting point you need a Linux PC, a Linux virtual machine or a Docker container with a clean installation of Apache Tomcat. This tutorial assumes you use a Docker container. If you have a virtual machine or a real Linux server, please apply these instructions differently such that they work for your environment. You also need to download the :download:`example Frank <../downloads/deploymentTomcat.zip>` that you will deploy in this tutorial.

.. NOTE::

   You are downloading a Frank here, not a Frank configuration like the download links of :ref:`gettingStarted`. You have one directory here that holds all the data the Frank!Framework should process. You are learning how to deploy the Frank!Framework on an Apache Tomcat application server, while :ref:`gettingStarted` covered deploying Frank configs on the Frank!Framework.

Please extract the .zip into a directory of your choice; we refer to it as ``work``. You should have the following directory structure: ::

  work
  |- classes
     |- Configuration.xml
     |- DeploymentSpecifics.properties
  |- configurations
     |- myConfig
        |- Configuration.xml
        |- ConfigurationReferenceProperties.xml
        |- DeploymentSpecifics.properties
  |- tests
     |- myConfig
        |- scenario01.properties
        |- step1.txt
        |- step2.txt
  |- downloadLibraries.sh
  |- Dockerfile
  |- resorceDef

When you are done with these preparations, please do the following:

#. Please make an account on Dockerhub, https://hub.docker.com/.
#. On the command prompt, login to Dockerhub: ::

     > docker login

#. Create a Docker container from the Tomcat 7.0.99 image hosted on Dockerhub. Use the following command: ::

     > docker run --name tomcat-frank -p 8080:8080 tomcat:7.0.99

   This creates a Docker container named ``tomcat-frank``. The ``-p 8080:8080`` is added to export port 8080 to the host computer, making the Frank!Framework reachable by a webbrowser. This command does not stop by itself, so:
#. When you see the output like ``INFO: Server startup in 40 ms``, press Ctrl-C to stop.
#. Start the Docker container with the following command: ::

     > docker start tomcat-frank

   Please note that Apache Tomcat is started automatically. You cannot run the container without running Apache Tomcat inside of it.

Deploy the Frank!Framework
--------------------------

Now you need to deploy the Frank!Framework within your Tomcat instance. The table below shows which files you need and where they need to be stored:

========================================================  =========================================================
Source                                                    Destination
--------------------------------------------------------  ---------------------------------------------------------
``ibis-adapterframework-webapp-7.5-20191211.175453.war``  ``/usr/local/tomcat/webapps/frankframework.war``
``h2-1.4.199.jar``                                        ``/usr/local/tomcat/lib/h2.jar``
``jtds-1.3.1.jar``                                        ``/usr/local/tomcat/lib/jtds-1.3.1.jar``
``geronimo-jms_1.1_spec-1.1.1.jar``                       ``/usr/local/tomcat/lib/geronimo-jms_1.1_spec-1.1.1.jar``
``commons-dbcp-1.4.jar``                                  ``/usr/local/tomcat/lib/commons-dbcp-1.4.jar``
``commons-pool-1.5.6.jar``                                ``/usr/local/tomcat/lib/commons-pool-1.5.6.jar``
========================================================  =========================================================

You do not have to download these files manually. For your convenience, we added a script ``downloadLibraries.sh`` to the example configuration. Please deploy the Frank!Framework as follows:

6. You need a home directory on your Docker container. To do this, you need to run interactive commands within your Docker container. Please run the following command in a command prompt (Windows) or a shell (Linux): ::
  
     > docker exec -it tomcat-frank bash

#. Your prompt changes, indicating you are within your container. Create a home directory by executing the following command: ::

     >> mkdir -p /home/root/Downloads

#. You will edit text files within your container. Install the nano text editor as follows: ::

     >> apt-get update
     >> apt-get install nano

#. Enter ``exit`` to exit your container.
#. Copy directory ``work`` to your docker container. From within your ``work`` directory, enter the following command: ::

     > docker cp . tomcat-frank:/home/root/Downloads/work

#. Enter your docker container again, with exactly the same command as before.
#. Change directory to ``/home/root/Downloads/work``: ::

     >> cd /home/root/Downloads/work

#. Execute the download script you copied: ::

     >> chmod a+x downloadLibraries.sh
     >> ./downloadLibraries.sh

#. With the previous step you added file ``/usr/local/tomcat/webapps/frankframework.war``. Check that Apache Tomcat unpacks this archive. Execute the following commands: ::

     >> cd /usr/local/tomcat/webapps/frankframework
     >> ls

   You should see that this directory exists and that it is not empty.
#. Enter ``exit`` to exit your container.

.. _deploymentTomcatBasicAddFrankConfiguration:

Add your Frank configuration
----------------------------

With these steps, you have deployed the Frank!Framework on your Docker container. It will not work properly yet because you do not have a configuration. Please continue as follows:

16. Enter your Docker container with the command documented earlier.
#. The contents of your ``classes`` folder must be stored inside the deployment on your application server. Within your container, copy your ``/home/root/Downloads/classes`` folder to your deployment: ::

     >> cd /home/root/Downloads/work/classes
     >> mkdir -p /usr/local/tomcat/webapps/frankframework/WEB-INF/classes
     >> cp -r * /usr/local/tomcat/webapps/frankframework/WEB-INF/classes
     >> cd /usr/local/tomcat/webapps/frankframework/WEB-INF/classes
     >> ls

   You should see the copied files within your deployment.
#. You need to set the DTAP stage as a system property. You can set system properties in Tomcat by defining them in file ``/usr/local/tomcat/conf/catalina.properties``. Please add the following line to this file:

   .. code-block:: none
      
      dtap.stage=LOC

   .. WARNING::

      It is not realistic that we do a manual deployment on Tomcat but that we have DTAP stage LOC. If you are developing, use Frank!Runner if possible. We choose DTAP stage LOC because we are including a Larva test in our deployment, which is not realistic in a production environment.

#. The ``configurations`` directory is stored outside the deployment on your application server. You can use the copy you stored in ``/home/root/Downloads/work/configurations``. This is not the default location expected by the Frank!Framework. You have to tell the Frank!Framework that you choose a custom directory for configuration ``myConfig``. You will do this by setting a system property. Please add the following line to ``catalina.properties``: ::

     configurations.myConfig.directory=/home/root/Downloads/work/configurations

#. Franks have a ``tests`` directory. This directory contains automated tests that can be executed using the Larva service. The Frank!Framework needs two system properties to be able to find them. Please append the following to ``catalina.properties``: ::

     scenariosroot1.directory=/home/root/Downloads/work/tests/
     scenariosroot1.description=My Larva tests

#. Finally configure your database by configuring a JNDI resource, see https://tomcat.apache.org/tomcat-7.0-doc/jndi-resources-howto.html for more information. Please add the following lines to ``/usr/local/tomcat/conf/context.xml``:

   .. code-block:: XML

      <Resource
          name="jdbc/deploymenttomcat"
          type="org.h2.jdbcx.JdbcDataSource"
          factory="org.apache.naming.factory.BeanFactory"
          URL="jdbc:h2:/usr/local/tomcat/logs/ibisname" />

   These lines should be placed to the end of the file, right before the last line ``</Context>``. It is important that the ``<Resource>`` tag is inside of the ``<Context>`` tag.

   .. NOTE::

      The JNDI name ``jdbc/deploymenttomcat`` is referenced in the example Frank configuration in ``classes/Configuration.xml``. The line ``<jmsRealm realmName="jdbc" datasourceName="jdbc/${instance.name.lc}"/>`` references it, because the value of property ``instance.name.lc`` is ``deploymenttomcat``. The property ``instance.name.lc`` is generated automatically by the Frank!Framework from property ``instance.name`` by replacing upper-case letters with lower-case letters. In file ``classes/DeploymentSpecifics.properties`` you can see that property ``instance.name`` is ``deploymentTomcat``.

#. Enter ``exit`` to exit from your Docker container.

With these steps you have added your Frank configuration and you have configured its database.

.. _deploymentTomcatBasicTest:

Test your work
--------------

You can test your work with the following steps:

23. Restart your docker container with the following commands: ::

     > docker stop tomcat-frank
     > docker start tomcat-frank

#. Remember that you exported port 8080 of your container. When you access port 8080 of your host computer, you reach into your container. Please start a webbrowser and go to http://localhost:8080/frankframework/iaf/gui. You should see the following.

   .. image:: frankHome.jpg

#. You are in the Adapter Status screen (number 1). Please click "Configuration messages" (number 2) to see that there are no error messages. You should see tabs "myConfig" (number 3) and "deploymentTomcat" (number 4).
#. If you have errors, you can click "Environment Variables" (number 5). Using Ctrl-F you can check whether property ``configurations.myConfig.directory`` is defined.
#. If you have errors, you can also examine the output produced by Tomcat. If you are using docker, use the command ``docker logs tomcat-frank``.

   .. NOTE::

      Also if everything is well, you will probably see a lot of errors. The reason is that Apache Tomcat was already running while you were deploying your Frank. The errors were produced when your Frank was not complete. Please look for the moment that you restarted your container. Only errors after that monent are relevant.

#. If you have no errors, you can proceed to testing your deployed configuration. Press "Testing" in the figure below. The "Testing" menu item expands as shown:

   .. image:: frankConsoleFindTestTools.jpg

#. Press "Test Pipeline". You are in the "Test Pipeline" screen (number 1 in the figure below). Choose adapter "AccessProperties" (number 2), which is part of the example Frank configuration. Enter an arbitrary message (number 3) and press "Send" (number 4).

   .. image:: testPipeline.jpg

#. Check that you get the result message ``From stage LOC, I say My text is Hello`` (number 5) and that processing was successful. You should see a green bar with the word "success" (number 6).

#. Please click "Larva" as shown in the screen below:

   .. image:: frankConsoleFindTestTools.jpg

#. You see you are in the Larva screen (number 1 in the figure below). Please enter "/" (number 2) to select all tests into your scenario root (number 3). Please note that you see the name here you configured using system property ``scenariosroot1.description``. Press "start" (number 4) to run your tests.

   .. image:: larva.jpg

#. Check that your tests succeed (number 5).
