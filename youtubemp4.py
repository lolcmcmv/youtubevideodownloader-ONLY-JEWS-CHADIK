import os
import yt_dlp

def download_video(video_url, download_path='.'):
    """Download the highest quality video from YouTube using yt-dlp."""
    try:
        # Create download path if it does not exist
        os.makedirs(download_path, exist_ok=True)

        # Define download options
        ydl_opts = {
            'format': 'best[ext=mp4]',  # Download the best available format that is mp4 (which combines audio and video)
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),  # Output template
            'noplaylist': True,  # Ensure only one video is downloaded
        }

        # Download video using yt-dlp
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading: {video_url}")
            ydl.download([video_url])
            print("Download completed!")

    except Exception as e:
        print(f"An error occurred: {e}")

def progress_hook(d):
    """Display download progress."""
    if d['status'] == 'downloading':
        print(f"Downloading: {d['filename']} | {d['_percent_str']} | {d['_eta_str']} remaining")

# Main function
if __name__ == '__main__':
    video_url = input("Enter the YouTube video URL: ").strip()
    
    # Get the download path and ensure it is valid
    download_path = input("Enter the download path (default is current directory): ").strip() or '.'
    
    # Remove any leading/trailing quotes
    download_path = download_path.strip('"').strip("'")

    # Validate the path (optional but good practice)
    if not os.path.exists(download_path):
        print(f"Path does not exist. Creating directory: {download_path}")
        os.makedirs(download_path, exist_ok=True)

    # Download the video
    download_video(video_url, download_path)
