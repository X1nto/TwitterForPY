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
        choose = input("1)Fetch your timeline\n2)Tweet\n3)Upload media (Not Working)\n4)Reply to a Tweet\n5)Retweet\n6)List DM\n7)Send DM\n\nq)Quit\n\n[Your Choice]:")
        if choose in ['1', '2', '3', '4', '5', '6', '7', 'q']:
            break
        
    if choose == '1':
        tweets = api.home_timeline(count = '20')
        for status in tweets:
            print ('\n' + status.user.name + ":", status.text, status.id)
        
    elif choose == '2':
        tweet = input("Make a tweet: ")
        api.update_status(status =(tweet))
        print ("Succesfully tweeted!")
        
    elif choose == '3':        
        media = input("Please specify a file: ")
        api.media_upload(filename =(media))
        print ("Succesfully Tweeted!")

    elif choose == '4':
        tweet = input("Make a reply: ")
        inreplyto = input("What status is this replying to? (Use an ID of tweet): ")        
        api.update_status(status =(tweet), in_reply_to_status_id =(inreplyto))
        print ("Succesfully replied!")
        
    elif choose == '5':
        retweet = input("Provide an ID of tweet that you wish to retweet: ")
        api.retweet(id =(retweet))
        print ("Succesfully retweeted!")
    
    elif choose == '6':
        dmcnt = input("How many DMs do you want to list: ")
        dmlist = api.list_direct_messages(count =(dmcnt))
        print (dmlist)
    
    elif choose == '6':
        dmid = input("Direct ID: ")
        dmtext = input("Text: ")
        api.send_direct_message(recipient_id =(dmid), text =(dmtext))
        
    elif choose == 'q':
        print ("Goodbye!")
        
else:
    print ("Config not found! Creating config from template...")
    os.rename(r'./tokenconfig.py.template',r'./tokenconfig.py')
    print ("restarting...")
    time.sleep(1.2)
    os.execl(sys.executable, sys.executable, *sys.argv)
