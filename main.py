# main
# author: gauss

import printer
import sys
import console
import os


def run(arg=None):
    printer.print_logo()
    console.run_console()
    # only unix like system
    os.system('clear')


def parse_args():
    args = sys.argv[1:]
    prime_arg = args[0]

    if prime_arg == '-h' or prime_arg == '--help':
        printer.print_help("help")
    elif prime_arg == '-c':
        console.run_console()
    else:
        print("Error args, try use 'byte-stalker -h or --help")


if __name__ == '__main__':
    if len(sys.argv) == 1:
        run()
    else:
        parse_args()
