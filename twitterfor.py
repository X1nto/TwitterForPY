#!/usr/bin/python3.8
import tweepy, os, sys, time
from pathlib import Path

logo = """
████████╗ ██╗       ██╗██╗████████╗████████╗███████╗██████╗   ███████╗ █████╗ ██████╗            
╚══██╔══╝ ██║  ██╗  ██║██║╚══██╔══╝╚══██╔══╝██╔════╝██╔══██╗  ██╔════╝██╔══██╗██╔══██╗           
   ██║    ╚██╗████╗██╔╝██║   ██║      ██║   █████╗  ██████╔╝  █████╗  ██║  ██║██████╔╝           
   ██║     ████╔═████║ ██║   ██║      ██║   ██╔══╝  ██╔══██╗  ██╔══╝  ██║  ██║██╔══██╗           
   ██║     ╚██╔╝ ╚██╔╝ ██║   ██║      ██║   ███████╗██║  ██║  ██║     ╚█████╔╝██║  ██║  ██╗██╗██╗
   ╚═╝      ╚═╝   ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚═╝  ╚═╝  ╚═╝      ╚════╝ ╚═╝  ╚═╝  ╚═╝╚═╝╚═╝
"""

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
    print (logo)

    while True:
        choose = input("1)Tweet\n2)Upload media\n3)Reply to a Tweet\n4)Retweet\n\n[Your Choice]:")
        if choose in ['1', '2', '3', '4']:
            break

    if choose == '1':
        tweet = input("Make a tweet: ")
            
        api.update_status(status =(tweet))
        print ("Succesfully tweeted!")
    elif choose == '2':        
        media = input("Please specify a file: ")
        extensions = ['.png', '.jpg', '.gif', '.mp4', '.mov']
        
        if media.endswith(('.png', '.jpg', '.gif', '.mp4', '.mov')):
            api.media_upload(filename =(media))
            print ("Succesfully Tweeted!")
        else:
            print ("Provide a valid media format (see README)")
            
    elif choose == '3':
        tweet = input("Make a reply: ")
        inreplyto = input("What status is this replying to? (Use an ID of tweet): ")
        
        api.update_status(status =(tweet), in_reply_to_status_id =(inreplyto))
        print ("Succesfully replied!")
        
    elif choose == '4':
        retweet = input("Provide an ID of tweet that you wish to retweet: ")
        api.retweet(id =(retweet))
        print ("Succesfully retweeted!")
else:
    print ("Config not found! Creating config from template...")
    os.rename(r'./tokenconfig.py.template',r'./tokenconfig.py')
    print ("restarting...")
    time.sleep(1.2)
    os.execl(sys.executable, sys.executable, *sys.argv)
    
