```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE configuration [
  <!ENTITY Destinations SYSTEM "ConfigurationDestinations.xml">
  <!ENTITY ProcessDestination SYSTEM "ConfigurationProcessDestination.xml">
  <!ENTITY CheckExpiration SYSTEM "ConfigurationCheckExpiration.xml">
]>
<Configuration name="NewHorizons">
  &Destinations;
  &ProcessDestination;
  &CheckExpiration;
</Configuration>
```
