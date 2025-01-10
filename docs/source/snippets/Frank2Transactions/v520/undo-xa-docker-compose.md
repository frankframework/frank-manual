```none
services:
  db:
    image: postgres
    ports:
      - 5432:5432
    environment:
      - POSTGRES_PASSWORD=testiaf_user00
      - POSTGRES_USER=testiaf_user
      - POSTGRES_DB=testiaf
  ff:
    image: frankframework/frankframework:8.3.0-SNAPSHOT
    ports:
      - 8080:8080
    volumes:
      - ./src/main/resources:/opt/frank/resources
    environment:
      jdbc.hostname: db
```
