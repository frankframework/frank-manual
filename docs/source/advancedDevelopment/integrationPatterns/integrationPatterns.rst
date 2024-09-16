*Under construction*

.. _advancedDevelopmentIntegrationPatterns:

Integration Patterns and Data Integrity
=======================================

The Frank!Framework is used to connect different applications from different vendors. When some system A sends requests that should be processed by some other system B, the Frank!Framework can be used to transform A's requests to a requests that B can understand. The same is true about responses. If some system A receives requests from a system B, then the Frank!Framework can transform A's responses to a responses that B can understand. Enterprises usually have many applications, databases and queues that together support the business processes. The Frank!Framework typically sits in the middle to transform all requests and responses from systems that would otherwise be incompatible. All these interactions produce and maintain data that is critical to the success of the business.

This section explains how to protect the integrity of this data. Some of the cooperating systems might temporarily be unavailable. Applications being integrated may experience internal errors. A User may issue the same request multiple times while it is meant to be processed only once. For example when a user places an order, that specific order should be processed only once even if the webapplication sends the related HTTP request multiple times. To analyse these issues, the maintainers of the Frank!Framework consider two basic integration patterns:

* **Request / reply:** Some system A sends a request to a system B. System B handles the request immediately and sends back a response to A. The response reports whether the request could be processed successfully or whether an error occurred.

* **Fire and forget:** Some system A sends a request to a system B, but B does not handle the request immediately. B may send a response, but that response does not reveal whether the request could really be processed successfully. Another way to say this is that A sends an asynchronous request. A does not wait until processing the request has been finished before proceeding. This pattern is useful if system A has to produce quick feedback to some upstream system or user. Or when B needs a long time to process A's request. This does not mean that A will never know whether the request was processed successfully. Eventually, some system may issue a request to A that reports about the success or failure of the original request.

This section introduces concepts and features of the Frank!Framework to implement these two integration patterns.

.. toctree::
   :maxdepth: 3

   onlyOnce
   transactions