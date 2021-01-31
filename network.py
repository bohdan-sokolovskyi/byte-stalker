# file network.py ->  implement network options
# author: gauss

import socket


def get_host_inf():
    """return (host_name, ip)"""
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)

    return host_name, host_ip
