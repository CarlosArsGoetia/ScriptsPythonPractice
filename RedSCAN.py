#!/usr/bin/python3
import nmap
from tqdm.auto import  tqdm 
import  sys , signal
"""
tqdm are for process bar //  sys and signal are for calling the function to close the script 
and nmap is for processing the scan  //
you can install nmap like this
pip install python-nmap
"""

def def_handler(sig,frame):
    print("\n\n[***] Running out...[***]\n")
    sys.exit(1)

#Ctrl+C for exit
signal.signal(signal.SIGINT, def_handler)

scaner = nmap.PortScanner()

while True:
     
        ip = input("Insert the ip range: ")
        if ip.isalpha() is True:
            print("Enter a valid IP address")
        else: break    
   
scaner.scan(ip)

print(scaner.all_hosts())

#Process bar
for x in tqdm(range(10000)):
   print("", end='\r' )
