/**
 * Google Apps Script - STT Recording Receiver
 * 
 * SETUP INSTRUCTIONS:
 * 1. Go to https://script.google.com and create a new project
 * 2. Replace the default Code.gs content with this file
 * 3. Click Deploy > New Deployment
 * 4. Select "Web app" as the type
 * 5. Set "Execute as" = "Me"
 * 6. Set "Who has access" = "Anyone"
 * 7. Click Deploy and copy the Web App URL
 * 8. Paste that URL into the web recorder page's config
 *
 * This script receives audio recordings via POST and saves them
 * to a Google Drive folder called "STT_Training_Recordings".
 */

// Get or create the recordings folder
function getOrCreateFolder() {
  var folderName = "STT_Training_Recordings";
  var folders = DriveApp.getFoldersByName(folderName);
  if (folders.hasNext()) {
    return folders.next();
  }
  return DriveApp.createFolder(folderName);
}

// Handle POST requests (audio uploads)
function doPost(e) {
  try {
    var data = JSON.parse(e.postData.contents);
    var audioBase64 = data.audio;
    var filename = data.filename || "recording.wav";
    var phrase = data.phrase || "";
    var recorderName = data.recorderName || "anonymous";
    var phraseIndex = data.phraseIndex || 0;
    
    // Decode base64 audio
    var audioBlob = Utilities.newBlob(
      Utilities.base64Decode(audioBase64),
      "audio/wav",
      filename
    );
    
    // Get or create main folder
    var mainFolder = getOrCreateFolder();
    
    // Create subfolder for this recorder if it doesn't exist
    var subFolders = mainFolder.getFoldersByName(recorderName);
    var recorderFolder;
    if (subFolders.hasNext()) {
      recorderFolder = subFolders.next();
    } else {
      recorderFolder = mainFolder.createFolder(recorderName);
    }
    
    // Save audio file
    var file = recorderFolder.createFile(audioBlob);
    
    // Save metadata as a sidecar JSON
    var metaFilename = filename.replace(".wav", ".json");
    var metadata = {
      phrase: phrase,
      phraseIndex: phraseIndex,
      recorder: recorderName,
      timestamp: new Date().toISOString(),
      fileId: file.getId()
    };
    recorderFolder.createFile(
      metaFilename,
      JSON.stringify(metadata, null, 2),
      "application/json"
    );
    
    return ContentService
      .createTextOutput(JSON.stringify({
        success: true,
        fileId: file.getId(),
        message: "Recording saved successfully"
      }))
      .setMimeType(ContentService.MimeType.JSON);
      
  } catch (error) {
    return ContentService
      .createTextOutput(JSON.stringify({
        success: false,
        error: error.toString()
      }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

// Handle GET requests (health check)
function doGet(e) {
  return ContentService
    .createTextOutput(JSON.stringify({
      status: "ok",
      message: "STT Recording receiver is running",
      folder: getOrCreateFolder().getName()
    }))
    .setMimeType(ContentService.MimeType.JSON);
}
