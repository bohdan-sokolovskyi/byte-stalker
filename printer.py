# printer module for print text
# author: Gauss

import platform
import os


def get_os():
    name_os = platform.system().lower()

    if name_os == "darwin":
        return name_os + " (Mac OS)"
    else:
        return name_os


def _get_size_of_terminal():
    return os.popen('stty size', 'r').read().split()


def print_logo():
    rows, columns = _get_size_of_terminal()

    print("#" * int(columns), end="")
    print("""
______       _       _____ _        _ _             
| ___ \     | |     /  ___| |      | | |            
| |_/ /_   _| |_ ___\ `--.| |_ __ _| | | _____ _ __ 
| ___ \ | | | __/ _ \`--. \ __/ _` | | |/ / _ \ '__|
| |_/ / |_| | ||  __/\__/ / || (_| | |   <  __/ |   
\____/ \__, |\__\___\____/ \__\____|_|_|\_\___|_|   
        __/ |                                       
       |___/                                        
    """)
    print("Author: gauss")
    print("Launched on {0}".format(get_os()))
    print("#" * int(columns))


def print_help(helper_file):
    for line in open(helper_file, "r"):
        print(line, end="")


def print_net_info(info):
    print("Host: {0}\nIP: {1}\n".format(info[0], info[1]))
