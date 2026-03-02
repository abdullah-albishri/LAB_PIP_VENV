from art import tprint , aprint
from colorama import Fore , Back 


print(Fore.GREEN + "Style: Success / Font: 'standard'")
tprint("PASSED", font="standard")
aprint("happy") 

print(Fore.RED + Back.YELLOW + " WARNING: SYSTEM OVERLOAD ")
tprint("DANGER", font="block")