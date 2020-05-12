.. _frankConsoleScheduling:

Scheduling
==========

.. highlight:: none

This section explains how to schedule tasks for periodic execution. This is very useful for batch processing jobs. You can also schedule tasks to do sanity checks of your site. You will practice with a sanity check for the database of the imaginary company New Horizons, see section :ref:`frankConsoleNewHorizons`.

In section :ref:`frankConsoleConfigsUploading`, you saw two versions of the NewHorizons configuration. In the second version, we added the column "MODIFICATIONDATE" to the database table "product". We also added an adapter that checks whether apartments within the "product" table are up-to-date. An apartment is up-to-date if its modification date is less than two minuts ago.

If you just did the previous section :ref:`frankConsoleConfigsUploading`, you do not have to do anything to prepare yourself. Otherwise please do the following:

#. Ensure that the second version of the NewHorizons config is running. Here is the :download:`download link <../downloads/configurations/forFrankConsole_2.zip>` again. It is not important whether you are uploading your config to the database or whether you have it on the file system.
#. Ensure that the directories ``work\input``, ``work\processing``, ``work\processed`` and ``work\error`` do exist and are empty.
#. Ensure that database table "product" is empty.

Now that you are prepared, please continue as follows:

#. Restart the Frank!Runner. Choose your command-line from the previous sections based on wether you are uploading your configs to the database. After your chosen command line, you have to add ``-DloadDatabaseSchedules.active=true``. For example, when you are uploading your configs to the database, you do: ::

     franks\frank-runner> start.bat -Djdbc.migrator.active=true -Dconfigurations.names="${instance.name.lc},NewHorizons" -Dconfigurations.NewHorizons.classLoaderType=DatabaseClassLoader -Dwork=work -DloadDatabaseSchedules.active=true

#. In the main menu choose "Scheduler" as shown:

   .. image:: mainMenuScheduler.jpg

#. You see a lot of details about the scheduler component of the Frank!Framework, see the figure below. You see that you are in the scheduler page (number 1). You also have the option to pause the scheduler (number 2). To the top-right, there is a button "Add new schedule" (not shown).

   .. image:: schedulingPauseButton.jpg

#. You need a string that defines how often you want to run your adapter. To get that string, you have to know that the scheduler of the Frank!Framework uses a Java component called "quartz". When you search the internet for "quartz expression", you may find the following site: https://www.freeformatter.com/cron-expression-generator-quartz.html.
#. Here you can specify that you want to run your task every minute. The site will give you the string ``0 * * ? * * *``. You will use it later.
#. Press the "Add new schedule" button. You see the page shown below:

   .. image:: schedulingUploadSchedule.jpg

#. Fill in the string you found in step 5. You should put it in the text field annotated with number 1.
#. Select adapter "adapterCheckExpiration" (number 3) and the only possible listener "listenerCheckExpiration" (number 4). In a realistic situation, you should ask a Frank developer for these names.
#. Put something in the "Message" field.
#. Leave check box "Store in Database" checked. This way, your schedule remains active after you restart the Frank!Runner.
#. Press "Save". To the top, a green bar should appear.
#. To the top-right, there is a button "Back". Please press it.
#. You are back in the main page of the scheduler. Now there is a job group "NewHorizons" as shown below:

   .. image:: schedulingJobGroupNewHorizons.jpg

You can see when your adapter was executed last and when it will fire next. You can see that there is one minute between these times as you intended. Now you will examine what your job is doing.

14. In the main menu, go to "Logging". search for the messate "There were 0 expired apartments" with log level "INFO". The loglevel should have a time stamp with seconds "00".

**Exercise:** Use the NewHorizons config to enter some apartments like you did in the previous sections of this chapter. After about three minutes, you should see a messages with log level "ERROR" and text "There were n expired apartments" with n the number of apartments you entered.

.. NOTE::

   Frank configs that write to the logfile can be used to set up a monitoring page. There are tools in the market that scan logfiles and build a dashboard with monitoring information. An example is Splunk, https://www.splunk.com.