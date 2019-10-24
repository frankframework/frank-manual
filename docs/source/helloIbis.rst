.. _helloIbis:

Hello World Source Code
=======================

In this section we study the example Frank provided in https://github.com/ibissource/docker4ibis/.
During installation, you put it in "classes/Configuration.xml" relative to the folder that contains
the "Ibis4DockerExample" Frank. It reads:

.. code-block:: XML

   <Configuration name="Ibis4DockerExample">
	   <jmsRealms>
		   <jmsRealm datasourceName="jdbc/${instance.name.lc}" realmName="jdbc"/>
	   </jmsRealms>
	   <Adapter name="HelloDockerWorld">
		   <Receiver name="HelloDockerWorld">
			   <JavaListener name="HelloDockerWorld"/>
		   </Receiver>
		   <Pipeline firstPipe="HelloDockerWorld">
			   <FixedResultPipe name="HelloDockerWorld" returnString="Hello Docker World">
				   <Forward name="success" path="EXIT"/>
			   </FixedResultPipe>
			   <Exit path="EXIT" state="success"/>
		   </Pipeline>
	   </Adapter>
   </Configuration>

Frank
-----

The outer part of it reads:

  .. code-block:: XML

     <Configuration name="Ibis4DockerExample">
         <jmsRealms>
             <jmsRealm datasourceName="jdbc/${instance.name.lc}" realmName="jdbc"/>
         </jmsRealms>
         ...
     </Configuration>

This part can be almost the same for each Frank. The only interesting thing here is
the ``name`` attribute that gives
this Frank the name ``Ibis4DockerExample``.

Adapter
-------

When we examine the ``<Configuration>`` tag, we find the following:

  .. code-block:: XML

     ...
     <Adapter name="HelloDockerWorld">
         <Receiver name="HelloDockerWorld">
             <JavaListener name="HelloDockerWorld"/>
         </Receiver>
         <Pipeline firstPipe="HelloDockerWorld">
         ...
         </Pipeline>
     </Adapter>
   
An adapter is a service that is triggered by a receiver and
executes a pipeline in response. The ``<Receiver>`` tag
defines the receiver, while the ``<Pipeline>`` tag defines the
pipeline.

Receiver
--------

Our receiver reads:

  .. code-block:: XML

     ...
     <Receiver name="HelloDockerWorld">
         <JavaListener name="HelloDockerWorld"/>
     </Receiver>
     ...

It has name ``HelloDockerWorld``. Its further definition
is provided by the tag within, ``<JavaListener>``. Listeners
are building blocks that accept input. The choice for
``<JavaListener>`` means that the adapter "HelloDockerWorld" is
called directly from Java code. This is a good choice if you
only want to call your adapter from other adapters.

There are other listeners, for example ``<ApiListener>`` and
``<DirectoryListener>``. ``ApiListener`` makes your adapter
listen to REST HTTP requests. ``DirectoryListener``
triggers your adapter when a file is added
to a chosen directory on a (server-side) local file system.
For a complete list of all listeners, see
https://ibis4example.ibissource.org/iaf/ibisdoc/.


Pipeline
--------

The pipeline defines how the message provided by the receiver
should be processed. It reads:

  .. code-block:: XML

     ...
     <Pipeline firstPipe="HelloDockerWorld">
         ...
         <Exit path="EXIT" state="success"/>
     </Pipeline>
     ...

A pipeline is a network of pipes. The ``firstPipe="HelloDockerWorld"``
attribute defines that the message coming from the receiver should go
to the pipe named "HelloDockerWorld". The ``<Exit>`` tag defines 
the state in which processing can end. In our case,
we have one state that we name "success". It can be
referenced from pipes by its path "EXIT".

Pipes and forwards
------------------

We have a very simple pipeline that has only one pipe.
It reads:

.. code-block:: XML

   ...
   <FixedResultPipe name="HelloDockerWorld" returnString="Hello Docker World">
       <Forward name="success" path="EXIT"/>
   </FixedResultPipe>
   ...

Pipes are predefined functions that can be performed on
the incoming message. The ``<FixedResultPipe>`` ignores
the input and outputs a fixed string that can be configured.
We configure the ``name`` to be "HelloDockerWorld".
This satisfies the reference made in the
``firstPipe`` attribute in the ``<Pipeline>`` tag. Therefore,
the (ignored) incoming message is the message we got from the
receiver. The fixed output string we want is in the ``returnString``
attribute.

In the remainder of the :ref:`gettingStarted`, we will see
pipes with more interesting functions, like applying
XSLT transformations and sending data to a database.

The ``<forward>`` within a pipe tag defines what should happen after
the execution of that pipe. A forward consists of a forward
name and a path. Each pipe predefines the forward names from which
it can send the output. For the fixed result pipe, the only
possibility is "success", but many pipes also have
the possibility "failure". This allows Frank developers
to handle errors and to have branching pipelines.

Our forward points to the path "EXIT", which is defined
within the ``<Exit>`` tag as the only possible exit of the pipeline. In more
complex pipelines, there are also forwards that reference other
pipes by their configured ``name`` attribute. It is also possible to have
multiple ``<Exit>`` tags within a ``<Pipeline>``.

.. NOTE::

   If you studied computer science or mathematics, the following
   may help. A pipeline is an example of a graph, with the
   pipes being the nodes and the forwards being the edges.
   Before or after configuring the individual pipes and forwards,
   you name all allowed exit states of the pipeline. Each forward
   then either references a next pipe by its name, or names
   one of the defined exits to indicate the end of processing.

Conclusion
----------

We implemented a simple adapter. It has a receiver that allows
us to trigger it. We have a pipeline with a single pipe that
outputs a fixed message. In the next section, :ref:`helloTestPipeline`, we
will see our adapter in action.
