#! /usr/bin/python3
# encryptPDF.py - Encrypts all files within a folder (recursively) using
# password provided
#
# Usage: encryptPDF.py <folder> <password>

import os, sys, PyPDF2

# Read command line arguments
if len(sys.argv) != 3:
    print('Invalid arguments. Usage: encryptPDF.py <folder> <password>')
    sys.exit()

folder = sys.argv[1]
password = sys.argv[2]

# Walk through the directory structure
for folderName, subfolders, filenames in os.walk(folder):
    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        print('This folder has a subfolder: ' + subfolder)
    for filename in filenames: 

    # Look for a pdf file
        if filename.endswith('pdf'):

            absPath = os.path.join(folderName, filename)

            pdfReader = PyPDF2.PdfFileReader(open(absPath, 'rb'))
            # Ignore if already encrypted
            if pdfReader.isEncrypted:
                print(filename + ' already encrypted. Skipping file...')
                continue
            
            # Encrypt the file using the password
            pdfWriter = PyPDF2.PdfFileWriter()
            for pageNum in range(pdfReader.numPages):
                pdfWriter.addPage(pdfReader.getPage(pageNum))
            pdfWriter.encrypt(password)

            # Write to encrypted file
            encryptName, ext = os.path.splitext(absPath)
            encryptName += '_encrypted.pdf'
            resultPdf = open(encryptName, 'wb')
            pdfWriter.write(resultPdf)
            resultPdf.close()
            
            # Verify encryption
            encryptedReader = PyPDF2.PdfFileReader(open(encryptName, 'rb'))
            if not(encryptedReader.isEncrypted and encryptedReader.decrypt(password)):
                print('Encryption failed for : ' + encryptName)
                continue
            
            # Delete old file
            os.remove(absPath)

print('Done.')
            
