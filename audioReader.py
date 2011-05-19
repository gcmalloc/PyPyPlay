import audiere
import offfm
import os
class AudioReader:
	def __init__(self):
		print("INIT")
		self.playlist = []
		
		self.device = audiere.open_device()
		print()
		
	def play(self): #read the stream
		self.actual = self.device.open_file(self.playlist[0])
		print("play")
		self.actual.play()
	
	def pause(self): #pause/play the stream
		print("pause")
		self.actual.pause()
		
	def next(self): #get the next element in the playlist
		if (len(self.playlist) == 0):
			#no next element return 0
			return 0
		remove(self.playlist)#remove the first element
	
	def repeat(self, value):
		self.actual.repeat(1)
		
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
	player = AudioReader();
	fm = offfm.OffFm("8bit");
	music_file = fm.fetch_file(0)
	player.add(music_file)
	player.print_playlist()
	player.play()

if __name__ == "__main__":
    main()	
