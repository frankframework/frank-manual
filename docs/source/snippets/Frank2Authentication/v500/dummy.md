```none
# Define the available authenticators
application.security.http.authenticators=inMem

# Configure the authenticator
application.security.http.authenticators.inMem.type=IN_MEMORY
application.security.http.authenticators.inMem.username=ADMIN
application.security.http.authenticators.inMem.password=PASSWORD1234

# Tell what should be secured
servlet.ApiListenerServlet.authenticator=inMem
servlet.ApiListenerServlet.securityRoles=IbisAdmin
```