ARG PG_VERSION
ARG ARTEMIS_VERSION
FROM frankframework/frankframework:latest
ARG PG_VERSION
ARG ARTEMIS_VERSION
ADD --chown=tomcat https://jdbc.postgresql.org/download/postgresql-${PG_VERSION}.jar /opt/frank/drivers/postgresql-${PG_VERSION}.jar
ADD --chown=tomcat https://repo1.maven.org/maven2/org/apache/activemq/artemis-jakarta-client-all/${ARTEMIS_VERSION}/artemis-jakarta-client-all-${ARTEMIS_VERSION}.jar /opt/frank/drivers/artemis-jakarta-client-all-${ARTEMIS_VERSION}.jar
COPY src/main/configurations/TransactionsExample /opt/frank/configurations/TransactionsExample
