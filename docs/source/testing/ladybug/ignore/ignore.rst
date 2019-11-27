.. _ignore:

Ignore Elements or Attributes
=============================

In subsection :ref:`capture`, you learned how to capture reports into test scripts. You saw how these tests could be run, allowing you to do regression tests of your system. In :ref:`edit`, you saw examples of failing tests. A test fails if there is any difference between the output captured in the past and the current output. This is not always what you want. As an example, your adapter may return the current time in some XML element. The output will then be different each time your System Under Test is run, but these differences do not indicate failures.

This subsection demonstrates how to ignore specific differences between the expected result of your test script and the actual result. These ignores can be configured globally for all tests, or locally for a specific test script. Both options are presented here.

Please do the following:

.. highlight:: none

#. Stop the Frank!framework.
#. Edit :code:`classes/Configuration.xml` to become:

   .. code-block: XML

      <?xml version="1.0" encoding="UTF-8" ?>
      <!DOCTYPE configuration [
          <!ENTITY external SYSTEM "externalTime.xml">
      ]>
      ...

#. Restart the Frank!framework.
#. Open Ladybug by clicking "Testing" and then "Ladybug" as shown below:

   .. image:: ../../frankConsoleFindTestTools.jpg

#. We delete all existing texts because they are no longer relevant. Click tab "Test" (number 1 in the picture below). Select the top node in the tree view (number 2). Press "Select all" (number 3) to select all tests (number 4). Then press "Delete" (number 5).

   .. image:: prepareDeleteOld.jpg

#. A confirmation dialog appears, proceed. Press "Refresh" (number 6). All test scripts should be gone.
#. Go to "Test Pipeline". To the top, you see you are indeed in the Test Pipeline screen (number 1 in the picture below). Select adapter "sutGet" (number 2). In the message field (number 3), enter the following XML: :code:`<docid>docid-12345</docid>`. Then press "Send" (number 4). You see that execution was successful (number 5) and you see a result (number 6).

   .. image:: sutGetTestPipeline.jpg

#. The result should be:

   .. code-block:: XML

      <result>
          <document>
              This is the document
          </document>
          <retrievalTime>
              2019-11-26T10:57:37UTC
          </retrievalTime>
      </result>

   You see that the current time is part of the result. This will be different each time the "sutGet" adapter is run.
#. Go back to Ladybug. Click tab "Debug" (number 1 in the picture below). Click "Refresh" (number 2). Select the row with the report about running "sutGet" (number 3). Select the topmost "Pipeline" node in the tree view (number 4). Select stub strategy "Never" (number 5). Then press "Copy" (number 6) and go to tab "Test" (number 7). The following scree appears:

   .. image:: afterCapture.jpg

#. You see you are in tab "Test" (number 1). Press "Refresh" (number 2). Your see the test script you captured. Press its "Run" button (number 3). You see a red message indicating that the test failed (number 4).
#. In subsection :ref:`edit` you saw that you can investigate why a test failed, but this was not shown in detail. This time, please press the "Compare" button (number 5). The following screen appears:

   .. image:: compare.jpg

#. You are in tab "Compare" (number 1). To the top, you see two tree views corresponding to the expected result (left) and the actual result (right). If you select a node in one of these, it is also selected in the other. To the bottom, a detailing comparison is shown between the node of the expected result and the node of the actual result. Both in the tree views and in the node details, differences are printed in red.
#. Go back to the "Debug" tab (number 2). You see the screenshot shown below, number 1 indicating you are in tab "Debug". Press "Options" (number 2). A dialog pops up. In that dialog, press "Transformation" (number 3).

   .. image:: openTransformation.jpg

#. A dialog appears that mainly consists of a text field. That text field shows an XSLT transformation. Edit it as shown. The highlighted lines indicate the change.

   .. code-block:: XML
      :emphasize-lines: 37, 38

      <xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="2.0">
	    <xsl:output method="xml" indent="yes" omit-xml-declaration="yes"/>
	    <xsl:strip-space elements="*"/>
	
	    <xsl:template match="/Report">
		    <xsl:copy>
		 	   <!-- Select the report name attribute -->
			   <xsl:apply-templates select="@Name"/>

               <!-- Select all report attributes -->
               <!-- <xsl:apply-templates select="@*"/> -->

               <!-- Select the first and last checkpoint -->
               <xsl:apply-templates select="Checkpoint[1]"/>
               <xsl:apply-templates select="Checkpoint[last()]"/>

               <!-- Select all checkpoints -->
               <!-- <xsl:apply-templates select="node()"/> -->

               <!-- Select the checkpoint with name "Pipe Example" -->
               <!-- <xsl:apply-templates select="Checkpoint[@Name='Pipe Example']"/> -->
		    </xsl:copy>
	    </xsl:template>
	
	    <xsl:template match="node()|@*">
		    <xsl:copy>
		 	   <xsl:apply-templates select="node()|@*"/>
		    </xsl:copy>
	    </xsl:template>
	
	    <!-- Ignore content of timestamp element -->
	    <!-- <xsl:template match="timestamp"><TIMESTAMP-IGNORED/></xsl:template> -->

	    <!-- Ignore content of Timestamp element in xml messages with namespaces (e.g. in case of SOAP messages) -->
	    <xsl:template match="*[local-name()='retrievalTime']"><xsl:element name="RETRIEVALTIME-IGNORED" namespace="{namespace-uri()}"/></xsl:template>

	    <!-- Ignore content of elements which content is ID:something -->
	    <!-- <xsl:template match="*[matches(text(), 'ID:.*')]">ID:IGNORED</xsl:template> -->

      </xsl:stylesheet>

#. Using Ctrl-C and Ctrl-V, copy the updated transformation to a textfile on your PC. You will need it later. This textfile is referenced later as :code:`updatedTransformation.xsl`.
#. Press "Save transformation" (number 1 in the figure below):

   .. image:: saveTransformation.jpg

#. Close the transformation dialog (number 2) and the options dialog (number 3). Go to tab "Test" (number 1 in the picture below)

   .. image:: runTestWithGlobalTransformation.jpg

#. Click "Reset" (number 2) to erase old test results. Press "Run" (number 3). You see that the test succeeds (number 4).
#. Press "Compare" (number 5). You come in the "Compare" tab (number 1 in the figure below). Select the last "sutGet" node (number 2) to the top-left. The same node is selected in the top-right (number 3).

   .. image:: compareWithTransformation.jpg

#. You see two equal elements :code:`RETRIEVALTIME-IGNORED/>` (number 4 and number 5). This is how ignored fields are shown.
#. Go to tab "Test" (number 6). Your screen changes as shown below. You see you are in tab "Test" (number 1). Press "Download all" (number 2). Finish the file save dialog to save your tests. We will refer to this file as :code:`savedTestsAfterTransformation`.
#. Stop the Frank!framework. Remove your docker container as follows. In a shell (Linux) or a command prompt (Windows), type the following: ::

     docker container rm ladybug

#. Restart the Frank!framework. Open Ladybug and go to tab "Test" (number 1 in the figure below). Press "Upload" (number 2) and select file :code:`savedTestsAfterTransformation`. Finish the dialog. This restores your tests.
#. Go to tab "Debug" (number 1 in the figure below). Press "Options" (number 2) and "Transformation" (number 3). You can see that the change you did earlier is not restored.

   .. NOTE::

      The global transformation, used to ignore XML elements for all tests, is not saved when you save your tests. Please save the global transformation when you edit it. After a restart of the Frank!framework, you cannot be sure that your changes are retained. If not, paste the saved transformation in the Options | Transformation dialog.

#. We will not restore the global transformation, but we will examine test-specific ignores. Go to tab "Test" (number 1 in figure below). You can see that your uploaded test is present (number 2).

   .. image:: tabTestAfterUpload.jpg

#. Press "Open" (number 3). You see the figure below. You are in a new tab (number 1). You are in a new tab (number 1). Select the topmost "Pipeline" node in the tree view (number 2).

   .. image:: afterUploadPrepareEdit.jpg

#. Press "Edit" (number 3). You see the figure below. The tab stays the same (number 1). Select the topmost "Pipeline" node (number 2). Then copy the contents of file :code:`updatedTransformation.xsl` to the clipboard. This is the updated XSLT transformation you had earlier in the Options | Transformation dialog.

   .. image:: afterUploadEdit.jpg

#. Paste the XSLT transformation from the clipboard to the Transformation field (number 3). Press "Save" (number 4) and "Close" (number 5).

   .. NOTE::

      In the Options | Transformation dialog, a default XSLT transaction was available. It had comments telling you how to update the transformation. The edit screen of a test script has an empty Transformation field. It is good to know that you can paste the transformation from Options | Transformation there.

#. You are back in tab "Test" (number 1 in the figure below). Press "Reset" (number 2) and the "Run" button of your test script (number 3). You see that your test succeeds again (number 4).

   .. image:: runWithTestSpecificTransformation.jpg

#. Press "Compare" (number 5). The screen becomes as shown below. You are in tab "Compare" (number 1). Select the topmost "Pipeline" node (number 2). You see the text "RETRIEVALTIME-IGNORED", both to the bottom-left and to the bottom-right.
#. If you save your test scripts now, the transformation will be included.


   .. image:: testWithLocalTransformationSuccessComparison.jpg