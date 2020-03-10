Troubleshooting
===============

This chapter lists some errors you may encounter and presents how to fix them.

Adapter status page ManageDatabase error
----------------------------------------

**Problem:** This section is about an error you may see in the Adapter Status page. The error is as shown below:

.. image:: manageDatabaseErrorInitializingPipeline.jpg

The adapter named ``ManageDatabase`` gives an error.

**Solution:** You did not add this adapter yourself. This adapter is part of the Frank!Framework. You see here that the Frank!Framework fails to start. This happens when your file names are lowercase. For example, when your files are named ``deploymentspecifics.properties`` and ``configuration.xml`` instead of ``DeploymentSpecifics.properties`` and ``Configuration.xml``, then this error occurs. Correct your file names to fix the issue.