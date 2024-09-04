import requests
import spotipy
import requests
import time
import lyricsgenius
from spotipy import SpotifyClientCredentials
from creds import SPOTIFY_CLIENT_ID,SPOTIFY_CLIENT_SECRET,GENIUS_ACCSESS_TOKEN
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
    sp=spotipy.Spotify(auth_manager=SpotifyClientCredentials(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET
    ))    
    tracks_name=list()
    for track in sp.artist_top_tracks(artist_id)['tracks'][:10]:
        tracks_name.append(track['name'])
    return tracks_name

def GetLyrics(SongName,ArtistName):    
    genius = lyricsgenius.Genius(GENIUS_ACCSESS_TOKEN)        
    genius.verbose = False
    genius.remove_section_headers = True
    song=genius.search_song(SongName, ArtistName)
    try:
        if int(song.to_json()[18:43].split(':')[-1])==0:
            return False
        else:
            return song.lyrics
    except ValueError as e:
        return False

def generate_data(artist_id):
    s=''    
    sp=spotipy.Spotify(auth_manager=SpotifyClientCredentials(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET
    ))      
    artist_name=sp.artist(artist_id=artist_id)['name'].replace(' ','-')
    songs=ArtistTop10Songs(artist_id=artist_id)

    for song in songs:
        lyrics=GetLyrics(song,artist_name)
        if lyrics==False:
            pass
        else:
            #print(GetLyrics(song,artist_name))
            s+=lyrics
            
    #print(s)    
    with open(f'{artist_name}.txt','w+',encoding='utf-8') as file:
        file.write(s)

def cloud_generator(data):
    #https://medium.com/@m3redithw/wordclouds-with-python-c287887acc8b
    pass
    
#generate_data(artist_id='1uNFoZAHBGtllmzznpCI3s')
#print('generated')

    
