.. |eup| unicode:: U+00e9
.. |edown| unicode:: U+00e8
.. |euro| unicode:: U+20AC
.. |japanese_ma| unicode:: U+307E

.. _propertiesSpecialChars:

Special characters
==================

This subsection presents some details about properties files and files containing secrets (see :ref:`advancedDevelopmentAuthorizationSecrets`). This material is important for you if:

* You use the ``\`` character in property names, property values or secrets.
* You use non-ASCII characters like |eup|, |edown|, |euro| or |japanese_ma| in property names, property values or secrets.

The Frank!Framework reads properties in two steps:

* It reads the raw bytes of the file and interprets them as a character string.
* It parses the character string as the list of name/value pairs.

To interpret bytes as characters, computers use character encodings like UTF-8, UTF-16, EBCDIC and CP437. When two character strings are compared that were parsed from a different character encoding, characters that look similar may be considered different. For example, when you specify a password in a file with one encoding and when you type the password in a terminal that applies another encoding, your password can unexpectedly be rejected. Encodings whose name start with "UTF-" are *unicode* character encodings. Character strings that were parsed with different unicode character encodings can be compared. Text files encoded with a unicode character encoding can start with special characters, the byte order mark, that specify which unicode character encoding applies. If the Frank!Framework reads a text file that has no byte order mark, it is interpreted as UTF-8. The Frank!Framework can only interpret byte order marks for UTF-8, UTF-16 little endian and UTF-16 big endian (the difference of the latter two is about the order of the bytes of a 16-bit value - highest or lowest byte first).

When a character stream is interpreted as a series of name/value pairs, character ``\`` has a special meaning. ``\n`` is interpreted as a newline, ``\r`` is interpreted as a carriage return and ``\t`` is interpreted as a tab. The character ``\`` itself is represented as ``\\``. See https://docs.oracle.com/cd/E23095_01/Platform.93/ATGProgGuide/html/s0204propertiesfileformat01.html for more details. Empty lines and lines starting with a ``#`` are ignored - the latter can be used as comments.
