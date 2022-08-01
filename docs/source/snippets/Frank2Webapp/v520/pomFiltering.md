```xml{6, 7, 8, 9, 10, 11}
...
        <scope>runtime</scope>
    </dependency>
</dependencies>
<build>
    <resources>
        <resource>
            <directory>src/main/resources</directory>
            <filtering>true</filtering>
        </resource>
    </resources>
    <plugins>
        <plugin>
            <groupId>org.eclipse.jetty</groupId>
            <artifactId>jetty-maven-plugin</artifactId>
...
```
