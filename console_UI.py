#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#       untitled.py
#       
#       Copyright 2011 Malik Bougacha <malik@Think-center>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

menu_option = {1:search,
			   2:audio,
			   3:playlist
			   4:exit
			   }

audio_option = {1:play_pause
				2:next
				}

search_option = {1:official
				 }
#audio interface to have 
def main_menu():
	print("Make your selection :")
	print("")
	print("1) Make a search")
	print("2) Audio control")
	print("3) Display playlist")
	print("4) exit")
	while ! isdigit(in):
		in = raw_input("Enter the choice and press enter:")
	menu_option[in]()
	
def search():
def audio():
def playlist():
	
def exit():
	print("exiting")
	exit(0)

def main():
	
	return 0

if __name__ == '__main__':
	main()

