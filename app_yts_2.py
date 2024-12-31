import streamlit as st
import yt_dlp
import os

def download_with_ytdlp(url):
    try:
        ydl_opts = {
            'format': 'best',
            'outtmpl': 'downloads/%(title)s.%(ext)s',  # Save in a "downloads" folder
        }
        st.write("Downloading...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            st.success("Download complete!")
            return filename
    except Exception as e:
        st.error(f"yt-dlp failed: {e}")
        return None

def main():
    st.title("Youtube Video Downloader")
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
# Disclaimer content
def display_disclaimer():
    st.markdown("---")  # Horizontal line
    st.markdown(
        """
        **Disclaimer**  
        This application is provided as is for educational and informational purposes only.  
        The author, Risz-Sgr, is not responsible for any misuse of this tool.  
        Please ensure compliance with YouTube's terms of service and copyright laws when using this application.  
        """
    )


if __name__ == "__main__":
    main()
    # Call this function at the end of the app
display_disclaimer()
