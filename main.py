import requests
from colorama import Style, Fore, Back

ip_addr = input(f"{Back.GREEN}Please provide the IP address:{Style.RESET_ALL} ")


def get_loc():
    res = requests.get(f"https://ipapi.co/{ip_addr}/json/").json()
    return res


if not ip_addr:
    print(
        f"{Fore.RED}ERROR:\nThe IP address must contain a value and cannot be left blank \nTerminating the program.....{Style.RESET_ALL}"
    )
else:
    output = str(get_loc())
    print("\n")
    for val in output.split(","):
        print(f"{Fore.WHITE}{val}{Style.RESET_ALL}")
