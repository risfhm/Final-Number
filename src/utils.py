# Utils

from colorama import init, Fore, Back, Style

init(autoreset=True)

# ----------------------------------------------

TITLE="""
█▀▀░▀█▀░█▀█░█▀█░█░░░░░█▀█░█░█░█▄█░█▀▄░█▀▀░█▀▄
█▀▀░░█░░█░█░█▀█░█░░░░░█░█░█░█░█░█░█▀▄░█▀▀░█▀▄
▀░░░▀▀▀░▀░▀░▀░▀░▀▀▀░░░▀░▀░▀▀▀░▀░▀░▀▀░░▀▀▀░▀░▀
"""

# ----------------------------------------------


MENU=f"""{Fore.GREEN} {TITLE} {Fore.WHITE}  
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

Choose an option:

[1] Casual Mode
[2] Extreme Mode
[3] Help
[4] Exit
"""

# ----------------------------------------------

DIFF_MENU=f""">>>> {Fore.LIGHTGREEN_EX}Difficulty Menu <<<<
{Fore.WHITE}
[1] Easy 
[2] Normal
[3] Hard
[4] Very Hard 
"""