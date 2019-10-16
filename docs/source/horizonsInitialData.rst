Database Initialization
=======================

The frank!framework can take care of database initialization. In
section :ref:`installationLinux`, we introduced the file
"<project directory>/properties.sh". We suggested the
following line there: ::

  DATABASE=h2

This line causes the frank!framework to work with an H2 database,
which is an in-memory database. No applications external to the
frank!framework are needed to run the database.

Database initialization should happen when an enterprise application starts
for the first time. When an enterprise application is restarted later,
database initialization should be omitted because data in the
database should be persistent.

The frank!framework internally uses LiquiBase, see http://www.liquibase.org/,
to initialize the database. LiquiBase expects a so-called
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
