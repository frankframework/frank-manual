Questions and Answers
=====================

This chapter lists questions and answers about the Frank!Framework.

Adapter status page ManageDatabase error
----------------------------------------

**Question:** Why do I see an error in adapter ManageDatabase, saying that there is no datasource? See below:

.. image:: manageDatabaseErrorInitializingPipeline.jpg

**Answer:** You did not add this adapter yourself. This adapter is part of the Frank!Framework. You see here that the Frank!Framework fails to start. This happens when your file names are lowercase. For example, when your files are named ``deploymentspecifics.properties`` and ``configuration.xml`` instead of ``DeploymentSpecifics.properties`` and ``Configuration.xml``, then this error occurs. Correct your file names to fix the issue.

On startup, syntax error in SQL
-------------------------------

**Question:** In the output of the Frank!Runner I see a Java stacktrace of a JdbcSQLSyntaxErrorException, as shown below:

.. code-block:: none

   Caused by: org.h2.jdbc.JdbcSQLSyntaxErrorException: Syntax error in SQL statement "CREATE TABLE VISIT (
                   BOOKINGID INT NOT NULL,
                   SEQ INT NOT NULL,
                   HOSTID INT NOT NULL,
                   PRODUCTID INT NOT NULL,
                   STARTDATE DATE NOT NULL,
                   ENDDATE DATE NOT NULL,
                   PRICE DECIMAL NOT NULL,
                   PRIMARY KEY (BOOKINGID, SEQ)
               )
               ALTER[*] TABLE VISIT ADD FOREIGN KEY (BOOKINGID) REFERENCES BOOKING(ID)"; SQL statement:
   CREATE TABLE visit (
                   bookingId INT NOT NULL,
                   seq INT NOT NULL,
                   hostId INT NOT NULL,
                   productId INT NOT NULL,
                   startDate date NOT NULL,
                   endDate date NOT NULL,
                   price DECIMAL NOT NULL,
                   PRIMARY KEY (bookingId, seq)
               )
               ALTER TABLE visit ADD FOREIGN KEY (bookingId) REFERENCES booking(id) [42000-200]
           at org.h2.message.DbException.getJdbcSQLException(DbException.java:453)
           at org.h2.message.DbException.getJdbcSQLException(DbException.java:429)
           at org.h2.message.DbException.get(DbException.java:205)
           at org.h2.message.DbException.get(DbException.java:181)
           at org.h2.message.DbException.getSyntaxError(DbException.java:229)
           at org.h2.command.Parser.getSyntaxError(Parser.java:1051)
           at org.h2.command.Parser.prepareCommand(Parser.java:741)
           at org.h2.engine.Session.prepareLocal(Session.java:657)
           at org.h2.engine.Session.prepareCommand(Session.java:595)
           at org.h2.jdbc.JdbcConnection.prepareCommand(JdbcConnection.java:1235)
           at org.h2.jdbc.JdbcStatement.executeInternal(JdbcStatement.java:212)
           at org.h2.jdbc.JdbcStatement.execute(JdbcStatement.java:201)
           at liquibase.executor.jvm.JdbcExecutor$ExecuteStatementCallback.doInStatement(JdbcExecutor.java:307)
           ... 35 more

What is wrong?

**Answer:** The SQL statements shown are in ``DatabaseChangelog.xml``. The error says that these statements have syntax errors. The error is in the following snippet of ``DatabaseChangelog.xml``:

.. code-block:: XML

   <changeSet id="2" author="martijn">
       <sql>
           CREATE TABLE visit (
               bookingId INT NOT NULL,
               seq INT NOT NULL,
               hostId INT NOT NULL,
               productId INT NOT NULL,
               startDate date NOT NULL,
               endDate date NOT NULL,
               price DECIMAL NOT NULL,
               PRIMARY KEY (bookingId, seq)
           )
           ALTER TABLE visit ADD FOREIGN KEY (bookingId) REFERENCES booking(id)
       </sql>
   </changeSet>

All SQL within a changeset is interpreted by the database engine. The shown example uses a H2 database, so the SQL dialect of H2 databases is being applied. A ``;`` is needed between the ``CREATE TABLE`` and the ``ALTER TABLE`` statements, right after the closing ``)`` of the ``CREATE TABLE`` statement.

You can see which ``<changeSet>`` has the SQL syntax error. Higher-up in the Java stack trace, there was a line ``Migration failed for change set DatabaseChangelog.xml::2::martijn:``. Here you see it was the change set with id  ``2``.

Passing XML parameter to XSLT
-----------------------------

**Question:** I have an XSLT transformation that expects a parameter of type XML. When I pass the parameter from my Frank config, it is interpreted as a string. How can I fix this?

**Answer:** To execute an XSLT transformation with parameters, you use an ``<XsltPipe>`` with ``<Param>`` tags. Within a ``<Param>`` tag, you can provide the value that will be passed to the XSLT transformation. For passing strings, this is all you have to know; you can find the details in the Frank!Doc. If your value is XML, you need one more trick. Within your ``<Param>`` tag, set ``type="domdoc"``. Here is an example:

.. code-block:: XML

   <XsltPipe
       name="transformHermesMessage"
       styleSheetName="printBridge.xsl"
       omitXmlDeclaration="true"
       xsltVersion="2"
       getInputFromSessionKey="originalMessage">
     <Param
         name="statistics"
         sessionKey="statistics"
         type="domdoc"/>
     <Forward name="success" path="sendToPrintBridge"/>
   </XsltPipe>

Inserting from XPath expression, default value null
---------------------------------------------------

**Question:** How to insert a table row from an XPath expression while using default value ``null``?

**Answer:** You can use a FixedQuerySender to insert rows in a table. The values to insert are given in ``<Param>`` elements. The value to insert can be given by an XPath expression, for example ``<Param name="myParam" xpathExpression="/BIJKANT/PK/PK_NUMMER"/>``. You cannot use the ``defaultValue`` attribute to use a default value of ``null``, but you do not need to. When you omit the ``defaultValue`` attribute, you will have ``null`` when your XPath expression does not find anything.

Logging
-------

Frank developers can add extra logging using to their configuration using the ``<LogSender>``. Log messages always have a category, which you can set using attribute ``logCategory``. When you do not set the log category, the sender's name appears in the log as the log category. By default, logging written by ``<LogSender>`` appears in log file ``${instance.name.lc}.log``. The system administrator who deploys the Frank application may override this however, see :ref:`deploymentCustomLogging`.

XSLT Testing with Larva
-----------------------

**Question:** How to test XSLT stylesheets with Larva?

**Answer:** Here is an example:

.. code-block:: none

   scenario.description = adapt input ldap insert into functionally expired passwords
   
   xpl.MaakLdapInput.className   = nl.nn.adapterframework.testtool.XsltProviderListener
   xpl.MaakLdapInput.filename    = ../../../JavaSource/CheckPasswordFunctionalExpired/xsl/AdaptInputLdapInsertIntoPasswordFunctionalExpired.xsl

   step1.xpl.MaakLdapInput.read              = scenario01/step1.xml
   step1.xpl.MaakLdapInput.read.param1.name  = userType
   step1.xpl.MaakLdapInput.read.param1.value = WN
   step2.xpl.MaakLdapInput.write             = scenario01/step2.xml

No adapter restart needed after editing Larva tests
---------------------------------------------------

**Question:** I edited my Larva tests. Do I have to restart the Frank!Runner or reload my configurations?

**Answer:** No. When you edit your Larva tests, you can run them immediately and the Frank!Framework will use the updated files.

Parameters in Larva tests
-------------------------

**Question:** How to pass parameters to Larva services?

**Answer:** You can pass a parameter by referencing the value from a file, or you can put the value directly in your scenario. Here is an example of the latter:

.. code-block:: none

   adapter.TitanGET.param1.name=uniqueIdentifier
   adapter.TitanGET.param1.value=abc

​And here is an example of fetching the value from a file:

.. code-block:: none

   adapter.TitanGET.param1.name=uniqueIdentifier
   adapter.TitanGET.param1.valuefile=01/input.xml

Transaction attribute on receiver or pipeline?
----------------------------------------------

**Question:** Both the ``<Receiver>`` and the ``<Pipeline>`` tag has attribute ``transactionAttribute``. Which element should you choose?

**Answer:** It really depends on what you want to achieve! The purpose of a transaction is that all data modifications should succeed or none should happen. The ``<Receiver>`` does part of the work such as accepting a message from a queue. Its responsibility is to safely read and processes the message. Depending on additional elements on the ``<Receiver>`` such as an ``<ErrorStorage>`` it also adds a fail-safe mechanism if the message cannot be processed at this time. The ``<Pipeline>`` processes the information, and can be fed by multiple receivers. Typically, some receivers support transactions and some do not. If a receivers that supports transactions has the ``transactionAttribute``, the pipeline after the receiver will inherit the transaction.

.. WARNING::

   If a receiver does not support transactions, regardless of the ``transactionAttribute``, and there is no ``transactionAttribute`` on the pipeline, the pipeline does not inherit a transaction!

Load multiple configs at once
-----------------------------

**Question:** I have about 20 different jars that I want to upload. How can I use the "Multiple Configurations" checkbox in the "Upload Configuration" screen (see below) to upload them all at once?

.. image:: configurationUpload.jpg

**Answer:** Pack all your configuration jar files into a single .zip, check the box and upload the zip file containing all the configurations you would like to upload.

Property configurations.<configname>.parentConfig
-------------------------------------------------

**Question:** What  is the use of the property configurations.<configname>.parentConfig exactly?

**Answer:** It changes the order in which files and properties are loaded. For every file or property the framework has to load, it will first look it up as a global setting (eq. classpath resource or system property) then in the local configuration, then (if specified) the parent configuration, and lastly the war (``src/main/resources``). Class loading is described in subsection :ref:`propertiesInitialization`.

Authorization to turn on Ladybug
--------------------------------

**Question:** Which role do you need at least to turn on Ladybug?

**Answer:** IbisDataAdmin, IbisAdmin or IbisTester. See also :ref:`deploymentOverviewSecurityRoles`.

Flow diagram images
-------------------

**Question:** The Frank!Console shows flow diagrams of Frank configurations. Where can I find image files of these diagrams?
 
**Answer:** There is a property ``flow.adapter.dir``. It holds the directory where the diagrams are saved as images. The Frank!Framework sets this property automatically. You can find the value of this property by choosing "Environment Variables" from the main menu of the Frank!Console.

XmlSwitchPipe exception "Premature end of file"
-----------------------------------------------

**Question:** Why does ``XmlSwitchPipe`` throw "Premature end of file"?

**Answer:** As the pipe name indicates, it expects the input message to be valid XML. When the input is not in XML format or if the XML is invalid, this error is thrown. You have to configure an XSLT stylesheet that is applied to the incoming message. The pipe uses the result of the transformation as the forward to follow. See also GitHub issue https://github.com/frankframework/frankframework/issues/1020.

**Additional:** But with the attribute ``sessionKey``, the XmlSwitchPipe can work without an XSLT transformation, the attribute value being used directly as the forward to follow.

Test ApiListener with authentication (without Larva)
----------------------------------------------------

**Question:** How can I locally test an ApiListener with authentication (without Larva)?

**Answer:** In the configuration, make the authenticationMethod a configurable property (for example ``${​​​​api.authMethod}​​​​​​​​​​​``.

Assuming you've set these exact properties in the DeploymentSpecifics.properties, you can 'disable' its behaviour in the StageSpecifics_LOC.properties by setting:

.. code-block:: none 

   api.authMethod=NONE
   servlet.ApiListenerServlet.securityroles=
 
Liquibase logging
-----------------

**Question:** Where can I find why Liquibase validation failed?

**Answer:** There will be a warning on the Frank!Console when Liquibase validation fails. From version 7.6 onwards, this warning includes the reason why validation failed. For older versions, no reason will be in that warning. You can also find the reason in the regular logfile when the log level is WARN or lower. Setting the log level is described here: https://frank-manual.readthedocs.io/en/latest/operator/diskUsage.html?highlight=log%20level#disk-usage. 

Filling adapter response with session key
-----------------------------------------

**Question:** My adapter stores some result in a session key. How can I change my adapter such that it produces a response message filled with the value of the session key?

**Answer:** Use the ``EchoPipe``. It is described in the Frank!Doc, see https://frank-manual.readthedocs.io/en/latest/gettingStarted/configurationSyntaxChecking.html.

Reading auto-generated keys when inserting into database
--------------------------------------------------------

**Question:** I am inserting into or updating a database table that auto-generates values, which may be primary keys or the results of database functions. How can I get these values in my adapter?

**Answer:** You can use a ``FixedQuerySender`` with an "INSERT" or "UPDATE" query. Fill the attribute ``columnsReturned`` of the ``FixedQuerySender`` with the columns for which you want to have the values. This is a comma-separated list of column names. See the Frank!Doc for more details.

.. WARNING::

   This feature of the Frank!Framework does not work for all database drivers and/or versions. See issue https://github.com/frankframework/frankframework/issues/1468.

By default, the value is wrapped into an XML message. If you just want a scalar, you can set the ``scalar`` attribute of the ``FixedQuerySender`` to ``true``.

Iterating over CSV file
-----------------------

**Question:** How to iterate over a .csv file?

**Answer:** Here is an example to download: :download:`Frank config <../downloads/configurations/forFrankConsole.zip>`. This example applies a ``BatchFileTransformerPipe``. This pipe may be more complicated to use then needed. Since version 7.6 you can use a ``CsvParserPipe``.

Liquibase script does not seem to work with H2 in-memory database
-----------------------------------------------------------------

**Question:** I have a Frank config that uses an in-memory H2 database. When I load it into the Frank!Framework I see that there is no IBISSTORE database table, even though the catalina log shows correct execution of Liquibase. If I change the URL to have a file H2 database, the IBISSTORE table is created as it should. How is this possible?

**Answer:** You need to use the correct ``type`` and ``driverClassName`` attributes in the ``<Resource>`` element of ``context.xml``:

.. code-block:: xml

   <Resource 
   name="jdbc/ibis4pt"
   type="javax.sql.DataSource"
   driverClassName="org.h2.Driver"
   url="jdbc:h2:mem:ibis4pt"
   /> 

Watching the startup of the F!F
-------------------------------

**Question:** I am starting my configuration with the F!F running on Apache Tomcat. How can I see whether my application is ready to receive HTTP requests?

**Answer:** You can open a browser and navigate to the main URL of the Frank!Framework, typically ``http://localhost`` in a development environment. If you see the Frank!Framework on this URL, it is done with its startup. Alternatively, you can look at the console output. When you work with the Frank!Runner, take care to look at the console window that is created during boot, not the original command prompt from which you start the Frank!Runner. You see many messages passing by in the console. When you see ``INFO [main] org.apache.catalina.core.ApplicationContext.log Starting IbisContext``, Apache Tomcat has loaded the Frank!Framework and the Frank!Framework's startup code starts executing. When you see ``INFO [main] org.apache.catalina.startup.Catalina.start Server startup in [xxx] milliseconds``, the Frank!Framework should be ready to receive HTTP requests.

ApiListener and curl
--------------------

**Question:** I have a configuration with an ``ApiListener`` to receive HTTP POST requests. I try to test it using ``curl --request POST --url http://localhost/api/ingestDocument --data 'C:\Users\martijn\git\ladybug-with-manual-tests\manual-test\configurations\Conclusion\exampleInputs\valid'``. This produces an unexpected result. When I look in Ladybug, I see that there is a session key with name ``C:\Users\martijn\git\ladybug-with-manual-tests\manual-test\configurations\Conclusion\exampleInputs\valid`` that has no value. When I look at the pipeline's input message, I see this: ``>> Captured stream was closed without being read.``. What is going wrong?

**Answer:** When you use curl like this, it automatically adds a header ``Content-Type: application/x-www-form-urlencoded``. You can check this by adding the ``--verbose`` option to the curl command. You can suppress this header by adding ``-H "Content-Type:"``. The following command thus works:

.. code-block:: none

   curl -H "Content-Type:" --request POST --url http://localhost/api/ingestDocument --data 'C:\Users\martijn\git\ladybug-with-manual-tests\manual-test\configurations\Conclusion\exampleInputs\valid'

Alternatively, you can use another tool to test your interface, for example `Bruno <https://www.usebruno.com/>`_.

Having adapters that are stopped by default
-------------------------------------------

**Question:** I have some adapters that I want to be stopped by default. I could stop the adapters in the Frank!Console, but then they are started again when I restart the Frank!Framework. This is not what I want. Is there a property that causes adapters to be stopped unless I start them in the Frank!Console?

**Answer:** Yes, use attribute ``autoStart`` of the ``<Adapter>`` element. For example:

.. code-block:: xml

   <Configuration
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:noNamespaceSchemaLocation="../FrankConfig.xsd"
   >
       <Adapter name="Adapter1a" autoStart="false">
       <Receiver name="Receiver1a">
           ...
       </Receiver>
       ...
   </Configuration>

I changed an example adapter of the Frank!Runner like this. When I started the Frank!Runner, the adapter was in state stopped. I was able to restart it by hand in the Adapter Status page as was intended.

SECURITY RISK: All path parameters and query parameters will be copied into the session
---------------------------------------------------------------------------------------

**Question:** I am seeing a console warning with the test: "SECURITY RISK: All path parameters and query parameters will be copied into the session". What does it mean and what can I do with it?

**Answer:** HTTP requests can have two kinds of parameters. Query parameters appear in the URL after the ``?`` character. Form data parameters are name/value pairs above the body of a POST HTTP message. It is a security risk if the Frank!Framework uses all supplied parameters. A malicious caller would have options to try hacking by adding unexpected parameters -- be it query parameters or form data parameters. You have a few options here. First, it can be that your Frank application needs all parameters the caller may provide. In that case you can suppress the warning. Search the warning in the logfile to find instructions for suppressing. Second, it can be that your adapter should not use any parameters. Then set attribute ``allowAllParams="false"`` on your ``<ApiListener>``. Third, it can be that you know what parameters you want to use. Then list them in attribute ``allowedParameters``. In this case you do not have to set ``allowAllParams`` -- the Frank!Framework changes the default value automatically.
