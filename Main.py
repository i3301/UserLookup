import requests
from colorama import Fore

def print_banner():
    try:
        with open("banner.txt", 'r', encoding='utf-8') as file:
            banner_content = file.read()
            print(f"{banner_content}")
    except FileNotFoundError:
        print(f"Error: File 'banner.txt' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print_banner()

Username = input(f"{Fore.MAGENTA}[*]Target Username: ")

with open("Sites.txt", "r") as file:
    Sites = [line.strip() for line in file.readlines()]

def Make_Request(site):
    url = f"{site}/{Username}"
    response = requests.get(url)
    if response.status_code == 200:
        if Username in response.text:
            print(f"{Fore.GREEN}[+]{url} -Username found")
        else:
            return None

if __name__ == "__main__":
    print(f"{Fore.MAGENTA}[!]Working. . .")
    for site in Sites:
        Make_Request(site)
        
input(f"{Fore.MAGENTA}[*]Press Enter To Exit. . .")