#!/usr/bin/env python
# -*- coding: utf-8 -*-
from amber_ssh_operation import ssh_command


def main():
    stop_command = 'sudo systemctl stop hr4c.service'
    ssh_command('172.16.1.101', stop_command)
    ssh_command('172.16.1.102', stop_command)


if __name__ == '__main__':
    main()
