.. _deploymentDtapAndInstance:

The instance name and the DTAP stage
====================================

This section describes two basic properties you have to set as a system administrator: ``instance.name`` and ``dtap.stage``. Property ``instance.name`` is a name for the set of configurations that is hosted on a single server or on a group of servers running in parallel. The Frank!Framework uses this name in many ways, so it is important that you provide it.

Property ``dtap.stage`` is about the life cycle of a Frank config. During this life cycle, a Frank is typically deployed on different servers (or server groups). During its development, the config lives on the development environment (D). When the developers consider releasing, they bring their work to another environment, the test environment (T). When the tests are successful, the Frank config is released to the customer. The customer should do acceptance tests on a dedicate environment (A). Only after acceptance testing succeeds, the work should go to production (P). These four letters form the famous DTAP acronym. The Frank!Framework uses an extra (fifth) stage: ``LOC``, the local development computer of a single developer. Please note that ``instance.name`` is usually the same for each DTAP stage.

As a system administrator, you have to set the DTAP stage by setting the system property ``dtap.stage``. The allowed values are ``LOC``, ``DEV``, ``TST``, ``ACC`` and ``PRD``.

Frank developers can make their application dependent on the DTAP stage. This may help you to configure different databases and different queues for each DTAP stage. Please contact the developer of the Frank application for more information.