import subprocess, shlex

def subprocess_cmd(command):
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
    proc_stdout = process.communicate()[0].strip()
    print proc_stdout

subprocess_cmd("sudo bluetoothctl")