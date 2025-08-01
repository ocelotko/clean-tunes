# Clean Tunes

This Python script helps you clean up your music library by automatically identifying **MP3** and **WAV** files, fetching their metadata, and renaming them. It uses the **Acoustid API** and audio fingerprinting to ensure accurate song identification, even on files with missing or incorrect tags.

---

## Features

- **Automatic Tagging**: Uses audio fingerprints to accurately identify your songs.
- **Metadata Updates**: Writes artist, title, album, and year directly to your music file's ID3 tags.
- **File Renaming**: Renames files to a consistent format (`Artist - Title.mp3` or `Artist - Title.wav`).
- **Cross-Platform**: Works on Windows and Linux.
- **Multi-Format Support**: Processes both **MP3** and **WAV** files.

---

## Prerequisites

Before you can run the script, you'll need the following:

- **Python 3** installed on your system.
- **An Acoustid API Key**.
- The **`fpcalc`** executable, which is used by the Acoustid library to generate audio fingerprints. **For Windows users, `fpcalc.exe` is already included in this repository.**

---

## Step 1: Get Your Acoustid API Key

1.  Go to the [Acoustid website](https://acoustid.org/).
2.  Create a free account or log in.
3.  Navigate to the **"API Keys"** section.
4.  Generate a new API key and copy it.

---

## Step 2: Install Dependencies

You'll need to install the required Python libraries and, for Linux users, the `fpcalc` tool.

### On Windows

1.  **Install Python Libraries**: Open a command prompt and run the following command:
    ```bash
    pip install acoustid mutagen
    ```
2.  No further steps are needed, as `fpcalc.exe` is already in the project folder.

### On Linux (Debian/Ubuntu)

1.  **Install `fpcalc`**: `fpcalc` is usually available in the official repositories.
    ```bash
    sudo apt update
    sudo apt install fpcalc
    ```
2.  **Install Python Libraries**:
    ```bash
    pip install acoustid mutagen
    ```

### On Fedora Linux

1.  **Install `fpcalc`**:
    ```bash
    sudo dnf install chromaprint-tools
    ```
    This package includes the `fpcalc` command-line tool.
2.  **Install Python Libraries**:
    ```bash
    pip install acoustid mutagen
    ```

---

## Step 3: Configure and Run the Script

1.  **Open `main.py`** in a text editor.
2.  **Replace the placeholder values** for `ACOUSTID_API_KEY` and `MUSIC_FOLDER` with your own information:

    ```python
    ACOUSTID_API_KEY = "YOUR_ACOUSTID_API_KEY"
    MUSIC_FOLDER = "path/to/your/music/folder"
    ```

    - Paste the API key you obtained in Step 1.
    - Specify the path to the folder containing the MP3/WAV files you want to organize.

3.  **Save the file**.
4.  **Run the script** from your terminal:
    ```bash
    python main.py
    ```

The script will now go through each music file in your specified folder, identify it, and update its metadata and filename.
