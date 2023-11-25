"""
Program:        QVD Data Analyzer
Version:        1.2
Author:         Ishfaque Ahmed
Date:           25.11.2023, Saturday
Description:    This Python script reads data from a Qlik Data File (.qvd) using the qvd_reader module and prints the resulting DataFrame using pandas package

Use cases:      - Data Exploration and Inspection
                - Data Validation
                - Testing and Debugging

"""

# Importing the 'os' module, which provides a way to interact with the operating system
# This module allows tasks such as file and directory manipulation, working with environment variables, and more
import os

# Importing the qvd_reader module from the qvd package
# qvd_reader module is used to read data from a QVD file, and it returns the data in the form of a DataFrame therefore, pandas package required
from qvd import qvd_reader

# Importing the 'pandas' library with the alias 'pd'
# Pandas is a powerful data manipulation library and is used here for further analysis and manipulation of the data
import pandas as pd

# Define the relative or absolute path to the QVD file
# Example of relative path: 'Data Sources\QVDs'
# Example of absolute path: r'C:\Users\Documents\QVDs'
# Example of server share folder path: r'\\Server1\DataSource'
QVD_PATH = r'Data Sources\QVDs'
QVD_FILENAME = 'F_Products.qvd'

# Check if the path is absolute
if os.path.isabs(QVD_PATH):
    # If absolute, use it directly
    QVD_FILE_PATH = os.path.join(QVD_PATH, QVD_FILENAME)
else:
    # If relative, construct the absolute path
    CURRENT_DIRECTORY = os.getcwd()
    QVD_FILE_PATH = os.path.join(CURRENT_DIRECTORY, QVD_PATH, QVD_FILENAME)

try:
    # Reading data from the QVD file and storing it in a DataFrame (df)
    df = qvd_reader.read(QVD_FILE_PATH)

    # Data Analysis
    # Displaying the entire DataFrame
    print("\n Display DataFrame:")
    print(df)

    # Displaying the first 5 rows of the DataFrame
    print("\n First 5 rows of the DataFrame:")
    print(df.head())

    # Displaying the last 5 rows of the DataFrame
    print("\n Last 5 rows of the DataFrame:")
    print(df.tail())

    # Printing a concise summary of the DataFrame, including data types and missing values
    print("\n DataFrame Information:")
    print(df.info())

    # Generating descriptive statistics of the DataFrame
    print("\n Descriptive Statistics:")
    print(df.describe())
    
except FileNotFoundError as e:
    # Handling the case when the QVD file is not found
    print(f"Error: QVD file not found - {e}")
except Exception as e:
    # Handling other exceptions that may occur while reading the QVD file
    print(f"Error reading the QVD file: {e}")