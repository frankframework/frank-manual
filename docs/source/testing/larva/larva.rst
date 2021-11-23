.. _testingLarva:

Larva
=====

This section is about Larva, the second tool you can use to test Frank configurations. Larva is intended for Frank developers. Before studying this section, please study chapter :ref:`gettingStarted` first. That chapter already gives you a quick introduction to Larva.

This section gives you a deeper insight into Larva. To understand it, please step back a moment and consider the purpose of the Frank!Framework. The Frank!Framework is mainly a tool to integrate other software packages. Typically, a company uses many different software systems. These systems have interfaces that allow them to cooperate with other systems (e.g. REST APIs, SOAP interfaces), but the systems have not been designed to cooperate within the context of a specific customer. To integrate the systems, you need an additional layer of software that connects them. When you talk about testing Frank configs, you talk about testing this integration layer.

It requires many resources in terms of time, networks and servers to set up integration tests. You need test installations of the systems being integrated. You also need to connect these copies like they are connected in production, requiring you to set up web servers, databases and queues. Typically, your team uses two copies: the development environment (D) and the test environment (T). Features under development are tested on the development environment. When your team considers a release to the customer, final tests are performed on the test environment. Then the customer tests on an acceptance environment (A) before bringing your work to production (P). This makes the DTAP environment, the infrastructure for integration testing and production.

Integration test environments are precious and scarse, so you need unit tests. A unit test tests a small piece of your configuration, typically an adapter, in isolation. Another reason you want unit tests has to do with the complexity of your adapters. A complex adapter can handle multiple types of input that each have to be processed in a different way. There are multiple program flows. When an integration test executes multiple adapters, the number of possible program flows grows exponentially. Integration tests do not allow you to test the detailed requirements of each adapter. To do this, you need to test each adapter in isolation. Larva allows you to test each of your adapters in isolation, which means that it is a tool to write unit tests.

The beginning of this section, subsections :ref:`testingLarvaStubbing` and :ref:`testingLarvaServices`, is a tutorial. It is about a fictive bank, the Rotterdam Bank, that has to integrate two third-party systems. You will test a Frank configuration that has been written to connect them. There are instructions allowing you to get hands-on experience, but you will not miss information if you just read along. The end of this section, subsections :ref:`testingLarvaIgnores` and :ref:`testingLarvaConsole`, contains reference material.

Here is the table of contents:

.. toctree::
   :maxdepth: 3

   stubbing
   services
   ignores
   larvaConsole

