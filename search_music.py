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
        return "No results found."

if __name__ == "__main__":
    # Input the song name
    song_name = input("Enter the song name: ")
    
    # Get and print the YouTube link
    youtube_link = get_youtube_link(song_name)
    print(f"YouTube link for '{song_name}': {youtube_link}")
