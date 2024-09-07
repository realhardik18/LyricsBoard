import spotipy
import lyricsgenius
from spotipy import SpotifyClientCredentials
from creds import SPOTIFY_CLIENT_ID,SPOTIFY_CLIENT_SECRET,GENIUS_ACCSESS_TOKEN

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
            s+=lyrics            
    with open(f'{artist_name}.txt','w+',encoding='utf-8') as file:
        file.write(s)

generate_data(artist_id='5K4W6rqBFWDnAN6FQUkS6x')
#print('generated')

    
