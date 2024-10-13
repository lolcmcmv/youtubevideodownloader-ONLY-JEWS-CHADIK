import os
from flask import Flask, render_template, request, redirect, url_for, flash
import yt_dlp

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Required for flashing messages


# Audio download function
def download_audio(video_url, download_path='.'):
    try:
        os.makedirs(download_path, exist_ok=True)

        ydl_opts = {
            'format': 'bestaudio/best[ext=mp3]',
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
            'noplaylist': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])

    except Exception as e:
        raise Exception(f"Audio download failed: {e}")


# Video download function
def download_video(video_url, download_path='.'):
    try:
        os.makedirs(download_path, exist_ok=True)

        ydl_opts = {
            'format': 'best[ext=mp4]',
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
            'noplaylist': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])

    except Exception as e:
        raise Exception(f"Video download failed: {e}")


# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')


# Route to handle the form submission
@app.route('/download', methods=['POST'])
def download():
    video_url = request.form['video_url'].strip()
    download_path = request.form['download_path'].strip() or '.'
    download_type = request.form['download_type']

    if not os.path.exists(download_path):
        os.makedirs(download_path)

    try:
        if download_type == 'audio':
            download_audio(video_url, download_path)
        elif download_type == 'video':
            download_video(video_url, download_path)

        flash(f"{download_type.capitalize()} download completed!")
    except Exception as e:
        flash(f"Error: {e}")

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)

