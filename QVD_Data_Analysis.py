"""
Program:        QVD Data Analysis Program
Version:        1.0
Author:         Ishfaque Ahmed
Date:           17.11.2023, Friday
Description:    This Python script reads data from a QlikView QVD file using the qvd_reader module and prints the resulting DataFrame.

Use cases:      - Data Exploration and Inspection
                - Data Validation
                - Testing and Debugging

"""

# Importing the qvd_reader module from the qvd package
# qvd_reader module, which is being used to read data from a QVD file, returns the data in the form of a Pandas DataFrame therefore, pandas package needed
from qvd import qvd_reader
import pandas as pd

# Define the path and filename variables
# Note: Replace the file path and file name with the actual path to your QVD file
QVD_PATH = r'C:\Users\Documents\QVD'
QVD_FILENAME = 'Test.qvd'

# Construct the full file path
QVD_FILE_PATH = f'{QVD_PATH}\\{QVD_FILENAME}'

# Reading data from the QVD file and storing it in a DataFrame (df)
df = qvd_reader.read(QVD_FILE_PATH)

# Printing the DataFrame to inspect the loaded data
print(df)