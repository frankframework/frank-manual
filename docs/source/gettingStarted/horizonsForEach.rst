Repetition
==========

This section continues implementing the requirements of :ref:`horizonsInterfaces`.
The aim is to read an XML document with a booking and insert it
in database tables "booking" and "visit". In section :ref:`insertDb` , we
did the insert in table "booking". The inserted values were
fetched using XPath expressions. In the previous section :ref:`transform`,
we transformed the booking XML such that the values for each "visit"
row are grouped together. In this section, we will insert
these rows.

A booking can have multiple destinations, each appearing in their
own ``<destination>`` element. These elements can be iterated
with the ``<ForEachChildElementPipe>``. Within this pipe you include a sender that is applied to each element, in our case a ``<destination>`` element. Please do the following to do the inserts in table "visit":

#. Please open ``projects/gettingStarted/configurations/NewHorizons/ConfigurationIngestBooking.xml``.
#. The ``<XsltPipe>`` you added in the previous section now points to path ``Exit``. Update it to point to a new pipe, as follows:

   .. code-block:: XML
      :emphasize-lines: 2

      ...
        <Forward name="success" path="iterateDestinations"/>
        <Forward name="failure" path="ServerError"/>
      </XsltPipe>

#. Insert the following XML into your adapter:

   .. code-block:: XML

      ...
        </XsltPipe>
        <ForEachChildElementPipe
            name="iterateDestinations"
            elementXPathExpression="/destinations/destination">
          <!-- You will add your sender here -->
          <Forward name="success" path="Exit"/>
          <Forward name="failure" path="ServerError"/>
        </ForEachChildElementPipe>
      </Pipeline>

The ``<ForEachChildElementPipe>`` applies the ``elementXPathExpression`` to the incoming message and iterates over the result set. In the transformed example booking shown in :ref:`transform`, there is one match:

.. code-block:: XML

   <destination>
     <bookingId>1</bookingId>
     <seq>1</seq>
     <hostId>3</hostId>
     <productId>4</productId>
     <startDate>2018-12-27</startDate>
     <endDate>2019-01-02</endDate>
     <price>400.00</price>
   </destination>

4. Replace the ``<!-- You will add your sender here -->`` line with the following XML:

   .. code-block:: XML

      <FixedQuerySender
          name="insertVisitSender"
          query="INSERT INTO visit VALUES(?, ?, ?, ?, ?, ?, ?)"
          jmsRealm="jdbc">
        <Param name="bookingId" xpathExpression="/destination/bookingId" />
        <Param name="seq" xpathExpression="/destination/seq" />
        <Param name="hostId" xpathExpression="/destination/hostId" />
        <Param name="productId" xpathExpression="/destination/productId" />
        <Param name="startDate" xpathExpression="/destination/startDate" />
        <Param name="endDate" xpathExpression="/destination/endDate" />
        <Param name="price" xpathExpression="/destination/price" />
      </FixedQuerySender>

This sender is similar to the sender of section :ref:`insertDb`. There is an INSERT query with a question mark for each inserted value. The inserted values are fetched using XPath expressions, which act on the current match of the ``elementXPathExpression`` as shown at step 2.
