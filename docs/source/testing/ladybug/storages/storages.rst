.. _testingLadybugStorages:

Ladybug storages and the database
=================================

Ladybug has to store reports persistently. It allows the user to choose whether reports are stored on the local file system, in the database, or another way. From Frank!Framework version 8.1 onwards, the default is to store reports in the database. If Ladybug stores reports in a database, it uses a table named ``LADYBUG``. As a Frank!Developer, you need to consider a few things to make this work or to override this behavior.

Properties
----------

Please consider the following properties:

.. csv-table::
   :widths: auto
   :header: Property, Explanation

   ``ladybug.jdbc.migrator.active``, "Boolean property that determines whether table ``LADYBUG`` should be created. The default value is ``${jdbc.migrator.active}``. The default behavior is thus to treat the creation of table ``LADYBUG`` like the other database initializations that are or are not performed by the Frank!Framework (e.g. creating table ``IBISSTORE``)."
   ``ladybug.jdbc.datasource``, "The database name that points to the database in which Ladybug should write reports. No default value. If empty, Ladybug writes reports to the local file system."

These properties have to be environment properties or application properties, see :ref:`propertiesDeploymentEnvironment`.

.. WARNING::

   Please consider the following before deciding not to use the database for Ladybug reports. The local filesystem is not a secure storage in a serverless environment because VMs and docker containers are often shut down and recreated. 

.. WARNING::

   In version 9.1.0-SNAPSHOT of the Frank!Framework, there is no default value for ``ladybug.jdbc.datasource``. It is NOT the case that default database were used when ``ladybug.jdbc.datasource`` would not be set. In some 8.x versions of the FF!, this behavior may be different.

.. NOTE::

   See :ref:`deployingDatabase` for information on how to configure database access in general.

Extra columns and the database
------------------------------
 
If you add columns to the table of Ladybug reports as explained in :ref:`ladybugExtendTable`, you have to add these columns to table ``LADYBUG`` in case reports are stored in the database. This can be done using Liquibase. Ladybug itself uses Liquibase to create table ``LADYBUG`` in the first place. It does so using a file ``DatabaseChangelog.xml`` that is part of Ladybug. To change table ``LADYBUG``, add file ``ladybug/DatabaseChangelog_Custom.xml`` to the classpath (directory ``classes`` or ``src/main/resources`` in your project). File ``DatabaseChangelog_Custom.xml`` is executed along with the internal ``DatabaseChangelog.xml``. Here is an example of ``ladybug/DatabaseChangelog_Custom.xml``:

.. code-block:: xml

   ...
   <changeSet id="LadybugCustom:1" author="Jaco de Groot">
       <comment>Add column EXTRACOLUMN</comment>
       <addColumn tableName="LADYBUG">
           <column name="EXTRACOLUMN" type="java.sql.Types.VARCHAR(255)"/>
       </addColumn>
   </changeSet>
   ...
