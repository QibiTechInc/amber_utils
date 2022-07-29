#!/usr/bin/env python
# -*- coding: utf-8 -*-
from amber_ssh_operation import ssh_command


def main():
    shutdown_command = 'sudo shutdown -h now'
    ssh_command('172.16.1.101', shutdown_command)
    ssh_command('172.16.1.102', shutdown_command)


if __name__ == '__main__':
    main()
