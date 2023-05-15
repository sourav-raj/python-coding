# -*- coding: utf-8 -*-
# Indentation: Visual Studio

'''
To access ftp server.

'''

__version__ = '0.0.1'
__author__ = "Sourav Raj"
__author_email__ = "souravraj.iitbbs@gmail.com"

from ftplib import FTP_TLS, FTP
import os
from config import HOST, PORT,USER,PASSWORD, CLIENTHOMEDIR

ftp_server = FTP()
ftp_server.connect(HOST, PORT)
# Output: '220 Server ready for new user.'
ftp_server.login(USER, PASSWORD)
# Output: '200 PROT command successful.'
print(ftp_server.nlst())
filenames=ftp_server.nlst()
# Output: ['mysubdirectory', 'mydoc']
ftp_server.dir()
if not os.path.exists(CLIENTHOMEDIR): os.makedirs(CLIENTHOMEDIR)
for file in filenames:
    with open(os.path.join(CLIENTHOMEDIR, f'download_{file}'), "wb") as f:
        # Command for Downloading the file "RETR filename"
        ftp_server.retrbinary(f"RETR {file}", f.write)


filename = os.path.join(CLIENTHOMEDIR, f'download_{file}')
 
# # Read file in binary mode
# with open(filename, "rb") as f:
#     # Command for Uploading the file "STOR filename"
#     filename = os.path.join(CLIENTHOMEDIR, f'upload_{file}')
#     ftp_server.storbinary(f"STOR {filename}", f)

ftp_server.quit()