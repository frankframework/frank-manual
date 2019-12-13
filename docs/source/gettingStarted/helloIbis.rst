.. _helloIbis:

Hello World Source Code
=======================

In this section we study the example Frank provided with the WeAreFrank! Quick Docker Installer, found at https://github.com/ibissource/docker4ibis/. To be able to run this Frank, please do the following:

.. highlight:: none

#. Follow the instructions at https://github.com/ibissource/docker4ibis/ to install the WeAreFrank! Quick Docker Installer.
#. When your projects directory is ``franks``, you should arrive at the following directory structure: ::

     franks
     |- docker4ibis
        |- docker4ibis.bat
        |- docker4ibis.properties
        |- docker4ibis.should
        |- ...
        |- README.md
     |- Ibis4DockerExample
        |- classes
           |- Configuration.xml

   ``docker4ibis`` is your git checkout of https://github.com/ibissource/docker4ibis/. You create ``Ibis4DockerExample`` by hand. The file ``Configuration.xml`` has the following contents:

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

#. Ensure that your file ``frank/docker4ibis/docker4ibis.properties`` has the following contents: ::

     projects_directory=..

In the remainder of this section, we examine the contents of ``Configuration.xml`` in detail. This study introduces you to the basic concepts of Frank development.

Frank configuration
-------------------

The outer part of ``Configuration.xml`` reads:

  .. code-block:: XML

     <Configuration name="Ibis4DockerExample">
         <jmsRealms>
             <jmsRealm datasourceName="jdbc/${instance.name.lc}" realmName="jdbc"/>
         </jmsRealms>
         ...
     </Configuration>

This part can be almost the same for each Frank configuration. The only interesting thing here is
the ``name`` attribute that gives
this Frank the name ``Ibis4DockerExample``.

.. NOTE::

   The XML code within ``Configuration.xml`` is named a "Frank configuration". In section :ref:`multipleConfigurations` you will learn how to include multiple configurations within the same deployment of the Frank!Framework. We call the combination of the Frank!Framework and all Frank configurations deployed on it a "Frank". A Frank is the solution your customer needs.

Adapter
-------

When we examine the contents of the ``<Configuration>`` tag, we find the following:

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
is provided by the tag within: ``<JavaListener>``. Listeners
are building blocks that accept input. The choice for
``<JavaListener>`` means that the adapter "HelloDockerWorld" is
called directly from Java code. This is a good choice if you
only want to call your adapter from other adapters.

There are other listeners, for example ``<ApiListener>`` and
``<DirectoryListener>``. ``ApiListener`` makes your adapter
listen to REST HTTP requests. ``DirectoryListener``
triggers your adapter when a file is added
to a chosen directory on a (server-side) local file system.
The Frank!Framework allows you to search the listener you
need. This is explained in subsection :ref:`horizonsMultipleFiles`.

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
XSLT transformations and sending data to a database. In
subsection :ref:`horizonsMultipleFiles` you will learn
how to search the pipe you need.

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
