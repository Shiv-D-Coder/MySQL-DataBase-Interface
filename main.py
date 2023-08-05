'''
COLOUR DESCRIPTION-->  BLUE: Heading 
                       MAGENTA: Default  
                       YELLOW: Description
                       GREEN: To indicate object works
                       WHITE: "Data"
                       RED: Error
'''
from DBclass import mydb

import colorama
from colorama import Fore, Back, Style
import time

# Function to start the main console app
def main():
    # Creating an instance of the mydb class
    obj = mydb()

    # Initializing colorama to automatically reset color settings
    colorama.init(autoreset=True)

    # Displaying a welcome message
    print(f"{Fore.BLUE}{Style.BRIGHT}************* WELCOME TO OUR CONSOLE APP *************")
    print(f'{Fore.MAGENTA}Preparing console for you, please wait....')
    time.sleep(3)

    # Main loop to present the user with options and handle their choice
    while True:
        # Displaying the menu
        print(f"{Fore.YELLOW}{Style.BRIGHT}DESCRIPTION")
        print(f"{Fore.YELLOW}Choose 1 to insert user.")
        print(f"{Fore.YELLOW}Choose 2 for display user.")
        print(f"{Fore.YELLOW}Choose 3 for delete user.")
        print(f"{Fore.YELLOW}Choose 4 for update user.")
        print(f"{Fore.YELLOW}Choose 5 for exit.")
        print()
        print()

        # Getting the user's choice
        choice = int(input(f"{Fore.MAGENTA}ENTER YOUR CHOICE: "))
        try:
            if choice == 1:
                # INSERTION
                userId = int(input(f"{Fore.MAGENTA}Enter user id: "))
                userName = input(f"{Fore.MAGENTA}Enter name of user: ")
                userAdd = input(f"{Fore.MAGENTA}Enter address of user: ")
                print(f"{Fore.GREEN}Inserting......")
                time.sleep(2)
                obj.add_into(userId, userName, userAdd)
                print(f"{Fore.GREEN}{Style.BRIGHT}INSERTED SUCCESSFULLY\n\n")

            elif choice == 2:
                # TO DISPLAY
                print(f"{Fore.GREEN}DISPLAYING.....")
                time.sleep(2)
                obj.fetch()
                print(f"{Fore.GREEN}{Style.BRIGHT}ALL DATA FROM TABLE HAS BEEN FETCHED\n\n")

            elif choice == 3:
                # TO DELETE
                userId = int(input(f"{Fore.MAGENTA}Enter user id: "))
                print(f"{Fore.GREEN}DELETING....")
                time.sleep(2)
                obj.delete(userId)
                print(f"{Fore.GREEN}{Style.BRIGHT}DELETED SUCCESSFULLY\n\n")

            elif choice == 4:
                # TO UPDATE
                col1_name = input(f"{Fore.MAGENTA}Enter the name of column you want to change: ")
                n_col1 = input(f"{Fore.MAGENTA}Enter new value:")
                col2_name = input(f"{Fore.MAGENTA}Enter the name of column you want to change: ")
                n_col2 = input(f"{Fore.MAGENTA}Enter new value:")
                userId = int(input(f"{Fore.MAGENTA}Enter user id: "))
                print(f"{Fore.GREEN}UPDATING....")
                time.sleep(2)
                obj.toUpdate(col1_name, n_col1, col2_name, n_col2, userId)
                print(f"{Fore.GREEN}{Style.BRIGHT}UPDATED SUCCESSFULLY\n\n")

            elif choice == 5:
                # TO EXIT
                print(f"{Fore.GREEN}Do you want to exit? Yes or No")
                ans = input("").lower()
                if ans == "yes":
                    print(f"{Fore.MAGENTA}{Back.WHITE}EXITING FROM THE APP...")
                    time.sleep(2)
                    break
                else:
                    continue
            else:
                # Invalid choice
                print(f"{Fore.RED}{Style.BRIGHT}{choice} IS NOT DEFINED. PLEASE ENTER A VALID INPUT")

        except Exception as e:
            # Handling any exceptions and displaying an error message
            print(e)
            print(f"{Fore.RED}{Style.BRIGHT}ERROR: It seems you have entered invalid details.")


if __name__ == "__main__":
    # Starting the main function when the script is run directly
    main()