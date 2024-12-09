```none{14}
services:
  db:
    image: private.docker.nexus.frankframework.org/ff-test/dbms/postgresql
    ports:
      - 5432:5432
  jms:
    image: private.docker.nexus.frankframework.org/ff-test/mq/artemis
    ports:
      - 8160:8160
      - 61615:61615
  ff:
    image: frankframework/frankframework:8.3.0-SNAPSHOT
    ports:
      - 8090:8080
    volumes:
      - ./src/main/resources:/opt/frank/resources
    environment:
      jdbc.hostname: db
      jms.hostname: jms
      transactionmanager.type.default: NARAYANA
      jms.createDestination: true
```