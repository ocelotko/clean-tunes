import os
import acoustid
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TDRC

# Set up your Acoustid API key and music folder
ACOUSTID_API_KEY = "YOUR_ACOUSTID_API_KEY"
MUSIC_FOLDER = "path/to/your/music/folder"

def process_music_folder(api_key, folder_path):
    """
    Analyzes all MP3 files in a specified folder, fetches metadata using the Acoustid API,
    and updates the files' metadata and filenames.
    """
    if not os.path.isdir(folder_path):
        print(f"Error: Folder not found at {folder_path}")
        return

    for filename in os.listdir(folder_path):
        if filename.endswith(".mp3"):
            file_path = os.path.join(folder_path, filename)
            
            try:
                print(f"Processing file: {filename}")
                results = list(acoustid.match(api_key, file_path))
                
                if results:
                    first_result = results[0]
                    title = "Unknown_Title"
                    artist = "Unknown_Artist"
                    album = "Unknown_Album"
                    year = ""
                    
                    if isinstance(first_result, tuple):
                        try:
                            score, musicbrainz_id, title, artist = first_result
                        except ValueError:
                            pass
                    else:
                        title = first_result.get("title", "Unknown_Title")
                        artist = first_result.get("artist_name", "Unknown_Artist")
                        album = first_result.get("album_title", "Unknown_Album")
                        year = first_result.get("year", "")
                    
                    print(f"Found: {artist} - {title} ({album})")
                    
                    # Update file metadata
                    audio = ID3(file_path)
                    audio.add(TIT2(encoding=3, text=title))
                    audio.add(TPE1(encoding=3, text=artist))
                    audio.add(TALB(encoding=3, text=album))
                    if year:
                        audio.add(TDRC(encoding=3, text=str(year)))
                    audio.save()

                    # Rename the file
                    if artist != "Unknown_Artist" or title != "Unknown_Title":
                        # Create a safe filename
                        new_filename = f"{artist} - {title}.mp3".replace("/", "_").replace("\\", "_")
                        new_file_path = os.path.join(folder_path, new_filename)
                        
                        if not os.path.exists(new_file_path):
                            os.rename(file_path, new_file_path)
                            print(f"File renamed to: {new_filename}")
                        else:
                            print(f"File with the name {new_filename} already exists. Keeping original filename.")
                    
                    print("-" * 20)
                
                else:
                    print(f"No results found for file {filename}.")
                    print("-" * 20)
                
            except Exception as e:
                print(f"An error occurred while processing file {filename}: {e}")
                print("-" * 20)

if __name__ == "__main__":
    process_music_folder(ACOUSTID_API_KEY, MUSIC_FOLDER)