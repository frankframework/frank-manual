FROM tomcat:7.0.99
ENV IAF_VERSION=7.5-20191211.175453
ENV HOME=/home/root/Downloads/work
ENV CATALINA_OPTS="-Dotap.stage=LOC -Dconfigurations.myConfig.directory=${HOME}/configurations -Dscenariosroot1.directory=/home/root/Downloads/work/tests/ -Dscenariosroot1.description=\"My Larva tests\""
ENV CONTEXT_FILE=/usr/local/tomcat/conf/context.xml
WORKDIR /usr/local/tomcat/webapps

RUN wget -O /usr/local/tomcat/webapps/frankframework.war "https://nexus.ibissource.org/content/groups/public/org/ibissource/ibis-adapterframework-webapp/${IAF_VERSION}/ibis-adapterframework-webapp-${IAF_VERSION}.war"
RUN wget -O /usr/local/tomcat/lib/h2.jar "https://repo1.maven.org/maven2/com/h2database/h2/1.4.199/h2-1.4.199.jar"
RUN wget -O /usr/local/tomcat/lib/jtds-1.3.1.zip "http://www.java2s.com/Code/JarDownload/jtds/jtds-1.3.1.jar.zip"
RUN wget -O /usr/local/tomcat/lib/geronimo-jms_1.1_spec-1.1.1.jar "https://repo1.maven.org/maven2/org/apache/geronimo/specs/geronimo-jms_1.1_spec/1.1.1/geronimo-jms_1.1_spec-1.1.1.jar"
RUN wget -O /usr/local/tomcat/lib/commons-dbcp-1.4.jar "https://repo1.maven.org/maven2/commons-dbcp/commons-dbcp/1.4/commons-dbcp-1.4.jar"
RUN wget -O /usr/local/tomcat/lib/commons-pool-1.5.6.jar "https://repo1.maven.org/maven2/commons-pool/commons-pool/1.5.6/commons-pool-1.5.6.jar"
RUN unzip /usr/local/tomcat/lib/jtds-1.3.1.zip -d /usr/local/tomcat/lib
RUN rm /usr/local/tomcat/lib/jtds-1.3.1.zip
RUN bash -c "catalina.sh start; sleep 5;"

RUN mkdir -p ${HOME}
COPY . ${HOME}
RUN apt-get update
RUN apt-get install nano
RUN mkdir -p /usr/local/tomcat/webapps/frankframework/WEB-INF/classes
RUN cp -r ${HOME}/classes /usr/local/tomcat/webapps/frankframework/WEB-INF
RUN sed -i -e "s|</Context>||g" ${CONTEXT_FILE}
RUN cat ${HOME}/resourceDef >> ${CONTEXT_FILE}
RUN echo "</Context>" >> ${CONTEXT_FILE}
