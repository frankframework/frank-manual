Database Initialization
=======================

The frank!framework can take care of database initialization. Database
initialization should happen when an enterprise application starts
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
change log:

.. literalinclude:: ../../classes/DatabaseChangelog.xml
   :language: xml

For clarity we chose to use SQL statements in the changelog.
As a consequence, it is not database independent is would
be the case for pure XML changelogs. The shown changelog
is specific for H2 databases.
