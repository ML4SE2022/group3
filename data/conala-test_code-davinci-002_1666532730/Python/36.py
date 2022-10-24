import subprocess

subprocess.call(['ls', '-l', '-a'])

subprocess.call(['ls', '-l', '-a', '-h'])

subprocess.call(['ls', '-l', '-a', '-h', '-s'])

subprocess.call(['ls', '-l', '-a', '-h', '-s', '-r'])

subprocess.call(['ls', '-l', '-a', '-h', '-s', '-r', '-t'])

subprocess.call(['ls', '-l', '-a', '-h', '-s', '-r', '-t', '-u'])

subprocess.call(['ls', '-l', '-a', '-h', '-s', '-r', '-t', '-u', '-i'])

subprocess.call(['ls', '-l', '-a', '-h', '-s', '-r', '-t', '-u', '-i', '-x'])

subprocess.call(['ls', '-l', '-a', '-h', '-s', '-r', '-t', '-u', '-i', '-x', '-y'])

subprocess.call(['ls', '-l', '-a', '-h', '-s', '-r', '-t', '-u', '-i', '-x', '-y', '-z'])

subprocess.call(['ls', '-l', '-a', '-h', '-s', '-r', '-t', '-u', '-i', '-x', '-y', '-z', '-1'])

subprocess.call(['ls', '-l', '-a', '-h', '-s', '-r', '-t', '-u', '-i', '-x', '-y', '-z', '-1', '-2'