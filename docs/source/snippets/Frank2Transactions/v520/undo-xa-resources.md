```none
jdbc:
  - name: "frank2transactions"
    type: "org.postgresql.Driver"
    url: "jdbc:postgresql://${jdbc.hostname:-localhost}:5432/testiaf"
    authalias: "${db.authalias}"
    username: "testiaf_user"
    password: "testiaf_user00"
```