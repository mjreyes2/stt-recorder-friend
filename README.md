# STT Voice Training Recorder

Help train Monica AI's speech recognition by reading phrases aloud. Two options available:

---

## Option 1: Web Recorder (Easiest — No Install Needed)

### For your friend:
Just send them this link:

**🔗 [https://mjreyes2.github.io/stt-recorder-friend/](https://mjreyes2.github.io/stt-recorder-friend/)**

They open it in Chrome/Edge, enter their name, and start reading phrases. That's it!

### Setting up Google Drive auto-save (optional):

Without this, recordings are saved in the browser and your friend downloads them manually.
With this, recordings go straight to your Google Drive.

1. Go to [script.google.com](https://script.google.com) and create a **New Project**
2. Delete the default code and paste the contents of [`docs/google-apps-script/Code.gs`](docs/google-apps-script/Code.gs)
3. Click **Deploy → New Deployment**
4. Type = **Web app**, Execute as = **Me**, Access = **Anyone**
5. Click **Deploy**, authorize when prompted, and copy the **Web App URL**
6. Edit `docs/index.html` → find the line `const APPS_SCRIPT_URL = "";` → paste your URL between the quotes
7. Commit & push — the page auto-updates

Recordings will appear in a **STT_Training_Recordings** folder in your Google Drive.

---

## Option 2: Desktop Recorder (Better Audio Quality)

Download the zip from [Releases](https://github.com/mjreyes2/stt-recorder-friend/releases) and follow the README inside.
Requires Python installed.

---

## Getting Recordings Back

- **Web recorder + Google Drive**: Recordings auto-save to your Drive
- **Web recorder (no Drive)**: Friend clicks "Download All" and sends the files
- **Desktop recorder**: Friend zips the `stt_training_recordings` folder and sends it via Google Drive, Dropbox, or WeTransfer
