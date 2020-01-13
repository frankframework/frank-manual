.. _deploymentTomcatDatabase:

Deploying with an External Database
===================================

.. highlight:: none

Preparations
------------

This subsection is the second tutorial about manually deploying a Frank on an Apache Tomcat application server. In the first tutorial you used an in-memory database. In this tutorial we migrate to an external database; for this tutorial we choose a MySQL database because it is free.

If you are using Docker, you can skip the first tutorial. In this case you should do the following preparations to catch up:

#. Please make an account on Dockerhub, https://hub.docker.com/.
#. On the command prompt, login to Dockerhub: ::

     docker login

#. Choose some directory to work in, say ``work``.
#. Download the :download:`example Frank config <../downloads/deploymentTomcat.zip>`; this is the same file as is used in the first tutorial. This zipfile also contains a file ``Dockerfile``. After unzipping, you should have a file ``work/deploymentTomcat/Dockerfile``.

   .. WARNING::

      If you are doing this second tutorial after the first tutorial, please note that ``work`` has changed meaning. The ``work`` of the first tutorial is now ``work/deploymentTomcat``.

#. Create a Docker image ``tomcat-frank-img`` with the Frank!Framework and the configuration of the first tutorial. Enter directory ``work/deploymentTomcat`` and then run the following (same for Windows and Linux): ::

   > docker build -t tomcat-frank-img .

#. Run the image to get a container ``tomcat-frank``: ::

   > docker run -p 8080:8080 --name tomcat-frank tomcat-frank-img

.. deploymentTomcatSetUpExternalDatabase:

Set up the external database
----------------------------

We assume now that you have the example Frank up and running using an in-memory H2 database. You need an external MySQL databasee now. You can have it on a separate server, a Virtual Machine or a Docker image. The database server should have network connectivity such that the Frank!Framework can connect to it. There should be a user that has permission to create tables and to modify and read data.

If you are using Docker, you can create your database server as follows:

#. Create a container with your database server using the following command: ::

   > docker run --name external-db -e MYSQL_ROOT_PASSWORD=mypwd mysql:5.7

#. Run the command ``docker inspect external-db``. This gives a lot of information, including the IP address of this container. We assume it is ``172.17.0.2``. If it is different, apply the real IP address in the next instructions.
#. Connect to your database server: ::

   > docker run -it --rm mysql mysql -h172.17.0.2 -uroot -p

   .. NOTE::

      This command runs image ``mysql`` and deletes the resulting container automatically when it stops. The ``-h``, ``-u`` and ``-p`` arguments are arguments of the ``mysql`` command-line tool.

#. Create a new database: ::

     mysql> CREATE DATABASE db;

   .. NOTE::

      In this tutorial we let the Frank!Framework connect as user ``root``. On production, you should make a dedicated database user for the Frank!Framework that only has rights on the ``db`` database. We do not demonstrate this here because we focus on configuring the Frank!Framework.

#. Enter ``exit``. Your MySQL client quits and the container that ran it is removed.

You should have a running container ``external-db`` with a MySQL server running. The server should have a database named ``db``. It is assumed that this server has IP address ``172.17.0.2``, but this can be different for you. Please use the real IP address instead of ``172.17.0.2`` in the remainder of this tutorial. You will use the ``root`` database user in this tutorial, although it is not wise to do so in production. You gave this user password ``mypwd``.

Migrate the database
--------------------

Please migrate the Frank!Framework to the new database, as follows:

7. Enter the server on which you installed the Frank!Framework. If you are using Docker, you can do this with the following command: ::

   > docker exec -it tomcat-frank bash

#. Download the MySQL driver ``mysql-connector-java-5.1.44.jar`` for the Frank!Framework and make it available to your application server: ::

   >> wget -O /usr/local/tomcat/lib/mysql-connector-java-5.1.44.jar https://repo1.maven.org/maven2/mysql/mysql-connector-java/5.1.44/mysql-connector-java-5.1.44.jar

#. You will change the definition of JNDI name ``jdbc/deploymenttomcat``, see https://tomcat.apache.org/tomcat-7.0-doc/jndi-resources-howto.html, to point to the new database. Please edit ``/usr/local/tomcat/conf/context.xml`` such that the ``<Resource>`` element become as follows:

   .. code-block:: xml

      <Resource
          name="jdbc/deploymenttomcat"
          auth="Container"
          type="javax.sql.DataSource"
          username="root"
          password="mypwd"
          driverClassName="com.mysql.jdbc.Driver"
          url="jdbc:mysql://172.17.0.2:3306/db"
          maxActive="8"
          maxIdle="3"
          validationQuery="select 1" />

   In the first tutorial you installed text editor ``nano``, so you can use it now if you want.

#. Enter ``exit`` to leave the Frank!Framework container. Restart it using the following commands: ::

   > docker stop tomcat-frank
   > docker start tomcat-frank

#. The Frank!Framework should be available as a website on URL http://localhost:8080/frankframework/iaf/gui. You can test it exactly as shown in the first tutorial, see :ref:`deploymentTomcatBasicTest`.
#. In addition, you can check that the Frank!Framework is indeed running on the MySQL database. You can check that some new tables have been created, as follows:

   a. Start a new MySQL client: ::

      > docker run -it --rm mysql mysql -h172.17.0.2 -uroot -p

   #. Select the database you created: ::

        mysql> use db;

   #. Run a query to see what tables you have: ::

        mysql> show tables;
        +-----------------------+
        | Tables_in_db          |
        +-----------------------+
        | DATABASECHANGELOG     |
        | DATABASECHANGELOGLOCK |
        | IBISCONFIG            |
        | IBISLOCK              |
        | IBISPROP              |
        | IBISSCHEDULES         |
        | IBISSTORE             |
        +-----------------------+
        7 rows in set (0.01 sec)

This finishes the tutorials on manually installing the Frank!Framework on Apache Tomcat. Remember that you should deploy the Frank!Framework as a webapplication. Next you should download additional libraries including the database driver for the database you choose. Finally you should configure the JNDI name of your database as a resource in ``context.xml>``. The Frank developer who programmed the Frank configuration should know the name you need to configure (in this tutorial it is``jdbc/deploymenttomcat``).
