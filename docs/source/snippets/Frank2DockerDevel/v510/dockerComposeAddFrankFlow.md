```none{8, 15, 16}
services:
  frank-docker-example:
    image: frankframework/frankframework:8
    ports:
      - 8080:8080
    volumes:
      - ./configurations:/opt/frank/configurations
      - ./frank-flow.war:/usr/local/tomcat/webapps/frank-flow.war:ro
    environment:
      instance.name: frank-docker-example
      dtap.stage: LOC
      configurations.directory.autoLoad: true
      configurations.names: ""
      jdbc.require: false
      # For Frank!Flow to run as webapp
      CATALINA_OPTS: -Dfrank-flow.context-path=
```
