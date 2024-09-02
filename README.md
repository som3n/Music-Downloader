# **MUSIC DOWNLOADER**

**Description:**
This project is a Python-based YouTube MP3 Downloader that allows you to search for songs on YouTube and download their audio as MP3 files. The downloader supports downloading both single and multiple songs in one run.

**Features:**
- **Search and Download:** Search for songs on YouTube and download the audio as MP3.
- **Multiple Song Support:** Input multiple songs separated by commas and download them all in one run.
- **Automatic Conversion:** Converts downloaded audio to MP3 format and saves it to your Music folder.
- **User-Friendly:** Simple command-line interface for easy usage.

**Requirements:**
- Python 3.x
- yt-dlp (for downloading YouTube videos)
- pydub (for audio conversion)
- youtube-search-python (for searching YouTube)
- ffmpeg (required by pydub for audio processing)

**Installation:**

1. **Install the Required Python Packages:**
   ```
   pip install yt-dlp pydub youtube-search-python
   ```

2. **Install ffmpeg on Linux:**
   ```
   sudo apt-get install ffmpeg
   ```

**Usage:**

1. **Clone the Repository:**
   ```
   git clone https://github.com/som3n/Music-Downloader
   cd Music-Downloader
   ```

2. **Run the Script:**
   ```
   python download_music.py
   ```

3. **Input Song Names:**
   - For a single song: `Tum Hi Ho`
   - For multiple songs: `Tum Hi Ho, Raabta, Channa Mereya`

4. **Script Functionality:**
   - Searches YouTube for the entered song names.
   - Downloads the audio of the top search result.
   - Converts the audio to MP3 format.
   - Saves the MP3 files in your Music folder.

**Example:**
```
$ python downloader.py
Enter the song name(s) (separate multiple songs with commas): Tum Hi Ho, Raabta, Channa Mereya
Found YouTube link for 'Tum Hi Ho': <YouTube Link>
MP3 downloaded and saved to: ~/Music/Tum Hi Ho.mp3
Found YouTube link for 'Raabta': <YouTube Link>
MP3 downloaded and saved to: ~/Music/Raabta.mp3
Found YouTube link for 'Channa Mereya': <YouTube Link>
MP3 downloaded and saved to: ~/Music/Channa Mereya.mp3
```

**Troubleshooting:**
- **`get_throttling_function_name` error:** This error might occur if `pytube` is used. Switching to `yt-dlp` as the downloader resolves this issue.
- **No results found:** Ensure the song name is spelled correctly, or try a different query.

**License:**
This project is licensed under the MIT License.

**Contributing:**
Contributions are welcome! If you find any issues or want to enhance the script, feel free to open a pull request.

**Contact:**
For any questions or suggestions, please contact thesomen123@gmail.com.
