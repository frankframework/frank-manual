.. _testingLarvaStubbingAndServices:

Stubbing and Services
=====================

Problem description
-------------------

In this section you study the most important concepts of Larva, namely stubbing and services. The Frank!Framework was designed to support system integration, so we start with a fictive integration problem. The Rotterdam Bank is a bank that provides current accounts and savings accounts to their customers. The Rotterdam Bank has purchased the Hermes system to send paper statements of account. Hermes comes from an external company.

To the Rotterdam Bank it is very important to have the proper contact information of their relations. They have a dedicated department for maintaining this data. The department maintains a system called Conscience to make this data available. Conscience also needs to be accessed by Hermes, because Hermes includes customer addresses in the statements of account.

The problem to be solved is that the interfaces of Hermes and Conscience are not compatible. When Hermes needs an address, it sends out a RESTful HTTP GET request with a body like the following:

.. literalinclude:: ../../../../srcSteps/Frank2Hermes/v510/tests/hermesBridge/scenario01/hermesAddressRequest.xml
   :language: xml

Conscience expects a different format. This format looks like the following example:

.. literalinclude:: ../../../../srcSteps/Frank2Hermes/v510/tests/hermesBridge/scenario01/conscienceAddressRequest.xml
   :language: xml

Conscience produces a response, for example:

.. literalinclude:: ../../../../srcSteps/Frank2Hermes/v510/tests/hermesBridge/scenario01/conscienceAddress.xml
   :language: xml

But Hermes expects something like this:

.. literalinclude:: ../../../../srcSteps/Frank2Hermes/v510/tests/hermesBridge/scenario01/hermesAddress.xml
   :language: xml

The solution
------------

The Rotterdam Bank needs an integration application, or as we say a Frank, that connects Hermes and Conscience. This integration application is named "Frank2Hermes". Its role is illustrated by the following figure:

.. image:: requestReply.jpeg

Frank2Hermes is a web application that receives address requests. Hermes is configured to send its address requests to Frank2Hermes. When Frank2Hermes receives an address request, it translates the request to the format needed by Conscience. Then this modified request is sent to Consience. The HTTP response from Conscience contains the address, but not in the format needed by Hermes. Frank2Hermes translates the address and then responds that address to the request received from Hermes.

The shown behavior has been implemented in a Frank config "hermesBridge". Please examine this configuration as follows:

#. Install the Frank!Runner as explained in section :ref:`horizonsMultipleFiles`.
#. Download :download:`Hermes Bridge <../../downloads/configurations/hermesBridge.zip>`.
#. Deploy this configuration to your Frank2Manual instance.
#. Start the Frank!Runner.
#. Browse to http://localhost. You see the Adapter Status page.
