ARG PG_VERSION
ARG ARTEMIS_VERSION
FROM ubuntu:latest AS downloader
ARG PG_VERSION
ARG ARTEMIS_VERSION
RUN apt-get update && apt-get install -y wget
WORKDIR /usr/src/app
RUN wget https://jdbc.postgresql.org/download/postgresql-${PG_VERSION}.jar
RUN wget https://repo1.maven.org/maven2/org/apache/activemq/artemis-jakarta-client-all/${ARTEMIS_VERSION}/artemis-jakarta-client-all-${ARTEMIS_VERSION}.jar

FROM frankframework/frankframework:latest
ARG PG_VERSION
ARG ARTEMIS_VERSION
COPY --from=downloader /usr/src/app/postgresql-${PG_VERSION}.jar /opt/frank/drivers/postgresql-${PG_VERSION}.jar
COPY --from=downloader /usr/src/app/artemis-jakarta-client-all-${ARTEMIS_VERSION}.jar /opt/frank/drivers/artemis-jakarta-client-all-${ARTEMIS_VERSION}.jar
