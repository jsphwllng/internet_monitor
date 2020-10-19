from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

import os
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

def upload_to_drive(file):
  # path = r".."
  print("1")
  f = drive.CreateFile({'title': file})
  print("2")
  f.Upload()
  print("3")
  f = None
