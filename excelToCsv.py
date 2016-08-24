#! /usr/bin/python3
# excelToCsv.py - Converts all excel sheets in given folder to CSV files
#
# Usage: excelToCsv.py <folder>

import os, sys, openpyxl, csv

# Read command line arguments
if len(sys.argv) != 2:
    print('Invalid arguments. Usage: encryptPDF.py <folder>')
    sys.exit()

folder = sys.argv[1]

# Walk through the directory structure
for excelFile in os.listdir(folder):
    # Skip non-xlsx files, load the workbook object.
    if not (excelFile.endswith('.xlsx') or excelFile.endswith('.xls')) : # Add another condition for xls
        continue
    wb = openpyxl.load_workbook(os.path.join(folder,excelFile))
    for sheetName in wb.get_sheet_names():
        print('Currently processing: ' + excelFile)
       # Loop through every sheet in the workbook.
        sheet = wb.get_sheet_by_name(sheetName)

        # Create the CSV filename from the Excel filename and sheet title.
        excelFilename, ext = os.path.splitext(excelFile)
        csvFilename = excelFilename + '_' + sheetName + '.csv'

        # Create the csv.writer object for this CSV file.
        csvFile = open(os.path.join(folder, csvFilename), 'w', newline='')
        outputWriter = csv.writer(csvFile)

        # Loop through every row in the sheet.
        for rowNum in range(1, sheet.max_row + 1):
            rowData = []    # append each cell to this list
            # Loop through each cell in the row.
            for colNum in range(1, sheet.max_column + 1):
                # Append each cell's data to rowData.
                rowData.append(sheet.cell(row=rowNum, column=colNum).value)
            # Write the rowData list to the CSV file.
            outputWriter.writerow(rowData)

        csvFile.close()

print('Done.')
            
