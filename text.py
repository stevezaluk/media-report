from colorama import Style, Fore, Back
import sys

def print_info(text):
    print(Fore.BLUE + '[i] ' + Style.RESET_ALL + text)

def print_info_no_end(text):
    print(Fore.BLUE + '[i] ' + Style.RESET_ALL + text, end=' ')

def print_error(text):
    print(Fore.RED + '[!] ' + Style.RESET_ALL + text)
    sys.exit(1)

def print_good(text):
    print(Fore.GREEN + '[+] ' + Style.RESET_ALL + text)

def print_header(text):
    print(Fore.MAGENTA + '==> ' + Style.RESET_ALL + text)

def print_movie(text, var=None):
    if var is None:
        print(Fore.RED + '[M] ' + Style.RESET_ALL + text)
    else:
        print(Fore.RED + '[M] ' + Style.RESET_ALL + text, var)

def print_tv(text, var=None):
    if var is None:
        print(Fore.CYAN + '[TV] ' + Style.RESET_ALL + text)
    else:
        print(Fore.CYAN + '[TV] ' + Style.RESET_ALL + text, var)
