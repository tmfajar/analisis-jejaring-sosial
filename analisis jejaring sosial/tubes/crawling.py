import tweepy,sys,jsonpickle

consumer_key = 'VAWGtDPbxEcMWPMzYEpjx22VF' 
consumer_secret = 'I01IOPgqIyKlLvOPZyBQ7h0dq4fCHDytPoz9rAtdu8hlTZL1DU' 

qry='Banjir'#query yang akan di cari
maxTweets =  100# Isi sembarang nilai sesuai kebutuhan anda
tweetsPerQry = 100  # Jangan isi lebih dari 100, ndak boleh oleh Twitter
fName='Banjir.json' # Nama File hasil Crawling

auth = tweepy.AppAuthHandler(consumer_key,consumer_secret)
api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

if (not api):
    sys.exit('Autentikasi gagal, mohon cek "Consumer Key" & "Consumer Secret" Twitter anda')

sinceId, max_id, tweetCount = None, -1, 0

print("Mulai mengunduh maksimum {0} tweets".format(maxTweets))
with open(fName,'w') as f:
    while tweetCount < maxTweets:
        try:
            if (max_id <= 0):
                if (not sinceId):
                    new_tweets=api.search(q=qry,count=tweetsPerQry)
                else:
                    new_tweets=api.search(q=qry,count=tweetsPerQry,since_id=sinceId)
            else:
                if (not sinceId):
                    new_tweets=api.search(q=qry,count=tweetsPerQry,max_id=str(max_id - 1))
                else:
                    new_tweets=api.search(q=qry,count=tweetsPerQry,max_id=str(max_id - 1),since_id=sinceId)
            if not new_tweets:
                print('Tidak ada lagi Tweet ditemukan dengan Query="{0}"'.format(qry));break
            for tweet in new_tweets:
                f.write(jsonpickle.encode(tweet._json,unpicklable=False)+'\n')
            tweetCount+=len(new_tweets)
            sys.stdout.write("\r");sys.stdout.write("Jumlah Tweets telah tersimpan: %.0f" %tweetCount);sys.stdout.flush()
            max_id=new_tweets[-1].id
        except tweepy.TweepError as e:
            print("some error : " + str(e));break # Aya error, keluar
print ('\nSelesai! {0} tweets tersimpan di "{1}"'.format(tweetCount,fName))