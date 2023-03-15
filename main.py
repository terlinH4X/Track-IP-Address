# Import the required packages and modules
import requests
from colorama import Style, Fore, Back
import time
from validate_IP import is_valid

# Ask the user to provide the IP address
ip_addr = input(f"{Back.GREEN}Please provide the IP address:{Style.RESET_ALL} ")

# Define a function to retrieve the location details
def get_loc():
    try:
        res = requests.get(f"https://ipapi.co/{ip_addr}/json/").json()
        return res
    except Exception:
        return None


# Check if the IP address is provided by the user
if not ip_addr:
    print(
        f"{Fore.RED}ERROR:\nThe IP address must contain a value and cannot be left blank \nTerminating the program.....{Style.RESET_ALL}"
    )
    time.sleep(3)
elif not is_valid(ip_addr):
    print(
        f"{Fore.RED}ERROR:\nInvalid IP address \nTerminating the program.....{Style.RESET_ALL}"
    )
    time.sleep(3)
elif not get_loc():
    print(
        f"{Fore.RED}ERROR:\nAn error occurred while retrieving the location details \nTerminating the program.....{Style.RESET_ALL}"
    )
    time.sleep(3)
else:
    # Retrieve the location details and display them
    try:
        output = str(get_loc())
        print("\n")
        for val in output.split(","):
            print(f"{Fore.WHITE}{val}{Style.RESET_ALL}")
        time.sleep(1)
    except KeyboardInterrupt:
        print(
            f"{Fore.RED}ERROR:\nUser has interrupted the process \nTerminating the program.....{Style.RESET_ALL}"
        )
        time.sleep(3)
