#!/usr/bin/env python3

from random import randint
from rich.table import Table
from rich.panel import Panel
from rich.console import Console

from load import parsing, get_name
from utils import *

PATH="../docs/rules.txt"

tries = 0
salt = 0
defeats = 0


def help():
    clear()

    with open(PATH, "r") as file:
        for line in file.readlines():
            print(line)
    
    exit(0)
    

def menu():
    clear()
    print(MENU)    


def diff_menu():
    
    while True:
        clear()

        print(DIFF_MENU)

        try:
            choice = int(input(f"{Style.BRIGHT}Enter your choice::> {Style.NORMAL}"))
        
        except ValueError:
            clear()
            continue
    
        if choice >= 1 and choice <= 4:
            return choice


def generate_report(name, mode_name, diff_name):
    
    msg = generate_msg(name, mode_name, diff_name, defeats)
    console = Console()
    
    console.print(Panel(
        msg,
        title="[cyan bold] GAME REPORT",
        subtitle="[cyan bold] >> FINAL NUMBER <<",
        expand=False, 
        style="white"
    ))
    print("\n")


def final_menu(msg):
    
    while True:
        
        if msg.lower() == "try":
            print(f"{Fore.RED}[-] Game Over! :(")
        
        choice = input(f"{Fore.YELLOW}[-] {msg} again? (y/n): ").lower()

        if choice in ("y", "n"):
            play_game() if choice == "y" else exit(0)
            

def is_winner(random_number, final_number, sub, max):
    
    if final_number >= 1 and final_number <= max:
        if final_number == random_number-sub:
            return True
         
    else:
        return False
    

def get_diff_name(tries):
    
    diff_dict = {
        5:"Easy",
        3:"Normal",
        2:"Hard",
        1:"Very Hard"
    }
    
    return diff_dict[tries]


def get_mode_mame(salt):
    
    mode_dict = {
        2:"Casual Mode",
        10:"Extreme Mode"
    }
    
    return mode_dict[salt]


def play_game():
    clear()
    
    global defeats
    
    max = 10
    name = get_name()
    mode_name = get_mode_mame(salt)
    diff_name = get_diff_name(tries)
    random = randint(1, max)
    current_tries = tries
    level = 1
    
    print(f"{Fore.GREEN}[#]{Fore.CYAN} Hello, {name}!")
    print(f"{Fore.GREEN}[#]{Fore.CYAN} Welcome to Final Number! Good luck...{Fore.RESET}\n")
    
    table_md = Table(show_header=False)
    table_md.add_column(style="green")
    table_md.add_row(f"[bold][*] MODE: {mode_name} (salt={salt})")
    table_md.add_row(f"[bold][*] DIFFICULTY: {diff_name} (tries={tries})")
    
    console = Console()
    console.print(table_md)
     
    while current_tries != 0:
        
        table_cm = Table(show_header=False)
        table_cm.add_column(style="cyan")
        table_cm.add_row(f"[bold][-] CURRENT TRIES: {current_tries}")
        table_cm.add_row(f"[bold][-] MAX RANDOM: (1 - {max})")
        table_cm.add_row(f"[bold][*] LEVEL: {level}")
        
        console.print(table_cm)
        
        print(f"\n{Style.BRIGHT}[x] Random: {random}{Style.NORMAL}\n")
        
        try:
            final_number = int(input(f"{Style.BRIGHT}[x] Final Number::> "))
            
            if final_number <= 0 or final_number > max:
                clear()
                continue
            
            sub = int(input(f"[x] Sub::> "))
            
        except ValueError:
            clear()
            continue
        
        if(is_winner(random, final_number, sub, max)):
            current_tries = tries
            max += salt
            random = randint(1, max)
            level += 1
           
            clear()
            
            if level == 5+1: 
                generate_report(name, mode_name, diff_name)
                final_menu("Play")

        else:
            current_tries -= 1
            defeats += 1
            
            clear()
            print(f"{Style.NORMAL}{Fore.RED}[-] You failed! :(\n{Fore.RESET}")
        
    final_menu("Try")


if __name__ == "__main__":
    
    if parsing():
        print(f"{Fore.CYAN}Your name has been updated successfully!{Fore.RESET}")
        exit(0)
        
    diff_list = [5, 3, 2, 1]
    salt_list = [2, 10]
    
    while True:
        
        menu()
        
        try:
            choice = int(input(f"{Style.BRIGHT}Enter your choice::> {Style.NORMAL}"))
        
        except ValueError:
            clear()
            continue
    
        if choice == 1 or choice == 2:
            tries = diff_list[diff_menu()-1]
            salt = salt_list[choice-1]

            play_game()

        elif choice == 3:
            help()

        elif choice == 4:
            exit(0)
    