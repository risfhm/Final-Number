#!/usr/bin/env python3

from random import randint
from os import system
from sys import platform

from load import parsing, get_name

max = 10
random = randint(1, max)
tries = 0

# --------------------------------------------------------------------

def help():
    pass

# --------------------------------------------------------------------

def clear():
    
    platforms = {
        "linux":"clear",
        "linux2":"clear",   
        "win32":"cls",
        "darwin":"clear"
    }
    
    if platform in platforms:
        system(platforms[platform])

# --------------------------------------------------------------------

def menu():

    print("""
-=-=- Final Number -=-=-
          
[1] Casual Mode 
[2] Extreme Mode
[3] Help
[4] Exit
    """)

# --------------------------------------------------------------------

def diff_menu():

    clear()

    print("""  
-=-=- Difficulty Menu -=-=-
          
[1]  Easy 
[2]  Normal
[3]  Hard
[4]  Very Hard 
    """)
    
    choice = int(input("Enter your choice: "))
    
    if choice >= 1 and choice <= 4:
        return choice
    
    diff_menu()

# --------------------------------------------------------------------

def is_winner(random_number, final_number, sub):
    
    if final_number >= 1 and final_number <= max:
        if final_number == random_number-sub:
            return True
         
    else:
        return False

# --------------------------------------------------------------------

def extreme_mode(tries, diff_name):
    
    name = get_name()
    
    print(f"Hello, {name}!\nWelcome to Final Number")
    exit(0)
    
    
    

# --------------------------------------------------------------------



def casual_mode(tries, diff_name):
    
    name = get_name()
    
    print(f"Hello, {name}!\nWelcome to Final Number")
    exit(0)
   
   
        
# ------------------ CÓDIGO PRINCIPAL ------------------------ #

if __name__ == "__main__":
    
    if parsing():
        print("Your name has been updated successfully!")
        
    
    diff_list = {
        1: 5, 
        2: 3, 
        3: 2, 
        4: 1
    }
    
    diff_name = {
        5: "Easy", 
        3: "Normal", 
        2: "Hard", 
        1: "Very Hard"
    }
    
    choice = 0
    
    while choice != 4:
        
        menu()
        choice = int(input("Enter your choice: "))
    
        tries = diff_list[diff_menu()]
    
        if choice == 1:

            casual_mode(tries, diff_name[tries])

        elif choice == 2:

            extreme_mode(tries, diff_name[tries])

        elif choice == 3:
            help()

        elif choice == 4:
            exit(0)
            
        else:
            clear()
            continue
    
    
# --------------------------------------------------------------------