.. _introduction:

Introduction
============

Ladybug is one of the two test tools offered by the Frank!Framework.
The proceeding subsections show you how to use Ladybug. The text is
written as a tutorial, but feel free to just read this material
and try it yourself.

If you use this text as a tutorial and if you want to follow the
given instructions, you should apply the instructions in
:ref:`preparations`. This subsection explains how to set up
the environment you need.

This tutorial is based on an electronic archive that WeAreFrank! built
for one of their customers. The archive has a portal before it that
handles requests from users. The portal accesses the archive
to service the user.

WeAreFrank! cannot give everyone access to the real archive. Therefore,
a very simple emulator of this archive is supplied within this
manual. A download link is available in :ref:`preparations`. The code
provides the portal and the archive. The archive is capable of
archiving a document and searching a document by id. When you archive
a document, you get the document id you need to find it back. When you
request a document by id, you get the document.

This emulator is very simple. In practice there is no error checking
whatsoever and the responses are fixed values. But this is good
anough for demonstrating Ladybug. Let's continue!