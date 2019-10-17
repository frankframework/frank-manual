.. _helloIbis:

Hello World Source Code
=======================

In this page we study the example Frank given in :ref:`installationLinux`.

Frank
-----

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

Adapter
-------

When we examine the ``<Configuration>`` tag, we find the following:

  .. code-block:: XML

     ...
     <adapter name="Hello">
       <receiver name="dummyInput">
         <ApiListener
             name="helloListener"
             uriPattern="hello"
             method="GET"/>
       </receiver>
       <pipeline firstPipe="hello">
         ...
       </pipeline>
     </adapter>
   
An adapter is a service that is triggered by a receiver and
executes a pipeline in response. The ``<receiver`` tag
defines the receiver, while the ``pipeline`` tag defines the
pipeline.

Receiver
--------

Our receiver reads:

  .. code-block:: XML

     ...
     <receiver name="dummyInput">
       <ApiListener
           name="helloListener"
           uriPattern="hello"
           method="GET"/>
     </receiver>
     ...

It has name ``dummyInput``. Its further definition
is provided by the tag within, ``<ApiListener>``. Listeners
are building blocks that accept input. The choice for
``<ApiListener`` means that the adapter ``Hello`` should
have a HTTP REST interface. The attribute ``uriPattern``
defines the relative URL to listen to, while the ``method="GET"``
attribute defines that we listen to HTTP GET requests.

There are other listeners, for example ``DirectoryListener``.
This listener triggers your adapter when a file is added
to a chosen directory on a (server-side) local file system.
For a complete list of all listeners, see
https://ibis4example.ibissource.org/iaf/ibisdoc/.


Pipeline
--------

The pipeline defines how the message provided by the receiver
should be processed. It reads:

  .. code-block:: XML

     ...
     <pipeline firstPipe="hello">
       <exits>
         <exit path="Exit" state="success" code="201"/>
       </exits>

     </pipeline>
     ...

A pipeline is a network of pipes. The ``firstPipe="hello"`` attribute
defines that the message coming from the receiver should go
to the pipe named ``hello``. The ``<exits>`` tag defines 
the states in which processing can end. In our case,
we have one state that we name ``"success"``. It can be
referenced from other pipes by its path ``"Exit"``.
It should result in HTTP response code 201.

.. NOTE::

   The ``code`` attribute is always defined for an exit,
   but only makes sense when you have a listener for
   incoming HTTP requests.

Pipes and forwards
------------------

We have a very simple pipeline that has only one pipe.
It reads:

.. code-block:: XML

   ...
   <FixedResultPipe name="hello" returnString="Hello 16">
     <forward name="success" path="Exit"/>
   </FixedResultPipe>
   ...

Pipes are predefined functions that can be performed on
the incoming message. The ``<FixedResultPipe>`` ignores
the input and outputs a fixed string that can be configured.
We configure the name to be ``"hello"``.
This satisfies the reference made in the
``firstPipe`` attribute in the ``<pipeline>`` tag. Therefore,
the (ignored) incoming message is the message we got from the
receiver. The fixed output string we want is in the ``returnString``
attribute.

In the remainder of the :ref:`gettingStarted`, we will see
pipes with more interesting functions, like applying
XSLT transformations and sending data to a database.

The ``<forward>`` within a pipe tag defines what should happen after
the execution of that pipe. A forward consists of a forward
name and a path. Each pipe defines the forward names to which
it can send the output. For the fixed result pipe, the only
possibility is ``"success"``, but many pipes also have
the possibility ``"failure"``. This allows Frank developers
to handle errors and to have branching pipelines.

Our forward points to the path ``"Exit"``, which was defined
earlier as the only possible exit of the pipeline. In more
complex pipelines, there are also forwards that reference other
pipes by their configured ``name`` attribute.

.. NOTE::

   If you studied computer science or mathematics, the following
   may help. A pipeline is an example of a graph, with the
   pipes being the nodes and the forwards being the edges.
   Before configuring the individual pipes and forwards,
   you name all allowed exit states of the pipeline. Each forward
   then either references a next pipe by its name, or names
   one of the predefined exits to indicate the end of processing.

Conclusion
----------

We implemented a simple adapter. It has a receiver that gives our adapter a
REST HTTP interface. We have a pipeline with a single pipe that
outputs a fixed message. In the next section, :ref:`helloRest`, we
will see our adapter in action.
