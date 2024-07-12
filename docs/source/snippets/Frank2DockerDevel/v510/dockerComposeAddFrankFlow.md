```none{3, 6, 14, 15, 16, 17, 18, 19}
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
      jdbc.require: false
      management.gateway.inbound.class: "org.frankframework.management.gateway.HazelcastInboundGateway"
  frank-flow:
    image: frankframework/frank-flow
    ports:
      - "8081:8080"
    volumes: *frank-volumes
```