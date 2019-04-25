import tweepy
import re
class fileProcess:
 	def __init__(self):
 		self.consumer_key = ''
 		self.consumer_secret = ''
 		self.access_key = ''
 		self.access_secret = ''
 		## selected account for testing
 		self.user = ["katyperry", "ConanOBrien", "Oprah", "jimmyfallon", "EmmaWatson", "LeoDiCaprio", "BillGates", "taylorswift13", "rihanna"]
 		self.comm = ["Padilla_Comm", "MayoClinic", "TheEconomist", "Google", "nytimes"]
 	def getAPI(self):
 		try: 
 			auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
 			auth.set_access_token(self.access_key, self.access_secret)
 			api = tweepy.API(auth)
 		except:
 			print("Error: authentication failed")
 		return api
 	def getUserTweet(self, api):
 		emoji_pattern = re.compile(
    u"(\ud83d[\ude00-\ude4f])|"  # emoticons
    u"(\ud83c[\udf00-\uffff])|"  # symbols & pictographs (1 of 2)
    u"(\ud83d[\u0000-\uddff])|"  # symbols & pictographs (2 of 2)
    u"(\ud83d[\ude80-\udeff])|"  # transport & map symbols
    u"(\ud83c[\udde0-\uddff])"  # flags (iOS)
    "+", flags=re.UNICODE)
 		## user account
 		for each in self.user:
 			total = []
 			temp = api.user_timeline(each, count = 200)
 			total.extend(temp)
 			last = total[-1].id - 1
 			while len(temp) > 0:
 				temp = api.user_timeline(each, count = 200, max_id = last)
 				total.extend(temp)
 				last = total[-1].id - 1
 			result = [emoji_pattern.sub(r'', tweet.text).encode('utf-8') for tweet in total]
 			## write tweets to file
 			s = "tweet_" + each + ".txt"
 			with open(s, "w") as f:
 				for item in result:
 					f.write(item + "\n")
 			print("finish " + each + "'s tweet scraping.")
 		## corporate account
 		for each in self.comm:
 			total = []
 			temp = api.user_timeline(each, count = 200)
 			total.extend(temp)
 			last = total[-1].id - 1
 			while len(temp) > 0:
 				temp = api.user_timeline(each, count = 200, max_id = last)
 				total.extend(temp)
 				last = total[-1].id - 1
 			result = [emoji_pattern.sub(r'', tweet.text).encode('utf-8') for tweet in total]
 			## write tweets to file
 			s = "/home/j/NLP traitsPredictor/data/" + "tweet_" + each + ".txt"
 			with open(s, "w") as f:
 				for item in result:
 					f.write(item + "\n")
 			print("finish " + each + "'s tweet scraping.")
## main function
x = fileProcess()
api = x.getAPI()
x.getUserTweet(api)
