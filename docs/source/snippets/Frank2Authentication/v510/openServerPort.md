```none{4, 5}
services:
  frank-authorization-server:
    image: frankframework/frankframework:8.3.0-SNAPSHOT
    ports:
      - 8081:8080
    volumes:
      - ./server/configurations:/opt/frank/configurations
      - ./server/resources:/opt/frank/resources
    environment:
      instance.name: frank-authorization-server
      dtap.stage: DEV
      configurations.directory.autoLoad: true
      application.security.http.transportGuarantee: none
  frank-authorization-client:
    image: frankframework/frankframework:8.3.0-SNAPSHOT
...
```