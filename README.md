# Twitter for ...  
This simple program lets you tweet via a custom "Twitter for" field  
This script uses tweepy module  

## Instructions:
First you need to create [Developer Account](https://developer.twitter.com) on Twitter  
After sign up, create the new Application
##### Note: Your application name will be important, as it will be replacing "Twitter for (Android/iPhone/Web Client)" fields. If you want a custom "Twitter For" field, name it "Twitter for <your choice>". If you change name later, this field will still use old name. Be careful when choosing a name  
After creating an application, go to Tokens tab and copy every token from there, now clone this repo and follow next steps:  

open terminal and install tweepy module: `pip install tweepy`  
Run the program via `twitterfor.py`  
Program will ask you to provide tokens, do what it says  
After you provided tokens, it will self restart  

![Screenshot](https://github.com/X1nto/twitter-for-x/blob/master/Screenshot.png)  
Now you'll see this menu, choose any option you want and fill out everything  
After you fill out everything there, congrats, you have succesfully tweeted via Gucci Smart Toilet.  

## Notes:
Second option isn't working as of now but it will be fixed soon  
Listing and sending DMs require special permissions. On app console, go to permissions tab, click edit and select 3rd option and click save. for this change to take effect you need to regenerate all tokens. If you're already logged in to this app, you need to edit config.py and overwrite tokes there.  
Listing DMs will output raw JSON strings and I have no idea how to fix it, if you know anything Pull Request would be highly appreciated.
