import streamlit as st
import yt_dlp
import os

def download_with_ytdlp(url):
    try:
        ydl_opts = {
            'format': 'best',
            'outtmpl': 'downloads/%(title)s.%(ext)s',  # Save in a "downloads" folder
        }
        st.write("Downloading with yt-dlp...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            st.success("Download complete with yt-dlp!")
            return filename
    except Exception as e:
        st.error(f"yt-dlp failed: {e}")
        return None

def main():
    st.title("YT Video Downloader")
    url = st.text_input("Enter the YouTube video URL:")
    if st.button("Download"):
        if url:
            filename = download_with_ytdlp(url)
            if filename:
                with open(filename, "rb") as file:
                    st.download_button(
                        label="Click here to download the video",
                        data=file,
                        file_name=os.path.basename(filename),
                        mime="video/mp4"
                    )

if __name__ == "__main__":
    main()