#!/usr/bin/env python
# -*- coding: utf-8 -*-
from amber_ssh_operation import ssh_command


def main():
    start_command = 'sudo systemctl start hr4c.service'
    ssh_command('172.16.1.101', start_command)
    ssh_command('172.16.1.102', start_command)


if __name__ == '__main__':
    main()
