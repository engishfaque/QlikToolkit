"""
Program:        QVD Data Analysis Program
Version:        1.1
Author:         Ishfaque Ahmed
Date:           19.11.2023, Sunday
Description:    This Python script reads data from a QlikView QVD file using the qvd_reader module and prints the resulting DataFrame using pandas package

Use cases:      - Data Exploration and Inspection
                - Data Validation
                - Testing and Debugging

"""

# Importing the 'os' module, which provides a way to interact with the operating system.
# This module allows tasks such as file and directory manipulation, working with environment variables, and more.
import os

# Importing the qvd_reader module from the qvd package.
# qvd_reader module is used to read data from a QVD file, and it returns the data in the form of a DataFrame therefore, pandas package required.
from qvd import qvd_reader

# Importing the 'pandas' library with the alias 'pd'.
# Pandas is a powerful data manipulation library and is used here for further analysis and manipulation of the data.
import pandas as pd

# Define the relative or absolute path to the QVD file
# Example of relative path: 'Data Sources\QVDs'
# Example of absolute path: r'C:\Users\Documents\QVDs'
# Example of server share folder path: r'\\Server1\DataSource'
QVD_PATH = r'C:\Users\Documents\QVDs'
QVD_FILENAME = 'F_Products.qvd'

# Check if the path is absolute
if os.path.isabs(QVD_PATH):
    # If absolute, use it directly
    QVD_FILE_PATH = os.path.join(QVD_PATH, QVD_FILENAME)
else:
    # If relative, construct the absolute path
    CURRENT_DIRECTORY = os.getcwd()
    QVD_FILE_PATH = os.path.join(CURRENT_DIRECTORY, QVD_PATH, QVD_FILENAME)

# Reading data from the QVD file and storing it in a DataFrame (df)
try:
    df = qvd_reader.read(QVD_FILE_PATH)
    # Printing the DataFrame to inspect the loaded data
    print(df)
except Exception as e:
    print(f"Error reading QVD file: {e}")