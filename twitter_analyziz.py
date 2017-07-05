import tweepy
from textblob import TextBlob 

consumer_key ='Cz0UBMmdJlZS2pZzaJq5k0miu'
consumer_secret ='2j8ahyW0xgxDvt1YxOkcMH08rw2t9wswwFNXFrFPOruGE8DilI' 

access_token ='142230875-F4zSV9kUDv76igmbnMHvDRrj0q7CHCzoZrM3B8oC'
access_token_secret ='Brp0t0g24u3uVZxM2gkn6jEtJUU14g6SD2Mvzu3ZGMm94'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
positive = 0.0
negative = 0.0
neutral = 0.0
total = 0.0

public_tweets = api.search(str(raw_input("Enter the search vector==>")),count=1000)

for tweet in public_tweets:
	analysis = TextBlob(tweet.text)
	if(analysis.sentiment.polarity>0):
		positive = positive + 1
	elif(analysis.sentiment.polarity<0):
		negative = negative + 1
	else:
		neutral = neutral + 1
	total = total + 1

print(positive)
percentage_positive = (positive/total)*float(100)
percentage_negative = (negative/total)*100
percentage_neutral = (neutral/total)*100
print("Tweet taken ==> %d" %total)
print("positive tweet percent ==> %0.3d %%" %percentage_positive)
print("negative tweet percent ==> %0.3d %%" %percentage_negative)
print("neutral tweet percent ==> %0.3d %%" %percentage_neutral)
if(percentage_positive>percentage_negative):
	print("positive")
else:
	print("negative")
