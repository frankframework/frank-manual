.. _databaseInitialization:

Database Initialization
=======================

Introduction
------------

We continue our case study about the imaginary firm NewHorizons, see :ref:`newHorizons` and :ref:`horizonsInterfaces`. In section :ref:`newHorizons` you started development by creating the file ``franks/Frank2Manual/configurations/NewHorizons/Configuration.xml``. You will extend this configuration by adding files to your directory ``NewHorizons``.

Enable Liquibase
----------------

The Frank!Framework can take care of database initialization. 
Database initialization should happen when an enterprise application starts
for the first time. When an enterprise application is restarted later,
database initialization should be omitted because data in the
database should be persistent.

The Frank!Framework internally uses Liquibase, see http://www.liquibase.org/,
to initialize the database. Please switch on Liquibase as follows:

#. Add file ``StageSpecifics_LOC.properties`` and give it the following contents:

   .. literalinclude:: ../../../srcSteps/NewHorizons/v410/configurations/NewHorizons/StageSpecifics_LOC.properties
      :language: none

   .. NOTE::

      You can use many different property files to configure properties. When you choose ``StageSpecifics_LOC.properties``, your settings will not be applied when your configuration is deployed on production. If you would choose ``DeploymentSpecifics.properties``, you settings would also be used in production, provided they are not overruled. More details are in section :ref:`properties`, but before reading that section please finish this chapter first.

We illustrate database initialization here for H2 databases, because this database is embedded within the Frank!Framework and does not
require a process external to it. More information about databases is available in section :ref:`advancedDevelopmentDatabase`. Liquibase expects a so-called changelog, an XML file that defines the data model and the initial data.

2. Please create file ``DatabaseChangelog.xml`` and add XML to initialize the database described in the previous section :ref:`horizonsInterfaces`. Here is the XML to add:

   .. literalinclude:: ../../../srcSteps/NewHorizons/v410/configurations/NewHorizons/DatabaseChangelog.xml
      :language: xml

For clarity we chose to use SQL statements in the changelog. As a consequence, it is not database independent as would
be the case if it were pure XML. The shown changelog is specific for H2 databases.

Test your database
------------------

You can test your work by querying the tables you created, "booking" and "visit". Please continue as follows:

3. Click "JDBC" (number 1 in the figure below). This link will expand.

   .. image:: jdbcExecuteQuery.jpg

#. Click "Execute Query" (number 2). The following screen appears:

   .. image:: jdbcExecuteQueryNoRowsYet.jpg

#. You see you are in the JDBC Execute Query screen (number 1). Select "Datasource" "jdbc/frank2manual" (number 2).

   .. NOTE::

      For more information, see section :ref:`advancedDevelopmentDatabase`.

#. You can choose to have comma-separated (csv) output instead of XML (number 3).
#. Enter query ``SELECT * FROM booking`` (number 4).
#. Press "Send" (number 5). You will see the result ``"ID","TRAVELERID","PRICE","FEE"`` (number 6). You have verified that the "booking" table exists.
#. Verify that table "visit" exists by executing the query ``SELECT * FROM visit``. Check that the result of this query is ``"BOOKINGID","SEQ","HOSTID","PRODUCTID","STARTDATE","ENDDATE","PRICE"``.

.. NOTE::

   Please do not modify existing change sets. When you have new requirements for initial data, please add new change sets. On start-up, the Frank!Framework checks which change sets have been executed and which change sets are new. Only new change sets are executed. This only works when existing change sets never change.
 
.. NOTE::

   If you are developing on the changelog within your own project, you will probably make some errors. In this situation, you want to remove all database tables to rerun all change sets within your changelog. You can do this using the query ``DROP ALL OBJECTS``. After running it, restart the Frank!Framework.

Solution
--------

If you did not get your database working, you can :download:`download <../downloads/configurations/NewHorizonsDatabase.zip>` the solution for the work you did so far. Before using these files, please put them in the directory structure explained earlier.
