#!/usr/bin/python
import base64
import sys, signal


"""Sys and sig are imported for the ctrl_c function as usual and in this case base64 for decode/encode.
"""
def def_handler(sig,frame):
    print("\n\n[!]Running Out \n")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)
#Ctrl+C for a clean exit

""" We will make the user choose between the two options controlling that he 
can only enter one of the two options "1" or "2" """

while True:
    options = input("ENCODE (1) \nDECODE(2)\n: ")
    if options.isdigit() and int(options) in [1, 2]:
        break
    else:
        print("[!]ONLY NUMBERS [1 or 2]")

# If the option is "1" encoded
# If the option is "2" decoded

if options == "1":
    message = input("Enter the phrase to be encoded: ")
    decode_message = base64.b64encode(message.encode())
    print("ENCODE Base64: ", decode_message.decode())
    
else:
    message_base64 = input("Enter the prhrase to be decode: ")
    decode_message = base64.b64decode(message_base64)
    print("DECODE MESSAGE: " + str(decode_message))









