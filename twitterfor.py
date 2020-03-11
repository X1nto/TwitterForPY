#!/usr/bin/python3.8
import tweepy, os, sys, time, datetime, timedelta
from pathlib import Path

logo = """
████████╗ ██╗       ██╗██╗████████╗████████╗███████╗██████╗   ███████╗ █████╗ ██████╗   ██████╗ ██╗   ██╗
╚══██╔══╝ ██║  ██╗  ██║██║╚══██╔══╝╚══██╔══╝██╔════╝██╔══██╗  ██╔════╝██╔══██╗██╔══██╗  ██╔══██╗╚██╗ ██╔╝
   ██║    ╚██╗████╗██╔╝██║   ██║      ██║   █████╗  ██████╔╝  █████╗  ██║  ██║██████╔╝  ██████╔╝ ╚████╔╝ 
   ██║     ████╔═████║ ██║   ██║      ██║   ██╔══╝  ██╔══██╗  ██╔══╝  ██║  ██║██╔══██╗  ██╔═══╝   ╚██╔╝  
   ██║     ╚██╔╝ ╚██╔╝ ██║   ██║      ██║   ███████╗██║  ██║  ██║     ╚█████╔╝██║  ██║  ██║        ██║   
   ╚═╝      ╚═╝   ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚═╝  ╚═╝  ╚═╝      ╚════╝ ╚═╝  ╚═╝  ╚═╝        ╚═╝   
"""

print ("Checking config file...")
config = Path("./config.py")
if config.is_file():
    import config as cfg
    
    auth = tweepy.OAuthHandler(cfg.api_key, cfg.api_secret_key)
    auth.set_access_token(cfg.AccessToken, cfg.AccessSecretToken)

    api = tweepy.API(auth)

    print ("Found config!")
    print ("Initialising...")
    
    def mainmenu():
        time.sleep(1)
        print (logo)
        user = api.me()
        print ("Logged in as: @" + user.screen_name)
        while True:
            choose = input("\n1)Fetch your timeline\n2)Tweet\n3)Tweet with media\n4)Reply to a Tweet\n5)Retweet\n6)List DM (Not working)\n7)Send DM\n\nq)Quit\n\n[Your Choice]:")
            if choose in ['1', '2', '3', '4', '5', '6', '7', '8', 'q']:
                break
            
        if choose == '1':
            def timeline():
                tweets = api.home_timeline(count = '40', tweet_mode="extended")
                for status in reversed(tweets):
                    print ('~~~~~~~~~~~~~~~~\n@' + status.user.screen_name + ' (' + status.user.name + ')' + ' [' + status.user.id_str + ']' + "\n-----------------\n" + status.full_text, '\n\n' + str(status.created_at), '\nTweet ID(' + str(status.id) + ')\n~~~~~~~~~~~~~~~~\n')
                while True:
                    choose1 = input("\n1)Re-fetch timeline\n2)Retweet a tweet\n3)Reply to a tweet\n4)Return to main menu\n\nq)Quit\n\n[Your Choice]:")
                    if choose1 in ['1', '2', '3', '4', 'q']:
                        break
                if choose1 == '1':
                    timeline()
                elif choose1 == '2':
                    retweet()
                elif choose1 == '3':
                    reply()
                elif choose1 == '4':
                    mainmenu()
                elif choose1== 'q':
                    print ("Goodbye!")
                    
            timeline()
            
        elif choose == '2':
            def tweet():
                tweet = input("Make a tweet: ")
                api.update_status(status =(tweet))
                print ("Succesfully tweeted!")
                
                while True:
                    choose2 = input("\n1)Make another tweet\n2)Return to main menu\n\nq)Quit\n\n[Your Choice]:")
                    if choose2 in ['1', '2', 'q']:
                        break
                if choose2 == '1':
                    tweet()
                elif choose2 == '2':
                    mainmenu()
                elif choose2 == 'q':
                    print ("Goodbye!")
                    
            tweet()
            
        elif choose == '3':
            def mediupload():
                tweet = input("Your status: ")
                media = input("Your file path: ")
                mediaupload = api.media_upload(media)
                api.update_status(status =(tweet), media_ids=[mediaupload.media_id_string])
                print ("Succesfully Tweeted!")
                
                while True:
                    choose3 = input("\n1)Upload another media\n2)Return to main menu\n\nq)Quit\n\n[Your Choice]:")
                    if choose3 in ['1', '2', 'q']:
                        break
                if choose3 == '1':
                    mediupload()
                elif choose3 == '2':
                    mainmenu()
                elif choose3 == 'q':
                    print ("Goodbye!")
                    
            mediupload()

        elif choose == '4':
            def reply():
                ogauthor = input("Who are you replying to? (Use their @name): ")
                replytxt = input("Make a reply: ")
                inreplyto = input("What status is this replying to? (Use an ID of tweet): ")
                toreply = ogauthor + " " + replytxt
                api.update_status(status =(toreply), in_reply_to_status_id =(inreplyto))
                print ("Succesfully replied!")
                while True:
                    choose4 = input("\n1)Reply to another post\n2)Return to main menu\n\nq)Quit\n\n[Your Choice]:")
                    if choose4 in ['1', '2', 'q']:
                        break
                if choose4 == '1':
                    reply()
                elif choose4 == '2':
                    mainmenu()
                elif choose4 == 'q':
                    print ("Goodbye!")
                    
            reply()
            
        elif choose == '5':
            def retweet():
                retweetid = input("Provide an ID of tweet that you wish to retweet: ")
                api.retweet(id =(retweetid))
                print ("Succesfully retweeted!")
                
                while True:
                    choose5 = input("\n1)Retweet another tweet\n2)Unretweet this tweet\n3)Return to main menu\n\nq)Quit\n\n[Your Choice]:")
                    if choose5 in ['1', '2', '3', 'q']:
                        break
                if choose5 == '1':
                    retweet()
                elif choose5 == '2':
                    api.unretweet(retweetid)
                    print ("Succesfully unretweeted!")
                    mainmenu()
                elif choose5 == '3':
                    mainmenu()
                elif choose5 == 'q':
                    print ("Goodbye!")
                    
            retweet()
            
        elif choose == '6':
            def dmlist():
                dm  = api.list_direct_messages()
                print (dm.list)
                while True:
                    choose6 = input("\n1)Refresh\n2)Return to main menu\n\nq)Quit\n\n[Your Choice]:")
                    if choose6 in ['1', '2', 'q']:
                        break
                if choose6 == '1':
                    dmlist()
                elif choose6 == '2':
                    mainmenu()
                elif choose6 == 'q':
                    print ("Goodbye!")
            dmlist()
        elif choose == '7':
            def senddm():
                dmid = input("Direct ID: ")
                def send():
                    dmtext = input("Text: ")
                    api.send_direct_message(recipient_id =(dmid), text =(dmtext))
                    while True:
                        choose7 = input("\n1)Send another DM to this person\n2)Fetch this DM (not working)\n3)Return to main menu\n\nq)Quit\n\n[Your Choice]:")
                        if choose7 in ['1', '2', '3', 'q']:
                            break
                    if choose7 == '1':
                        send()
                    elif choose7 == '2':
                        def refresh():
                            refresh = api.get_direct_message(id =(dmid), full_text = true)
                            print (refresh)
                            while True:
                                choose8 = input("\n1)refresh this Dm\n\nq)Quit\n\n[Your Choice]:")
                                if choose8 in ['1', 'q']:
                                    break
                            if choose8 == '1':
                                refresh()
                            elif choose8 == 'q':
                                print ("Goodbye!")
                        refresh()
                    elif choose7 == '3':
                        senddm()
                    elif choose7 == '4':
                        mainmenu()
                    elif choose7 == 'q':
                        print ("Goodbye!")
                send()
            senddm()
        elif choose == 'q':
            print ("Goodbye!")
    mainmenu()
else:
    print ("Config not found! Creating config...")
    with open('config.py', 'a') as file:
        apikey = input("Please enter your api key: ")
        file.write("api_key: " + "'" + apikey + "'")
        apiseckey = input("Please enter your API Secret Key: ")
        file.write("\napi_secret_key: " + "'" + apiseckey + "'")
        acctok = input("Please enter your access token: ")
        file.write("\nAccessToken: " + "'" + acctok + "'")
        accsectok = input("Please enter your Access Secret Token: ")
        file.write("\nAccessSecretToken: " + "'" + accsectok + "'")
    os.execl(sys.executable, sys.executable, *sys.argv)
