.. _insertDb:

Sending to Database
===================

Extending the ingest booking adapter
------------------------------------

The Frank!Framework can send data to external systems. This is done by pipe ``<SenderPipe>``. Within this pipe, you add a sender to specify the destination.

As an example, we extend the New Horizons case by writing the "booking" table introduced in section :ref:`horizonsInterfaces`. We use sender ``<FixedQuerySender>`` to specify that we are targeting the database. Please do the following:

#. Please open file ``Configuration.xml`` again.
#. The ``<XmlValidatorPipe>`` you included in the previous section points to path ``Exit`` now. Update it to point to the pipe that will write the database. The highlighted line shows the update:

   .. include:: ../snippets/NewHorizons/v460/refSenderPipe.txt

#. Insert the new pipe after the ``</FixedResultPipe>``:

   .. include:: ../snippets/NewHorizons/v460/addSenderPipe.txt

You see that we send an INSERT query to the database with parameters. The parameters appear with question marks in the SQL statement. The values of the parameters are provided through the ``<Param>`` tags. These tags contain XPath expressions to select the values from the incoming message. Xpath is explained here: https://www.w3schools.com/xml/xpath_intro.asp. You can see that elements are selected through ``/`` while attributes are selected through ``/@``. We know that the incoming message is a valid booking, because it passed the ``<XmlValidatorPipe>``.

The database is selected in an indirect way; the line ``datasourceName="jdbc/${instance.name.lc}"`` does the trick. Its meaning is explained in depth in section :ref:`advancedDevelopmentDatabase`. If you are reading this section for the first time, please finish it before studying database details.

Named query parameters
----------------------

In the update above, you used query string ``INSERT INTO booking VALUES(?, ?, ?, ?)``. Instead of using anonymous parameters with ``?``, you can also reference the parameters by the name you give them in the ``<Param>`` elements. If you want to try this, you can update your adapter as shown:

.. include:: ../snippets/NewHorizons/v465/namedQueryParameters.txt

This update is optional; it does not change the results produced by your adapter. It presents an alternative approach however that is useful in more advanced queries. This update is not applied in the solution download of this tutorial.

Testing (Windows and Linux)
---------------------------

Please test your work as follows:

#. Copy the booking XML presented in :ref:`horizonsInterfaces` to some file.
#. Edit that file to update the ``id`` attribute of the ``<booking>`` element. This corresponds to the primary key of database table "booking". You need a value that differs from the values you applied so far.
#. In the Frank!Console, go to Testing | Test Pipeline. Run the "IngestBooking" adapter with your booking XML. See section :ref:`gettingStartedTestPipelines` for details.

The response should be something like the following:

.. code-block:: XML

   <results>
     <result item="1">
       <result><rowsupdated>1</rowsupdated></result>
     </result>
   </results>

The output message is no longer the incoming booking XML. Please remember this when you add more pipes to the adapter.

4. In the Frank!Console, click "JDBC" (number 1 in the figure below). That link will expand:

   .. image:: jdbcExecuteQuery.jpg

#. Click "Execute Query" (number 2). You see the following screen:

   .. image:: executeJdbcQuery.jpg

#. You see you are in the execute screen (number 1). Select "Datasource" "jdbc/frank2manual" (number 2). If you want, you can choose to see comma-separated output instead of XML (number 3).
#. Leave the Query Type to "Auto". You only need to change it for complicated queries for which the Frank!Framework cannot sort out whether a value is returned or not.
#. Type the following query: ``SELECT * FROM booking`` (number 4).
#. Press "Send" (number 5). Check that the query result (number 6) shows some of the data you entered in step 2, in particular the "id" you chose.

The presented version of the ingest booking adapter only inserts in table "booking". In the coming sections, you will extend
the adapter to also insert into table "visit".

solution
--------

If you are having troubles, you can :download:`download <../downloads/configurations/NewHorizonsOnlyTableBooking.zip>` the solution.