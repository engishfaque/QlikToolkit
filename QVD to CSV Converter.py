"""
Program:        QVD to CSV Converter
Version:        1.0
Author:         Ishfaque Ahmed
Date:           25.11.2023, Saturday
Description:    This Python script reads data from a Qlik Data File (.qvd) using the qvd_reader module and saves it as a CSV file using the pandas package

Use cases:      - Data Conversion
"""

# Importing the 'os' module for file and directory manipulation
import os

# Importing the qvd_reader module from the qvd package
from qvd import qvd_reader

# Importing the 'pandas' library with the alias 'pd' for data manipulation
import pandas as pd

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

# Define the path to save the CSV file
CSV_PATH = r'Data Sources\CSVs'
CSV_FILENAME = 'F_Products.csv'

# Check if the path is absolute
if os.path.isabs(CSV_PATH):
    CSV_FILE_PATH = os.path.join(CSV_PATH, CSV_FILENAME)
else:
    CURRENT_DIRECTORY = os.getcwd()
    CSV_FILE_PATH = os.path.join(CURRENT_DIRECTORY, CSV_PATH, CSV_FILENAME)

try:
    # Reading data from the QVD file and storing it in a DataFrame (df)
    df = qvd_reader.read(QVD_FILE_PATH)

    # Saving the DataFrame as a CSV file
    df.to_csv(CSV_FILE_PATH, index=False)

    print(f"Conversion successful! CSV file saved at: {CSV_FILE_PATH}")

except FileNotFoundError as e:
    # Handling the case when the QVD file is not found
    print(f"Error: QVD file not found - {e}")
except Exception as e:
    # Handling other exceptions that may occur while reading the QVD file or saving as CSV
    print(f"Error during conversion: {e}")
