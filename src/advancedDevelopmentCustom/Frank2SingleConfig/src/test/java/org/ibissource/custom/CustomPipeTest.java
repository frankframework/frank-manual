package org.ibissource.custom;

import org.junit.Test;
import org.junit.Assert;

public class CustomPipeTest {
    @Test
    public void test() {
        Assert.assertEquals(8, CustomPipe.calculate(5));
    }
}