# Import the required packages and modules
import requests
from colorama import Style, Fore, Back

# Ask the user to provide the IP address
ip_addr = input(f"{Back.GREEN}Please provide the IP address:{Style.RESET_ALL} ")

# Define a function to retrieve the location details
def get_loc():
    res = requests.get(f"https://ipapi.co/{ip_addr}/json/").json()
    return res


# Check if the IP address is provided by the user
if not ip_addr:
    print(
        f"{Fore.RED}ERROR:\nThe IP address must contain a value and cannot be left blank \nTerminating the program.....{Style.RESET_ALL}"
    )
else:
    # Retrieve the location details and display them
    output = str(get_loc())
    print("\n")
    for val in output.split(","):
        print(f"{Fore.WHITE}{val}{Style.RESET_ALL}")
