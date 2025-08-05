package org.wearefrank.mermaid.dashboard;

import java.io.IOException;
import java.util.stream.Collectors;

import org.frankframework.core.PipeLineSession;
import org.frankframework.core.PipeRunException;
import org.frankframework.core.PipeRunResult;
import org.frankframework.pipes.FixedForwardPipe;
import org.frankframework.stream.Message;

public class AnalyzeMermaidTemplatePipe extends FixedForwardPipe {
    public PipeRunResult doPipe(Message message, PipeLineSession session) throws PipeRunException {
        try {
            String template = message.asString();
            Analysis analysis = new Analysis(template);
            analysis.run();
            String mapping = analysis.getMappingItems().stream()
                .map(mappingItem -> String.format("""
                  <item>
                    <name>%s</name>
                    <mermaid-line>%d</mermaid-line>
                  </item>""".indent(4), mappingItem.statusName(), mappingItem.edgeNumber()))
                .collect(Collectors.joining(""))
                .stripTrailing();
            String result = String.format("""
              <mermaid-template>
                <original><![CDATA[%s]]></original>
                <body><![CDATA[%s]]></body>
                <mapping>
              %s
                </mapping>
              </mermaid-template>""", template, analysis.getBody(), mapping);
            Message m = new Message(result);
            return new PipeRunResult(getSuccessForward(), m);
        }
        catch(IOException e) {
            throw new PipeRunException(this, "IOException encountered", e);
        }
    }
}
