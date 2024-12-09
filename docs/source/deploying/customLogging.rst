.. _deploymentCustomLogging:

Custom Logging
==============

Frank applications can be debugged using the debugger Ladybug, see :ref:`ladybug`. The Frank!Framework produces additional information. By default, this information is written to log files that can be accessed via the Frank!Console, see :ref:`frankConsoleLogs`. Log information can be used to debug complex issues and it can be used for monitoring. Some users want control over the way that the log information is stored. For example, they may have a central storage for log information coming from multiple servers and multiple applications. There are tools on the market that support this, for example Splunk (https://www.splunk.com/). This section explains how the generation of log information is organized and how system administrators can bring the log information to the destination they want.

The Frank!Framework, which has been programmed in the programming language Java, generates log information using a Java library log4j2, see for example https://logging.apache.org/log4j/2.12.x/. This is a very well-known library, not only for Java developers but also for system administrators. For this reason, the maintainers of the Frank!Framework do not provide a custom user interface for routing log information. Instead, system administrators are encouraged to provide configuration files to log4j2 as part of deploying the Frank!Framework.

About the generation of log information
---------------------------------------

Log4j2 decouples the way Java applications provide log information from writing that information to the intended destination. Java code writes every line of log information to a specific *logger*. Along with this message a *log level* is provided that expresses the importance of the line. The most important log levels are ``ERROR``, ``WARN``, ``INFO`` and ``DEBUG``. The logger chosen by the Java developer reveals information about the part of the Java application that is writing the log line. Log4j2 writes the information provided via loggers using *appenders*. An appender determines how a log line is formatted and where the information is written. On the web many third-party appenders are available to write log information to specific destinations, e.g. Splunk.

A system administrator typically provides a configuration file that references loggers and maps them to appenders. In this file, loggers are referenced along with the lowest log level for which the information has to be shown. By carefully choosing the loggers to which the appenders are connected, system administrators can differentiate between parts of the application that require detailed monitoring and parts that need less attention.

Configuring logging for Frank applications
------------------------------------------

To configure custom logging in Frank application, a system property ``log4j.configurationFile`` has to be set. Its value is a comma-separated list of all log4j2 configuration files to be read. A typical value is ``log4j4ibis.xml,my-log4j2.xml``. ``log4j4ibis.xml`` is the default log configuration provided by the Frank!Framework. ``my-log4j2.xml`` is a custom log configuration. The shown value references the two log configuration from the classpath of the Java Virtual Machine (JVM). System administrators can manipulate the classpath by properly configuring the application server (e.g. Apache Tomcat). It is also possible to reference files outside the JVM using URLs like ``file:///absolute/path/to/file``.

When you use a third-party appender, make sure to configure the application server so that the appender's library is on the classpath.

.. NOTE::

   Logging can also be adjusted using properties. As an example, consider the property setting ``logging.level.org.springframework=WARN``. This sets the log level for all Java packages starting with ``org.springframework`` to ``WARN``. To the right of the ``=`` sign is the log level; to the left is the Java class or package prepended by ``logging.level.``.

References and reference information
------------------------------------

The Frank!Framework writes important log information to loggers that are not related to Java classes in the source code. The following list shows their names and descriptions of the information provided:


**Root logger:** outputs by default to file ``${instance.name.lc}.log``. Applied when no other logger in log config matches.

**Logger** ``MSG``: outputs by default to file ``${instance.name.lc}-messages.log`` and ``${instance.name.lc}-messages.json``. Processed messages in human readable format.

**Logger** ``SEC``: outputs by default to file ``${instance.name.lc}-security.log``. Audit logging.

**Logger** ``HEARTBEAT``: outputs by default to file ``${instance.name.lc}-heartbeat.log``. Each Frank adapter (defined by ``<Adapter>`` in a Frank configuration) periodically writes a message as long as it is working properly. The heartbeat log can be checked to see whether all adapters are up and running.

**Logger** ``CONFIG``: outputs by default to file ``${instance.name.lc}-config.xml``. Prints the current configuration.

**Logger** ``APPLICATION``: outputs by default to the console. Shows how the Frank!Framework boots: what subsystems are discovered? How about connecting to databases and queues? What configurations are present? After booting, a message is shown when a configuration is reloaded.

The Frank!Framework also writes to loggers that are related to specific Java classes and packages. For a complete overview, see the contents of the default log configuration ``log4j4ibis.xml`` that is part of the Frank!Framework source code. It can be found at https://github.com/frankframework/frankframework/blob/master/core/src/main/resources/log4j4ibis.xml. An overview also appears in the Frank!Console, see https://frank2example.frankframework.org/#/logging/settings.


External references:

* https://www.baeldung.com/log4j2-appenders-layouts-filters.
* https://logging.apache.org/log4j/2.x/manual/configuration.html.
* https://logging.apache.org/log4j/2.x/manual/appenders.html.
