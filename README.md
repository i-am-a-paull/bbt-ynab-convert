Convert transactions exported from BB&T as a CSV to YNAB 4-formatted CSV

Useful for Windows, Mac, linux (running YNAB under WINE).

# Installation: 
- Install the python 2 version [for your operating system](https://www.python.org/downloads/).
- Copy ynabConvert.py & convert.bat to the same folder you save bank transactions to. 

# Command Line Usage: 
```shell
./ynabConvert.py [inputFile] [[outputFile]]
```
- This will generate an output you can import into YNAB successfully (Filename 'ynabImport.csv' if outputFile is not specified)
- First argument is always import file (default is 'EXPORT.CSV' if inputFile is not given)

# GUI Usage:
**Linux/Mac:**
- Drag and drop the CSV from BB&T on the convert.bat file. 
- Import the ynabImport.csv file into YNAB

**Windows:**
- Drag and drop the CSV from BB&T on the convert.bat file. 
- Import the ynabImport.csv file into YNAB
