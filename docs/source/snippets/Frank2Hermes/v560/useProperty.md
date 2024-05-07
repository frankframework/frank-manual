```none{5}
scenario.description = Hermes requests address from Conscience

include = common.properties

step1.adapter.toConscience.write = scenario01/${hermesAddress}
step2.stub.conscience.read = scenario01/conscienceAddressRequest.xml
step3.stub.conscience.write = scenario01/conscienceAddressResponse.xml
step4.adapter.toConscience.read = scenario01/hermesAddressResponse.xml
```
