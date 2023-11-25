"""
Program:        QVD to Excel Converter
Version:        1.0
Author:         Ishfaque Ahmed
Date:           25.11.2023, Saturday
Description:    This Python script reads data from a Qlik Data File (.qvd) using the qvd_reader module and saves it as an Excel file (.xlsx) using the pandas package

Use cases:      - Data Conversion
"""

# Importing the 'os' module for file and directory manipulation
import os

# Importing the qvd_reader module from the qvd package
from qvd import qvd_reader

# Importing the 'pandas' library with the alias 'pd' for data manipulation
import pandas as pd

# Importing the 'openpyxl' library for Excel file handling
import openpyxl

# Define the relative or absolute path to the QVD file
# Example of relative path: 'Data Sources\QVDs'
# Example of absolute path: r'C:\Users\Documents\QVDs'
# Example of server share folder path: r'\\Server1\DataSource'
QVD_PATH = r'Data Sources\QVDs'
QVD_FILENAME = 'F_Products.qvd'

# Check if the path is absolute
if os.path.isabs(QVD_PATH):
    QVD_FILE_PATH = os.path.join(QVD_PATH, QVD_FILENAME)
else:
    CURRENT_DIRECTORY = os.getcwd()
    QVD_FILE_PATH = os.path.join(CURRENT_DIRECTORY, QVD_PATH, QVD_FILENAME)

# Define the path to save the Excel file
EXCEL_PATH = r'Data Sources\XLSX'
EXCEL_FILENAME = 'F_Products.xlsx'

# Check if the path is absolute
if os.path.isabs(EXCEL_PATH):
    EXCEL_FILE_PATH = os.path.join(EXCEL_PATH, EXCEL_FILENAME)
else:
    CURRENT_DIRECTORY = os.getcwd()
    EXCEL_FILE_PATH = os.path.join(CURRENT_DIRECTORY, EXCEL_PATH, EXCEL_FILENAME)

try:
    # Reading data from the QVD file and storing it in a DataFrame (df)
    df = qvd_reader.read(QVD_FILE_PATH)

    # Saving the DataFrame as an Excel file
    df.to_excel(EXCEL_FILE_PATH, index=False, engine='openpyxl')

    print(f"Conversion successful! Excel file saved at: {EXCEL_FILE_PATH}")

except FileNotFoundError as e:
    # Handling the case when the QVD file is not found
    print(f"Error: QVD file not found - {e}")
except Exception as e:
    # Handling other exceptions that may occur while reading the QVD file or saving as Excel
    print(f"Error during conversion: {e}")