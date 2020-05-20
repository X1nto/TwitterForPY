#!/usr/bin/python3.8
import time
import functions as fn
import os
import sys
from pathlib import Path

print ("Checking config file...")
config = Path("./config.py")
if config.is_file():
    print ("Found config!")
    print ("Importing functions...")
    time.sleep(1)
    print ("Initialising...")
    fn.mainmenu()
    
else:
    print ("Config not found! Creating config...")
    with open('config.py', 'a') as file:
        apikey = input("Please enter your api key: ")
        file.write("api_key = " + "'" + apikey + "'")
        apiseckey = input("Please enter your API Secret Key: ")
        file.write("\napi_secret_key = " + "'" + apiseckey + "'")
        acctok = input("Please enter your access token: ")
        file.write("\nAccessToken = " + "'" + acctok + "'")
        accsectok = input("Please enter your Access Secret Token: ")
        file.write("\nAccessSecretToken = " + "'" + accsectok + "'")
    os.execl(sys.executable, sys.executable, *sys.argv)
