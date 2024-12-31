import streamlit as st
from pytube import YouTube
import yt_dlp

def download_with_pytube(url):
    try:
        yt = YouTube(url)
        st.write(f"Title: {yt.title}")
        streams = yt.streams.filter(progressive=True)
        for stream in streams:
            st.write(f"{stream.itag}: {stream.resolution} ({stream.mime_type})")
        
        itag = st.text_input("Enter the itag of the desired stream:")
        if itag:
            stream = yt.streams.get_by_itag(itag)
            stream.download()
            st.success("Download complete with pytube!")
        return True
    except Exception as e:
        st.error(f"Pytube failed: {e}")
        return False

def download_with_ytdlp(url):
    try:
        ydl_opts = {
            'format': 'best',
            'outtmpl': '%(title)s.%(ext)s',
        }
        st.write("Downloading with yt-dlp...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        st.success("Download complete with yt-dlp!")
    except Exception as e:
        st.error(f"yt-dlp also failed: {e}")

def main():
    st.title("YouTube Video Downloader")
    url = st.text_input("Enter the YouTube video URL:")
    if url:
        if not download_with_pytube(url):
            download_with_ytdlp(url)

if __name__ == "__main__":
    main()