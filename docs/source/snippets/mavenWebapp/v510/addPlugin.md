```xml{6, 7, 8, 9, 10, 11, 12, 13}
...
                <configuration>
                    <release>11</release>
                </configuration>
            </plugin>
            <plugin>
                <groupId>org.codehaus.mojo</groupId>
                <artifactId>exec-maven-plugin</artifactId>
                <version>3.0.0</version>
                <configuration>
                    <mainClass>org.wearefrank.maven.webapp.example.Main</mainClass>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```
