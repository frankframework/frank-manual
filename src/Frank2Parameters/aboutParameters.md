# About Parameters

*This text is not published on ReadTheDocs. It is for internal use at WeAreFrank!*

On September 15 2022, WeAreFrank! is working on the Frank!Doc documentation about parameters. In particular, on the [page about Param](https://frankdoc.frankframework.org/#!/Other/Param) the explanation of the `type` attribute needs improvement. The behavior of this attribute does not match a programmer's intuition about what data types are. The files in this directory are a Frank application that demonstrates the effect of the `type` attribute. The remainder of this document explains this example and provides its output. After that, Martijn's analysis of the corresponding source code of the Frank!Framework is given. This text should clarify the confusion about the `type` attribute and it should allow discussion about further action.

### Example configurations

There are three example configurations. The example configuration [configurations/Parameters/Configuration.xml](/configurations/Parameters/Configuration.xml) does the following:

* It executes an SQL query with a parameter.
* It executes a pipe that needs parameters with specific names.
* It executes an XSLT stylesheet with parameters.

First, the SQL query reads `INSERT INTO WithTimestamp VALUES(?)`. The parameter is of type `XMLDATETIME` and its value is `2022-09-14T15:00:00`. In file [configurations/Parameters/DatabaseChangelog.xml](/configurations/Parameters/DatabaseChangelog.xml) the manipulated database table is created (H2 database). The table being inserted has one column of data type `TIMESTAMP`.

Second, a `CompareIntegerPipe` is executed. It compares the values of parameters `operand1` and `operand2`. These parameters are considered as integers even though they do not have a `type` attribute.

Third, the XSLT stylesheet [configurations/Parameters/template.xsl](/configurations/Parameters/template.xsl) is executed. It takes three parameters and includes their values in its output. The values are included using `<xsl:copy-of>`. In the configuration, each parameter is given the value `<xmlRoot>This is the value</xmlRoot>`, the contents of file [configurations/Parameters/fileXmlParameter.xml](/configurations/Parameters/fileXmlParameter.xml). They are passed with different `type` attributes however, namely `STRING`, `XML` and `DOMDOC`. The result is as follows:

```<?xml version="1.0" encoding="UTF-8"?>
<root xmlns:xs="http://www.w3.org/2001/XMLSchema">
	<parameterTypeString>This is the value</parameterTypeString>
	<parameterTypeXml>&lt;xmlRoot&gt;This is the value&lt;/xmlRoot&gt;</parameterTypeXml>
	<parameterTypeDomDoc>
		<xmlRoot>This is the value</xmlRoot>
	</parameterTypeDomDoc>
</root>
```

The second example is very much like the XSLT part of the first example. The difference is that the XSLT transformation produces a node set without a common root. This does not work with `type=DOMDOC` (that case produces an error) and hence only `type=STRING` and `type=XML` are tried. The output is:

```
<?xml version="1.0" encoding="UTF-8"?>
<root xmlns:xs="http://www.w3.org/2001/XMLSchema">
	<parameterTypeString>
        Value first child
     
        Value second child
    </parameterTypeString>
	<parameterTypeXml>&lt;xmlChild&gt;
        Value first child
    &lt;/xmlChild&gt;&lt;xmlChild&gt;
        Value second child
    &lt;/xmlChild&gt;</parameterTypeXml>
</root>
```

This comes from applying XPath expression `xmlRoot/xmlChild` to an XML document in which root element `<xmlRoot>` haw two child elements `<xmlChild>`.

The third example tries `type=NODE` which is only allowed for XSLT version 1.0. The example uses XSLT 1.0. The parameter value is obtained by applying XPath expression `xmlRoot/xmlChild` to the following XML:

```
<xmlRoot>
    <xmlChild>This is the value</xmlChild>
    <xmlChild>This is another value</xmlChild>
</xmlRoot>
```

This example produces an error:

```
<errorMessage timestamp="Thu Sep 22 14:29:42 CEST 2022" originator="IAF 7.9-20220921.131044" message="error during pipeline processing: Pipe [applyParameters] msgId [testmessage0a0000ab-2c03d458_183652cda71_-8000]  Exception on transforming input: XsltSender [applyParameters] Cannot transform input: XsltSender [applyParameters] Exception on creating transformerHandler chain: Parameter [parNode] exception on transformation to get parametervalue: (XPathException) line [1] column [7]: (DOMException) HIERARCHY_REQUEST_ERR: An attempt was made to insert a node where it is not permitted.">
	<location class="nl.nn.adapterframework.pipes.XsltPipe" name="applyParameters"/>
	<details>nl.nn.adapterframework.core.ListenerException: Pipe [applyParameters] msgId [testmessage0a0000ab-2c03d458_183652cda71_-8000]  Exception on transforming input: XsltSender [applyParameters] Cannot transform input: XsltSender [applyParameters] Exception on creating transformerHandler chain: Parameter [parNode] exception on transformation to get parametervalue: (XPathException) line [1] column [7]: (DOMException) HIERARCHY_REQUEST_ERR: An attempt was made to insert a node where it is not permitted.
	at nl.nn.adapterframework.core.Adapter.processMessageWithExceptions(Adapter.java:670)
	at nl.nn.adapterframework.core.Adapter.processMessage(Adapter.java:555)
	at nl.nn.adapterframework.webcontrol.api.TestPipeline.processMessage(TestPipeline.java:215)
	at nl.nn.adapterframework.webcontrol.api.TestPipeline.postTestPipeLine(TestPipeline.java:142)
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:498)
	at org.apache.cxf.service.invoker.AbstractInvoker.performInvocation(AbstractInvoker.java:179)
	at org.apache.cxf.service.invoker.AbstractInvoker.invoke(AbstractInvoker.java:96)
	at org.apache.cxf.jaxrs.JAXRSInvoker.invoke(JAXRSInvoker.java:201)
	at org.apache.cxf.jaxrs.JAXRSInvoker.invoke(JAXRSInvoker.java:104)
	at org.apache.cxf.interceptor.ServiceInvokerInterceptor$1.run(ServiceInvokerInterceptor.java:59)
	at org.apache.cxf.interceptor.ServiceInvokerInterceptor.handleMessage(ServiceInvokerInterceptor.java:96)
	at org.apache.cxf.phase.PhaseInterceptorChain.doIntercept(PhaseInterceptorChain.java:307)
	at org.apache.cxf.transport.ChainInitiationObserver.onMessage(ChainInitiationObserver.java:121)
	at org.apache.cxf.transport.http.AbstractHTTPDestination.invoke(AbstractHTTPDestination.java:265)
	at org.apache.cxf.transport.servlet.ServletController.invokeDestination(ServletController.java:234)
	at org.apache.cxf.transport.servlet.ServletController.invoke(ServletController.java:208)
	at org.apache.cxf.transport.servlet.ServletController.invoke(ServletController.java:160)
	at org.apache.cxf.transport.servlet.CXFNonSpringServlet.invoke(CXFNonSpringServlet.java:225)
	at nl.nn.adapterframework.webcontrol.api.ServletDispatcher.invoke(ServletDispatcher.java:149)
	at org.apache.cxf.transport.servlet.AbstractHTTPServlet.handleRequest(AbstractHTTPServlet.java:304)
	at org.apache.cxf.transport.servlet.AbstractHTTPServlet.doPost(AbstractHTTPServlet.java:217)
	at javax.servlet.http.HttpServlet.service(HttpServlet.java:681)
	at org.apache.cxf.transport.servlet.AbstractHTTPServlet.service(AbstractHTTPServlet.java:279)
	at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:227)
	at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:162)
	at org.apache.tomcat.websocket.server.WsFilter.doFilter(WsFilter.java:53)
	at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:189)
	at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:162)
	at nl.nn.adapterframework.webcontrol.LoginFilter.doFilter(LoginFilter.java:226)
	at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:189)
	at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:162)
	at nl.nn.adapterframework.http.CacheControlFilter.doFilter(CacheControlFilter.java:55)
	at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:189)
	at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:162)
	at org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:337)
	at org.springframework.security.web.access.ExceptionTranslationFilter.doFilter(ExceptionTranslationFilter.java:122)
	at org.springframework.security.web.access.ExceptionTranslationFilter.doFilter(ExceptionTranslationFilter.java:116)
	at org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:346)
	at org.springframework.security.web.session.SessionManagementFilter.doFilter(SessionManagementFilter.java:126)
	at org.springframework.security.web.session.SessionManagementFilter.doFilter(SessionManagementFilter.java:81)
	at org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:346)
	at org.springframework.security.web.authentication.AnonymousAuthenticationFilter.doFilter(AnonymousAuthenticationFilter.java:109)
	at org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:346)
	at org.springframework.security.web.servletapi.SecurityContextHolderAwareRequestFilter.doFilter(SecurityContextHolderAwareRequestFilter.java:149)
	at org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:346)
	at org.springframework.security.web.savedrequest.RequestCacheAwareFilter.doFilter(RequestCacheAwareFilter.java:63)
	at org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:346)
	at org.springframework.security.web.authentication.preauth.AbstractPreAuthenticatedProcessingFilter.doFilter(AbstractPreAuthenticatedProcessingFilter.java:146)
	at org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:346)
	at org.springframework.security.web.authentication.logout.LogoutFilter.doFilter(LogoutFilter.java:103)
	at org.springframework.security.web.authentication.logout.LogoutFilter.doFilter(LogoutFilter.java:89)
	at org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:346)
	at org.springframework.security.web.header.HeaderWriterFilter.doHeadersAfter(HeaderWriterFilter.java:90)
	at org.springframework.security.web.header.HeaderWriterFilter.doFilterInternal(HeaderWriterFilter.java:75)
	at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:117)
	at org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:346)
	at org.springframework.security.web.context.SecurityContextPersistenceFilter.doFilter(SecurityContextPersistenceFilter.java:112)
	at org.springframework.security.web.context.SecurityContextPersistenceFilter.doFilter(SecurityContextPersistenceFilter.java:82)
	at org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:346)
	at org.springframework.security.web.context.request.async.WebAsyncManagerIntegrationFilter.doFilterInternal(WebAsyncManagerIntegrationFilter.java:55)
	at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:117)
	at org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:346)
	at org.springframework.security.web.session.DisableEncodeUrlFilter.doFilterInternal(DisableEncodeUrlFilter.java:42)
	at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:117)
	at org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:346)
	at org.springframework.security.web.FilterChainProxy.doFilterInternal(FilterChainProxy.java:221)
	at org.springframework.security.web.FilterChainProxy.doFilter(FilterChainProxy.java:186)
	at org.springframework.web.filter.DelegatingFilterProxy.invokeDelegate(DelegatingFilterProxy.java:354)
	at org.springframework.web.filter.DelegatingFilterProxy.doFilter(DelegatingFilterProxy.java:267)
	at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:189)
	at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:162)
	at org.apache.logging.log4j.web.Log4jServletFilter.doFilter(Log4jServletFilter.java:71)
	at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:189)
	at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:162)
	at org.apache.catalina.core.StandardWrapperValve.invoke(StandardWrapperValve.java:197)
	at org.apache.catalina.core.StandardContextValve.invoke(StandardContextValve.java:97)
	at org.apache.catalina.authenticator.AuthenticatorBase.invoke(AuthenticatorBase.java:659)
	at org.apache.catalina.core.StandardHostValve.invoke(StandardHostValve.java:135)
	at org.apache.catalina.valves.ErrorReportValve.invoke(ErrorReportValve.java:92)
	at org.apache.catalina.valves.AbstractAccessLogValve.invoke(AbstractAccessLogValve.java:687)
	at org.apache.catalina.core.StandardEngineValve.invoke(StandardEngineValve.java:78)
	at org.apache.catalina.connector.CoyoteAdapter.service(CoyoteAdapter.java:357)
	at org.apache.coyote.http11.Http11Processor.service(Http11Processor.java:382)
	at org.apache.coyote.AbstractProcessorLight.process(AbstractProcessorLight.java:65)
	at org.apache.coyote.AbstractProtocol$ConnectionHandler.process(AbstractProtocol.java:895)
	at org.apache.tomcat.util.net.NioEndpoint$SocketProcessor.doRun(NioEndpoint.java:1732)
	at org.apache.tomcat.util.net.SocketProcessorBase.run(SocketProcessorBase.java:49)
	at org.apache.tomcat.util.threads.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1191)
	at org.apache.tomcat.util.threads.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:659)
	at org.apache.tomcat.util.threads.TaskThread$WrappingRunnable.run(TaskThread.java:61)
	at java.lang.Thread.run(Thread.java:748)
Caused by: nl.nn.adapterframework.core.PipeRunException: Pipe [applyParameters] msgId [testmessage0a0000ab-2c03d458_183652cda71_-8000]  Exception on transforming input: XsltSender [applyParameters] Cannot transform input: XsltSender [applyParameters] Exception on creating transformerHandler chain: Parameter [parNode] exception on transformation to get parametervalue: (XPathException) line [1] column [7]: (DOMException) HIERARCHY_REQUEST_ERR: An attempt was made to insert a node where it is not permitted.
	at nl.nn.adapterframework.pipes.XsltPipe.doPipe(XsltPipe.java:145)
	at nl.nn.adapterframework.pipes.XsltPipe$$FastClassBySpringCGLIB$$3d9ec3bb.invoke(&lt;generated&gt;)
	at org.springframework.cglib.proxy.MethodProxy.invoke(MethodProxy.java:218)
	at org.springframework.aop.framework.CglibAopProxy$CglibMethodInvocation.invokeJoinpoint(CglibAopProxy.java:793)
	at org.springframework.aop.framework.ReflectiveMethodInvocation.proceed(ReflectiveMethodInvocation.java:163)
	at org.springframework.aop.framework.CglibAopProxy$CglibMethodInvocation.proceed(CglibAopProxy.java:763)
	at org.springframework.aop.interceptor.ExposeInvocationInterceptor.invoke(ExposeInvocationInterceptor.java:97)
	at org.springframework.aop.framework.ReflectiveMethodInvocation.proceed(ReflectiveMethodInvocation.java:186)
	at org.springframework.aop.framework.CglibAopProxy$CglibMethodInvocation.proceed(CglibAopProxy.java:763)
	at org.springframework.aop.framework.CglibAopProxy$DynamicAdvisedInterceptor.intercept(CglibAopProxy.java:708)
	at nl.nn.adapterframework.pipes.XsltPipe$$EnhancerBySpringCGLIB$$3344ed6f.doPipe(&lt;generated&gt;)
	at nl.nn.adapterframework.processors.CorePipeProcessor.processPipe(CorePipeProcessor.java:33)
	at nl.nn.adapterframework.processors.PipeProcessorBase.lambda$processPipe$0(PipeProcessorBase.java:49)
	at nl.nn.adapterframework.processors.CheckMessageSizePipeProcessor.processPipe(CheckMessageSizePipeProcessor.java:38)
	at nl.nn.adapterframework.processors.PipeProcessorBase.processPipe(PipeProcessorBase.java:49)
	at nl.nn.adapterframework.processors.PipeProcessorBase.lambda$processPipe$0(PipeProcessorBase.java:49)
	at nl.nn.adapterframework.processors.LockerPipeProcessor.processPipe(LockerPipeProcessor.java:62)
	at nl.nn.adapterframework.processors.PipeProcessorBase.processPipe(PipeProcessorBase.java:49)
	at nl.nn.adapterframework.processors.PipeProcessorBase.lambda$processPipe$0(PipeProcessorBase.java:49)
	at nl.nn.adapterframework.processors.TransactionAttributePipeProcessor.processPipe(TransactionAttributePipeProcessor.java:59)
	at nl.nn.adapterframework.processors.PipeProcessorBase.processPipe(PipeProcessorBase.java:49)
	at nl.nn.adapterframework.processors.PipeProcessorBase.lambda$processPipe$0(PipeProcessorBase.java:49)
	at nl.nn.adapterframework.processors.CheckSemaphorePipeProcessor.processPipe(CheckSemaphorePipeProcessor.java:59)
	at nl.nn.adapterframework.processors.PipeProcessorBase.processPipe(PipeProcessorBase.java:49)
	at nl.nn.adapterframework.processors.CheckSemaphorePipeProcessor.processPipe(CheckSemaphorePipeProcessor.java:67)
	at nl.nn.adapterframework.processors.CheckSemaphorePipeProcessor$$FastClassBySpringCGLIB$$3159a29c.invoke(&lt;generated&gt;)
	at org.springframework.cglib.proxy.MethodProxy.invoke(MethodProxy.java:218)
	at org.springframework.aop.framework.CglibAopProxy$CglibMethodInvocation.invokeJoinpoint(CglibAopProxy.java:793)
	at org.springframework.aop.framework.ReflectiveMethodInvocation.proceed(ReflectiveMethodInvocation.java:163)
	at org.springframework.aop.framework.CglibAopProxy$CglibMethodInvocation.proceed(CglibAopProxy.java:763)
	at org.springframework.aop.aspectj.MethodInvocationProceedingJoinPoint.proceed(MethodInvocationProceedingJoinPoint.java:102)
	at nl.nn.ibistesttool.IbisDebuggerAdvice.debugPipeGetInputFrom(IbisDebuggerAdvice.java:173)
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:498)
	at org.springframework.aop.aspectj.AbstractAspectJAdvice.invokeAdviceMethodWithGivenArgs(AbstractAspectJAdvice.java:634)
	at org.springframework.aop.aspectj.AbstractAspectJAdvice.invokeAdviceMethod(AbstractAspectJAdvice.java:624)
	at org.springframework.aop.aspectj.AspectJAroundAdvice.invoke(AspectJAroundAdvice.java:72)
	at org.springframework.aop.framework.ReflectiveMethodInvocation.proceed(ReflectiveMethodInvocation.java:175)
	at org.springframework.aop.framework.CglibAopProxy$CglibMethodInvocation.proceed(CglibAopProxy.java:763)
	at org.springframework.aop.interceptor.ExposeInvocationInterceptor.invoke(ExposeInvocationInterceptor.java:97)
	at org.springframework.aop.framework.ReflectiveMethodInvocation.proceed(ReflectiveMethodInvocation.java:186)
	at org.springframework.aop.framework.CglibAopProxy$CglibMethodInvocation.proceed(CglibAopProxy.java:763)
	at org.springframework.aop.framework.CglibAopProxy$DynamicAdvisedInterceptor.intercept(CglibAopProxy.java:708)
	at nl.nn.adapterframework.processors.CheckSemaphorePipeProcessor$$EnhancerBySpringCGLIB$$4ee35eb2.processPipe(&lt;generated&gt;)
	at nl.nn.adapterframework.processors.PipeProcessorBase.lambda$processPipe$0(PipeProcessorBase.java:49)
	at nl.nn.adapterframework.processors.InputOutputPipeProcessor.processPipe(InputOutputPipeProcessor.java:89)
	at nl.nn.adapterframework.processors.PipeProcessorBase.processPipe(PipeProcessorBase.java:49)
	at nl.nn.adapterframework.processors.InputOutputPipeProcessor.processPipe(InputOutputPipeProcessor.java:183)
	at nl.nn.adapterframework.processors.InputOutputPipeProcessor$$FastClassBySpringCGLIB$$feb9be85.invoke(&lt;generated&gt;)
	at org.springframework.cglib.proxy.MethodProxy.invoke(MethodProxy.java:218)
	at org.springframework.aop.framework.CglibAopProxy$CglibMethodInvocation.invokeJoinpoint(CglibAopProxy.java:793)
	at org.springframework.aop.framework.ReflectiveMethodInvocation.proceed(ReflectiveMethodInvocation.java:163)
	at org.springframework.aop.framework.CglibAopProxy$CglibMethodInvocation.proceed(CglibAopProxy.java:763)
	at org.springframework.aop.aspectj.MethodInvocationProceedingJoinPoint.proceed(MethodInvocationProceedingJoinPoint.java:102)
	at nl.nn.ibistesttool.IbisDebuggerAdvice.debugPipeInputOutputAbort(IbisDebuggerAdvice.java:143)
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:498)
	at org.springframework.aop.aspectj.AbstractAspectJAdvice.invokeAdviceMethodWithGivenArgs(AbstractAspectJAdvice.java:634)
	at org.springframework.aop.aspectj.AbstractAspectJAdvice.invokeAdviceMethod(AbstractAspectJAdvice.java:624)
	at org.springframework.aop.aspectj.AspectJAroundAdvice.invoke(AspectJAroundAdvice.java:72)
	at org.springframework.aop.framework.ReflectiveMethodInvocation.proceed(ReflectiveMethodInvocation.java:175)
	at org.springframework.aop.framework.CglibAopProxy$CglibMethodInvocation.proceed(CglibAopProxy.java:763)
	at org.springframework.aop.interceptor.ExposeInvocationInterceptor.invoke(ExposeInvocationInterceptor.java:97)
	at org.springframework.aop.framework.ReflectiveMethodInvocation.proceed(ReflectiveMethodInvocation.java:186)
	at org.springframework.aop.framework.CglibAopProxy$CglibMethodInvocation.proceed(CglibAopProxy.java:763)
	at org.springframework.aop.framework.CglibAopProxy$DynamicAdvisedInterceptor.intercept(CglibAopProxy.java:708)
	at nl.nn.adapterframework.processors.InputOutputPipeProcessor$$EnhancerBySpringCGLIB$$1309f273.processPipe(&lt;generated&gt;)
	at nl.nn.adapterframework.processors.PipeProcessorBase.lambda$processPipe$0(PipeProcessorBase.java:49)
	at nl.nn.adapterframework.processors.ExceptionHandlingPipeProcessor.processPipe(ExceptionHandlingPipeProcessor.java:38)
	at nl.nn.adapterframework.processors.PipeProcessorBase.processPipe(PipeProcessorBase.java:49)
	at nl.nn.adapterframework.processors.PipeProcessorBase.lambda$processPipe$0(PipeProcessorBase.java:49)
	at nl.nn.adapterframework.processors.MonitoringPipeProcessor.processPipe(MonitoringPipeProcessor.java:77)
	at nl.nn.adapterframework.processors.PipeProcessorBase.processPipe(PipeProcessorBase.java:49)
	at nl.nn.adapterframework.processors.CorePipeLineProcessor.processPipeLine(CorePipeLineProcessor.java:231)
	at nl.nn.adapterframework.processors.CorePipeLineProcessor$$FastClassBySpringCGLIB$$cf1091e5.invoke(&lt;generated&gt;)
	at org.springframework.cglib.proxy.MethodProxy.invoke(MethodProxy.java:218)
	at org.springframework.aop.framework.CglibAopProxy$CglibMethodInvocation.invokeJoinpoint(CglibAopProxy.java:793)
	at org.springframework.aop.framework.ReflectiveMethodInvocation.proceed(ReflectiveMethodInvocation.java:163)
	at org.springframework.aop.framework.CglibAopProxy$CglibMethodInvocation.proceed(CglibAopProxy.java:763)
	at org.springframework.aop.aspectj.MethodInvocationProceedingJoinPoint.proceed(MethodInvocationProceedingJoinPoint.java:102)
	at nl.nn.ibistesttool.IbisDebuggerAdvice.debugPipeLineInputOutputAbort(IbisDebuggerAdvice.java:122)
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:498)
	at org.springframework.aop.aspectj.AbstractAspectJAdvice.invokeAdviceMethodWithGivenArgs(AbstractAspectJAdvice.java:634)
	at org.springframework.aop.aspectj.AbstractAspectJAdvice.invokeAdviceMethod(AbstractAspectJAdvice.java:624)
	at org.springframework.aop.aspectj.AspectJAroundAdvice.invoke(AspectJAroundAdvice.java:72)
	at org.springframework.aop.framework.ReflectiveMethodInvocation.proceed(ReflectiveMethodInvocation.java:175)
	at org.springframework.aop.framework.CglibAopProxy$CglibMethodInvocation.proceed(CglibAopProxy.java:763)
	at org.springframework.aop.interceptor.ExposeInvocationInterceptor.invoke(ExposeInvocationInterceptor.java:97)
	at org.springframework.aop.framework.ReflectiveMethodInvocation.proceed(ReflectiveMethodInvocation.java:186)
	at org.springframework.aop.framework.CglibAopProxy$CglibMethodInvocation.proceed(CglibAopProxy.java:763)
	at org.springframework.aop.framework.CglibAopProxy$DynamicAdvisedInterceptor.intercept(CglibAopProxy.java:708)
	at nl.nn.adapterframework.processors.CorePipeLineProcessor$$EnhancerBySpringCGLIB$$f5bd8893.processPipeLine(&lt;generated&gt;)
	at nl.nn.adapterframework.processors.LockerPipeLineProcessor.processPipeLine(LockerPipeLineProcessor.java:60)
	at nl.nn.adapterframework.processors.TransactionAttributePipeLineProcessor.processPipeLine(TransactionAttributePipeLineProcessor.java:47)
	at nl.nn.adapterframework.processors.CheckSemaphorePipeLineProcessor.processPipeLine(CheckSemaphorePipeLineProcessor.java:58)
	at nl.nn.adapterframework.processors.CachePipeLineProcessor.processPipeLine(CachePipeLineProcessor.java:41)
	at nl.nn.adapterframework.processors.InputOutputPipeLineProcessor.processPipeLine(InputOutputPipeLineProcessor.java:44)
	at nl.nn.adapterframework.core.PipeLine.process(PipeLine.java:471)
	at nl.nn.adapterframework.core.Adapter.processMessageWithExceptions(Adapter.java:646)
	... 93 more
Caused by: nl.nn.adapterframework.core.SenderException: XsltSender [applyParameters] Cannot transform input: XsltSender [applyParameters] Exception on creating transformerHandler chain: Parameter [parNode] exception on transformation to get parametervalue: (XPathException) line [1] column [7]: (DOMException) HIERARCHY_REQUEST_ERR: An attempt was made to insert a node where it is not permitted.
	at nl.nn.adapterframework.senders.XsltSender.sendMessage(XsltSender.java:348)
	at nl.nn.adapterframework.pipes.XsltPipe.doPipe(XsltPipe.java:133)
	... 198 more
Caused by: nl.nn.adapterframework.stream.StreamingException: XsltSender [applyParameters] Exception on creating transformerHandler chain: Parameter [parNode] exception on transformation to get parametervalue: (XPathException) line [1] column [7]: (DOMException) HIERARCHY_REQUEST_ERR: An attempt was made to insert a node where it is not permitted.
	at nl.nn.adapterframework.senders.XsltSender.createHandler(XsltSender.java:310)
	at nl.nn.adapterframework.senders.XsltSender.sendMessage(XsltSender.java:332)
	... 199 more
Caused by: nl.nn.adapterframework.core.ParameterException: Parameter [parNode] exception on transformation to get parametervalue: (XPathException) line [1] column [7]: (DOMException) HIERARCHY_REQUEST_ERR: An attempt was made to insert a node where it is not permitted.
	at nl.nn.adapterframework.parameters.Parameter.getValue(Parameter.java:505)
	at nl.nn.adapterframework.parameters.Parameter$$FastClassBySpringCGLIB$$8b71ce06.invoke(&lt;generated&gt;)
	at org.springframework.cglib.proxy.MethodProxy.invoke(MethodProxy.java:218)
	at org.springframework.aop.framework.CglibAopProxy$CglibMethodInvocation.invokeJoinpoint(CglibAopProxy.java:793)
	at org.springframework.aop.framework.ReflectiveMethodInvocation.proceed(ReflectiveMethodInvocation.java:163)
	at org.springframework.aop.framework.CglibAopProxy$CglibMethodInvocation.proceed(CglibAopProxy.java:763)
	at org.springframework.aop.aspectj.MethodInvocationProceedingJoinPoint.proceed(MethodInvocationProceedingJoinPoint.java:89)
	at nl.nn.ibistesttool.IbisDebuggerAdvice.debugParameterResolvedTo(IbisDebuggerAdvice.java:453)
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:498)
	at org.springframework.aop.aspectj.AbstractAspectJAdvice.invokeAdviceMethodWithGivenArgs(AbstractAspectJAdvice.java:634)
	at org.springframework.aop.aspectj.AbstractAspectJAdvice.invokeAdviceMethod(AbstractAspectJAdvice.java:624)
	at org.springframework.aop.aspectj.AspectJAroundAdvice.invoke(AspectJAroundAdvice.java:72)
	at org.springframework.aop.framework.ReflectiveMethodInvocation.proceed(ReflectiveMethodInvocation.java:175)
	at org.springframework.aop.framework.CglibAopProxy$CglibMethodInvocation.proceed(CglibAopProxy.java:763)
	at org.springframework.aop.interceptor.ExposeInvocationInterceptor.invoke(ExposeInvocationInterceptor.java:97)
	at org.springframework.aop.framework.ReflectiveMethodInvocation.proceed(ReflectiveMethodInvocation.java:186)
	at org.springframework.aop.framework.CglibAopProxy$CglibMethodInvocation.proceed(CglibAopProxy.java:763)
	at org.springframework.aop.framework.CglibAopProxy$DynamicAdvisedInterceptor.intercept(CglibAopProxy.java:708)
	at nl.nn.adapterframework.parameters.Parameter$$EnhancerBySpringCGLIB$$6a935996.getValue(&lt;generated&gt;)
	at nl.nn.adapterframework.parameters.ParameterList.getValue(ParameterList.java:160)
	at nl.nn.adapterframework.parameters.ParameterList.getValues(ParameterList.java:153)
	at nl.nn.adapterframework.parameters.ParameterList.getValues(ParameterList.java:117)
	at nl.nn.adapterframework.senders.XsltSender.createHandler(XsltSender.java:236)
	... 200 more
Caused by: net.sf.saxon.trans.XPathException: org.w3c.dom.DOMException: HIERARCHY_REQUEST_ERR: An attempt was made to insert a node where it is not permitted.
	at net.sf.saxon.dom.DOMWriter.startElement(DOMWriter.java:191)
	at net.sf.saxon.event.ProxyReceiver.startElement(ProxyReceiver.java:139)
	at net.sf.saxon.event.SequenceNormalizer.startElement(SequenceNormalizer.java:84)
	at net.sf.saxon.event.ComplexContentOutputter.startElement(ComplexContentOutputter.java:530)
	at net.sf.saxon.tree.tiny.TinyTextualElement.copy(TinyTextualElement.java:103)
	at net.sf.saxon.expr.instruct.CopyOf.copyOneNode(CopyOf.java:629)
	at net.sf.saxon.expr.instruct.CopyOf.lambda$processLeavingTail$1(CopyOf.java:561)
	at net.sf.saxon.om.SequenceIterator.forEachOrFail(SequenceIterator.java:136)
	at net.sf.saxon.expr.instruct.CopyOf.processLeavingTail(CopyOf.java:559)
	at net.sf.saxon.expr.instruct.Instruction.process(Instruction.java:142)
	at net.sf.saxon.expr.instruct.ForEach.lambda$processLeavingTail$0(ForEach.java:526)
	at net.sf.saxon.om.SequenceIterator.forEachOrFail(SequenceIterator.java:136)
	at net.sf.saxon.expr.instruct.ForEach.processLeavingTail(ForEach.java:526)
	at net.sf.saxon.expr.instruct.Block.processLeavingTail(Block.java:752)
	at net.sf.saxon.expr.instruct.NamedTemplate.expand(NamedTemplate.java:264)
	at net.sf.saxon.expr.instruct.CallTemplate$CallTemplatePackage.processLeavingTail(CallTemplate.java:548)
	at net.sf.saxon.trans.Mode.applyTemplates(Mode.java:478)
	at net.sf.saxon.trans.XsltController.applyTemplates(XsltController.java:663)
	at net.sf.saxon.s9api.AbstractXsltTransformer.applyTemplatesToSource(AbstractXsltTransformer.java:360)
	at net.sf.saxon.s9api.XsltTransformer.transform(XsltTransformer.java:349)
	at net.sf.saxon.jaxp.TransformerImpl.transform(TransformerImpl.java:74)
	at nl.nn.adapterframework.util.TransformerPool.transform(TransformerPool.java:424)
	at nl.nn.adapterframework.util.TransformerPool.transform(TransformerPool.java:415)
	at nl.nn.adapterframework.parameters.Parameter.transformToDocument(Parameter.java:364)
	at nl.nn.adapterframework.parameters.Parameter.getValue(Parameter.java:493)
	... 225 more
Caused by: org.w3c.dom.DOMException: HIERARCHY_REQUEST_ERR: An attempt was made to insert a node where it is not permitted.
	at org.apache.xerces.dom.CoreDocumentImpl.insertBefore(Unknown Source)
	at org.apache.xerces.dom.NodeImpl.appendChild(Unknown Source)
	at net.sf.saxon.dom.DOMWriter.startElement(DOMWriter.java:156)
	... 249 more
</details>
	<originalMessage messageId="testmessage0a0000ab-2c03d458_183652cda71_-8000" receivedTime="Thu Sep 22 14:29:41 CEST 2022">&lt;xxx/&gt;</originalMessage>
</errorMessage>
```

### Calculation of parameter values

The value of a parameter is calculated in the Java class that corrsponds with XML tag `<Param>`, namely `nl.nn.adapterframework.parameters.Parameter`. The method that calculates the value has the following signature:

```
public Object getValue(ParameterValueList alreadyResolvedParameters, Message message, PipeLineSession session, boolean namespaceAware) throws ParameterException
```

The behavior of this method can be summarized as follows (some calculations that are not relevant for analyzing `type` are omitted):

1. It calculates a raw value based `<Param>`'s attributes `value`, `sessionKey`, `sessionKeyXPath`, `pattern` and also the input message.
1. If `xpathExpression` is set, create an XSLT stylesheet that includes it.
1. If attribute `styleSheetName` or `xpathExpression` is set, apply the transformation to the raw value. A `styleSheetName` is applied as-is and for an `xpathExpression` the XSLT from the previous step is executed.
1. Based on the `type` attribute, convert the result so far to the desired Java type: a string, a number, a date or an XML document.

Parameters are used in many ways by the Frank!Framework. Martijn did not have the time to check every spot in the source code where parameter values are used. Only some cases of parameter usa are considered here in detail.

### XSLT 2.0 parameters

This section is about pipes and senders that perform XSLT 2.0 transformations. These pipes and senders have parameters that can have `type` value `STRING`, `XML` or `DOMDOC`. In this case, the value of the `type` attribute influences the parameter's value in two ways:

1. It influences how the parameter`s XPath expression is transformed to an XSLT stylesheet.
1. It influences the Java type to which the parameter value is finally transformed.

The effect of the `type` attribute can be expressed with the following table:

`type` | XPath wrapper | Result type
------ | ------------- | -----------
``STRING`` | ``<xsl:value-of>`` | String
``XML`` | ``<xsl:copy-of>`` | String
``DOMDOC`` | ``<xsl:copy-of>`` | XML document

The consequences of this table are examined for the first example (configuration `Parameters`). For each tested value for `type`, the produced result is explained:

**STRING:** To calculate the parameter value, the string `<xmlRoot>This is the value</xmlRoot>` is transformed with XPath expression `xmlRoot`. This XPath expression is first converted to an XSLT stylesheet. That stylesheet contains something like `<xsl:value-of select="xmlRoot" />`. The XSLT element `<xsl:value-of>` selects the text inside the selected node set without the surrounding tags. This produces parameter value `This is the value`. This value is passed as a parameter when `template.xsl` is executed. The following snippet of `template.xsl` uses the parameter: `<parameterTypeString><xsl:copy-of select="$parString" /></parameterTypeString>`. The `xsl:copy-of` is applied to the parameter value and hence the parameter value is just wrapped here inside the `<parameterTypeString>` element.

**XML:** The XSLT stylesheet contains something like `<xsl:copy-of select="xmlRoot" />`. The `<xsl:copy-of>` tag takes the select result including the XML tags. This is the string `<xmlRoot>This is the value</xmlRoot>`, but that string is not passed down as an XML document. This lets the Frank!Framework escape the `<` and `>` characters by default. The parameter is applied in `template.xsl` using the snippet `<parameterTypeXml><xsl:copy-of select="$parXml" /></parameterTypeXml>`. It would not work to give this `<xsl:copy-of>` a `select` attribute, because the engine would not recognize the input as XML.

**DOMDOC:** The parameter value becomes the XML document `<xmlRoot>This is the value</xmlRoot>`. When `template.xsl` is applied, the input is an XML document that is properly formatted.

### XSLT 1.0

Martijn wonders whether the F!F has a bug for XSLT 1.0 and `type=NODE`, because the shown example produces an error.

### SQL query parameters

The Frank!Framework executes SQL queries using the JDBC protocol. The Frank!Framework has to pass parameter values using setter methods defined by JDBC. The `type` attribute influences in two ways how query parameters are set:

1. The `type` attribute determines how the raw parameter value is converted into a Java object.
1. The `type` attribute determines the chosen setter method provided by the JDBC protocol. This setter has to match the data type within the underlying database engine.

It is interesting to compare `type=DATETIME` and `type=XMLDATETIME`. If a paramter has `type=DATETIME`, the raw value should match date format `yyyy-MM-dd HH:mm:ss` (according to the JavaDoc, Martijn did not test this). If the raw value matches this format, the parameter value is a Java object of type `Date`. It is passed to the underlying database engine using JDBC setter `setTimestamp()`. This will only work if the related database field has a vendor-specific data type that matches JDBC setter `setTimestamp()`.

If `type=XMLDATETIME`, the raw value should match date format that is something like `yyyy-mm-ddThh:mm:ss`. The resulting parameter value becomes a Java `Date` that is passed with JDBC setter `setTimestamp()`. The allowed database field types for Frank!Framework parameters having `type=DATETIME` or having `type=XMLDATETIME` are the same.

### A case where `type` is ignored

The `<CompareIntegerPipe>` ignores the `type` attribute of parameters. It converts everything integers and compares those. Martijn can imagine that there are some edge cases with rounding. What if parameters of type `NUMBER` are used? Martijn would expect that these are first parsed as Java variables of type `double`. If two `double` values are different but are rounded to the same integer, the comparison may produce equality.
