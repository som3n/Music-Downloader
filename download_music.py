import os
import yt_dlp
from pydub import AudioSegment
from youtubesearchpython import VideosSearch

def get_youtube_link(song_name):
    # Search for the song on YouTube
    video_search = VideosSearch(song_name, limit=1)
    results = video_search.result()

    # Extract the video link from the search results
    if results['result']:
        video_url = results['result'][0]['link']
        return video_url
    else:
        return None

def download_mp3(youtube_url, song_name):
    # Define the path to the Music folder
    music_folder = os.path.join(os.path.expanduser('~'), 'Music')
    
    # Download the audio from YouTube using yt-dlp
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(music_folder, f'{song_name}.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
        
        print(f"MP3 downloaded and saved to: {music_folder}/{song_name}.mp3")
    
    except Exception as e:
        print(f"An error occurred while downloading {song_name}: {e}")

if __name__ == "__main__":
    # Input the song names (can be one or multiple, separated by commas)
    songs_input = input("Enter the song name(s) (separate multiple songs with commas): ")
    
    # Split the input into a list of songs
    songs = [song.strip() for song in songs_input.split(',')]
    
    # Process each song
    for song_name in songs:
        # Get the YouTube link for the song
        youtube_link = get_youtube_link(song_name)
        
        if youtube_link:
            print(f"Found YouTube link for '{song_name}': {youtube_link}")
            
            # Download and convert the audio to MP3
            download_mp3(youtube_link, song_name)
        else:
            print(f"No results found for the song: {song_name}")
