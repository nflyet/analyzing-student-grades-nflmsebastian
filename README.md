[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/UAZ7c9Cm)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=18274013)
# Project 1: Analyzing Student Grades

## Overview
This project introduces you to the basics of data import, cleaning, and simple statistical analysis using Python. You will work with a CSV file containing student grades and perform essential tasks such as handling missing values, converting data types, and calculating basic statistics. By the end of this project, you will have a solid foundation in managing and exploring data using Python.

## Learning Objectives
- **Import data from flat files using Python libraries like `pandas`.**
- **Identify and handle missing values in a dataset.**
- **Convert data types to ensure consistency and accuracy.**
- **Calculate basic statistical measures such as mean, median, and mode.**
- **Summarize and report the characteristics of a dataset.**

##Dataset Description
The dataset (`student_grades.csv`) contains the following columns:
- **Student_ID:** Unique identifier for each student.
- **First Name:** Student's first name.
- **Last Name:** Student's last name.
- **Grade Level:** Student's current grade level (eg. 9, 10, 11, 12).
- **Math:** Grade in Math (may have missing values).
- **Science:** Grade in Science.
- **English:** Grade in English.
- **History:** Grade in History.
*Note: The dataset includes 100 observations with some missing values and data type inconsistencies to simulate real-world data. Your task is to clean and convert them appropriately.*

## Step-by-Step Tasks

### 1. Importing the Dataset
- Use the `pandas` library to import `student_grades.csv`.

### 2. Handling Missing Values
- Identify missing values in each column.
- Replace missing values with an appropriate measure (e.g., mean or median of the respective column).

### 3. Data Type Conversion
- Ensure all grade columns are numeric.
- Convert any non-numeric entries into appropriate numeric values.

### 4. Calculating Statistics
- Calculate the mean, median, and mode for each subject.
- Output the results in a clear and organized format.

### 5. Generating a Summary Report
- Create a Python script that prints:
  - The number of missing values per column (before and after cleaning).
  - The mean, median, and mode for each subject.
- Ensure the output is user-friendly and well-structured.

## Submission Instructions
1. **Fork this repository on GitHub Classroom.**
2. **Complete the project tasks in a Jupyter Notebook or Python script (`project1_analysis.ipynb` or `project1_analysis.py`).**
3. **Push your completed project to your forked repository.**
4. **Submit the link to your forked repository via GitHub Classroom.**
5. **Submit the link to your repository in Google Classroom as well.**

*Ensure that your code is well-commented and your output is clear. Good luck and happy coding!*
