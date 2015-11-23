# twitter_spider
A twitter spider

# Require
<strong>tweepy</strong> : pip install tweepy<br>
<strong>request security</strong> : pip install 'requests[security]'

You need to create a config.ini file in your root folder. It must be like this.
````
[Twitter]
consumer_key = your_key
consumer_secret = your_key
access_token = your_key
access_token_secret = your_key
```

#Usage:
python app.py screen_name
<br>
Example:
```
python app.py google
```
#Return result

````
User: google 
User ID : 20536157
Follower count : 13124207
Friend count : 439
```
