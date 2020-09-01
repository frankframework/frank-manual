package org.ibissource.custom;

import nl.nn.adapterframework.core.IPipe;
import nl.nn.adapterframework.core.PipeRunResult;
import nl.nn.adapterframework.core.IPipeLineSession;
import nl.nn.adapterframework.configuration.ConfigurationException;
import nl.nn.adapterframework.stream.Message;
import nl.nn.adapterframework.core.PipeRunException;
import nl.nn.adapterframework.pipes.FixedForwardPipe;

import java.io.IOException;

class CustomPipe extends FixedForwardPipe {
    private static final int ADDITION = 3;

    @Override
    public PipeRunResult doPipe(Message message, IPipeLineSession session) throws PipeRunException {
        try {
            String msg = message.asString();
            int val = Integer.parseInt(msg);
            int result = calculate(val);
            return new PipeRunResult(getForward(), (Object) Integer.valueOf(result));
        } catch(IOException e) {
            throw new PipeRunException(this, "An IOException occurred", e);
        }
    }

    static int calculate(int val) {
        return val + ADDITION;
    }

    @Override
    public int getMaxThreads() {
        return 0;
    }
}