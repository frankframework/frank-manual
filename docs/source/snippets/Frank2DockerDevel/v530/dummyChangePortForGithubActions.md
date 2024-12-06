```none{5}
services:
  frank-docker-example:
    image: frankframework/frankframework:8.3.0-SNAPSHOT
    ports:
      - 8090:8080
    volumes: &frank-volumes
      - ./configurations:/opt/frank/configurations
      - ./resources:/opt/frank/resources
    environment:
      instance.name: frank-docker-example
      dtap.stage: LOC
      configurations.directory.autoLoad: true
      management.gateway.inbound.class: "org.frankframework.management.gateway.HazelcastInboundGateway"
      jdbc.datasource.default: "jdbc/db-loc"
  frank-flow:
    image: frankframework/frank-flow
    ports:
      - "8081:8080"
    volumes: *frank-volumes
```
