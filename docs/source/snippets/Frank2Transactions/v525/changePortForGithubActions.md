```none{9}
services:
  db:
    image: private.docker.nexus.frankframework.org/ff-test/dbms/postgresql
    ports:
      - 5432:5432
  ff:
    image: frankframework/frankframework:latest
    ports:
      - 8090:8080
    volumes:
      - ./src/main/resources:/opt/frank/resources
    environment:
      jdbc.hostname: db
```
