*Work in progress*

About large messages
====================

In order to improve memory management while not impacting the performance too much the Frank!Framework may store (large) messages on disk instead of in memory. Especially when dealing with large messages this may greatly improve performance, but it comes with the caveat that more disk IO is required. The property ``message.max.memory.size`` may be used to configure the threshold (in bytes) in the Frank!Framework. By default this has been set to 5MB, files under this threshold are stored in memory, and files larger are persistent to disk. When an application has a high volume of smaller sized traffic it may be beneficial to set the threshold to 30MB so files are kept longer in memory. The Frank!Framework only preserves messages on disk when it needs to, for example when the message can be read multiple times and does not already have a pointer to disk.

Files stored on disk are stored in ``${java.io.tmpdir}/${instance.name}/temp-messages/`` and are cleaned up automatically.

.. WARNING::

   If there is not enough disk space available the application will throw an exception or log a warning!




TODO: What is different before 7.9 from the behavior from 7.9 and later?
