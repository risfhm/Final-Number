from colorama import init, Fore, Back, Style
from os import system
from sys import platform

init(autoreset=True)

# ----------------------------------------------

TITLE="""
█▀▀░▀█▀░█▀█░█▀█░█░░░░░█▀█░█░█░█▄█░█▀▄░█▀▀░█▀▄
█▀▀░░█░░█░█░█▀█░█░░░░░█░█░█░█░█░█░█▀▄░█▀▀░█▀▄
▀░░░▀▀▀░▀░▀░▀░▀░▀▀▀░░░▀░▀░▀▀▀░▀░▀░▀▀░░▀▀▀░▀░▀
"""

# ----------------------------------------------


MENU=f"""{Fore.GREEN} {TITLE} {Fore.CYAN}
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-{Fore.YELLOW}

[1] {Fore.CYAN}Casual Mode{Fore.YELLOW}
[2] {Fore.CYAN}Extreme Mode{Fore.YELLOW}
[3] {Fore.CYAN}Help{Fore.YELLOW}
[4] {Fore.CYAN}Exit{Fore.YELLOW}
"""

# ----------------------------------------------

DIFF_MENU=f"""{Fore.CYAN}>>>> {Fore.LIGHTGREEN_EX}Difficulty Menu {Fore.CYAN}<<<<
{Fore.YELLOW}
[1] {Fore.CYAN}Easy{Fore.YELLOW}
[2] {Fore.CYAN}Normal{Fore.YELLOW}
[3] {Fore.CYAN}Hard{Fore.YELLOW}
[4] {Fore.CYAN}Very Hard{Fore.YELLOW}
"""

def generate_msg(name, mode_name, diff_name, defeats):
    return f"""[cyan bold][+][/cyan bold] [green]Congratulations, [bold]{name}[/bold]! Thank you for playing our considerably difficult game, you really 
should be proud at this point. Well, can you repeat this feat?
    
[cyan bold][+][/cyan bold] [green]MODE: {mode_name}
[cyan bold][+][/cyan bold] [green]DIFFICULTY: {diff_name}
[cyan bold][+][/cyan bold] [green]FAILURE: {defeats}"""

def clear():
    
    platforms = {
        "linux":"clear",
        "linux2":"clear",
        "win32":"cls",
        "darwin":"clear"
    }
    
    if platform in platforms:
        system(platforms[platform])
    