# -*- coding: utf-8 -*-
import paramiko
import sys


def ssh_command(ipaddr, command):
    with paramiko.SSHClient() as ssh:
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # ssh接続
        ssh.connect(ipaddr,
                    username='hr4c',
                    password='AmberM0del4')

        # コマンド実行
        stdin, stdout, stderr = ssh.exec_command(command)

        # 実行結果を表示
        for o in stdout:
            sys.stdout.write('[std]{}'.format(o))
        for e in stderr:
            sys.stdout.write('[err]{}'.format(e))
