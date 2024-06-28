*Work in progress*

Streaming
=========

This section is about an implementation detail of the Frank!Framework. The Frank!Framework handles large messages differently from small messages to save memory usage - large messages are *streamed*. Usually Frank developers do not have to worry about streaming. However, some errors you may encounter have to do with streaming and hence you need some knowledge about it.

First, large messages are written to a temporary file before they are streamed. Under Linux, they are typically stored in the ``/tmp`` folder. If this folder is on a small disk partition, you may experience OutOfMemory exceptions. There is a property to configure the threshold for this behavior, ``xxx``. If a message is larger than ``xxx`` bytes, it is written to a temporary file and then streamed.

TODO: Find the right property name for ``xxx`` and the right comparison criterion.

Second, messages that are already in a file are not copied to a temp file before they are streamed. This typically applies to the contents of a file handled by a ``LocalFileSystemPipe``. This behavior is more general: the Frank!Framework has intelligence to determine whether a file has been stored already - it is only written to a temp file if it is not available otherwise.

Ladybug helps you to debug issues with streaming. Checkpoints about streamed messages are clearly shown to be so.

TODO: Add screenshot here.
TODO: What is different before 7.9 from the behavior from 7.9 and later?
