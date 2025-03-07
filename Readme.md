# YouTube MP3 Downloader

A simple web app that lets you download YouTube videos as MP3 files.

## What I Made

1. A website where you can paste YouTube links
2. The app downloads the video and converts it to MP3
3. You get the MP3 file directly in your downloads

## How to Use

1. Open the website
2. Paste any YouTube video link
3. Click download
4. Get your MP3 file!

## How to Run

1. Install Python if you haven't already
2. Install required packages:
   ```
   pip install -r requirements.txt
   ```
3. Run the app:
   ```
   python main.py
   ```
4. Open your browser and go to: `http://localhost:5000`

## What I Used

- Flask (for the website)
- yt-dlp (for downloading YouTube videos)
- HTML/CSS (for the design)

## Features

- Simple and easy to use
- Downloads best quality audio
- Works with any YouTube video
- Clean and modern design

## How it's working 

### Step by Step Process:

1. **User Input**
   - User enters a YouTube URL in the web form
   - The URL is sent to the server using POST method

2. **Download Process**
   - Creates a temporary directory called "temp_downloads"
   - Uses yt-dlp to download the video's audio stream
   - Downloads in best available audio quality
   - Stores as webm format initially

3. **Conversion Process**
   - Uses FFmpeg to convert webm to MP3
   - Sets audio quality to 192kbps
   - Maintains original video title
   - The conversion happens automatically through yt-dlp's postprocessors:
     ```python
     'postprocessors': [{
         'key': 'FFmpegExtractAudio',
         'preferredcodec': 'mp3',
         'preferredquality': '192',
     }]
     - original webm or m4a gets delete after converting mp3 
     ```

4. **Delivery Process**
   - Sends the MP3 file to user's browser
   - Browser automatically downloads the file
   - Cleans up temporary files after download

### Technical Details:

- **Security Features:**
  - CSRF protection enabled
  - Input validation for URLs
  - Secure file handling

- **Audio Settings:**
  - Format: MP3
  - Quality: 192kbps
  - Codec: FFmpeg
  - Conversion happens automatically after download
  - No manual conversion needed

- **Error Handling:**
  - Validates empty URLs
  - Handles download failures
  - Cleans up temporary files
  - Shows user-friendly error messages

### Dependencies:
- Flask: Web framework
- yt-dlp: YouTube downloader (handles both download and conversion)
- FFmpeg: Audio conversion (used by yt-dlp)
- Flask-WTF: Form handling and CSRF protection 