.. _deploymentProperties:

Properties 
==========

Properties are key/value pairs, both the key and the value being strings. There are
different ways to set properties, which is the subject of section
:ref:`deploymentConfigureProperties`. This section focuses on the meaning of
properties. What impact does setting a property have on the behavior of
your Frank?

Here follows a list of properties with their meaning:

log.dir
  The value of this property is the directory to which the frank!framework
  writes its log files.

log.level
  Defines how much log lines are produced by the frank!framework. The most
  log lines are produced with value "DEBUG", while less
  are produced with "INFO", less with "WARN" and the least
  with "ERROR". The value is case insensitive.

otap.stage
  Defines the OTAP stage of this deployment. Possible values are "LOC",
  "DEV", "TST", "ACC" and "PRD". These values are case insensitive. The
  value determines whether additional properties are read from file
  "StageSpecifics_LOC.properties" or "StageSpecifics_DEV.properties" or
  ... or "StageSpecifics_PRD.properties". See section
   :ref:`deploymentConfigureProperties` for more details on how properties
   are read.


* How properties are accessed inside Frank configurations.
* How properties can be viewed within the frank!framework.
