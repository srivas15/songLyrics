import requests
import urllib2
from bs4 import BeautifulSoup

song = raw_input('Enter the song name: ')
artist = raw_input('Enter the artist: ')

artist = '\"' + artist + ' '
song = song + '\"'

lyricsWebsite = 'metrolyrics+'
url = 'http://google.com/search?sourceid=navclient&btnI=1&q=' #lyricswebsite+%s
url = url+lyricsWebsite+artist+song
print url

var = requests.get(url)
print var.url

html = urllib2.urlopen(var.url).read()
soup = BeautifulSoup(html, "html.parser")

content = soup.find("div", {"id": "lyrics-body-text"})
paras = content.find_all('p')

for para in paras:
	print '\n'
	print para.getText()

print '\n'
