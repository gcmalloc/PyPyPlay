import audiere
import offfm
import os

class AudioInterface:
	def __init__(self):
		self.playlist = []
		#try:
		print(audiere.get_devices())
		#self.device = audiere.open_device(audiere.device())
		#except:
		#	print("error in opening main device")
		
	def play(self): #read the stream
		self.current = self.device.open_file(self.playlist[0])
		self.current.play()
		
	def add(self,file): #add a stream to the playlist
		self.playlist.append(file)
		
	def remove(self,file): #remove a stream from the playlist
		if (len(self.playlist) == 0):
			#no next element return 0
			return 0
		if (self.playlist[0] == file):
			self.next()
			return
		playlist.remove(file)

	def print_playlist(self):
		for i in self.playlist:
			print(i)

def main():
	player = AudioReader()
	fm = offfm.OffFm("8bit")
	music_file = fm.fetch_file(0)
	player.add(music_file)

if __name__ == "__main__":
    main()	
