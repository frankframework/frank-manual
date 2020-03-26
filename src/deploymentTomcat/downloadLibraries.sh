#!/bin/bash
IAF_VERSION=7.6-20200325.131312
wget -O /usr/local/tomcat/webapps/frankframework.war "https://nexus.ibissource.org/content/groups/public/org/ibissource/ibis-adapterframework-webapp/${IAF_VERSION}/ibis-adapterframework-webapp-${IAF_VERSION}.war"
wget -O /usr/local/tomcat/lib/h2.jar "https://repo1.maven.org/maven2/com/h2database/h2/1.4.199/h2-1.4.199.jar"
wget -O /usr/local/tomcat/lib/jtds-1.3.1.zip "http://www.java2s.com/Code/JarDownload/jtds/jtds-1.3.1.jar.zip"
wget -O /usr/local/tomcat/lib/geronimo-jms_1.1_spec-1.1.1.jar "https://repo1.maven.org/maven2/org/apache/geronimo/specs/geronimo-jms_1.1_spec/1.1.1/geronimo-jms_1.1_spec-1.1.1.jar"
wget -O /usr/local/tomcat/lib/commons-dbcp-1.4.jar "https://repo1.maven.org/maven2/commons-dbcp/commons-dbcp/1.4/commons-dbcp-1.4.jar"
wget -O /usr/local/tomcat/lib/commons-pool-1.5.6.jar "https://repo1.maven.org/maven2/commons-pool/commons-pool/1.5.6/commons-pool-1.5.6.jar"
unzip /usr/local/tomcat/lib/jtds-1.3.1.zip -d /usr/local/tomcat/lib
rm /usr/local/tomcat/lib/jtds-1.3.1.zip
