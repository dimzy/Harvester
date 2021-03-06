##twiAuth.py
##Harvester Twitter Authentication module
import glob
from twython import Twython
import twython
from termcolor import colored
import twitter
import tweetpony

class twiAuth:
	def loadCredentialfile(self):
		credFile = glob.glob("AuthFile")
		if len(credFile) > 1:
			print colored("ERROR: Why are there more than Auth file in your inventory? Sell that to a merchant.", "yellow")
			return False
		if len(credFile) < 1:
			print colored("ERROR: There are no Auth files detected", "yellow")
			return False
		self.mycredFile = open(credFile[0])
			
	def parseCredFile(self):
		for line in self.mycredFile:
			myline = line.split('\t')
			myType = myline[0]
			cred = myline[-1]
			myType = myType.rstrip()
			cred = cred.rstrip()
			if myType == "Consumer_key":
				self.ck = cred
			elif myType == "Consumer_secret":
				self.cks = cred
			elif myType == "Access_token":
				self.at = cred
			elif myType == "Access_token_secret":
				self.ats = cred
				
	def authCredsPythonTwitter(self):
		try:
			testApi = twitter.Api(consumer_key=self.ck, consumer_secret=self.cks, access_token_key=self.at, access_token_secret=self.ats)
			myCreds = testApi.VerifyCredentials()
			screen_name = myCreds.screen_name
			msg = "Twitter Authentication seems to be successful with screen_name: " + str(screen_name)
			print colored(msg, "green")
			return testApi
		except twitter.TwitterError:
			print "Twitter authentication failed with the given authenticators. "		
		
	def authCredsTwython(self):
		testApi = Twython(self.ck, self.cks, self.at, self.ats) 
		#Test if the API keys are the developers:
		if self.ck in 'UmTtg8DMpMXcgzkbIErSQ':
			print colored("WARNING: You're using the developer's Twitter API keys. Did you forget to change the keys in the AuthFile?" , 'yellow') 
		try: 
			testApi.verify_credentials()
		except twython.exceptions.TwythonAuthError:
			print "Twitter authentication failed with the given authenticators. "
		else:
			print colored("Twitter Authentication seems to be successful", "green")
			return testApi
	
	def authCredsTweetPony(self):
		try:
			api = tweetpony.API(self.ck, self.cks, self.at, self.ats) 
			user = api.user
			msg = "Twitter Authentication seems to be successful with screen_name: " + str(user.screen_name)
			print colored(msg,"green")
			return api
		except (ValueError, tweetpony.APIError) as e:
			if ValueError in e:
				print "Value error in Twitter Authentication"
			elif tweetpony.APIError in e:
				msg = "Twitter is rejecting your credentials: " + str(e)
				print colored(msg, "red")
			else:
				print colored(str(e), "red")
	
	def __init__(self, Type="Twython"):
		self.ck = ""
		self.cks = ""
		self.at = ""
		self.ats = ""
		self.mycredFile = file
		if self.loadCredentialfile() == False:
			return
		self.parseCredFile()
		if Type in "Twython":
			self.Api = self.authCredsTwython()
		elif Type in "Python-Twitter":
			self.Api = self.authCredsPythonTwitter()
		elif Type in "TweetPony":
			self.Api = self.authCredsTweetPony() 
		
		

		
