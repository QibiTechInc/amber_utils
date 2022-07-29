# -*- coding: utf-8 -*-
import paramiko


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
            print('[std]', o, end='')
        for e in stderr:
            print('[err]', e, end='')
