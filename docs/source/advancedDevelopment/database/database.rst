.. _advancedDevelopmentDatabase:

The Database
============

Introduction
------------

In chapter :ref:`gettingStarted` you accessed a relational database already. In your file ``classes/Configuration.xml``, you added the following line:

.. code-block:: XML

   <jmsRealm datasourceName="jdbc/${instance.name.lc}" realmName="jdbc"/>

Your database was then created and managed automatically. This behavior is fine during development, but on the production site the system administrator probably wants control over the database. If you are a system administrator yourself, please read chapter :ref:`deploying`. 

This chapter provides the information you need as a Frank developer to support the system administrator. You also learn how to work with multiple databases within the same Frank. Finally you learn more about initial data.

The application server
----------------------

In chapter :ref:`deploying`, it is explained how the Frank!Framework is deployed. The Frank!Framework is a Java webapplication that is served by an application server. Examples of application servers are Apache Tomcat and Websphere Application Server. The Frank!Framework is deployed as a webapplication on your application server. You may have missed this when you studied chapter :ref:`gettingStarted`, because you used the Tomcat4Frank tool that automates interaction with the application server. Using Tomcat4Frank is fine during development, but probably not on production. On production, the system administrator wants control over the application server. The role of the application server is explained in more detail in subsection :ref:`propertiesDeploymentEnvironment`.

Datasource names
----------------

In chapter :ref:`gettingStarted`, you managed your database with the following line in file ``classes/Configuration.xml``:

.. code-block:: XML

   <jmsRealm datasourceName="jdbc/${instance.name.lc}" realmName="jdbc"/>

To understand this line, you first have to understand property ``instance.name.lc``, see subsection :ref:`propertiesFramework`. Each Frank must define a property ``instance.name``. The Frank!Framework automatically calculates property ``instance.name.lc`` by taking the value of ``instance.name`` and replacing uppercase letters with lowercase letters. For example, if ``instance.name`` is ``MyApp``, then ``instance.name.lc`` becomes ``myapp``. In this case, the above line is equivalent to:

.. code-block:: XML

   <jmsRealm datasourceName="jdbc/myapp" realmName="jdbc"/>

The exact meaning of this line is explained later in this section. Now you need to know that it causes your Frank to use a database that is referenced by the name ``jdbc/myapp`` (or ``jdbc/otherapp`` if ``instance.name`` would be ``OtherApp``).

The name ``jdbc/myapp`` is a Java Naming and Directory Interface (JNDI) name. JNDI names allow you as a developer to reference a database without defining the database name, the database user and the password. You do not have to include sensitive information in your Frank config and your Frank can easily be deployed on different environments that each may have their own database. It is up to the system administrator to link each JNDI name in your Frank config to a concrete database, a concrete database user, a concrete password etc. You can see an example in subsection :ref:`deploymentTomcatDatabaseMigrate`.

This knowledge allows you to use multiple databases. If you have a second database then give it a JNDI name, say ``jdbc/alternative``. The senders and listeners that access the database all have an attribute ``datasourceName``. Set this attribute within your Frank config, ``datasourceName="jdbc/alternative"``, every time you want to access your second database.

In section :ref:`insertDb`, you encountered the following XML to insert something into the database:

.. code-block:: XML

   <SenderPipe
       name="insertBooking">
     <FixedQuerySender
         name="insertBookingSender"
         query="INSERT INTO booking VALUES(?, ?, ?, ?)"
         jmsRealm="jdbc">
       <Param name="id" xpathExpression="/booking/@id" />
       <Param name="travelerId" xpathExpression="/booking/travelerId" />
       <Param name="price" xpathExpression="/booking/price" />
       <Param name="fee" xpathExpression="/booking/fee" />
     </FixedQuerySender>
     <Forward name="success" path="Exit" />
     <Forward name="failure" path="ServerError" />
   </SenderPipe>

If you would write into a database with JNDI name ``jdbc/alternative``, you would update the above to:

.. code-block:: XML
   :emphasize-lines: 6

   <SenderPipe
       name="insertBooking">
     <FixedQuerySender
         name="insertBookingSender"
         query="INSERT INTO booking VALUES(?, ?, ?, ?)"
         datasourceName="jdbc/alternative">
       <Param name="id" xpathExpression="/booking/@id" />
       <Param name="travelerId" xpathExpression="/booking/travelerId" />
       <Param name="price" xpathExpression="/booking/price" />
       <Param name="fee" xpathExpression="/booking/fee" />
     </FixedQuerySender>
     <Forward name="success" path="Exit" />
     <Forward name="failure" path="ServerError" />
   </SenderPipe>

.. WARNING::

   Tomcat4Frank and Docker4Frank (see sections :ref:`deploymentDocker4Frank` and :ref:`deploymentDocker4Frank`) do not support multiple databases. These tools automate deploying the Frank!Framework and they automatically create a database for your Frank. You cannot use these projects to connect to an existing database or to use multiple databases.

If you are using an Apache Tomcat application server, then the Frank!Framework expects that there is a database with JNDI name ``jdbc/${instance.name.lc}`` with ``${instance.name.lc}`` a property reference as explained. The expected database name depends on property ``instance.name``.

Realms
------

If you have only one database, you do not want to set property ``datasourceName`` on each sender and each listener that accesses it. You can give a list of attribute/value combinations a so-called "realm name". This is what you do with the ``<jmsRealm>`` element. Consider the following line again:

.. code-block:: XML

   <jmsRealm datasourceName="jdbc/myapp" realmName="jdbc"/>

This line simply gives the attribute/value combination ``datasourceName="jdbc/myapp"`` the realm name ``jdbc``. In the ``<SenderPipe>`` tag cited earlier, you saw the attribute ``jmsRealm="jdbc"``. This means: apply all attribute/value combinations combined in the definition of realm name ``jdbc``. This is another way of setting property ``datasourceName``. This finishes the explanation of the ``<jmsRealm>`` tag.

.. NOTE::

   The name of tag ``<jmsRealm>`` is misleading. It suggests that realms are related to the Java Message Service. It is true that realms can be applied to listeners and senders that access the Java Message Service, but their application is much more general as explained. A better name for the tag would be just ``<realm>``.

Initial data
------------

The Frank!Framework uses Liquibase to populate your database with tables and with initial data. In your Frank config you include a file ``DatabaseChangelog.xml`` that defines what tables you want to create and what initial data you want. You can provide this information in SQL statements or in pure XML, the latter being database agnostic. See https://www.liquibase.org/ to learn how to write ``DatabaseChangelog.xml``. You saw an example in chapter :ref:`gettingStarted`, section :ref:`databaseInitialization`. Your initial data is split into change sets, each wrapped within XML element ``<changeSet>``.

Liquibase allows multiple deployments of your Frank to share the same database. Liquibase maintains database tables to remember what change sets have been processed. If one instance applies a change set, the others will see that the change set has been applied. Each instance only applis change sets not yet processed, which causes each change set to be executed only once. This approach only works if change sets are never altered. When you update your Frank config, please do not change existing change sets but append new ones.

.. NOTE::

   If you want to undo initialization by Liquibase, you can execute SQL query ``DROP ALL OBJECTS`` in the JDBC | Execute Query screen. This screen allows you to select the database by its realm ("JMS Realm").

The Frank!Framework only does database initialization when property ``jdbc.migrator.active`` is true. Remember from section :ref:`properties` that you can set this property in your Frank config, but that it can be overruled by the system administrator when she sets this property as a system property.

If you have multiple databases, what database is selected? By default, it is the database with JNDI name ``jdbc/${instance.name.lc}``. You can override this by setting property ``jdbc.migrator.dataSource``. Each configuration can select one database for setting initial data. If you have multiple databases that each have their own initial data, then do this by using multiple configurations.

Conclusion
----------

If you have only one database, please give it JNDI name ``jdbc/${instance.name.lc}`` and make a ``<jmsRealm>`` for it, like you did in chapter :ref:`gettingStarted`. If you have another database, you can reference it by another JNDI name, leaving it to the system administrator to link that name to a concrete database. You cannot use Tomcat4Frank or Docker4Frank with multiple databases. You can wrap the other database in a ``<jmsRealm>`` to make referencing it easier. If you have multiple databases that each have their own initial data, please have each of them managed by its own Frank config. Each Frank config then has its own ``DatabaseChangelog.xml`` file. Each Frank config sets property ``jdbc.migrator.dataSource`` to the JNDI name of the database it manages.
