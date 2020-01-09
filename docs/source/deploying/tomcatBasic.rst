.. _deploymentTomcatBasic:

Deploying with a H2 database
============================

.. highlight: none

This subsection is the first tutorial about manually deploying a Frank on an Apache Tomcat application server. It uses an in-memory H2 database. In this tutorial we do not set up an external database.

As a starting point you need a Linux PC, a Linux virtual machine or a Docker container with a clean installation of Apache Tomcat. This tutorial assumes you use a Docker container. If you have a virtual machine or a real Linux server, please apply these instructions differently such that they work for your environment. You also need to download the :download:`example Frank config <../downloads/deploymentTomcat.zip>` that you will deploy in this tutorial. Please extract this .zip into a directory of your choice; we refer to it as ``work``. You should have the following directory structure: ::

  work
  |- classes
     |- Configuration.xml
     |- DeploymentSpecifics.properties
  |- configurations
     |- myConfig
        |- Configuration.xml
        |- ConfigurationReferenceProperties.xml
        |- DeploymentSpecifics.properties
  |- downloadLibraries.sh

When you are done with these preparations, please do the following:

#. Please make an account on Dockerhub, https://hub.docker.com/.
#. Create a Docker container from the Tomcat 7.0.99 image hosted on Dockerhub. Use the following command: ::

     > docker run --name tomcat-frank -p 8080:8080 tomcat:7.0.99

   This creates a Docker container named ``tomcat-frank``. The ``-p 8080:8080`` is added to export port 8080 to the host PC, making the Frank!Framework reachable by a webbrowser.

#. Start the Docker image with the following command: ::

     > docker start tomcat-frank

   Please note that Apache Tomcat is started automatically. You cannot run the container without running Apache Tomcat inside of it.

Now you need to deploy the Frank!Framework within your Tomcat instance. The table below shows which files you need and where they need to be stored:

========================================================  =========================================================
Source                                                    Destination
--------------------------------------------------------  ---------------------------------------------------------
``ibis-adapterframework-webapp-7.5-20191211.175453.war``  ``/usr/local/tomcat/webapps/frankframework.war``
``h2-1.4.199.jar``                                        ``/usr/local/tomcat/lib/h2.jar``
``jtds-1.3.1.jar.zip``                                    ``/usr/local/tomcat/lib/jtds-1.3.1.zip``
``geronimo-jms_1.1_spec-1.1.1.jar``                       ``/usr/local/tomcat/lib/geronimo-jms_1.1_spec-1.1.1.jar``
``commons-dbcp-1.4.jar``                                  ``/usr/local/tomcat/lib/commons-dbcp-1.4.jar``
``commons-pool-1.5.6.jar``                                ``/usr/local/tomcat/lib/commons-pool-1.5.6.jar``
========================================================  =========================================================

.. NOTE::

   If you wonder what files you need, please look at the Docker4Frank project, https://github.com/ibissource/docker4ibis. In file ``IAF_Image/Dockerfile``, you see the commands that Docker4Frank uses to deploy the Frank!Framework automatically. You see the commands there that download the files. You can omit the drivers for databases you do not need, but the rest of the download commands tell you which files you need.

You do not have to download these files manually. For your convenience, we added a script ``downloadLibraries.sh`` to the example configuration. Please deploy the Frank!Framework as follows.

4. You need a home directory on your Docker container. To do this, you need to run interactive commands within your Docker container. Therefore you need to start an interactive bash session. This is done differently depending on the operating system of your host computer:

   * On Linux, enter the following command: ::
  
       > docker exec -it tomcat-frank bash

   * On Windows, enter the following command: ::

       > winpty docker exec -it tomcat-frank bash

     You may have to install ``winpty`` before this works.

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
#. Unzip the only .zip file you have: ::

     >> unzip /usr/local/tomcat/lib/jtds-1.3.1.zip -d /usr/local/tomcat/lib
     >> rm /usr/local/tomcat/lib/jtds-1.3.1.zip

#. Enter ``exit`` to exit your container.

With these steps, you have deployed the Frank!Framework on your Docker container. It will not work properly yet because you do not have a configuration. Please continue as follows:

15. Enter your Docker container with the command documented earlier.
#. Within your container, copy your ``/home/root/Downloads/classes`` folder to your deployment: ::

     >> cd /home/root/Downloads/work/classes
     >> mkdir -p /usr/local/tomcat/webapps/frankframework/WEB-INF/classes
     >> cp -r * /usr/local/tomcat/webapps/frankframework/WEB-INF/classes
     >> cd /usr/local/tomcat/webapps/frankframework/WEB-INF/classes
     >> ls

   You should see the copied files within your deployment.
#. You have to tell the Frank!Framework that you chose a custom directory to store configuration ``myConfig`` by setting a system property. Please enter the following commands: ::

     >> cd /usr/local/tomcat/conf
     >> echo "configurations.myConfig.directory=/home/root/Downloads/work/configurations" >> catalina.properties

   .. WARNING::

      Please take care to use ``>>`` in the previous command. If you use ``>``, you will delete the existing contents of ``catalina.properties``. The ``>>`` symbol appends the echoed text to the existing contents.

#. Finally configure your database by configuring a JNDI resource, see https://tomcat.apache.org/tomcat-7.0-doc/jndi-resources-howto.html for more information. Please add the following lines to ``/usr/local/tomcat/conf/context.xml``:

   .. code-block:: XML

      <Resource
          name="jdbc/deploymenttomcat"
          type="org.h2.jdbcx.JdbcDataSource"
          factory="org.apache.naming.factory.BeanFactory"
          URL="jdbc:h2:/usr/local/tomcat/logs/ibisname" />

   These lines should be placed to the end of the file, right before the last line ``</Context>``. It is important that the ``<Resource>`` tag is inside of the ``<Context>`` tag.

   .. NOTE::

      The JNDI name ``jdbc/deploymenttomcat`` is referenced in the example Frank configuration in ``classes/Configuration.xml``. The line ``<jmsRealm realmName="jdbc" datasourceName="jdbc/${instance.name.lc}"/>`` defines it, because the value of property ``instance.name.lc`` is ``deploymenttomcat``. The property ``instance.name.lc`` is generated automatically by the Frank!Framework from property ``instance.name`` by replacing upper-case letters with lower-case letters. In file ``classes/DeploymentSpecifics.properties`` you can see that property ``instance.name`` is ``deploymentTomcat``.

#. Enter ``exit`` to exit from your Docker container.

With these steps you have added your Frank configuration and you have configured its database. You can test your work with the following steps:

20. Restart your docker container with the following commands: ::

     > docker stop tomcat-frank
     > docker start tomcat-frank

#. Remember that you exported port 8080 of your container. When you access port 8080 of your host computer, you reach into your container. Please start a webbrowser and go to http://localhost:8080/frankframework/iaf/gui. You should see the following.

   .. image:: frankHome.jpg

#. You are in the Adapter Status screen (number 1). Please click "Configuration messages" (number 2) to see that there are no error messages. You should see tabs "myConfig" (number 3) and "deploymentTomcat" (number 4).
#. If you have errors, you can click "Environment Variables" (number 5). Using Ctrl-F you can check whether property ``configurations.myConfig.directory`` is defined.
#. If you have no errors, you can proceed to testing your deployed configuration. Press "Testing" in the figure below. The "Testing" menu item expands as shown:

   .. image:: frankConsoleFindTestTools.jpg

#. Press "Test Pipeline". You are in the "Test Pipeline" screen (number 1 in the figure below). Choose adapter "AccessProperties" (number 2), which is part of the example Frank configuration. Enter an arbitrary message (number 3) and press "Send" (number 4).

   .. image:: testPipeline.jpg

#. Check that you get the result message ``From stage PRD, I say My text is Hello`` (number 5) and that processing was successful. You should see a green bar with the word "success" (number 6).
