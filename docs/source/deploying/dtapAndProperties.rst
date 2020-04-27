.. _deploymentDtapAndProperties:

The DTAP stage and setting properties
-------------------------------------

In the previous sections :ref:`deploymentTomcat4Frank` and :ref:`deploymentTomcat`, you learned how to get the Frank!Framework running. This section and the next are about fine-tuning the Frank!Framework. The details of your application server are not so important anymore; you can read this section without understanding the previous.

As a system administrator, you should understand the life cycle of a Frank config. During this life cycle, a Frank is deployed on different instances of the Frank!Framework. During its development, the config lives on the development environment (D). When the develpers consider releasing, they bring their work to another instance of the Frank!Framework, the test environment (T). When the tests are successful, the Frank config is released to the customer. The customer should do acceptance tests on a dedicate Frank!Framework instance (A). Only after acceptance testing succeeds, the work should go to production (P). These four letters form the famous DTAP acronym. At WeAreFrank! we add a fifth letter, L, the local development computer of a single developer.

As a system administrator, you have to set the DTAP stage by setting the system property ``dtap.stage``. You already did this in section :ref:`deploymentTomcat`. The allowed values are ``LOC``, ``DEV``, ``TST``, ``ACC`` and ``PRD``. If you use the Frank!Runner, you get DTAP stage "LOC" by default.

Remember that there are two methods to set system properties when you are using Apache Tomcat:

#. You can set Java properties with the command line that starts Apache Tomcat or the Frank!Runner. You use command-line arguments like ``-D<property-name>=<value>``, for example ``-Ddtap.stage=ACC``. If you have spaces in your value, add quotes.
#. You can add properties to the text file ``<tomcat root>/conf/catalina.properties``.

There are many more properties than "dtap.stage" that have impact on the Frank!Framework, but you do not have to know much about them. Frank!Developers are responsible for setting them. They can configure different properties for different DTAP stages, allowing them to do a lot of fine-tuning for you already. Occasionally, a Frank developer may ask you to set a property when you are cooperating to fix an issue. The Frank developer should understand the impact in this case.
