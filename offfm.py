import urllib, json
from random import randint
from os import remove, path
from math import floor

class OffFm:
	"this class gives all the way to access official fm"
	url_search = ["http://api.official.fm/search/tracks/","?api_max_responses=20&format=json&key=lBZLgyJlImbRf529dTVS"]
	url_mp3 = ["http://cdn.official.fm/mp3s/","/",".mp3?l="]
	def __init__(self, search):
		if (len(search) < 3):
			return 
		req_url = str(self.url_search[0] + str(search) + self.url_search[1])
		#try to make the connexion 
		try:
			con = urllib.urlopen(req_url)
		except:
			print("Connexion Issue")
			return
		#try to read the url to retriveve the answer
		try:
			answ = con.read() 
		except:
			print("read error")
			return 
		finally:
			con.close
			
		self.data = json.loads(answ)
		return
		
	def get_number_result(self):
		return len(self.data)
		
	def get_value(self, key):
		ret = []
		for i in self.data:
			 ret.append(i[key])
		return ret
	
	def get_title(self):
		return get_value('title')
	
	def get_artist(self):
		return get_value('artist_string')
	
	def get_descriptor():
		return zip(get_title(),get_artist())
	
	def get_ids(self):
		return self.get_value('id')	
	
	def get_picture_url(self):
		return self.get_value('picture_absolute_url')
			
	def get_keys(self):
		keys = self.data[0].keys()
		return keys
		
	def get_length(self):
		return self.get_value('length')
		
	def gen_magic_key(self):
		ret = ""
		for i in range(7):
			ret += str(randint(0,9))
		return ret
	
	def gen_mp3_url(self, id):
		direct = floor(id/1000)
		print(direct)
		return self.url_mp3[0] + direct + self.url_mp3[1] + str(id) + self.url_mp3[2] + self.gen_l()
	
	def fetch_file(self, selection):
		print(self.data[1])
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
			f = open(file_path, 'wb')
		except:
			print("connexion issue")
			return 
			
		try:
			f.write(conn.read())
		except:
			print("read issue")
			return 
		finally:
			f.close()
			conn.close()
		
		return file_path
		
	def file_exist(self, path):
		if os.exists(path):
			#test if the length is correct 
			supposed_len = get_length()
			real_len = os.path.getsize(path)
			return supposed_len == real_len
		else: 
			return False
		
	def end(self, file_path):
		remove(file_path)
