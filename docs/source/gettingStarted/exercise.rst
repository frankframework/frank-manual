.. advancedDevelopmentExercise:

Exercise
========

This page provides an exercise to work with the material of this chapter. It does not provide detailed instructions what to do. Doing this exercise will help you to write your own Frank applications.

The assignment is about a fictive company Conclusion that offers pension services. Customers can save for their pension. From the saved money, Conclusion pays them a monthly allowance when they reach retirement. Customers of Conclusion should receive a yearly overview by paper mail. They also have access to a webportal in which this mail is archived.

Conclusion has outsourced marking up and sending letters to customers. These services are provided by Gilgamesh, a company named after one of the first stories written by mankind. Conclusion also does not manage its own webportal. The webportal is managed by a company Mundo. These three companies cooperate as follows:

#. Conclusion and Gilgamesh have access to a Windows network share. The share is not accessible by Mundo.
#. When Conclusion has a message for a customer, it sends an XML file with the data to Gilgamesh and stores the XML as a file on the share.
#. Gilgamesh creates a PDF with the letter that is sent to the customer and places the PDF on the file share. In this exercise, we simplify this by working with text files - this makes testing easier for you.
#. Conclusion polls the file share regularly.
#. When there is a combination of an XML message and its related PDF letter (text file), Conclusion transforms this information into a HTTP request that can be processed by Mundo.

You are not asked to implement all these steps. The exercise is only about programming the last step - Conclusion's processing of documents given in XML documents and text files.

Each message that Conclusion sends to Gilgamesh has a unique ID that is a string consisting of lower-case letters, upper-case letters and digits. The filename of an XML file is ``<ID>.xml``, so if the ID is ``abc123``, then it is stored as file ``abc123.xml``. The PDF produced by Gilgamesh is then stored as ``abc123.txt``. The part before the dot, the base file name, is common to the XML file and the PDF file.

Here is an example of an input XML message to be processed:

.. literalinclude:: ../../../srcSteps/exercise/v500/tests/Conclusion/valid.xml
   :language: xml

All elements of this request have namespace ``http://frankframework.org/manual/exercise/conclusion``.

This message should be transformed according to the following:

* Mundo needs an XML in which every element has namespace ``http://frankframework.org/manual/exercise/mundo``.
* The ``<to>`` and ``<cc>`` elements are wrapped inside a ``<header>``.
* The ``<accountId>``, ``<email>``, ``<street>``, ``<houseNumber>``, ``<city>``, ``<zip>`` and ``<country>`` inside ``<to>`` and ``<cc>`` elements remain the same apart from the namespace.
* The ``<firstName>`` and ``<lastName>`` elements of a Conclusion request are not copied. Their values are combined and the resulting string is wrapped in an element ``<displayName>``.
* The ``id`` attribute of the ``<document>`` element of the Conclusion request reappears in the ``<document>`` element posted to Mundo.
* The Mundo request has an element ``<body>`` that is a brother of the ``<header>`` element. The value of that element is the message of the PDF file encoded as Base 64 string. In the exercise this is text data but we keep for the exercise that Base 64 encoding is necessary. To help you, the Mundo application in Frank2Example checks that the Base 64 decoded body, that should be plain text because the exercise works with text instead of PDF, contains the word ``document``.

Here is an example of a valid request to Mundo, although the values may not match the values in the shown Conclusion request:

.. literalinclude:: validMundo.xml
   :language: xml

You are asked to write a Frank application that takes the base name of an XML / text file pair and sends the information to Mundo. The Frank!Framework organisation provides a webapp that plays Mundo's part. Access it with the following URL: https://frank2example.frankframework.org/api/mundo. The following steps will guide you:

* The input message is the base file name. Have a receiver with a JavaListener to capture that input.
* Read the XML file using a LocalFileSystemPipe. Check the Frank!Doc to learn how to use this pipe.
* Check the syntax of the XML file. You can do so by creating an XML Schema document. Use an XmlValidatorPipe to apply that XML schema document.
* Read the text file, also with a LocalFileSystemPipe. You need session keys to hold the XML document and the text file contents before they are combined. You can use the PutInSessionPipe to store information in session keys. To work with this pipe you need parameters. Please read the Frank!Doc page about a Param element carefully - it contains information you will probably need.
* Base64 encode the contents of the text file. You can do so using the Base64Pipe.
* Transform the contents of the XML file to the format needed by Mundo. Do this using an XSLT transformation that takes the XML file's contents as the main message and the base64'd text data as a parameter. The transformation you write should be applied using an XsltPipe.

  .. NOTE::

     You are recommended to study XSLT thoroughly before writing the XSLT transformation that is requested here. If you have a good command of XSLT, you will be able to keep the XSLT transformation concise.

* Send the message to Mundo. You need a SenderPipe that has a HttpSender as child element.
* Your pipe should have three exits. One possibility is that the input was valid and that it was processed successfully by Mundo. The second possibility is that the input was invalid. In this case, no attempt should have been made to contact Mundo. The last possibility is that Mundo was not accessible. Give each of these possibilities its own ``<Exit>`` and take care that your adapter always exits with the correct exit.

Test your work using the Frank!Console's Test a Pipeline screen. Please also spent some time on your development environment. Put your code into version control. Set up your project such that it can be run from within Visual Studio Code. You can do this using Ant. See https://github.com/ibissource/frank-runner for help.

.. NOTE::

   You do not have the complete solution that Conclusion needs at this stage. In chapter :ref:`advancedDevelopment`, a section will be added with additional instructions. You will learn what functionality is still missing and you will get directions for creating it.
