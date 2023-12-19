""""
Network Utilities. FTP Testing Section
The file is called SHA256SUMS and you should be able to find it via a web browser.
Anonymous FTP is still used to distribute open-source software, 
we refer to these locations as mirror sites. Look at ftp.heanet.ie using a web browser. 

This is the simplest possible usable and useful script! 

By: MF
    v0.1    13DEC23  
"""

import ftplib

FTP = {
    "PATH": '/mirrors/ubuntu-cdimage/releases/22.04/release',
    "FILENAME": 'SHA256SUMS',
    "URL": 'ftp.heanet.ie'
}

# Make the connection
ftp = ftplib.FTP(FTP['URL'])
# Anonymous login
ftp.login() 
# Change to the correct directory
ftp.cwd(FTP["PATH"])
# Retrieve the file
ftp.retrbinary("RETR " + FTP["FILENAME"], open(FTP["FILENAME"], 'wb').write)
ftp.quit()