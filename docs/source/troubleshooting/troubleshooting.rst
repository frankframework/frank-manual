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
