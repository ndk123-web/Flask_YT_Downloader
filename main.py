# Import necessary modules for Flask and file handling
from flask import Flask, request, render_template, url_for, send_file, make_response, redirect, flash
import yt_dlp  # For downloading YouTube videos
from flask_wtf import CSRFProtect  # For CSRF protection in forms
import os  # For creating directories and file handling
from dotenv import load_dotenv  # For loading environment variables

# Load environment variables from .env file
load_dotenv()

# Initialize Flask application
app = Flask(__name__)

# Enable CSRF protection for security
csrf = CSRFProtect(app)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')  # Get secret key from environment variable

# Function to render home page
def home_Page_For_User():
    return make_response(render_template('index.html'))

# Function to handle YouTube audio download
def download_Video_On_User_Browser():
    if request.method == 'POST':  
        url = request.form.get('url', '').strip()  # Get YouTube URL from user input
        
        if not url:  
            flash("URL is Empty", 'danger')  # Show error if URL is empty
            return redirect(url_for('Home'))
        
        try:
            temp_dir = "temp_downloads"  # Temporary directory for downloaded files
            os.makedirs(temp_dir, exist_ok=True)  # Create directory if not exists

            # yt-dlp options for downloading best quality audio
            ydl_opts = {
                'format': 'bestaudio/best',  # gives best audio quality
                'quiet': True,               # don't show download progress
                'no_warnings': True,          # don't show warnings
                'noplaylist': True,          # don't download playlists, only single videos
                'outtmpl': f'{temp_dir}/%(title)s.%(ext)s',  # output where mp3 file will be stored
                'cookiesfrombrowser': ('chrome',),  # Use Chrome cookies
                'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'extract_flat': True,
                'no_check_certificate': True,
                'ignoreerrors': True,
                'no_warnings': True,
                'quiet': True,
                'extract_audio': True,
                'audio_format': 'mp3',
                'audio_quality': 0,  # Best quality
            }
            
            # Download audio using yt-dlp
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)  # Extract video info & download
                downloaded_file = f"{temp_dir}/{info['title']}.{info['ext']}"  # get the mp3 file path
            
            # Send file to user browser for download
            return send_file(
                downloaded_file, # sending mp3 file to user browser
                as_attachment=True, # force browser to download it
                download_name=f"{info['title']}.mp3",  # name shown in browser
                mimetype='audio/mp3' # mime type for the file
            )
            
        except Exception as e:
            flash(f"Error: {str(e)}", 'danger')  # Handle download errors
            return redirect(url_for('Home'))

    return redirect(url_for('Home'))  # Redirect to home if method is not POST

# URL routing
app.add_url_rule('/', endpoint='Home', view_func=home_Page_For_User, methods=['GET'])  # Home page
app.add_url_rule('/downloads', endpoint='downloads', view_func=download_Video_On_User_Browser, methods=['POST', 'GET'])  # Download page


# Run Flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # Start server with debug mode
