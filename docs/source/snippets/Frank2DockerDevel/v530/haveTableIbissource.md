```none{15}
services:
  frank-docker-example:
    image: frankframework/frankframework:8.2.0-SNAPSHOT
    ports:
      - 8080:8080
    volumes: &frank-volumes
      - ./configurations:/opt/frank/configurations
    environment:
      instance.name: frank-docker-example
      dtap.stage: LOC
      configurations.directory.autoLoad: true
      configurations.names: ""
      management.gateway.inbound.class: "org.frankframework.management.gateway.HazelcastInboundGateway"
      jdbc.datasource.default: "jdbc/db-loc"
      jdbc.migrator.active: true
  frank-flow:
    image: frankframework/frank-flow
    ports:
      - "8081:8080"
    volumes: *frank-volumes
```
