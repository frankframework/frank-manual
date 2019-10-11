.. _helloIbis:

Hello World Source Code
=======================

.. role:: xml(code)
   :language: xml

Let's first study the example Frank given in :ref:`installationLinux`.
The outer part of it reads:

  .. code-block:: XML

     <?xml version="1.0" encoding="UTF-8" ?>
     <Configuration
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:noNamespaceSchemaLocation="./ibisdoc.xsd"
         name="ibis4manual">
       <jmsRealms>
         <jmsRealm realmName="jdbc" datasourceName="jdbc/${instance.name.lc}"/>
       </jmsRealms>
       ...
     </Configuration>

This part can be almost the same for each Frank. If you want to understand
it in detail, you can look `here <https://www.w3schools.com/xml/>`_ .
The only interesting thing here is the ``name`` attribute that gives
this Frank the name ``ibis4manual``.

Can we have inline XML? :xml:`<?xml version="1.0" encoding="UTF-8" ?>`.
