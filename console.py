# file console.py -> implement console option
# author: gauss

import printer
import network
import os

# codes of operations
_EXIT = 0x0
_ERROR = 0x1
_SUCCESS = 0x2


def run_console():
    print("\nRunning console...")
    while True:
        res = input("-> ")
        resp_code = parse_command(res)

        if resp_code == _EXIT:
            break
        elif resp_code == _ERROR:
            print("Unknown command :(, try use 'help' or 'get help'", end="\n\n")


def parse_command(command):
    lst_command = command.split(' ')
    first = lst_command[0]

    if first == 'exit' or first == 'quit':
        return _EXIT
    elif first == 'get':
        return _parse_get_command(lst_command[1:])
    elif first == 'net':
        return _parse_net_command(lst_command[1:])
    elif first == 'clear':
        # only unix-like system
        os.system('clear')
        printer.print_logo()
        print()
    elif first == 'help':
        if lst_command[1:]:
            printer.print_help('man-' + lst_command[1])
        else:
            printer.print_help("help-console")
        print("\n\n")
    else:
        return _ERROR

    return _SUCCESS


def _parse_get_command(command):
    first = command[0]

    if first == 'os':
        print(printer.get_os(), end="\n\n")
    elif first == 'help':
        parse_command(first)
    else:
        return _ERROR

    return _SUCCESS


def _parse_net_command(command):
    first = command[0]

    if first == 'host':
        print(network.get_host_inf()[0], end="\n\n")
    elif first == 'ip':
        print(network.get_host_inf()[1], end="\n\n")
    elif first == 'info':
        printer.print_net_info(network.get_host_inf())
    else:
        return _ERROR

    return _SUCCESS





