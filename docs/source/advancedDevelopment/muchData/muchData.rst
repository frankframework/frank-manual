*Work in progress*

About large messages
====================

The Frank!Framework treats large messages in a special way to save memory. Frank developers sometimes need some knowledge about this to fix issues with their Frank applications. There is a property ``message.max.memory.size`` to configure the threshold: messages larger than this size are treated specially. Large messages are written to a temporary file before they are processed. Under Linux, they are typically stored in the ``/tmp`` folder. If this folder is on a small disk partition, an OutOfMemory Java exception may result. As an exception, messages that are already in a file are not copied to a temp file before they are processed. This exception typically applies to the contents of a file handled by a ``LocalFileSystemPipe``. This exception is more general: the Frank!Framework has intelligence to determine whether a file has been stored already - it is only written to a temp file if it is not available otherwise.

TODO: What is different before 7.9 from the behavior from 7.9 and later?
