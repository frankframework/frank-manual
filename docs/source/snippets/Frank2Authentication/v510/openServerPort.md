```none{12, 13}
...
    - ./client/configurations:/opt/frank/configurations
    - ./client/secrets:/opt/frank/secrets
  environment:
    instance.name: frank-authorization-client
    dtap.stage: LOC
    configurations.directory.autoLoad: true
    credentialFactory.class: nl.nn.credentialprovider.PropertyFileCredentialFactory
    credentialFactory.map.properties: /opt/frank/secrets/credentials.properties
frank-authorization-server:
  image: frankframework/frankframework:8.3.0-SNAPSHOT
  ports:
    - 8081:8080
  volumes:
    - ./server/configurations:/opt/frank/configurations
  environment:
    instance.name: frank-authorization-server
    dtap.stage: LOC
    configurations.directory.autoLoad: true
    application.security.http.transportGuarantee: none
```
