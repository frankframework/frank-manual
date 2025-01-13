.. _advancedDevelopmentIntegrationPatternsOnlyOnce:

Message Id and Correlation Id
=============================

This section introduces the concepts of the *message id* and the *correlation id*. It is often important that an incoming message is processed only once, even though the upstream system may send the same request multiple times. The upstream system can be expected to provide a unique id of the request it sends, the *message id*. The receiver of the request can maintain a message log that keeps the message id's of all received requests. If a message is received that has a duplicate message id, the request can be discarded or an error can be reported.

In a fire and forget situation, the sender of some request may later receive a notification about the success or failure of the request. The sender has to relate the received notification to the original request. To this end, the notification should include a *correlation id*, a unique id of the conversation that includes the original request and the notification. When the original request has a message id, the correlation id of the notification can equal that message id. The original request can also provide a correlation id up front instead of a message id.

You can experiment with the message id and the correlation by downloading this :download:`example Frank application <../../downloads/advancedDevelopmentIntegrationPatternsMessageId.zip>`. Its root directory is ``messageIdExample``. It can be started using docker compose, see :ref:`advancedDevelopmentDockerDevel`. A Frank configuration is included with an ``<ApiListener>``, which means that it listens to HTTP requests. Please install an API client that can send HTTP requests to this Frank configuration, for example Bruno. It can be downloaded from https://www.usebruno.com/. When the application is running, it can be visited at http://localhost:8080. The incoming HTTP requests should be HTTP POST requests to URL http://localhost:8080/api/write.

The example detects whether a duplicate message id is received and returns HTTP code 304 Not Modified in this case. This behavior is configured in the receiver of adapter ``writeDb``. The receiver is shown below (the remainder is a bit more complicated than needed here, but it is a useful example to explain transactions in the next section :ref:`advancedDevelopmentIntegrationPatternsTransactions`):

.. literalinclude:: ../../../../srcSteps/Frank2Transactions/v480/src/main/resources/Configuration.xml
   :emphasize-lines: 6, 8
   :language: xml

Attribute ``checkForDuplicates="true"`` does the trick. The example expects the message id in HTTP header ``Message-Id``. This can be changed by setting attribute ``messageIdHeader`` of the ``<ApiListener>``, as is documented in the Frank!Doc.

.. WARNING::

   Setting attribute ``processResultCacheSize="0"`` is a workaround for issue https://github.com/frankframework/frankframework/issues/7432. When this issue will have been solved, setting this attribute will not be necessary anymore.

The ``<JdbcMessageLog>`` configures the Frank!Framework to remember the incoming messages. They are stored in a database table named ``IBISSTORE``. The ``slotId`` attribute is needed to distinguish between the different ``<JdbcMessageLog>`` elements that can appear in a Frank application. Message logs have another purpose in addition to remembering message ids already received - they act as audit logs as well. See :ref:`managingProcessedMessagesLog`.

.. WARNING::

   Table ``IBISSTORE`` is only created if property ``jdbc.migrator.active`` is true and if this is configured as a system property or application property. Setting this within a configuration is not sufficient.

.. NOTE::

   The fact that the ``<JdbcMessageLog>`` is backed by the database has an important consequence. When multiple instances of the application run in parallel, the message log still behaves as expected. This would not be possible if a message log would only keep its data in memory. If that would be the case, other instances would not know that some incoming message was seen already because in-memory information is not shared.

.. NOTE::

   If table IBISSTORE is created, it appears in the database referenced by ``jdbc.datasource.default``. If that property does not have its default value, then table IBISSTORE does not appear in the database with name ``jdbc/${instance.name.lc}``. In that case it appears in the database with the name that is the value of property ``jdbc.datasource.default``.

The receiver can be changed to expect a correlation id that is extracted from the incoming message, instead of a message id. The changes shown below modify ``Configuration.xml`` to process a message only if the extracted correlation id has not been seen before:

.. include:: ../../snippets/Frank2Transactions/v490/toCorrelationId.txt

First, attribute ``checkForDuplicatesMethod="CORRELATIONID"`` is set to inform the Frank!Framework that a correlation id is expected now instead of a message id. The input is no longer expected to be plain text, but XML. An XPath expression is needed to extract the correlation id, which is configured by attribute ``correlationIDXPath="/input/@correlationId"``. Then, an ``<XmlInputValidator>`` is added to check the syntax of the input. The XSD file ``input.xsd`` is shown below:

.. literalinclude:: ../../../../srcSteps/Frank2Transactions/v490/src/main/resources/input.xsd
   :language: xml

Next, an ``<XsltPipe>`` is added to extract the message to be written to the database. The remaining changes of ``Configuration.xml`` save this message. The ``<PutInSessionPipe>`` saves the message into session key ``inputMessage``. The response of adapter ``writeTableMessage`` reports how many rows have been updated and is not relevant for adapter ``writeTableOtherMessage``. The input for that adapter is fetched by the ``<EchoPipe>``, which reads back the session key.

.. NOTE::

   It is also possible to extract the correlation id from a HTTP header. According to the Frank!Doc, this can be achieved by setting attribute ``correlationIdHeader`` of the ``<ApiListener>`` and keeping ``checkForDuplicatesMethod="CORRELATIONID"`` in the ``<Receiver>``.

Tutorial
--------

To get hands-on experience with the message id and the correlation id, you can do the following:

1. Download the :download:`example Frank application <../../downloads/advancedDevelopmentIntegrationPatternsMessageId.zip>` and unzip it. This gives you a directory ``messageIdExample``.
#. If you are working with Docker Desktop, allow docker to work with this directory, see :ref:`advancedDevelopmentDockerDevelConfigureDocker`.
#. Start the application on a command prompt with the command ``docker compose up``. You can stop it using Ctrl-C and you can remove its state using ``docker compose down``. That command removes the docker containers running the application and hence all data in the database is gone.
#. Using a HTTP client, send a HTTP POST request to http://localhost:8080/api/write and include header ``Message-Id``. The value of this header should be a number.
#. Go to the Frank!Console at http://localhost:8080. From the main menu, choose JDBC | Execute Query. Check that the message given as the body of your HTTP request is in the database. It should be in table ``Message`` and in table ``otherMessage``.

   .. WARNING::

      For some unkown reason, quotes are needed to query table ``otherMessage``: ``SELECT * FROM "otherMessage"``.

#. In Ladybug, check that there are reports for the incoming HTTP request and the executions of the SQL queries of the previous step.
#. Re-send the HTTP request of step 4. Check that the HTTP response code is 304 Not Modified. Check in Ladybug that there is no new report.
#. Stop the application and update it to expect a correlation id in the body of the HTTP request, as shown in this section.
#. Redo this test for the modified application. Do not send headers this time. As a starting point, you can use the HTTP body ``<input correlationId="1000" message="My first message" />``.
