.. _propertiesReference:

How To Reference Properties
===========================

The following ``Configuration.xml`` file demonstrates how to reference properties within you Frank configuration:

.. include:: ../../../../src/advancedDevelopmentProperties/classes/ConfigurationReferenceProperties.xml
   :emphasize-lines: 8

The highlighted line shows that properties are referenced by surrounding the property name with ``${`` and ``}``. The Frank!Framework replaces property references by the values of the referenced properties. If this configuration is deployed in DTAP stage ``LOC`` and if property ``my.text`` equals ``My text is Hello``, then the output will be: ::

   From stage LOC, I say My text is Hello
