#! /usr/bin/python3
# decryptPDF.py - Decrypts all files within a folder (recursively) using
# password provided
#
# Usage: decryptPDF.py <folder> <password>

import os, sys, PyPDF2

# Read command line arguments
if len(sys.argv) != 3:
    print('Invalid arguments. Usage: decryptPDF.py <folder> <password>')
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
            # Ignore if already decrypted
            if not pdfReader.isEncrypted:
                print(filename + ' already decrypted. Skipping file...')
                continue

            # Decrypt and verify
            if not pdfReader.decrypt(password):
                print('Decryption failed for: ' + absPath)
                continue
            
            # Retrieve content of the file
            pdfWriter = PyPDF2.PdfFileWriter()
            for pageNum in range(pdfReader.numPages):
                pdfWriter.addPage(pdfReader.getPage(pageNum))

            # Write to decrypted file
            decryptName, ext = os.path.splitext(absPath)
            decryptName += '_decrypted.pdf'
            resultPdf = open(decryptName, 'wb')
            pdfWriter.write(resultPdf)
            resultPdf.close()            

print('Done.')
            
