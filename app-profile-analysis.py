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
# print('Rows for Apple')
# print(explore_data(a_data, 0, 5, True))
# 
# print('Rows for Google')
# print(explore_data(g_data, 0, 5, True))

# Future Plans:

# Remove rows with errors in the description columns (as mentioned in discussion section of google data)
# Discussion mentions that row 10472
# Check the row

# print(g_header)
# print(g_data.iloc[10472])

# From the printout, we can see that the 'category' column was supposed to be empty,
# which moved all the data up and the 'Android Ver' is NaN
# We will delete this row
# del g_data.iloc[10472] # run once only


# There were no reported issues for the apple dataset

# Look for duplicates within the data

def duplicates(dataset):
    duplicate_apps = []
    unique_apps = []

    for lab, app in dataset.iterrows():
        name = app[0]
        if name in unique_apps:
            duplicate_apps.append(name)  # Add to duplicate apps
        else:
            unique_apps.append(name)  # Add to unique apps

    return [unique_apps, duplicate_apps]


g_duplicates = duplicates(g_data)
a_duplicates = duplicates(a_data)

print('No. duplicates in google data:', len(g_duplicates[1]))
print('No. duplicates in apple data:', len(a_duplicates[1]))

print('Examples of duplicates:', g_duplicates[1][0:9])

# Why is there duplicates? Print each row of the duplicates
# for lab, app in g_data.iterrows():
#     name = app[0]
#     if name == 'Google Ads':
#         print(list(app))

# The printed output columns are the same, apart from no.views
# This means the duplicate rows are data collected at different times

# Delete the old data values and keep the newest
print('Expected length after cleaning:', len(g_data)-len(g_duplicates[1]))

# Create a dictionary with the duplicate titles as keys
reviews_max = {}

for lab, app in g_data.iterrows():
    name = app[0]
    n_reviews = float(app[3])

    if name in reviews_max and reviews_max[name] < n_reviews:
        reviews_max[name] = n_reviews
    elif name not in reviews_max:
        reviews_max[name] = n_reviews

print(len(reviews_max))

# duplicate the old data and clean it
g_clean_data = g_data

for labs, app in g_clean_data:
    name = app[0]
    n_reviews = app[3]
    if name 

# We plan to only look at apps that are free within our data

# Our audience is English-speaking, so remove non-english apps
