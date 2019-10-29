.. _deploymentProperties:

Properties 
==========

Properties are key/value pairs, both the key and the value being strings. Keys
are restricted to consist of letters separated by dots (".") and they
are case insensitive. There are
different ways to set properties, which is the subject of section
:ref:`deploymentConfigureProperties`. This section focuses on the impact of
setting properties. First, any key can be used as a property name and its value can be
used within a Frank. Second, some 
properties also change the way the frank!framework operates.

Properties in Frank configurations
----------------------------------

Any key, which is a case-insensitive string of letters and dots, can be used as a property name.
Consider for example the following adapter:

.. code-block:: XML

   <Adapter name="AccessProperties">
     <Receiver name="receiverAccessProperties">
       <JavaListener name="listenerAccessProperties" />
     </Receiver>
     <Pipeline firstPipe="accessProperties">
       <Exit state="success" path="Exit" />
       <FixedResultPipe name="accessProperties"
           returnString="From stage ${otap.stage}, I say ${my.text}" >
         <Forward name="success" path="Exit" />
       </FixedResultPipe>
     </Pipeline>
   </Adapter>

.. highlight:: none

The ``<FixedResultPipe>`` outputs a fixed string that is configured
in attribute ``returnString``. The value of this XML attribute
contains the substrings ``${otap.stage}`` and ``${my.text}``.
These substrings reference the values associated with keys "otap.stage"
and "my.text". The way to assign values to properties is described in section
:ref:`deploymentConfigureProperties`. A possible output of this pipe is: ::

  From stage LOC, I say My text is Hello

Property values can be viewed in the console of the frank!framework. On
the menu on the left, go to "Environment Variables":

.. image:: viewProperties.jpg

Note that property "my.text" has no special meaning for the
frank!framework. Setting it has no other impact than changing
the output from this adapter (or possible other adapters
that reference it). This is different for property "otap.stage"
as is explained in the next subsection.

Configuration properties of the frank!framework
-----------------------------------------------

Here follows a list of properties with a predefined meaning:

application.server.type
  The application server used in your deployment. You do not have to set
  this property explicitly. It gets its value automatically. Here is
  a list of possible values:

  * "WAS" means "WebSphere Application Server".
  * "TOMCAT" means "Apache Tomcat". You also get this value if you deploy with the Wearefrank! Quick Docker Installer.
  * TODO: What is it for JBoss Application Server?

application.server.type.custom
  TODO: This property is referenced from "sprintContext.xml". How is it used to boot the frank!framework?

log.dir
  The value of this property is the directory to which the frank!framework
  writes its log files.

log.level
  Defines how much log lines are produced by the frank!framework. The most
  log lines are produced with value "DEBUG", while less
  are produced with "INFO", less with "WARN" and the least
  with "ERROR". The value is case insensitive.

jdbc.convertFieldnamesToUppercase
  Can be "true" or "false" (the default). When true, all field names and
  table names of a database are automatically converted to upper case. For example,
  a query "SELECT id FROM booking" is interpreted as "SELECT ID FROM BOOKING"

jdbc.migrator.active
  Can be "true" or "false" (the default). When true, database initialization
  is switched on. The default behavior is to do this with LiquiBase, see 
  https://www.liquibase.org/. With LiquiBase, the file
  "classes/DatabaseChangelog.xml" in your project directory is executed.

otap.side
  If your site has multiple networks or departments, you can use this
  property to have specific properties for each. For example, if this property
  has value "v", then additional properties are read from file
  "SideSpecifics_v.properties". The default value is "xxx", causing
  additional properties to be read from file "classes/SideSpecifics_xxx.properties"
  relative to your project directory. This file is optional. See section
  :ref:`deploymentConfigureProperties` for more details on how properties
  are read.

otap.stage
  Defines the DTAP stage of this deployment. Possible values are "LOC",
  "DEV", "TST", "ACC" and "PRD". These values are case insensitive. The
  value determines whether additional properties are read from file
  "StageSpecifics_LOC.properties" or "StageSpecifics_DEV.properties" or
  ... or "StageSpecifics_PRD.properties". All these files are relative to
  the "classes" directory of your project. They are all optional. See section
  :ref:`deploymentConfigureProperties` for more details on how properties
  are read.

.. NOTE::

   OTAP is the Duch equivalent of the DTAP acronym.
