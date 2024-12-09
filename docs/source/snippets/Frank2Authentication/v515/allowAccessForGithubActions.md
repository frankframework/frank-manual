```none{1, 2, 3}
# Allow access for GitHub Actions test, to check the server console does not have warnings
application.security.console.authentication.type=NONE

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