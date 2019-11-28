.. _global:

Global ignore
=============

In sub-subsection :ref:`preparations`, we set the stage to examine the ignore feature of Ladybug. The purpose of this feature was introduced in :ref:`ignore`. In this sub-subsection we are going to do a global ignore. This means we will ignore the contents of an XML element for all test scripts.

In :ref:`preparations`, we changed the System Under Test. It now produces an element :code:`<retrievalTime>` that has the current time as its contents. This contents will be different each time the "sutGet" adpater is run. We started the Frank!framework, ran adapter "sutGet" and captured a test script.

Please continue as follows:

#. Open Ladybug and go to tab "Test" (number 1 in the figure below). Press "Refresh" (number 2). Your see the test script you captured. Press its "Run" button (number 3). You see a red message indicating that the test failed (number 4).

   .. image:: afterCapture.jpg

#. In subsection :ref:`edit` you saw that you can investigate why a test failed, but this was not shown in detail. This time, please press the "Compare" button (number 5). The following screen appears:

   .. image:: compare.jpg

#. You are in tab "Compare" (number 1). To the top, you see two tree views corresponding to the expected result (left) and the actual result (right). If you select a node in one of these, it is also selected in the other. To the bottom, a detailing comparison is shown between the node of the expected result and the node of the actual result. Both in the tree views and in the node details, differences are printed in red.
#. Go back to the "Debug" tab (number 2). You see the screenshot shown below, number 1 indicating you are in tab "Debug". Press "Options" (number 2). A dialog pops up. In that dialog, press "Transformation" (number 3).

   .. image:: openTransformation.jpg

#. A dialog appears that mainly consists of a text field. That text field shows an XSLT transformation. Edit it as shown. The highlighted lines indicate the change.

   .. code-block:: XML
      :emphasize-lines: 35

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

#. Using Ctrl-C and Ctrl-V, copy the updated transformation to a textfile on your laptop. You will need it later. This textfile is referenced later as :code:`updatedTransformation.xsl`.
#. Press "Save transformation" (number 1 in the figure below):

   .. image:: saveTransformation.jpg

#. Close the transformation dialog (number 2) and the options dialog (number 3). Go to tab "Test" (number 1 in the picture below)

   .. image:: runTestWithGlobalTransformation.jpg

#. Click "Reset" (number 2) to erase old test results. Press "Run" (number 3). You see that the test succeeds (number 4).
#. Press "Compare" (number 5). You come in the "Compare" tab (number 1 in the figure below). Select the last "sutGet" node (number 2) to the top-left. The same node is selected in the top-right (number 3).

   .. image:: compareWithTransformation.jpg

#. You see two equal elements :code:`RETRIEVALTIME-IGNORED/>` (number 4 and number 5). This is how ignored fields are shown.
