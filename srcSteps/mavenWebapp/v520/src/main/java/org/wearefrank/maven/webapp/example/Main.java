package org.wearefrank.maven.webapp.example;

import org.apache.commons.lang3.StringUtils;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;

public class Main extends HttpServlet {
    public void doGet(HttpServletRequest req,HttpServletResponse res) throws IOException, ServletException {
        PrintWriter pw = res.getWriter();
        pw.println(StringUtils.upperCase("Hello World!"));
        pw.close();
    }
}