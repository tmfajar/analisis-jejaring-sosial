import sys,tweepy



 def twitter_auth():
     try:
        consumer_key = 'VAWGtDPbxEcMWPMzYEpjx22VF' 
        consumer_secret = 'I01IOPgqIyKlLvOPZyBQ7h0dq4fCHDytPoz9rAtdu8hlTZL1DU' 
        access_token = '864948672-6JbAzTt7OXyqLUcqHRWOq3yQXX6q7g7UQqcLdB8v'
        access_token_secret = 'n651dR2uGoYfDq6poeqE3xnvB68AO1THhDrCXtzAPEfTY'
    except KeyError:
        sys.stderr.write("TWITTER_* environment varaible not set\n")
        sys.exit(1)
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return auth

get_twitter_client():
    auth = twitter_auth 
    client = tweepy.API(auth.wait_on_rate_limit=True)
    return client

if __name__ == '__main__':
    user = input("Enter username: ")
    client = get_twitter_client()
    for status in tweepy.cursor(client.home_timeline, screen_name=user).items(user_timeline)   
        print(status.text)             