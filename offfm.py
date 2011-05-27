import urllib, json
from random import randint
from os import remove, path
from math import floor
from urlparse import urlparse

#this will still disapear
MIN_SEARCH_SIZE = 3
BASE_URL = http://api.official.fm
key=lBZLgyJlImbRf529dTVS


"this class keep the data needed to access the api"
class OffFm():
		__init__(self, key):
			dev_key = key
			
		def fetch_json(self, url):
			connection = connect(url)
			answer = connection.read()
		
		def connect(self, url):
			urllib.openurl(url)
"this class is just a way to handle the url we use in all the instance"	
class OffApi(OffFm):
	"this class gives all the way to access official fm"
	"the default key is the devlopper key"
	"the default user is set to null for no binded user"
	def __init__(self, key=lBZLgyJlImbRf529dTVS, option=null,user=null):
		key = key
		self.user = user
		return
	
	def search(self, search_param, max_reponse):
		url = urllib.parse(urlbase + search param + track + options)
		answer = fetch_json(url)
		for json in answer:
			yield json 
	"this method does the following request"	
	"http://api.official.fm/search/tracks/{searchparam}?api_max_responses=20"
	"return a list of 20 Track"
	def search_track(self, search_param, max_response=20):
			search(search_param, max_response)
			map(Track(i), json) 
	
	"this method does the following request"	
	"http://api.official.fm/search/user/{searchparam}?api_max_responses=20"
	"return a list of 20 users"
	def search_user(self, search_param, max_response=20):
			search(search_param, max_response)
			map(Track(i), json) 
			
	"this method does the following request"	
	"http://api.official.fm/search/user/{searchparam}?api_max_responses=20"
	"return a list of 20 playlist"
	def search_playlist(self, search_param, max_response=20):
			search(search_param, max_response)
			map(Track(i), json) 
	
	"http://api.official.fm/tracks/latest"
	def latest_track(self):
		url 
		answer = fetch_json(url)
		return Track(answer)
		
	"http://api.official.fm/tracks/charts?charting=today"
	def charting_track(self, time):
		fetch_json(url)
		
"instanciate a simple object from a parsed json object"
class JsonObject:
	def __init__(self, json_descriptor):
		for k, v in json_descriptor.items():
			settart(self, k, v)
			
class Track(JsonObject, OffFm):
	"define a song with the field given by official.fm"
	"return a stream on the audio file"
	"initialise a track object"
	def __init__(self, json):
		super(JsonObject, self).__init__(json)
	
	"define a song given its id"
	"implents the showTrack request"
	"http://api.official.fm/track/{tracknumber}"
	def __init__(self, track_number):
		
		
	"return a stream on the track"
	def return_stream(self):
		#url handling
		url = self.gen_mp3_url(id)
		
		try:
			conn = urllib.urlopen(url)
		except:
			print("connexion issue")
		return conn
		
		def get_value(self, key):
			ret = []
			for i in self.data:
				ret.append(i[key])
			return ret
		
	
	def gen_mp3_url(self, id):
		direct = floor(id/1000)
		print(direct)
		return self.url_mp3[0] + direct + self.url_mp3[1] + str(id) + self.url_mp3[2] + self.gen_l()
		
	def end(self, file_path):
		remove(file_path)	
	
	"generate the magic key for the track"
	def gen_magic_key():
		ret = ""
		for i in range(7):
			ret += str(randint(0,9))
		return ret	
	
class User(JsonObject, OffFm):
	def __init__(self, json):
			
		
	def __init__(user_id):
			
	"http://api.official.fm/user/{userid}/playlists"
	def get_playlists(self):
		url = playlist_url
		
	"http://api.official.fm/user/{userid}/contacts"
	def get_contacts(self):
	
	"http://api.official.fm/user/{userid}/subscribers"
	def get_subscribers(self):
	
	"http://api.official.fm/user/{userid}/subscriptions"
	def get_subscribtions(self):
	
	"http://api.official.fm/user/{userid}/voted_tracks"
	def get_voted_tracks(self):
	
	"http://api.official.fm/user/{userid}/voted_playlists"
	def get_voted_Playlists(self):
	
	"this method "
	"http://api.official.fm/user/{userid}/tracks"
	def get_track(self):
		
class Playlist(JsonObject, OffFm):
	def __init(self):
		
	def show_playlist(self):
		
	def votes_playlist:
	
