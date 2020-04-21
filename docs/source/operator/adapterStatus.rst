.. _frankConsoleAdapterStatus:

Adapter Status
--------------

In the previous section :ref:`frankConsolePreparations`, you installed the Frank!Runner and you used it to start the Frank!Framework. You also deployed an example configuration about the imaginary company :ref:`frankConsoleNewHorizons`. In this section, you examine the Adapter Status page, the first page you see when you start the Frank!Runner.

The page is split into two parts. To the left, you see the main menu. The "Adapter Status" item is highlighted, indicating you are on the Adapter Status page, see the picture below:

.. image:: mainMenuAdapterStatus.jpg

To the right, you see a dashboard with many different items. To the top-left, you see general information about your Frank!Framework instance as shown below:

.. image:: adapterStatusTopLeft.jpg

You see the Frank!Framework version you are running (number 1) and the instance name of your Frank!Framework deployment (number 2). Within your instance, you can host multiple configurations. Each Frank config has its own tab and there is also a tab "All" (number 3). By default, "All" is selected, indicating that the information below the text "Configuration summary" (not shown) applies to all configurations. There is a tab for the configuration you deployed, "NewHorizons" (number 4), and there are additional tabs for predefined configurations.

Below you see the next section of the Adapter Status page, namely "Configuration Summary". You are still in tab "All" (number 1). This means that the shown data applies to all configurations. We first examine the matrix having its rows annotated with number 2 and its columns annotated with numbers 3 - 7. Number 2 shows the words "Adapters" and "Receivers". A receiver is a building block that gathers messages. These messages are then processed by adapters. Each adapter and each receiver has its own state, which can be "Started" (number 3), "Starting" (number 4), "Stopped" (number 5), "Stopping" (number 6) or "Error" (number 7). Each number within the matrix indicates how many adapters or receivers are in the corresponding state. You see that 10 adapters and 12 receivers have started and that no receivers and adapters are in another state (all zeros).

.. image:: adapterStatusConfigurationSummary.jpg

To the right, you see "Info messages", "Warning messages" and "Error messages", with counts behind them (number 7). These counts summarize the "Configuration messages" panel (number 8). The figure below shows the configuration messages panel (number 1). You see a clickable heading for each adapter (number 2). When you count them, you will see that there are 10 adapters, the number you saw in the matrix of the previous figure. In the previous figure you also saw numbers of configuration messages (number 8). These counted configuration messages are under the ten links of the configuration messages panel (present figure).

.. image:: adapterStatusConfigurationMessages.jpg

Please press the "NewHorizons" tab now, above the text "Configuration summary". The configuration summary panel should change as shown below. You see you selected the "NewHorizons" tab (number 1). You see 2 adapters and 2 receivers (number 2), because you are only seeing Frank config "NewHorizons", not anymore the predefined Frank configs. The number of configuration messages has decreased a lot (number 3).

.. image:: adapterStatusConfigurationSummaryNewHorizons.jpg

The configuration messages panel now looks as shown below. You see two adapters as you could expect from the previous figure.

.. image:: adapterStatusConfigurationMessagesNewHorizons.jpg

Please click "adapterGetDestinations" now to expand it. The screen should look like shown below. You see it is about adapter "adapterGetDestinations" (number 1). First you see adapter information (numbers 2 - 5) like the state (number 2) and the time since the adapter is up (number 4). You can also stop the adapter (number 3) and get more statistics (number 5).

.. image:: adapterStatusAdapterGetDestinations.jpg

Next comes information about the receivers feeding "adapterGetDestinations". There is one, namely "receiverGetDestinations" (number 6). There is a button to stop this receiver to the far right of the screen (not shown). When you stop an adapter, all its receivers are stopped as well. When you stop a receiver, the adapter it feeds still keeps running. The effect of this situation will be explained later in this tutorial.

Below the receivers you see the pipes that send output. There is one, "pipeSendApartments" (number 7). Finally you see six messages (number 8). If you open the other adapter you see also six messages. These add up to 12 messages, the number you are seeing in the configuration summary panel. The numbers add because there are no error and no warning messages. If there are error and warning messages, the individual error messages add up to the number of error messages and the same holds for the warnings and the info messages.
