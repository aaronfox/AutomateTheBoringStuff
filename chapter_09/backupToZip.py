#! python3
# backupToZip.py - copies an entire folder and its contents into a 
# ZIP file whose filename increments

import zipfile, os

def backupToZip(folder):
    # backup the entire content of "folder" into a ZIP file

    folder = os.path.abspath(folder) # make sure folder is absolute

    # figure out the filename this code should use based on what 
    # files already exist
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    # create the ZIP file
    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # walk the entire folder tree and compress the files in each folder
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        # Add the current folder the ZIP file
        backupZip.write(foldername)
        # add all the files in this folder to the zip file
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue # don't backup the backup Zip files
            backupZip.write(os.path.join(foldername, filename))

    backupZip.close()
        

    print('Done.')

backupToZip(r"C:\cygwin64\home\aaron\python\automateStuff\chapter_09\testFolder")

