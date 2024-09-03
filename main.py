import requests
import spotipy
import requests
from spotipy import SpotifyClientCredentials
from creds import SPOTIFY_CLIENT_ID,SPOTIFY_CLIENT_SECRET,GENIUS_CLIENT_SECRET,GENIUS_CLEINT_ID
from bs4 import BeautifulSoup

def Top100():
    data=list()
    response=requests.get('https://kworb.net/spotify/listeners.html').content
    soup=BeautifulSoup(response,'html.parser')
    artists=soup.find_all('tr')
    for artist in artists[1:101]:
        artist_id=artist.find('a')['href'][7:29]
        artist_name=artist.find('a').text
        data.append([artist_name,artist_id])
    return data

def ArtistTop10Songs(artist_id):
    #under progress
    sp=spotipy.Spotify(auth_manager=SpotifyClientCredentials(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET
    ))
    for track in  sp.artist_top_tracks(artist_id)['tracks'][:10]:
        print()
print(Top100())


