from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

import os

try:
  gauth = GoogleAuth()
  gauth.LocalWebserverAuth()
  drive = GoogleDrive(gauth)
except:
  pass

def upload_to_drive(file):
  f = drive.CreateFile()
  f.SetContentFile(file)
  f.Upload()
  f = None
