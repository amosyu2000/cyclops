import urllib.request
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def wifi_connected():
    try:
        urllib.request.urlopen('http://google.com')
        return True
    except:
        return False

class Upload_Videos:

    def __init__(self, credential_directory:str, video_storage_directory:str):
        self.credential_directory = credential_directory
        self.video_storage_directory = video_storage_directory
        self.gauth = GoogleAuth()
        self.drive = None
        self.folder_id:str = None
    
    def authenticate_user(self):
        # the end product would ship without a 'user_drive_credentials.txt' file
        # this results in the user being propted to log into their google account once.
        # These log in credentials will then be stored in 'user_drive_credentials.txt' 
        # preventing the need for subsequent log ins.

        # Currently, only authorised test users can use this service.
        # such users must be registered here: https://console.cloud.google.com/apis/credentials/consent?project=cyclops-file-upload
        # using the CyclopsRideAssist@gmail.com account
        self.gauth.LoadCredentialsFile(self.credential_directory + 'user_drive_credentials.txt')
        if self.gauth.credentials is None:
            # Authenticate if they're not there
            self.gauth.LocalWebserverAuth()
        elif self.gauth.access_token_expired:
            # Refresh them if expired
            self.gauth.Refresh()
        else:
            # Initialize the saved credentials
            self.gauth.Authorize()
        # Save the current credentials to a file
        self.gauth.SaveCredentialsFile(self.credential_directory + 'user_drive_credentials.txt')
        self.drive = GoogleDrive(self.gauth)

    def validate_folder(self):
        # iterate through all files 
        # attempt to locate 'Cyclops Video Files' folder (look in all directories in case the user has moved it)
        entity_list = self.drive.ListFile({'q': "trashed=false"}).GetList()
        for entity in entity_list:
            if entity['mimeType'] == "application/vnd.google-apps.folder" and entity['title'] == 'Cyclops Video Files':
                self.folder_id = entity['id']
                break
        if self.folder_id == None: # 'Cyclops Video Files' folder not located, create it at the root
            file_metadata = {
                'title': 'Cyclops Video Files',
                'parents': [{'id': 'root'}], #parent folder
                'mimeType': 'application/vnd.google-apps.folder'
            }
            new_folder = self.drive.CreateFile(file_metadata)
            new_folder.Upload()
            self.folder_id = new_folder['id']

    def transfer_files(self):
        # determine what files currently exist in 'Cyclops Video Files'
        temp_list = self.drive.ListFile({'q':"'%s' in parents and trashed=false" % self.folder_id}).GetList()
        drive_list =[]
        for temp in temp_list:
            drive_list.append(temp['title'])
        for local_file in os.listdir(self.video_storage_directory):
            if '.mp4' in local_file: # only want to upload.mp4 videos
                if local_file not in drive_list: # upload files not in the drive
                    new_file = self.drive.CreateFile({'parents': [{'id': self.folder_id}], 'title': local_file})
                    new_file.SetContentFile(self.video_storage_directory + local_file)
                    new_file.Upload()
                # delete the local file to free space
                os.remove(self.video_storage_directory + local_file)
        
def attempt_upload(credential_directory:str, video_storage_directory:str):
    """
    1. ensure a functional network connection exists
    2. Connect to a user's google drive account using user_drive_credentials.txt located at credential_directory.
    3. Verify that a folder 'Cyclops Video Files' exists in the users google drive. If it does not create it at the root.
    4. Iterate through files located at video_storage_directory. Upload (overwrite) the file to the 'Cyclops Video Files' google drive folder and delete the file from video_storage_directory.
    
    @credential_directory: The complete path which contains the user_drive_credentials.txt file.
    @video_storage_directory: The complete path which to which video recordings are uploaded by video_buffer
    """
    if wifi_connected():
        app = Upload_Videos(credential_directory, video_storage_directory)
        app.authenticate_user()
        app.validate_folder()
        app.transfer_files()
    else:
        print('UPLOAD FAILED \nNo internet connection detected. Please try again when a functional network is connected.')

