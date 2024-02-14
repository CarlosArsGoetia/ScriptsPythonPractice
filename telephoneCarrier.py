#!/usr/bin/env python3
from colorama import Fore
import phonenumbers 
from phonenumbers import geocoder, timezone, carrier
import sys, signal

def def_handler(sig,frame):
    print(Fore.WHITE+"\n\n[***] Running out...[***]\n")
    sys.exit(1)

#Ctrl+C for exit
signal.signal(signal.SIGINT, def_handler)


while True:
     
        target = input(Fore.LIGHTBLACK_EX+"Please enter your phone number" + Fore.LIGHTYELLOW_EX+"(PhoneNumberFormat)" + Fore.YELLOW+"\nEXAMPLE: +58412330xxx\n" + Fore.LIGHTBLACK_EX+" Type the Number: ")
        if target.isalpha() is True:
            print("Enter a valid phone number")
        else: break   


number = phonenumbers.parse(target)

zone = timezone.time_zones_for_number(number)

geo = geocoder.description_for_number(number, 'en')

carrier = carrier.name_for_number(number, 'en')

print(Fore.RED+f"\nZone: {zone}  \nCountry: {geo}  \nCompany: {carrier}")
