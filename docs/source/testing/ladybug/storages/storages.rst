.. _testingLadybugStorages:

Storages
========

Ladybug has to store reports persistently. It allows the user to choose whether reports are stored on the local file system, in the database, or another way. From Frank!Framework version 8.1 onwards, the default is to store reports in the database. This can only be done if table LADYBUG exists. The Frank!Framework can create this table but only does so if ``jdbc.migrator.active=true`` has been set in the ``classes`` directory (or ``src/main/resources`` for a Maven-lik project).

If you do not want to use the database storage, you can disable it by setting property ``ladybug.jdbc.datasource=`` (without a vaile after the ``=`` sign) in ``src/main/resources`` (or ``classes``). This tells Ladybug that is not allowed to access a datasource and hence it cannot access the database. If you want more fine-grained control on the storage used, configure it using ``springIbisTestToolCustom.xml`` as explained in :ref:`ladybugExtendTable`.

You can add extra columns to the LADYBUG database table by adding file ``src/main/resources/ladybug/DatabaseChangelog.xml``. That file is executed along with the internal ``DatabaseChangelog.xml`` that is part of Ladybug itself. Here is an example of ``src/main/resources/ladybug/DatabaseChangelog.xml``:

.. code-block:: xml

   <changeSet id="LadybugCustom:1" author="Jaco de Groot">
       <comment>Add column EXTRACOLUMN</comment>
       <addColumn tableName="LADYBUG">
           <column name="EXTRACOLUMN" type="java.sql.Types.VARCHAR(255)"/>
       </addColumn>
   </changeSet>

