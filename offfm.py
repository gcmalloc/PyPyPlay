import urllib, json
from random import randint
from os import remove, path
from math import floor
from urlparse import urlparse

MIN_SEARCH_SIZE = 3
BASE_URL = http://api.official.fm
"this class is just a way to handle the url we use in all the instance"
class OffFm ():	
class OffApi():
	"this class gives all the way to access official fm"
	"the default key is the devlopper key"
	"the default user is set to null for no binded user"
	def __init__(self, key=lBZLgyJlImbRf529dTVS, option=null,user=null):
		self.key = key
		self.user = user
		return
		
	"this method does the following request"	
	"http://api.official.fm/search/tracks/{searchparam}?api_max_responses=20"
	"return a list of 20 Track"
	def search_track(self, search_param, max_response=20):
		url = urllib.parse(urlbase + search param + track + options)
		answer = get_json(url)
		for json in answer:
			yield Track(json) 
	
	"this method does the following request"	
	"http://api.official.fm/search/user/{searchparam}?api_max_responses=20"
	"return a list of 20 users"
	def search_user(self, search_param, max_response=20):
		url = urllib.parse(urlbase + search param + track + options)
		answer = get_json(url)
		for json in answer:
			yield User(json) 
	
	"this method does the following request"	
	"http://api.official.fm/search/user/{searchparam}?api_max_responses=20"
	"return a list of 20 playlist"
	def search_playlist(self, search_param, max_response=20):
		url = urllib.parse(urlbase + search param + track + options)
		answer = get_json(url)
		for json in answer:
			yield Playlist(json) 
	
	"http://api.official.fm/tracks/latest"
	def latest_track(self):
		url 
		answer = get_json(url)
		return Track(answer)
		
	"http://api.official.fm/tracks/charts?charting=today"
	def charting_track(self, time):
		


"instanciate a simple object from a parsed json object"
class JsonObject:
	def __init__(self, json_descriptor):
		for k, v in json_descriptor.items():
			settart(self, k, v)
	
	def get_json(self, url):
		
class Track(JsonObject, OffFm):
	"define a song with the field given by official.fm"
	"return a stream on the audio file"
	"initialise a track object"
	def __init__(self):
		
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
	
	"return a stream on the track"
	def return_stream(self):
		assert selection < len(self.data)
		ids = self.get_ids()
		id = ids[selection]
		#file handling
		file_path = str(id) + ".mp3"
		if self.file_exist:
			return file_path
		#url handling
		url = self.gen_mp3_url(id)
		
		print(url)
		#test if file already exist in tmp file 
		try:
			conn = urllib.urlopen(url)
		except:
			print("connexion issue")
		
		return conn
	
class User(JsonObject, OffFm):
	def __init__(self)
		tracks, voted_tracks, playlists, voted_playlists, contacts
		subscribers	
		subscriptions
	
	def show_user(self):
	def get_playlist(self):
	def get_contact(self):
	def get_subscriber(self):
	def get_subscribtion(self):
	def get_voted_track(self):
	def get_voted_Playlist(self):
	def track_user(self):
		
class Playlist(JsonObject, OffFm):
	def __init(self):
		
	def show_playlist(self):
		
	def votes_playlist:
	
