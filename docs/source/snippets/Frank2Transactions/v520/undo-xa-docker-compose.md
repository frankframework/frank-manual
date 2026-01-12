```none
services:
  db:
    image: postgres
    ports:
      - 5432:5432
    environment:
      POSTGRES_PASSWORD: testiaf_user00
      POSTGRES_USER: testiaf_user
      POSTGRES_DB: testiaf
  ff:
    build:
      context: .
      dockerfile: Dockerfile
      args:
        PG_VERSION: 42.7.8
    ports:
      - 8080:8080
    volumes:
      - ./src/main/resources:/opt/frank/resources
    environment:
      jdbc.hostname: db
```
