# Project 1 Starter Code: Analyzing Student Grades

# Import necessary libraries
import pandas as pd

# 1. Importing the Dataset
# Load the dataset into a DataFrame
# TODO: Replace 'your_file_path_here' with the path to your CSV file
# Example: df = pd.read_csv('student_grades.csv')
df = pd.read_csv("your_file_path_here")

# Display the first few rows of the dataset to inspect it
# TODO: Uncomment the line below to display the dataset
# print(df.head())


# 2. Handling Missing Values
# Check for missing values in each column
# TODO: Use df.isnull().sum() to find missing values
# print(df.isnull().sum())

# TODO: Fill missing values with the mean of each column
# Example: df['Math'].fillna(df['Math'].mean(), inplace=True)


# 3. Data Type Conversion
# TODO: Ensure all grade columns are numeric using pd.to_numeric
# Example: df['Math'] = pd.to_numeric(df['Math'], errors='coerce')


# 4. Calculating Statistics
# TODO: Calculate mean, median, and mode for each subject
# Example: mean_math = df['Math'].mean()
# median_math = df['Math'].median()
# mode_math = df['Math'].mode()[0]

# TODO: Print the calculated statistics clearly


# 5. Generating a Summary Report
# TODO: Print the number of missing values before and after cleaning
# TODO: Display the calculated statistics for each subject in a readable format

# Note: Add comments to explain each part of your code as you complete the tasks.
