# Purpose: Analyse apps in the app market for google and ios
# Author: Hanifa Huq
# Start Date: 11/10/2022
# End Date:
# Notes:

# Import relevant packages
import pandas as pd
import numpy as np

# Open and read data files
apple_csv = pd.read_csv('AppleStore.csv', header=None)
a_header = list(apple_csv.iloc[0])  # Extract the header
a_data = apple_csv.iloc[1:]  # Extract data without header

google_csv = pd.read_csv('googleplaystore.csv', header=None)
g_header = list(google_csv.iloc[0])
g_data = google_csv.iloc[1:]


# Create function to explore rows in a more readable way
def explore_data(dataset, start, end, rows_and_columns=False):
    data_slice = dataset.iloc[start:end]  # Where dataset does NOT have a header row

    # Print each row on a single line listed out
    for lab, row in data_slice.iterrows():
        print(list(row), '\n')

    # Print number of Rows and columns if condition is True
    if rows_and_columns:
        print('Number of rows:', dataset.shape[0])
        print('Number of columns:', dataset.shape[1])


# Print the first few rows out for each dataset
print('Rows for Apple')
print(explore_data(a_data, 0, 5, True))

print('Rows for Google')
print(explore_data(g_data, 0, 5, True))

# Future Plans:

# Remove rows with errors in the description columns (as mentioned in discussion section of google data)

# We plan to only look at apps that are free within our data

# Our audience is English-speaking, so remove non-english apps