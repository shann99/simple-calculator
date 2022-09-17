#!/usr/bin/env python3

import pyfiglet
from simple_term_menu import TerminalMenu

print("\n")

print(pyfiglet.figlet_format("Welcome to the Simple Calculator App!", justify="center"))
print("\n")

def main():
    
    #calculator stuff
    def calculator():
        options = ["addition", "subtraction", "multiplication", "division"]
        terminal_menu = TerminalMenu(options, title="Select the type of calculation you would like to do! \n")
        menu_entry_index = terminal_menu.show()
        #print(f"\033[0;29mLet's do some {options[menu_entry_index]}\n")

        if menu_entry_index == 0:
            try:
                num1 = float(input("\nPlease enter the first number: "))
                num2 = float(input("\nPlease enter the second number: "))
                total = num1 + num2
                print(f"\n{num1} + {num2} = {total}")
            except:
                print("please make sure you are entering only a number and not a string")

        elif menu_entry_index == 1:
            try:
                num1 = float(input("\nPlease enter the first number: "))
                num2 = float(input("\nPlease enter the second number: "))
                total = num1 - num2
                print(f"\n{num1} - {num2} = {total}")
            except:
                print("please make sure you are entering only a number and not a string")

        elif menu_entry_index == 2:
            try:
                num1 = float(input("\nPlease enter the first number: "))
                num2 = float(input("\nPlease enter the second number: "))
                total = num1 * num2
                print(f"\n{num1} x {num2} = {total}")
            except:
                print("please make sure you are entering only a number and not a string")

        elif menu_entry_index == 3:
            try:
                num1 = float(input("\nPlease enter the first number: "))
                num2 = float(input("\nPlease enter the second number: "))
                total = num1 / num2
                print(f"\n{num1} / {num2} = {total}")
            except:
                print("please make sure you are entering only a number and not a string")
        
        
   #actually calling the calculator stuff
    calculator()
    print("\n")
    
    while True:
        print("\n")
        print('\033[1;36mWould you like to do another calculation? \n')
        restartOps = ["Yes", "No"]
        restart_menu = TerminalMenu(restartOps)
        restart_menu_index = restart_menu.show()

        if restart_menu_index == 0:
            calculator()
            
        elif restart_menu_index == 1:
            print('\033[1;31mThe program has ended')
            exit()

    

    



#mention to select and hit enter
#once a selection is made and the numbers are inputted, ask if they want to calculate again or exit
if __name__ == "__main__":
    main()



