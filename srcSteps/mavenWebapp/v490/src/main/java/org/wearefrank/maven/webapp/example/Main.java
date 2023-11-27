package org.frankframework.maven.webapp.example;

import org.apache.commons.lang3.StringUtils;

/**
 * Although the package name contains "webapp", this is not a webapp yet. It will become so later.
 */
class Main {
    public static void main(String[] args) {
        System.out.println(StringUtils.upperCase("Hello World!"));
    }
}