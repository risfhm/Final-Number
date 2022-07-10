#!/usr/bin/env python3

import random
from datetime import datetime

MAX=10
RANDOM = random.randint(1, MAX)


def menu():

    print("""

    [1] Casual Mode 
    [2] Extreme Mode
    [3] Help
    [4] Exit

    """)
    
def help():
    pass

def is_winner(random_number, final_number, sub):
    
    if final_number >= 1 and final_number <= MAX:
        if final_number == random_number-sub:
            return True
        
    else:
        return False

def extreme_mode():
    pass

def casual_mode():
    pass
    
    
if __name__ == "__main__":
    
    print(f"Random: {RANDOM}")
    
    final_number = int(input("Final: "))
    sub = int(input("Sub: "))
    
    if(is_winner(RANDOM, final_number, sub)):
        print("You won!")
        
    else:
        print("You lost!")
    
    
        
        
    
        
    
    


