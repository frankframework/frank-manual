.. _propertiesSpecialChars:

Special characters
==================

The Frank!Framework does some subtle translations on properties. This also applies to credentials files that have the format of properties files, see :ref:`advancedDevelopmentAuthorizationSecrets`. The sequence ``\t`` is interpreted as a TAB character, ``\n`` as a newline and ``\r`` as a carriage return. The character ``\`` itself is represented as the sequence ``\\``. When you end a line with ``\``, the value of the property is taken to continue on the next line. See https://docs.oracle.com/cd/E23095_01/Platform.93/ATGProgGuide/html/s0204propertiesfileformat01.html for details.

This has an important consequence for passwords stored as secrets. Suppose that your Frank application accesses an external system. The operator of the external system tells you that the password is ``abcd\t``. When you would type ``abcd\t`` in ``credentials.properties`` then authentication would fail. The Frank!Framework would interpret the ``\t`` charachter as a TAB. The correct value to write in ``credentials.properties`` is ``abcd\\t`` to escape the ``\``.
