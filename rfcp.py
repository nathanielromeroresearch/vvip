import subprocess
import os
import requests
import logging
from colorama import init, Fore, Style

# Initialize colorama
init()

# Check for requests installation
def check_install_requests():
    try:
        import requests
    except ModuleNotFoundError:
        os.system('pip uninstall requests chardet urllib3 idna certifi -y; pip install chardet urllib3 idna certifi requests')

check_install_requests()


# ASCII Art Logo
logo = r"""
             ██████╗ ███████╗ ██████╗██████╗ 
             ██╔══██╗██╔════╝██╔════╝██╔══██╗
             ██████╔╝█████╗  ██║     ██████╔╝
             ██╔══██╗██╔══╝  ██║     ██╔═══╝ 
             ██║  ██║██║     ╚██████╗██║     
             ╚═╝  ╚═╝╚═╝      ╚═════╝╚═╝  [V1.1]
             ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ ʟᴇɪɴᴀᴛʜᴀɴ ᴏʀᴇᴍᴏʀ
"""

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def run_script(script_name):
    try:
        subprocess.run(['python', script_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}Error occurred while running {script_name}: {e}{Style.RESET_ALL}")

def get_approval_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def approval():
    clear_console()
    print(Fore.CYAN + logo + Style.RESET_ALL)  # Display logo in cyan
    user_id = str(os.geteuid())
    uuid = f"{user_id}DS{user_id}"
    key = f"RFCP-{uuid}"

    print("\033[1;37m [\u001b[36m•\033[1;37m] You Need Approval To Use This Tool   \033[1;37m")
    print(f"\033[1;37m [\u001b[36m•\033[1;37m] Your Key :\u001b[36m {key}")
    
    urls = [
        "https://github.com/nathanielromerorfcp/approval/blob/main/VVIPTools/approval.txt"
    ]
    
    key_found = False
    for url in urls:
        approval_data = get_approval_data(url)
        if key in approval_data:
            key_found = True
            break

    if key_found:
        print(f"\033[1;97m >> Your Key Has Been Approved!!!")
        return key
    else:
        
        exit()

def main():
    approval()  # Get approval first
    
    while True:
        clear_console()  # Clear the console before displaying the menu
        print(Fore.CYAN + logo + Style.RESET_ALL)  # Display logo in cyan
        print(Fore.GREEN + "Choose a script to run:" + Style.RESET_ALL)
        print(Fore.YELLOW + "[1.] BOOSTING TOOL" + Style.RESET_ALL)
        print(Fore.YELLOW + "[2.] AUTO CREATE PAGE" + Style.RESET_ALL)
        print(Fore.YELLOW + "[3.] AUTO SPAM SHARE" + Style.RESET_ALL)
        print(Fore.YELLOW + "[4.] TOKEN GETTER [FAST]" + Style.RESET_ALL)
        print(Fore.YELLOW + "[5.] REMOVE INVALID ACCOUNT" + Style.RESET_ALL)
        print(Fore.YELLOW + "[6.] STOP" + Style.RESET_ALL) 
        
        choice = input(Fore.MAGENTA + "Enter the number of your choice: " + Style.RESET_ALL)
        
        if choice == '1':
            run_script('tools/vvip.py')
        elif choice == '2':
            run_script('tools/createpage.py')
        elif choice == '3':
            run_script('tools/removeerror.py')
        elif choice == '4':
            run_script('tools/Tokengetter.py')
        elif choice == '5':
            run_script('tools/removeerror.py')
      
        elif choice == '6':
            print(Fore.GREEN + "Exiting program. Goodbye!" + Style.RESET_ALL)
            break  # Exit the loop to stop the program
        else:
            print(Fore.RED + "Invalid choice. Please choose 1, 2, 3, 4, or 5." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
