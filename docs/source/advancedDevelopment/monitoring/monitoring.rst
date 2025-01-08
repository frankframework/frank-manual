.. _deploymentMonitoring:

Monitoring
==========

Operators and system administrators want to monitor the status of their Frank application. The Adapter Status page shows general information. The Frank!Framework also allows operators and Frank developers to define custom monitoring information. This is partly done in the Frank!Console and it is partly done by editing ``Configuration.xml`` (or files included by ``Configuration.xml``). Defining and using monitoring information is the subject of this page.

.. WARNING::

   This feature of the Frank!Framework only works if property ``monitoring.enabled`` is ``true``. This should be the default. In case your monitors do not work, consider setting ``monitoring.enabled=true`` explicitly.

Concepts
--------

The central concept of monitoring is a *monitor*. A monitor can be or not be in state *raised*. A monitor has a list of triggers that can change the raised / not raised state of a monitor. Triggers come in two flavors. Alarm triggers cause a monitor to enter the raised state. Clearing triggers cause a monitor to leave the raised state (be cleared). Each trigger has a list of events, for example ``Pipe Exception`` or ``Receiver Shutdown``. Each trigger can also have a threshold (a number) and a period (time interval in seconds). The effect of these two is explained in more detail later.

A monitor can also have *destinations*, actions that are performed when the monitor is raised. Destinations can for example be used to write messages in the log file or to send an email to someone.

Each monitor is specific for a single Frank configuration. When a Frank application has multiple configurations, only events that occur in the configuration that owns the monitor affect it. Triggers can be configured to further limit the scope. It is possible to configure triggers so that only events within specific adapters take effect.

A tour of defining and using a monitor
--------------------------------------

For Frank developers, defining monitors is different from writing the other parts of Frank configurations. The reason is that the Frank!Console is needed to develop monitors. This is the case because the set of events that can be added to triggers is only available in the Frank!Console. On the other hand, the Frank!Console does not help to define destinations, only to choose them within definitions of monitors.

Defining a destination
----------------------

As a starting point of the tour we take a Frank application with two configurations, namely ``MonitorContainer`` and ``OnMonitorTriggered``. We are defining our monitor in configuration ``MonitorContainer``. We start by defining a destination that triggers an adapter in configuration ``OnMonitorTriggered``. Here is the ``Configuration.xml`` of ``MonitorContainer`` including the destination:

.. literalinclude:: ../../../../srcSteps/Frank2Monitoring/v500/configurations/MonitorContainer/Configuration.xml
   :language: xml
   :emphasize-lines: 21-25

All definitions about monitoring appear in XML element ``<Monitoring>``. There is only one kind of destination, which is the ``<SenderMonitorAdapterDestination>``. There are no other XML elements (you can use ``<Destination classname="org.frankframework.monitoring.SenderMonitorAdapter">``, but that does the same). Within this element, you put the sender that will receive a message when the monitor is raised. We choose to trigger a Pipeline through its listener named ``OnMonitorTriggered``. That called adapter just writes a line to the log file, but the example illustrates that any action can be performed by a destination.

.. WARNING::

   It is mandatory to give each destination a name. It is not sufficient if only the sender inside the destination has a name.

Defining the monitor in the UI
------------------------------

Next, we define the monitor in the UI. First we select "Monitoring" in the main menu:

.. IMAGE:: mainMenuMonitors.jpg

The following screen appears:

.. IMAGE:: tabMonitoring.jpg

There is a separate tab for each configuration and there is a button to create a monitor. We use it to create our monitor in configuration ``<MonitorContainer>``. The monitor just gets a name as shown below:

.. IMAGE:: monitorCreated.jpg

Apart from the name of the monitor, you see the following:

* There is a tag "TECHNICAL". You can change this tag to provide visual information about the purpuse of the monitor. The possible tags are "TECHNICAL", "FUNCTIONAL", "HEARTBEAT" and "CLEARING".
* There is a green line. The line will be red if the monitor is raised.
* Above the monitors, there is a message stating how many monitors are raised.

To continue defining the monitor, we press its edit button:

.. IMAGE:: editingMonitor.jpg

This screen allows us to select or not to select destinations. It also allows us to change tag "TECHNICAL" to something else. And it allows us to define the triggers. For simplicity, we define only one trigger as shown below:

.. IMAGE:: editingTrigger.jpg

.. WARNING::

   Do not forget to select the severity of the trigger!

The type of the trigger is "Alarm", which means that this trigger will raise, not clear, the monitor. It will raise the monitor if receivers are stopped. Only receivers inside adapter "First" are considered. The Threshold and the Period are 2 and 60 seconds. This means the following: the trigger will only fire if two receiver shutdown events (within adapter "First") happen within 60 seconds. Otherwise the trigger will not fire and hence the monitor will not be raised. We press "Save" to save our work. 

We return to the screen that we saw after creating the monitor, but now the additional information about the monitor is shown.

Saving the monitor by putting its XML in the configuration
----------------------------------------------------------

There is a button "XML" to grab the XML representation of the monitor. You have to copy/paste this XML into ``Configuration.xml``, otherwise the monitor is gone when the Frank!Framework is restarted. Here is the result:

.. include:: ../../snippets/Frank2Monitoring/v510/monitorTextThatShouldComeFromGui.txt

.. WARNING::

   At the time of writing there is a bug in the Frank!Framework that causes it to omit the destination from the generated XML. See issue https://github.com/frankframework/frankframework/issues/8024. Please check the XML by hand and use the Frank!Doc to correct it after pasting. The example shown above is correct -- it includes the destination.

.. NOTE::

   The ``<Event>`` tag has a string as contents. This is exceptional, because the other XML tags of Frank configurations only have attributes and child elements.
 
Viewing monitors
----------------

When you click "Monitoring" in the main menu, you see all monitors within a configuration and you can choose what configuration to watch. As shown above, you see how many monitors are raised and each monitor is colored red if it is raised.

.. WARNING::

   Presently, the UI does not check automatically if monitors are raised or cleared. You have to use the refresh button of the browser to update the page with the latest statuses of the monitors. See issue https://github.com/frankframework/frankframework/issues/8026.

We stop and start adapter "First" two times in the Adapter Status page to have the monitor raised. Then we refresh the browser tab with our monitor. We have the following:

.. IMAGE:: monitorRaised.jpg

Please note that there is a button to clear the monitor by hand. This is useful for operators after they have resolved an issue that caused a monitor to raise.