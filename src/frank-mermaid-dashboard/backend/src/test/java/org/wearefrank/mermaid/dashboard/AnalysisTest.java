package org.wearefrank.mermaid.dashboard;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNull;
import static org.junit.jupiter.api.Assertions.assertTrue;
import org.junit.jupiter.api.Test;

public class AnalysisTest {
    @Test
    public void whenLineHasNameThenNameReturned() {
        String actual = Analysis.getStatusNameIfApplicable("#myName# A --> N");
        assertEquals("myName", actual);
    }

    @Test
    public void whenLineHasNoNameThenNullReturned() {
        assertNull(Analysis.getStatusNameIfApplicable("A --> N"));
    }

    @Test
    public void whenNamePatternIsNotAtStartThenNoNameReturned() {
        assertNull(Analysis.getStatusNameIfApplicable("xxx #myName#"));
    }

    @Test
    public void whenLineHasStatusNameThenCanBeRemoved() {
        String actual = Analysis.removeStatusNameIfPresent("#myName# A --> N");
        assertEquals(" A --> N", actual);
    }

    @Test
    public void whenLineHasNoStatusNameThenOriginalLineKapt() {
        String actual = Analysis.removeStatusNameIfPresent("A --> N");
        assertEquals("A --> N", actual);
    }

    @Test
    public void whenLineIsMermaidEdgeThenIsDetected() {
        assertTrue(Analysis.isMermaidEdge("#myName# A --> N"));
    }

    @Test
    public void whenLineIsMermaidNodeThenNotDetectedAsEdge() {
        assertFalse(Analysis.isMermaidEdge("A(Aap)"));
    }
}
