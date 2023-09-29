import subprocess

def restart_computer():
    subprocess.call(["shutdown", "-r", "-t", "0"])

restart_computer()
