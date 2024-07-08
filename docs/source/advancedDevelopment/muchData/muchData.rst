*Work in progress*

About large messages
====================

The Frank!Framework has a few features to properly handle large messages. Usually Frank developers do not have to bother, but sometimes knowledge about these features is needed to resolve errors. These features are:

* Storing large messages on disk.
* Streaming.

**Storing large messages on disk**

In order to improve memory management while not impacting the performance too much the Frank!Framework may store (large) messages on disk instead of in memory. Especially when dealing with large messages this may greatly improve performance, but it comes with the caveat that more disk IO is required. The property ``message.max.memory.size`` may be used to configure the threshold (in bytes) in the Frank!Framework. By default this has been set to 5MB, files under this threshold are stored in memory, and files larger are persistent to disk. When an application has a high volume of smaller sized traffic it may be beneficial to set the threshold to 30MB so files are kept longer in memory. The Frank!Framework only preserves messages on disk when it needs to, for example when the message can be read multiple times and does not already have a pointer to disk.

Files stored on disk are stored in ``${java.io.tmpdir}/${instance.name}/temp-messages/`` and are cleaned up automatically.

.. WARNING::

   If there is not enough disk space available the application will throw an exception or log a warning!

**Streaming**

The Frank!Framework in general `streams` messages flowing through a pipeline. This means that the Frank!Framework only holds in memory the bytes it is currently working with, not entire messages. This helps the Frank!Framework to process large messages without getting out of memory, but there is a caveat. The caveat is related to XSLT processing. When XSLT version 2.0 or version 3.0 is being applied (attribute ``xsltVersion=2`` or ``xsltVersion=3``), then XSLT processor Saxon is used. This XSLT processor does not support streaming. This means that if some message is transformed using an XSLT transformation and if XSLT version 2.0 or 3.0 is used for this, then the entire message has to be stored in memory. This can cause an out of memory exception for large messages.

This issue can be fixed by using ``xsltVersion=1``. In that case, XSLT processor Xalan is used. Xalan does implement streaming and hence large messages can be processed without memory issues. The price to pay is that XSLT 1.0 is less feature-rich than version 2.0 and version 3.0, making it harder to code the intended XSLT transformation. Most XSLT processing senders and pipes use Saxon by default. The exception is the ``ForEachChildElementPipe``. That pipe uses Xalan by default. This exception has been made by WeAreFrank! because the ``ForEachChildElementPipe`` is meant to iterate over large messages.
