.. _frankConsoleDiskUsage:

Disk Usage
==========

In section :ref:`frankConsoleLadybug` and section :ref:`frankConsoleLogs`, you encountered two features of the Frank!Framework that sometimes use a lot of disk space. In this section, you will learn how to control disk space usage. You can best do this section after doing section :ref:`frankConsoleScheduling`. In that section, you schedule a job that is executed every minute.

Please do the following:

#. In the main menu, go to "Environment Variables" as shown below.

   .. image:: mainMenuEnvironmentVariables.jpg

#. You see the page shown below. You get confirmed that you are in the Environment Variables page (number 1). To the top, you see a panel "Dynamic parameters" (number 2).

   .. image:: diskUsageDynamicParameters.jpg

#. Initially, the "Log Level" should be "DEBUG". Adjust it to "INFO" (number 3).

   .. NOTE::

      The initial value of the log level is controlled by the parameters you supply when starting the Frank!Framework. Please consult a Frank developer for details. In production, the initial value of the "Log Level" is typically "INFO", "WARN" or "ERROR".

#. Initially, "Enable Ladybug Debugger" checkbox should be checked. Please uncheck it (number 4).
#. Press "Send" (number 5).

You have adjusted the minimum loglevel to "INFO", causing lines with log level "DEBUG" to be omitted from the logfiles. You have also disabled Ladybug. Executing an adapter will no longer result in a test report in Ladybug. Please check these statements as follows:

6. Please wait for about two minutes, making sure that "adapterCheckExpiration" has run. You scheduled this adapter to run every minute in section :ref:`frankConsoleScheduling`.
#. In the main menu, please select "Logging". Then open logfile "frank2manual.log".
#. Verify that you do not see recent messages with log level "DEBUG".
#. Search for the string "expired apartments". You need the last occurrence of "There were n expired apartments" with "n" some number. Note the timestamp of this line.
#. In the main menu, go to Testing | Ladybug. You see the following page:

   .. image:: diskUsageLadybug.jpg

#. You are confirmed you are in Ladybug (number 1). Ensure you are in tab "Debug" (number 2).
#. Press "Refresh" (number 3). Check that there is no Ladybug test report with the timestamp you noted.
#. Press "Options..." (number 4). You see the following dialog:

   .. image:: diskUsageLadybugOptions.jpg

#. Check that "Report generator enabled" is "No" (number 1). You see that this value mirrors the "Enable Ladybug Debugger" value you configured in step 4.
#. If you like, you can also update this setting here.
#. Close the dialog (number 2).

The updates you apply in the "Dynamic parameters" panel within Environment Variables are not persistent, which means that your changes are undone by restarting the Frank!Framework. Adjusting the "Report generator enabled" setting within Ladybug also is not persistent. Please verify this by restarting the Frank!Framework and selecting "Environment Variables" from the main menu.