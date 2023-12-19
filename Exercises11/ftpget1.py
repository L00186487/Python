""""
Network Utilities. Testing Section
The file is called SHA256SUMS and you should be able to find it via a web browser.
Anonymous FTP is still used to distribute open-source software, 
we refer to these locations as mirror sites. Look at ftp.heanet.ie using a web browser. 
By: MF
    v0.1    13DEC23  
"""

import ftplib

# Set the path
path = '/mirrors/ubuntu-cdimage/releases/22.04/release'
# What file to download
filename = 'SHA256SUMS'
# Make the connection
ftp = ftplib.FTP("ftp.heanet.ie")
# Anonymous login
ftp.login() 
# Change to the correct directory
ftp.cwd(path)
# Retrieve the file
ftp.retrbinary("RETR " + filename, open(filename, 'wb').write)
# Cleanly exit
ftp.quit()