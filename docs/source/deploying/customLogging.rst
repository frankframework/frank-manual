.. _advancedDevelopmentCustomLogging:

Custom Logging
==============

Frank applications can be debugged using the debugger Ladybug, see :ref:`ladybug`. The Frank!Framework produces additional information. By default, this information is written to log files that can be accessed via the Frank!Console, see :ref:`frankConsoleLogs`. Log information can be used to debug complex issues and it can be used for monitoring. Some users want control over the way that the log information is stored. For example, they may have a central storage for log information coming from multiple servers and multiple applications. There are tools on the market that support this, for example Splunk (https://www.splunk.com/). This section explains how the generation of log information is organized and how system administrators can bring the log information to the destination they want.

The Frank!Framework, which has been programmed in the programming language Java, generates log information using a Java library log4j2, see for example https://logging.apache.org/log4j/2.12.x/. This is a very well-known library, not only for Java developers but also for system administrators. For this reason, the maintainers of the Frank!Framework do not provide a custom user interface for routing log information. Instead, system administrators are encouraged to provide configuration files to log4j2 as part of deploying the Frank!Framework.

About the generation of log information
---------------------------------------

Log4j2 decouples the way Java applications provide log information from writing that information to the intended destination. Every line of log information is written to a specific *logger* and has a *log level* that expresses the importance of the line. A Java class typically creates a logger by a statement like the following:

.. code-block:: java

   protected Logger log = LogUtil.getLogger(this);	

This creates a member variable named ``log`` to which information coming from the current Java class can be written. This statement appears for example in Java class ``org.frankframework.filesystem.AmazonS3FileSystemTest`` (not used in production, only for testing the Frank!Framework). Log information written to this variable ``log`` is considered to be about the operation of Java class ``org.frankframework.filesystem.AmazonS3FileSystemTest`` or some larger part of the Frank!Framework that is implemented by this Java class - in this case some tests related to the Amazon cloud.

The Frank!Framework also writes log information to loggers that are not related to a Java class. For example, there is a logger named ``HEARTBEAT`` to which each Frank adapter (defined by ``<Adapter>`` in a Frank configuration) writes a message as long as it is working properly.

Log information is actually written by a statement like the following:

.. code-block:: java

   log.error("unable to remove bucket", e);

The method ``error()`` is used here, which means that an error is being reported. The message has log level ``ERROR``. Less important log levels are for example ``WARN``, ``INFO`` and ``DEBUG``. System administrators typically use the log level to control how much information they want to see. If they want to see little, they typically set the log level to ``ERROR`` or ``WARN`` to see only the most relevant information. If they want more detailed information, they use ``INFO`` or ``DEBUG``. The logger chosen by the Java developer reveals information about the part of the Java application that is writing the log line. System administrators can use this information to differentiate between parts of the application that require detailed monitoring and parts that need less attention.

Log4j2 writes the information provided via loggers using *appenders*. An appender determines how a log line is formatted and where the information is written. On the web many third-party appenders are available to write log information to specific destinations, e.g. Splunk. A system administrator typically provides a configuration file that references loggers and maps them to appenders. Here is a simple example that modifies the destination and the layout of the log information provided by the Frank!Framework:

.. literalinclude:: ../../../src/customLogging/my-log4j2.xml
   :language: xml

This file routes logger ``HEARTBEAT`` to the console and adds some nonsensical text to each log line. Here are two lines of the output written by this log configuration:

.. code-block:: none

   customlogging-custom-logging-1  | LAYOUT TEST 2024-09-10 13:39:38,291 [WebSocket-TaskScheduler3] DEBUG org.springframework.integration.channel.PublishSubscribeChannel - postSend (sent=true) on channel 'bean 'frank-management-bus'', message: GenericMessage [payload=NONE, headers={replyChannel=org.springframework.messaging.core.GenericMessagingTemplate$TemporaryReplyChannel@1760fa14, errorChannel=org.springframework.messaging.core.GenericMessagingTemplate$TemporaryReplyChannel@1760fa14, topic=ADAPTER, action=GET, meta-expanded=all, id=fc75f940-2fa1-ee0b-e852-f47fb9534216, timestamp=1725975578281}]
   customlogging-custom-logging-1  | LAYOUT TEST HEARTBEAT 2024-09-10 13:39:41,129 [recover Adapters[IbisScheduler_Worker-3]] INFO  HEARTBEAT - adapter [ManageDatabase] has state [STARTED]

Configuring logging for Frank applications
------------------------------------------

To configure custom logging in Frank application, a system property ``log4j.configurationFile`` has to be set. Its value is a comma-separated list of all log4j2 configuration files to be read. To produce the above output, the value was set to ``log4j4ibis.xml,my-log4j2.xml``. ``log4j4ibis.xml`` is the default log configuration provided by the Frank!Framework. The example log configuration shown above was in a file named ``my-log4j2.xml``. The Frank!Framework was run using docker. Both the default log configuration and the custom log configuration appeared on the classpath of the Java Virtual Machine (JVM). It is also possible to reference files outside the JVM using URLs like ``file:///absolute/path/to/file``.

When you use a third-party appender, make sure to configure the application server so that the appender's library is on the classpath.

References and reference information
------------------------------------

The Frank!Framework writes important log information to loggers that are not related to Java classes in the source code. The following list shows their names and descriptions of the information provided:


**Root logger:** outputs by default to file ``${instance.name.lc}.log``. Applied when no other logger in log config matches.

**Logger** ``MSG``: outputs by default to file ``${instance.name.lc}-messages.log`` and ``${instance.name.lc}-messages.json``. Processed messages in human readable format.

**Logger** ``SEC``: outputs by default to file ``${instance.name.lc}-security.log``. Audit logging.

**Logger** ``HEARTBEAT``: outputs by default to file ``${instance.name.lc}-heartbeat.log``. Periodic adapter status status.

**Logger** ``CONFIG``: outputs by default to file ``${instance.name.lc}-config.xml``. Prints the current configuration.

**Logger** ``APPLICATION``: outputs by default to the console.

For a complete overview, see the contents of the default log configuration ``log4j4ibis.xml`` that is part of the Frank!Framework source code. See https://github.com/frankframework/frankframework/blob/master/core/src/main/resources/log4j4ibis.xml.

Reference information on log4j2:

* https://www.baeldung.com/log4j2-appenders-layouts-filters.
* https://logging.apache.org/log4j/2.x/manual/configuration.html.
* https://logging.apache.org/log4j/2.x/manual/appenders.html.

Overview of third-party appenders:

* TODO.