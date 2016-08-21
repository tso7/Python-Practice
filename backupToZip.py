#! /usr/bin/python3
# backupToZip.py - Copies an entire folder and its contents into a ZIP file
# whose filename increments

import zipfile, os

def backupToZip(folder):
    # Backup the entire contents of "folder" into a ZIP file

    folder = os.path.abspath(folder)    # Ensure path is absolute

    # Figure out the filename this code should use based on what file exists
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number += 1

    # Create the zip file
    print ('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Walk the entire folder tree and compress the files in each folder
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        # Add the current folder to the Zip file
        backupZip.write(foldername)
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue                # Don't backup other ZIPs
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done')

# TODO: Change to use command line argument in the future
backupToZip('quiz')
