.. _databaseInitialization:

Database Initialization
=======================

The Frank!Framework can take care of database initialization. 
Database initialization should happen when an enterprise application starts
for the first time. When an enterprise application is restarted later,
database initialization should be omitted because data in the
database should be persistent.

The Frank!Framework internally uses Liquibase, see http://www.liquibase.org/,
to initialize the database. Please switch on Liquebase as follows:

#. Add the following line to ``projects/gettingStarted/classes/DeploymentSpecifics.properties``: ::

    jdbc.migrator.active=true

#. Restart the Frank!Framework.

We illustrate database initialization here for H2 databases, because this database is embedded within the Frank!Framework and does not
require a process external to it. More information about databases is available in section :ref:`advancedDevelopmentDatabase`. Liquibase expects a so-called changelog, an XML file that defines the data model and the initial data.

3. Please create file ``projects/gettingStarted/configurations/NewHorizons/DatabaseChangelog.xml`` and add XML to initialize the database described in the previous section :ref:`horizonsInterfaces`. Here is the XML to add:

   .. literalinclude:: ../../../src/gettingStarted/configurations/NewHorizons/DatabaseChangelog.xml
      :language: xml

For clarity we chose to use SQL statements in the changelog. As a consequence, it is not database independent as would
be the case if it were pure XML. The shown changelog is specific for H2 databases.

.. NOTE ::

  If you are working on the changelog within your own project,
  you will probably make some errors. In this situation, you
  want to remove all database tables to rerun all change sets within
  your changelog.

  You can do this as follows. Start the Frank!Framework and browse
  to http://localhost/ibis/iaf/gui. On the left-hand menu
  select "JDBC" and then "Execute Query". Issue the following
  SQL: "DROP ALL OBJECTS". Finally restart the Frank!Framework.
