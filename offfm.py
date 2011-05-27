import urllib, json
from random import randint
from os import remove, path
from math import floor

http://api.official.fm/search/tracks/{searchparam}?api_max_responses=20
"this class is just a way to handle the url we use in all the instance"
class OffFm:
	url_base="https://api.official.fm"
	url_format="&format=json"
	search_url=""
	
	
class OffApi(OffFm):
	url_maxresponse="api_max_responses="
	url_search_playlist="search/playlists/"
	"this class gives all the way to access official fm"
	"the default key is the devlopper key"
	"the default user is set to null for no binded user"
	def __init__(self, key=lBZLgyJlImbRf529dTVS, user=null):
		self.key = key
		self.user = user
		return
	
	def search_track(self, search_param, max_response=20):
		
	def search_user(self, search_param, max_response=20):
	def latest_track(self):
	def charting_track(self):
	

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

"instanciate a simple object from a parsed json object"
class JsonObject:
	def __init__(self, json_descriptor):
		for k, v in json_descriptor.items():
			settart(self, k, v)
		
class Track(JsonObject, OffFm):
	"define a song with the field given by official.fm"
	"return a stream on the audio file"
	"initialise a track object"
	def __init__(self):
		
	
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

"return a json object ready to be parse from the url given"
def return_json(url):
	
