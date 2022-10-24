String[] cmd = {"/bin/sh", "-c", "echo 'hello' | grep 'hello'"};
Process p = Runtime.getRuntime().exec(cmd);