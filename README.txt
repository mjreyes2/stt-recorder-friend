================================================================================
        STT TRAINING RECORDER - FRIEND HELPER PACKAGE
================================================================================

Hi! You're helping record speech-to-text training data. This is simple:
You read phrases out loud and the computer records them.

================================================================================
STEP 1: INSTALL PYTHON (if you don't have it)
================================================================================

1. Go to: https://www.python.org/downloads/
2. Click the big yellow "Download Python" button
3. Run the installer
4. IMPORTANT: Check the box that says "Add Python to PATH" at the bottom!
5. Click "Install Now"
6. Wait for it to finish, then click "Close"

To verify it worked:
- Press Windows key + R
- Type: cmd
- Press Enter
- Type: python --version
- You should see something like "Python 3.12.0"

================================================================================
STEP 2: INSTALL REQUIRED PACKAGE
================================================================================

1. Press Windows key + R
2. Type: cmd
3. Press Enter
4. Type this command and press Enter:

   pip install pyaudio

If you get an error, try:

   pip install pipwin
   pipwin install pyaudio

================================================================================
STEP 3: RUN THE RECORDER
================================================================================

Option A - Easy way:
   Double-click the file: START_RECORDING.bat

Option B - Manual way:
   1. Open Command Prompt (Windows key + R, type cmd, press Enter)
   2. Navigate to this folder by typing:
      cd "PATH_TO_THIS_FOLDER"
      (replace PATH_TO_THIS_FOLDER with where you unzipped this)
   3. Type: python record_stt_training.py

================================================================================
STEP 4: RECORDING PROCESS
================================================================================

When the program starts:
1. It will ask you to select your MICROPHONE - type the number next to your mic
2. It will ask you to select your SPEAKERS - type the number (for playback)
3. Press ENTER to begin

For each phrase:
1. Press ENTER to start recording
2. READ THE PHRASE OUT LOUD clearly
3. Press ENTER to stop recording
4. You can now:
   - Press ENTER again to ACCEPT and move to next phrase
   - Press L then ENTER to LISTEN to what you recorded
   - Press R then ENTER to REDO (delete and record again)
   - Press S then ENTER to SKIP this phrase
   - Press Q then ENTER to QUIT (your progress is saved!)

TIPS:
- Speak clearly and at a normal pace
- It's okay to quit and resume later - progress is saved automatically
- Try to record in a quiet environment
- You don't have to finish all phrases in one session

================================================================================
STEP 5: SENDING RECORDINGS BACK
================================================================================

When you're done (or want to send a batch):

1. Find the folder called: stt_training_recordings
   (it's in the same folder as this README)

2. RIGHT-CLICK on the "stt_training_recordings" folder

3. Click "Compress to ZIP file" (Windows 11)
   OR
   Click "Send to" -> "Compressed (zipped) folder" (Windows 10)

4. This creates a file like: stt_training_recordings.zip

5. Send this ZIP file back via:
   - Google Drive (upload and share link)
   - Dropbox
   - WeTransfer.com (free, no account needed)
   - Discord (if small enough)
   - Email (if small enough)

================================================================================
TROUBLESHOOTING
================================================================================

"Python not found":
   - Reinstall Python and make sure to check "Add to PATH"

"No module named pyaudio":
   - Run: pip install pyaudio
   - If that fails: pip install pipwin && pipwin install pyaudio

"Can't hear playback":
   - Make sure you selected the right speaker when starting
   - Check your volume isn't muted

"Microphone not working":
   - Make sure you selected the right microphone when starting
   - Check Windows privacy settings allow microphone access

================================================================================
THANK YOU FOR HELPING!
================================================================================
