'''
COLOUR DESCRIPTION-->  BLUE: Heading 
                       MAGENTA: Default  
                       YELLOW: Description
                       GREEN: To indicate object works
                       WHITE: "Data"
                       RED: Error
'''
# CODE STARTS FROM HERE2
from DBclass import mydb
import colorama
from colorama import Fore, Back, Style
import time

def main():
    obj = mydb()
    colorama.init(autoreset=True)
    print(f"{Fore.BLUE}{Style.BRIGHT}************* WELLCOME TO OUR CONSOULE APP *************")
    print(f'{Fore.MAGENTA}Preapring consoule for you please wait....')
    time.sleep(3)

    while True:
        print(f"{Fore.YELLOW}{Style.BRIGHT}DESCRIPTION")
        print(f"{Fore.YELLOW}Choose 1 to insert user.")
        print(f"{Fore.YELLOW}Choose 2 for display user .")
        print(f"{Fore.YELLOW}Choose 3 for delete user.")
        print(f"{Fore.YELLOW}Choose 4 for update user.")
        print(f"{Fore.YELLOW}Choose 5 for exit.")
        print()
        print()

        choice = int(input(f"{Fore.MAGENTA}ENTER YOUR CHOICE: "))
        try:      
            if(choice == 1):   
               # INSERTION
                userId = int(input(f"{Fore.MAGENTA}Enter user id: "))
                userName = input(f"{Fore.MAGENTA}Enter name of user: ")
                userAdd = input(f"{Fore.MAGENTA}Enter addres of user: ")
                print(f"{Fore.GREEN}Inserting......")
                time.sleep(2)
                obj.add_into(userId,userName,userAdd)
                print(f"{Fore.GREEN}{Style.BRIGHT}INSERTED SUCSSECFULLY\n\n")               
            
            elif(choice == 2):
                # TO DISPLAY
                print(f"{Fore.GREEN}DISPLAYING.....")
                time.sleep(2)
                obj.fetch()
                print(f"{Fore.GREEN}{Style.BRIGHT}ALL DATA FROM TABLE HAS BEEN FATCHED\n\n")                
                
            elif(choice == 3):
                # TO DELETE
                userId = int(input(f"{Fore.MAGENTA}Enter user id: "))
                print(f"{Fore.GREEN}DELETING....")
                time.sleep(2)
                obj.delete(userId)
                print(f"{Fore.GREEN}{Style.BRIGHT}Deleted SUCSSECFULLY\n\n")
                                       
            elif(choice == 4):
                # TO UPDATE
                col1_name = input(f"{Fore.MAGENTA}Enter the name of coloum you want to change: ")
                n_col1 = input(f"{Fore.MAGENTA}Enter new value:")
                col2_name = input(f"{Fore.MAGENTA}Enter the name of coloum you want to change: ")
                n_col2 = input(f"{Fore.MAGENTA}Enter new value:")  
                userId = int(input(f"{Fore.MAGENTA}Enter user id: "))
                print(f"{Fore.GREEN}UPADATING....")
                time.sleep(2)                
                obj.toUpdate(col1_name,n_col1,col2_name,n_col2,userId)
                print(f"{Fore.GREEN}{Style.BRIGHT}UPDATED SUCCESSFULLY\n\n")             
                              
            elif(choice == 5):
                # TO EXIT
                print(f"{Fore.GREEN}Do you want to exit. Yes or No")
                ans = input("").lower()
                if ans=="yes":
                    print(f"{Fore.MAGENTA}{Back.WHITE}EXITING FROM THE APP...")
                    time.sleep(2)
                    break
                else:
                    continue                             
            else:
                print(f"{Fore.RED}{Style.BRIGHT}{choice} IS NOT DEFINED.PLEASE, ENTER VALID INPUT")
                            
        except Exception as e:
            print(e)   
            print(f"{Fore.RED}{Style.BRIGHT}ERROR, it seem's you have entered invalid details.")    


if __name__ == "__main__":
    main()