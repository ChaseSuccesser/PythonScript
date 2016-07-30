#coding=utf-8
__author__ = 'lgx'

import sys
import subprocess

if len(sys.argv) < 2:
    print(sys.argv[0])
    print(sys.argv[1])
    print("Usage: python AppManager.py app start|stop|status|restart")
    sys.exit(0)

app = sys.argv[0]
action = sys.argv[1]


def start():
    subprocess.call("./app_start.sh", shell=True)

def stop():
    pid = find_app_process()
    if pid > 0:
        subprocess.call("kill -9 %s" % str(pid), shell=True)

def status():
    pid = find_app_process()
    if pid > 0:
        print("%s is running" % app)
    else:
        print("%s is not running" % app)

def restart():
    stop()
    start()


def find_app_process():
    shell = "ps -ef | grep %s | grep java | awk 'print $2'" % sys.argv[1]
    child = subprocess.Popen(shell, shell=True, stdout=subprocess.PIPE)
    pid = child.communicate()
    print("shell: %s" % shell)
    print("pid: %s" % pid)
    return pid


if action == "start":
    start()
elif action == "stop":
    stop()
elif action == "status":
    status()
elif action == "restart":
    restart()
elif action == "debug":
    find_app_process()

