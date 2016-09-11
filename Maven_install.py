# coding=utf-8
import subprocess
import os
import sys

__author__ = 'lgx'

mvn_install_shell = 'mvn clean install -Dmaven.test.skip=true'
mvn_deploy_shell = 'mvn clean deploy -Dmaven.test.skip=true'


def install_or_deploy_commons(shell):
    os.chdir('/Users/ligx/enjoy_project/commons')
    subprocess.call(shell, shell=True)


def install_or_deploy_base(shell):
    os.chdir('/Users/ligx/enjoy_project/base')
    subprocess.call(shell, shell=True)


def install_or_deploy_pay(shell):
    os.chdir('/Users/ligx/enjoy_project/pay/')
    subprocess.call(shell, shell=True)


def install_or_deploy_order(shell):
    os.chdir('/Users/ligx/enjoy_project/order/')
    subprocess.call(shell, shell=True)


def install_or_deploy_aggregator(shell):
    os.chdir('/Users/ligx/enjoy_project/aggregator/')
    subprocess.call(shell, shell=True)


def install_or_deploy_3_project(shell):
    install_or_deploy_pay(shell)
    install_or_deploy_order(shell)
    install_or_deploy_aggregator(shell)


def install_or_deploy_4_project(shell):
    install_or_deploy_base(shell)
    install_or_deploy_pay(shell)
    install_or_deploy_order(shell)
    install_or_deploy_aggregator(shell)


def install_or_deploy_5_project(shell):
    install_or_deploy_commons(shell)
    install_or_deploy_base(shell)
    install_or_deploy_pay(shell)
    install_or_deploy_order(shell)
    install_or_deploy_aggregator(shell)

if __name__ == '__main__':
    if(sys.argv[1] == 'help'):
        print('Usage: python Maven_install.py [help|install|deploy] [3|4|5]')
    elif(sys.argv[1] == 'install'):
        if(sys.argv[2] == '3'):
            install_or_deploy_3_project(mvn_install_shell)
        elif(sys.argv[2] == '4'):
            install_or_deploy_4_project(mvn_install_shell)
        elif(sys.argv[2] == '5'):
            install_or_deploy_5_project(mvn_install_shell)
    elif(sys.argv[1] == 'deploy'):
        if (sys.argv[2] == '3'):
            install_or_deploy_3_project(mvn_deploy_shell)
        elif (sys.argv[2] == '4'):
            install_or_deploy_4_project(mvn_deploy_shell)
        elif (sys.argv[2] == '5'):
            install_or_deploy_5_project(mvn_deploy_shell)
