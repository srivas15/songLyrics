#works using metrolyrics with google search's first result

import requests
import urllib2
from bs4 import BeautifulSoup

song = raw_input('Enter the song name: ')
artist = raw_input('Enter the artist: ')

song = song.lower()
artist = artist.lower()

#artist = '\"' + artist + ' '
#song = song + '\"'

lyricsWebsite = 'metrolyrics+'
url = 'http://google.com/search?sourceid=navclient&btnI=1&q=' #lyricswebsite+%s
url = url+lyricsWebsite+'\"'+artist+' '+song+'\"'
print url

var = requests.get(url)
print var.url

if 'www.metrolyrics.com' in var.url:
	html = urllib2.urlopen(var.url).read()
	soup = BeautifulSoup(html, "html.parser")

	content = soup.find("div", {"id": "lyrics-body-text"})
	paras = content.find_all('p')

	for para in paras:
		print '\n'
		print para.getText()

	print '\n'

else:
	url = 'http://www.azlyrics.com/lyrics/'
	song = song.replace(" ","")
	artist = artist.replace(" ","")
	url = url+artist+'/'+song+'.html'
	print url

	html = urllib2.urlopen(url).read()
        soup = BeautifulSoup(html, "html.parser")
	
	content = soup.find("div", {"class": None, "id": None})
	print content.getText()
