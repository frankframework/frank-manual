.. _ladybugExtendTable:

Extend the test reports table
=============================

When you enter Ladybug, you are in tab "Debug". To the top, this tab shows a table with all Ladybug reports. You saw this table many times when you did the preceeding subsections. You use this table to quickly find a (not yet captured) test report. Some want more information in this table, because they repeatedly run the same adapter. To distinguish between these runs, they want an extra column with data extracted from the test report.

A solution has been developed for this need, but it has a different nature than the Ladybug functions presented in earlier subsections. This option is not provided through a well-developed user interface, but requires the user to hack the Frank!Framework. This way, it was possible to provide a solution quickly. When more customers want this option, a user interface will be provided.

There are two sub-subsections. Sub-subsection :ref:`ladybugExtendTableHowto` just tells you how to do the job, without bothering you with knowledge about the implementation of the Frank!Framework. Sub-subsection :ref:`ladybugExtendTableBackground` gives some background information.

.. _ladybugExtendTableHowto:

How to do it
------------

Please do the following:

#. Create file ``Frank2Manual/classes/springIbisTestToolCustom.xml`` with the following contents:

   .. literalinclude:: ../../../../../srcSteps/ladybugInstance/v500/classes/springIbisTestToolCustom.xml
      :language: xml
      :emphasize-lines: 14, 15, 16, 17, 18, 19, 36

   When you want to add your own column in your own project, you can use the above XML and then edit the highlighted lines.
#. Create file ``Frank2Manual/classes/DeploymentSpecifics.properties`` with the following contents:

   .. literalinclude:: ../../../../../srcSteps/ladybugInstance/v500/classes/DeploymentSpecifics.properties
      :language: none

   If this file already exists on your Frank!Framework instance, then you can append the shown line.
#. Start the Frank!Runner and go to Ladybug. Your screen should look like shown below.

   .. image:: extendTableResult.jpg

You see that an extra column with label ``Customer`` is added. Its data is obtained by applying the following XPath expression: ``/message/customer``. This XPath is applied to the test report the line is about.

As it stands, the XPath expression is applied to every input message supplied to your adapters. You can also extract data from the output messages. If you want this, uncomment the line ``<!-- <property name="extractFrom" value="first"/> -->`` and change the property value to ``last``. If you want to query both inputs and outputs you can apply the value ``all``.

.. _ladybugExtendTableBackground:

Background information
----------------------

To understand how this hack works, you have to know that the Frank!Framework is a Java application developed using the Spring framework. The Spring framework is used to instantiate Java objects from configuration data. These objects are referred to as Java beans. The Spring framework assigns a name to each Java bean. The Spring framework allows the configuration data to be supplied through XML files.

Ladybug is implemented by Java objects, some of them being Java beans that are instantiated by the Spring framework. Many of these beans are by default configured through file ``springIbisTestTool.xml``, which is part of the Frank!Framework. When you want to change Ladybug, you want to provide your own version of this file. This is achieved by setting the property ``ibistesttool.custom=Custom``, as you do in ``DeploymentSpecifics.properties``. This line tells the Frank!Framework to read ``springIbisTestToolCustom.xml`` instead of ``springIbisTestTool.xml``. You added ``springIbisTestToolCustom.xml`` to the ``classes`` folder.

You do not want to change Ladybug completely. Many Java beans still have to be created like is defined in ``springIbisTestTool.xml``. This is achieved by the line ``<import resource="springIbisTestTool.xml"/>``. To add a column, you have to change the definitions of the following beans: ``metadataExtractor`` and ``metadataNames``. In ``springIbisTestToolCustom.xml``, you see the new definitions of these beans. These definitions specify what other objects have to be linked to the "metadataExtractor" and the "metadataNames" beans. Your new column is defined in two additional Java beans that are linked to the two mentioned beans. You see this in the highlighted lines of ``springIbisTestToolCustom.xml``.

.. WARNING::

   In case Ladybug needs data from the database, set ``jdbc.migrator.active=true`` in a properties file in the ``classes`` directory or in ``src/main/resources`` for a Maven project. Ladybug cannot read data that is specific to a configuration. See also subsection :ref:`testingLadybugStorages`.
