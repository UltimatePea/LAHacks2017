#!/usr/bin/python
import os
import sys

#print ('Are you using Mac or Ubuntu? Enter M or U?')
systemName = raw_input('Are you using Mac or Ubuntu? Enter M or U? : ');
if systemName == "M":
	print("for Mac")
	print("installing brew")
	os.system('/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"')

	print("installing ffmpeg")
	os.system('brew install ffmpeg')

	print("installing python")
	os.system('brew install python3')

	print('installing request for python 3')
	os.system('pip install requests')

	print('installing mid')
	os.system('pip install mad')

if systemName == "U":
	print("for Ubuntu")
	print("installing ffmpeg")
	os.system('sudo add-apt-repository ppa:mc3man/trusty-media')
	os.system('sudo apt-get update')
	os.system('sudo apt-get install ffmpeg gstreamer0.10-ffmpeg')


	print("installing python")
	os.system('sudo apt-get install python3')

	print("insalling pip")
	os.system("apt-get update")
	os.system('apt-get -y install python-pip')

	print('installing request for python 3')
	os.system('sudo easy_install requests')

	print('installing mid')
	os.system('pip install mad')

else:
	print("Invalid input")