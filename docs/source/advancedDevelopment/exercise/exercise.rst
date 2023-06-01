.. advancedDevelopmentExercise:

Exercise
========

This page provides an exercise to work with the material of this chapter and of :ref:`gettingStarted`. It does not provide detailed instructions what to do. Instead, you are asked to study the other pages of the Frank!Manual and the Frank!Doc. WeAreFrank! hopes that doing this exercise will help you to write your own Frank applications.

The assignment is about a fictive company Conclusion that offers pension services. Customers can save for their pension. From the saved money, Conclusion pays them a monthly allowance when they reach retirement. Customers of Conclusion should receive a yearly overview by paper mail. They also have access to a webportal in which this mail is archived.

Conclusion has outsourced marking up and sending letters to customers. These services are provided by Gilgamesh, a company named after one of the first stories written by mankind. Conclusion also does not manage its own webportal. The webportal is managed by a company Mundo. These three companies cooperate as follows:

#. Conclusion and Gilgamesh have access to a Windows network share. The share is not accessible by Mundo.
#. When Conclusion has a message for a customer, it sends an XML file with the data to Gilgamesh and stores the XML as a file on the share.
#. Gilgamesh creates a PDF with the letter that is sent to the customer and places the PDF on the file share. In this exercise, we simplify this by working with text files - this makes testing easier for you.
#. Conclusion polls the file share regularly.
#. When there is a combination of an XML message and its related PDF letter (text file), Conclusion transforms this information into a HTTP request that can be processed by Mundo.

Each message that Conclusion sends to Gilgamesh has a unique ID that is a string consisting of lower-case letters, upper-case letters and digits. The filename of an XML file is ``<ID>.xml``, so if the ID is ``abc123``, then it is stored as file ``abc123.xml``. The PDF produced by Gilgamesh is then stored as ``abc123.txt``. The part before the dot, the base file name, is common to the XML file and the PDF file.

All processing is done in some subdirectory ``base`` in the file share. Incoming files are put in subdirectory ``base/input``. After successful processing, the files should be moved to ``base/processed``. When an error occurs, the files should be moved to ``base/error``.

Here is an example of an input XML message to be processed:

.. literalinclude:: ../../../../srcSteps/exercise/v500/tests/Conclusion/valid.xml
   :language: xml

All elements of this request have namespace ``http://wearefrank.nl/manual/exercise/conclusion``.

This message should be transformed according to the following:

* Mundo needs an XML in which every element has namespace ``http://wearefrank.nl/manual/exercise/mundo``.
* The ``<to>`` and ``<cc>`` elements are wrapped inside a ``<header>``.
* The ``<accountId>``, ``<email>``, ``<street>``, ``<houseNumber>``, ``<city>``, ``<zip>`` and ``<country>`` inside ``<to>`` and ``<cc>`` elements remain the same apart from the namespace.
* The ``<firstName>`` and ``<lastName>`` elements of a Conclusion request are not copied. Their values are combined and the resulting string is wrapped in an element ``<displayName>``.
* The ``id`` attribute of the ``<document>`` element of the Conclusion request reappears in the ``<document>`` element posted to Mundo.
* The Mundo request has an element ``<body>`` that is a brother of the ``<header>`` element. The value of that element is the message of the PDF file encoded as Base 64 string. In the exercise this is text data but we keep for the exercise that Base 64 encoding is necessary. To help you, the Mundo application in Frank2Example checks that the Base 64 decoded body, that should be plain text because the exercise works with text instead of PDF, contains the word ``document``.

Here is an example of a valid request to Mundo, although the values may not match the values in the shown Conclusion request:

.. literalinclude:: validMundo.xml
   :language: xml

You are asked to write a Frank application that polls the share (for simplicity on your local file system) and sends the data to Mundo (WeAreFrank! provides a webapp that plays Mundo's part). The final result will be a pretty advanced Frank application. The following steps will guide you:

1. Create an adapter that processes a single letter. The adapter should do the following:

   * The input message is the base file name. You can use a ``<JavaListener>`` in your receiver because this adapter will be called by another adapter in later steps.
   * Read the XML file.
   * Check the syntax of the XML file. You can do so by creating and using an XML Schema document.
   * Read the PDF file.
   * Base64 encode its contents.
   * Transform the contents of the XML file to the format needed by Mundo. Do this using an XSLT transformation that takes the XML file's contents as the main message and the base64'd PDF data as a parameter.
   * Send the message to Mundo.
   * Move the input files to ``base/processed`` or ``base/error`` depending on whether or not there are errors. What forward can you use to handle errors?

   Test your work using the Frank!Console's Test a Pipeline screen.

2. Create an adapter that polls the file share. It only has to look for PDF files because XML files from Conclusion are always written before PDF files from Gilgamesh. Polling a directory can be done with a ``LocalFileSystemPipe``. Scheduling when to poll is done in step 3. Your adapter has to do the following:

   * Take a dummy argument. What listener do you then need in your receiver?
   * Use a ``LocalFileSystemPipe`` to get a list of all PDF files on the share.
   * Iterate over these PDF files to process them each using the adapter of step 1.

   .. NOTE::

      You may have considere using a DirectoryListener. That listener is triggered when a new file appears. With this listener, you do not have to poll the input directory. The DirectoryListener also moves files to processed or error directories automatically. This approach is not chosen here because only the .pdf files would be handled automatically. You still would have to code moving the .xml files. Having two different mechanisms to move the files is more complicated than doing all file manipulations explicitly as is proposed here.

3. Extend your work with a ``<Scheduler>`` to schedule when the file share is polled. Introduce a Boolean variable ``polling.active`` that depends on the DTAP stage. When it is false, polling is disabled for testing purposes. When it is true, polling is done like is the case in production. What attribute of which element do you need to make this variable effective? How do you set this variable for each specific DTAP stage?

4. Extend your outer adapter such that files that are in the process of being written are ignored. In a real-world system, writing a .pdf file to the file share may take some time. The aim is to prevent the following sequence of events:

   * Gilgamesh connects to the file share and starts writing a .pdf file.
   * Before writing is complete, your adapter starts processing files and it tries to read the .pdf file. It gets corrupt data because writing is not finished.
   * Writing the file by Gilgamesh finishes.
   * Mundo receives invalid data that is based on an improperly read .pdf file.

   Implement this using an XSLT stylesheet that compares a file's timestamp to the time when your adapter starts. The XSLT should omit files for which the timestamp is too close to the reference time. Use a variable for the threshold of the time difference that can be configured in property files or by the system administrator of the deployment environment.

5. Your present adapter has a serious drawback. If processing a letter fails, the adapter polling the input directory aborts. The remaining letters that are ready for processing are skipped. Fix this issue by letting the two adapters communicate asynchronously. The calling adapter should put the base names of the found files on a queue, each base name in a separate message. The called adapter is triggered separately for every message on the queue. If the calling adapter fails, the error does not propagate to the calling adapter. Therefore the calling adapter will always process all files it has observed. Do this by using a ``MessageStoreSender`` and a ``MessageStoreListener``. When the called adapter generates an error, a message is written to the error store that comes with your ``MessageStoreListener``. Operators that have access to the Frank!Console will be able to retry base file names stored in the error store. At this stage, you can prevent your adapter from filling the error store because the related files will be in inaccessible - they are moved to ``base/error``.

6. Make error handling more smart by taking into account the difference between technical errors and invalid input. If a received letter or its XML metadata is invalid, retrying does not make sense. If your HttpSender gets a negative response from Mundo then the reason may be a temporary network error or server error of Mundo. In that case retrying makes sense. Adjust your adapter to achieve the following:

   * If the called adapter's HttpSender fails in some way, do not move the XML file and do not move the PDF file. Instead, keep the base file name as a message in the error store.
   * If some other error occurs, do not write the error store and move the files to directory ``base/error``.
