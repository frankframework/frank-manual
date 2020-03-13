.. _helloIbis:

Hello World Source Code
=======================

Introduction
------------

In the previous section you installed the Frank!Runner, a tool to quickly start the Frank!Framework. You saw the directory structure resulting from this installation. There was subdirectory ``configurations`` with subdirectories ``Example1`` and ``Example2``, which are deployed Frank configs. These directories contain files with extension ``.xml`` and files with extension ``.properties``. XML stands for Extensible Markup Language, see https://www.w3.org/XML/. Property files are text files that contain name/value pairs. In this section you start learning how to write these files.

The simplest configuration you encountered in the previous section was ``Example2``. You will examine its XML text in detail to learn the basic concepts of Frank development. It consists of only one file, ``Configuration.xml``. This file reads as follows:

.. code-block:: XML

   <Configuration name="Example2">
     <Adapter name="Example2Adapter">
       <Receiver name="Example2Receiver">
         <JavaListener name="Example2" serviceName="Example2"/>
       </Receiver>
       <Pipeline firstPipe="Example">
         <FixedResultPipe name="Example" returnString="Hello World2">
           <Forward name="success" path="EXIT"/>
         </FixedResultPipe>
         <Exit path="EXIT" state="success"/>
       </Pipeline>
     </Adapter>
   </Configuration>

Frank configuration
-------------------

The outer part of ``Configuration.xml`` reads:

.. code-block:: XML

   <Configuration name="Example2">
     ...
   </Configuration>

It gives the configuration its name ``Example2``.

Adapter
-------

When we examine the contents of the ``<Configuration>`` tag, we find the following:

.. code-block:: XML

   ...
   <Adapter name="Example2Adapter">
     <Receiver name="Example2Receiver">
       <JavaListener name="Example2" serviceName="Example2"/>
     </Receiver>
     <Pipeline firstPipe="Example">
       ...
     </Pipeline>
   </Adapter>
   ...
   
An adapter is a service that is triggered by a receiver and executes a pipeline in response. The ``<Receiver>`` tag
defines the receiver, while the ``<Pipeline>`` tag defines the pipeline. You encountered adapters and receivers in the previous section on the Adapter Status webpage. That webpage shows their names and their state (e.g. started, stopped, error).

Receiver
--------

Our receiver reads:

.. code-block:: XML

   ...
   <Receiver name="Example2Receiver">
     <JavaListener name="Example2" serviceName="Example2"/>
   </Receiver>
   ...

It has name ``Example2Receiver``. Its further definition is provided by the tag within: ``<JavaListener>``. Listeners
are building blocks that accept input. The choice for ``<JavaListener>`` means that the adapter "Example2Adapter" is
called directly from Java code. This is a good choice if you only want to call your adapter from other adapters.

There are other listeners, for example ``<ApiListener>`` and ``<DirectoryListener>``. ``ApiListener`` makes your adapter listen to REST HTTP requests. ``DirectoryListener`` triggers your adapter when a file is added to a chosen directory on a (server-side) local file system. The Frank!Framework allows you to search the listener you need. This is explained in subsection :ref:`configurationSyntaxChecking`.

Pipeline
--------

The pipeline defines how the message provided by the receiver should be processed. It reads:

.. code-block:: XML

   ...
   <Pipeline firstPipe="Example">
     ...
     <Exit path="EXIT" state="success"/>
   </Pipeline>
   ...

A pipeline is a network of pipes. The ``firstPipe="Example"`` attribute defines that the message coming from the receiver should go
to the pipe named "Example". The ``<Exit>`` tag defines the state in which processing can end. In our case, we have one state that we name "success". It can be referenced from pipes by its path "EXIT".

Pipes and forwards
------------------

We have a very simple pipeline that has only one pipe.
It reads:

.. code-block:: XML

   ...
   <FixedResultPipe name="Example" returnString="Hello World2">
     <Forward name="success" path="EXIT"/>
   </FixedResultPipe>
   ...

Pipes are predefined functions that can be performed on the incoming message. The ``<FixedResultPipe>`` ignores the input and outputs a fixed string that can be configured. We configure the ``name`` to be "Example". This satisfies the reference made in the ``firstPipe`` attribute in the ``<Pipeline>`` tag. Therefore, the (ignored) incoming message is the message we got from the receiver. The fixed output string we want is in the ``returnString`` attribute.

In the remainder of the :ref:`gettingStarted` chapter, we will see pipes with more interesting functions, like applying XSLT transformations and sending data to a database. In subsection :ref:`configurationSyntaxChecking` you will learn how to search the pipe you need.

The ``<Forward>`` within a pipe tag defines what should happen after the execution of that pipe. A forward consists of a forward
name and a path. Each pipe predefines the forward names from which it can send the output. For the fixed result pipe, the only
possibility is "success", but many pipes also have the possibility "failure". This allows Frank developers to handle errors and to have branching pipelines.

Our forward points to the path "EXIT", which is defined within the ``<Exit>`` tag as the only possible exit of the pipeline. In more
complex pipelines, there are also forwards that reference other pipes by their configured ``name`` attribute. It is also possible to have
multiple ``<Exit>`` tags within a ``<Pipeline>``.

.. NOTE::

   If you studied computer science or mathematics, the following may help. A pipeline is an example of a graph, with the pipes being the  nodes and the forwards being the edges. Before or after configuring the individual pipes and forwards, you name all allowed exit states of the pipeline. Each forward then either references a next pipe by its name, or names one of the defined exits to indicate the end of processing.

Conclusion
----------

You studied a simple adapter that is included as an example within the Frank!Runner. It has a receiver that allows us to trigger it. It has a pipeline with a single pipe that outputs a fixed message. In the next section, :ref:`helloTestPipeline`, we will see this adapter in action.