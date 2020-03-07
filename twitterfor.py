#!/bin/python3.8
import tweepy, os, sys, time
from pathlib import Path


print ("Checking config file...")
config = Path("./tokenconfig.py")
if config.is_file():
    import tokenconfig as cfg
    
    auth = tweepy.OAuthHandler(cfg.ConsumerAPI['api_key'], cfg.ConsumerAPI['api_secret_key'])
    auth.set_access_token(cfg.AccessToken['access_token'], cfg.AccessToken['access_token_secret'])

    api = tweepy.API(auth)

    print ("Found config!")
    print ("Initialising...")
    time.sleep(1)
    print ("\nTwitter For [redacted]")
    print ("Is this tweet a reply? Use Y or N")



    while True:
        isitareply = input("[Y/N]:")
        if isitareply in ['Y', 'N']:
            break

    if isitareply == 'Y':
        tweet = input("Make a reply: ")

        inreplyto = input("What status is this replying to? (Use an ID of tweet): ")

        api.update_status(status =(tweet), in_reply_to_status_id =(inreplyto))
        print ("Succesfully replied!")
    else:
        tweet = input("Make a tweet: ")

        api.update_status(status =(tweet))
        print ("Succesfully tweeted!")
        
else:
    print ("Config not found! Creating config from template...")
    os.rename(r'./tokenconfig.py.template',r'./tokenconfig.py')
    print ("restarting...")
    time.sleep(1.2)
    os.execl(sys.executable, sys.executable, *sys.argv)

    
