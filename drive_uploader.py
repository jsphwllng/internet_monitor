from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

import os
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

def upload_to_drive(file):
  # path = r".."
  f = drive.CreateFile()

  f.SetContentFile(file)
  f.Upload()
  print("file uploaded!")
  f = None
