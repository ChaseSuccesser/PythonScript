#coding=utf-8
__author__ = 'lgx'

import sys
import subprocess
import os

if len(sys.argv) < 3:
    print("Usage: python AppManager.py app start|stop|status|restart")
    sys.exit(0)

app = sys.argv[1]
action = sys.argv[2]


def start():
    subprocess.call("./app_start.sh", shell=True)

def stop():
    pid = find_app_process()
    if pid:
        subprocess.call("kill -9 %s" % str(pid), shell=True)

def status():
    pid = find_app_process()
    if pid:
        print("%s is running on pid: %s" % (app, pid))
    else:
        print("%s is not running" % app)

def restart():
    stop()
    start()


def find_app_process():
    child = subprocess.Popen("jps", shell=True, stdout=subprocess.PIPE)
    shell_result = child.communicate()
    is_running = shell_result[0].find(app.capitalize() + "Application") > 0
    pid = filter(lambda str:str.find(app.capitalize() + "Application")>0, shell_result[0].split("\n"))[0].split(" ")[0] if is_running else None
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

