import subprocess

subprocess.call("ls -l | grep test", shell=True)