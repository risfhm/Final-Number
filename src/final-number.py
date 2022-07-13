#!/usr/bin/env python3

from random import randint
from os import system
from sys import platform

from load import parsing, get_name

PATH="../docs/rules.txt"

tries = 0
salt = 0
victorys = 0
defeats = 0

# --------------------------------------------------------------------

def help():

    with open(PATH, "r") as f:
        for i in f.readlines():
            print(i)
    
    exit(0)
    
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
          
[1] Easy 
[2] Normal
[3] Hard
[4] Very Hard 
    """)
    
    choice = int(input("Enter your choice: "))
    
    if choice >= 1 and choice <= 4:
        return choice
    
    diff_menu()

# --------------------------------------------------------------------

def is_winner(random_number, final_number, sub, max):
    
    if final_number >= 1 and final_number <= max:
        if final_number == random_number-sub:
            return True
         
    else:
        return False
# --------------------------------------------------------------------

def get_diff_name(tries):
    
    diff_dict = {
        5:"Easy",
        3:"Normal",
        2:"Hard",
        1:"Very Hard"
    }
    
    return diff_dict[tries]


# --------------------------------------------------------------------

def get_mode_mame(salt):
    
    mode_dict = {
        2:"Casual Mode",
        10:"Extreme Mode"
    }
    
    return mode_dict[salt]

# --------------------------------------------------------------------

def play_game():
    
    clear()
    
    max = 10
    random = randint(1, max)
    name = get_name()
    current_tries = tries
    level = 1
    
    print(f"Hello, {name}!\nWelcome to Final Number!\n")
    
    print(f"Mode: {get_mode_mame(salt)} (salt: {salt})")
    print(f"Difficulty: {get_diff_name(tries)} (tries: {tries})")
    
     
    while current_tries != 0:
        
        print(f"\nLevel: {level}\nCurrent tries: {current_tries}")
        # print(f"Random: {random}")
        
        final_number = int(input("\nFinal Number: "))
        sub = int(input("\nSub: "))
        # print(f"Result: {random-sub}")
        
        if level != 5:
            if(is_winner(random, final_number, sub, max)):
        
                current_tries = tries
                max += salt
                random = randint(1, max)
                level += 1
                
                clear()
        
            else:
                current_tries -= 1
                clear()
                print("\nyou fail !\n")
                
        else:
            clear()
            print("Congratulations!")
            
            choice = input("Try again? [y/n]: ")
            
            if choice.lower() == "y":
                play_game()
    
            else:
                exit(0)
        
    
    print("Gamer Over!  ): ")
    choice = input("Try again? [y/n]: ")
    
    if choice.lower() == "y":
        play_game()
    
    else:
        exit(0)
    
    

        
# ------------------ CÓDIGO PRINCIPAL ------------------------ #

if __name__ == "__main__":
    
    if parsing():
        print("Your name has been updated successfully!")
        
    diff_list = [5, 3, 2, 1]
    salt_list = [2, 10]
    
    choice = 0
    
    while choice != 4:
        
        menu()
        choice = int(input("Enter your choice: "))
    
        if choice == 1 or choice == 2:
            tries = diff_list[diff_menu()-1]
            salt = salt_list[choice-1]

            play_game()

        elif choice == 3:
            help()

        elif choice == 4:
            exit(0)
            
        else:
            clear()
            continue
    
    
# --------------------------------------------------------------------
