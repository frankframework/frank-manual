Database Initialization
=======================

The frank!framework can take care of database initialization. 
Database initialization should happen when an enterprise application starts
for the first time. When an enterprise application is restarted later,
database initialization should be omitted because data in the
database should be persistent.

The frank!framework internally uses LiquiBase, see http://www.liquibase.org/,
to initialize the database. To use LiqueBase, it has to be switched on. There are multiple ways to
to this. One possibility is as follows:

* Go to the "classes" directory within your project.
* Create a file DeploymentSpecifics.properties there if it does not exist.
* Ensure this file has the following line: ::

    jdbc.migrator.active=true

* Restart the frank!framework.

We illustrate database initialization here for H2 databases, because
this database is embedded within the frank!framework and does not
require a process external to it. Please see https://github.com/ibissource/docker4ibis/
to see how to select a database.

LiquiBase expects a so-called
changelog, an XML file that defines the data model and the initial data.
The frank!framework expects it in the file
"<project directory>/classes/DatabaseChangelog.xml".
The New Horizons database described in the previous section
:ref:`horizonsInterfaces` is initialized with the following
changelog:

.. literalinclude:: ../../classes/DatabaseChangelog.xml
   :language: xml

For clarity we chose to use SQL statements in the changelog.
As a consequence, it is not database independent as would
be the case if it were pure XML. The shown changelog
is specific for H2 databases.

.. NOTE ::

  If you are working on the changelog within your own project,
  you will probably make some errors. In this situation, you
  want to remove all database tables to rerun all change sets within
  your changelog.

  You can do this as follows. Start the frank!framework and browse
  to http://localhost/docker/iaf/gui. On the left-hand menu
  select "JDBC" and then "Execute Query". Issue the following
  SQL: "DROP ALL OBJECTS". Finally restart the frank!framework.
