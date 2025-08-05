package org.wearefrank.mermaid.dashboard;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.StringReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Collectors;

class Analysis {
    private static final String STATUS_NAME_REGEX = "^#\\w+#";
    private static final Pattern STATUS_NAME_PATTERN;

    static {
        STATUS_NAME_PATTERN = Pattern.compile(STATUS_NAME_REGEX, Pattern.CASE_INSENSITIVE);
    }

    private String mermaidTemplate;
    private StringBuilder body = new StringBuilder();
    // First edge should have number 0
    private int edgeNumber = -1;
    private Map<String, Integer> nameToNumber = new HashMap<>();

    Analysis(String mermaidTemplate) {
        this.mermaidTemplate = mermaidTemplate;
    }

    String getBody() {
        return body.toString();
    }

    List<MappingItem> getMappingItems() {
        List<String> statusNames = new ArrayList<>(nameToNumber.keySet());
        statusNames.sort(Comparator.naturalOrder());
        return statusNames.stream()
                .map(statusName -> new MappingItem(statusName, nameToNumber.get(statusName)))
                .collect(Collectors.toList());
    }

    public void run() throws IOException {
        String line = null;
        BufferedReader r = new BufferedReader(new StringReader(mermaidTemplate));
        while ((line = r.readLine()) != null) {
            processLine(line);
        }
    }

    private void processLine(String line) {
        body.append(removeStatusNameIfPresent(line) + "\n");
        if (isMermaidEdge(line)) {
            ++edgeNumber;
            String statusName = getStatusNameIfApplicable(line);
            if (statusName != null) {
                if (nameToNumber.containsKey(statusName)) {
                    throw new IllegalStateException("Status name is not unique: " + statusName);
                }
                nameToNumber.put(statusName, edgeNumber);
            }
        }
    }

    static String getStatusNameIfApplicable(String line) {
        String trimmed = line.trim();
        Matcher matcher = STATUS_NAME_PATTERN.matcher(trimmed);
        if (matcher.find()) {
            int idxEnd = trimmed.indexOf("#", 1);
            return trimmed.substring(1, idxEnd);
        } else {
            return null;
        }
    }

    static String removeStatusNameIfPresent(String line) {
        String trimmed = line.trim();
        Matcher matcher = STATUS_NAME_PATTERN.matcher(trimmed);
        if (matcher.find()) {
            return matcher.replaceFirst("");
        } else {
            return line;
        }
    }

    static boolean isMermaidEdge(String line) {
        return line.indexOf("-->") >= 0;
    }
}
