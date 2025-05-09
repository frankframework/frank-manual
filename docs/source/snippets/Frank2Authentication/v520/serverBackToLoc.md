```none{9}
services:
  frank-authorization-server:
    image: frankframework/frankframework:latest
    volumes:
      - ./server/configurations:/opt/frank/configurations
      - ./server/resources:/opt/frank/resources
    environment:
      instance.name: frank-authorization-server
      dtap.stage: LOC
      configurations.directory.autoLoad: true
      application.security.http.transportGuarantee: none
  frank-authorization-client:
    image: frankframework/frankframework:latest
    ports:
      - 8080:8080
    volumes:
      - ./client/configurations:/opt/frank/configurations
      - ./client/resources:/opt/frank/resources
      - ./client/secrets:/opt/frank/secrets
    environment:
      instance.name: frank-authorization-client
      dtap.stage: LOC
      configurations.directory.autoLoad: true
      credentialFactory.class: org.frankframework.credentialprovider.PropertyFileCredentialFactory
      credentialFactory.map.properties: /opt/frank/secrets/credentials.properties
```
