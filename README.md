# Udacity - Explore US Bikeshare Data
**My First Data Analysis Project**

## Description
In this project, I used Python to explore data related to bike share systems for three major cities in the United States: Chicago, New York City, and Washington. I wrote a script that imports data, calculates descriptive statistics, and provides an interactive experience in the terminal.

## What's Inside this Project
This repository contains my implementation of the bikeshare analysis tool. Here are the key features:

*   **Interactive User Interface:** The script asks for your input to choose a city and filter the data by month or day.
*   **Time Statistics:** It calculates the most frequent travel times (most common month, day of the week, and start hour).
*   **Station Statistics:** It identifies the most popular start and end stations, as well as the most common trip path.
*   **Trip Duration Statistics:** It calculates the total and average travel time, formatted into hours, minutes, and seconds.
*   **User Information:** It provides a breakdown of user types, and (where available) gender and birth year statistics.
*   **Data Safety:** Specifically handles the Washington dataset which is missing gender and birth year columns.
*   **Raw Data Viewer:** Allows you to see the actual data 5 rows at a time if you're curious about the details!

## Project Files
- `bikeshare.py`: The main Python script containing all the analytical logic.
- `.gitignore`: Ensures large data files are kept out of the repository.
- `README.md`: This file, explaining the project.
- `readme.txt`: A text-version of the documentation.

## Rubric Highlights
This project was built to meet the following standards:
- **Functionality:** All code runs without errors.
- **Data Handling:** Uses Pandas and NumPy for efficient data processing.
- **Input Validation:** Gracefully handles user typos and invalid inputs.
- **Clean Code:** Uses functions, clear variable names, and comments for readability.

---
*Developed as part of Udacity's Data Analyst Nanodegree Program.*
