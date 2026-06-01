# US Bikeshare Data Explorer

## Project Overview
This project is an interactive command-line application that allows users to explore bikeshare data from three major US cities: Chicago, New York City, and Washington. The script provides detailed statistical analysis on trip times, popular stations, trip durations, and user demographics.

## System Requirements
To run this application, you will need:
- **Python 3.6 or higher**
- **Pandas** library
- **NumPy** library

## Installation & Setup
1. Ensure you have Python installed. You can check this by running `python --version` in your terminal.
2. Install the necessary dependencies using pip:
   ```bash
   pip install pandas numpy
   ```
3. Place the following files in the same directory:
   - `bikeshare.py`
   - `chicago.csv`
   - `new_york_city.csv`
   - `washington.csv`

## How to Use
Run the script from your terminal:
```bash
python bikeshare.py
```
Follow the interactive prompts to:
1. Select a city (Chicago, New York City, or Washington).
2. Filter by a specific month (January to June) or select 'all'.
3. Filter by a specific day of the week or select 'all'.

The script will then display:
- **Time Statistics:** Most frequent month, day, and hour of travel.
- **Station Statistics:** Most popular start station, end station, and trip path.
- **Trip Duration Statistics:** Total and average travel time formatted for readability.
- **User Statistics:** Counts of user types, gender, and birth year information (where available).
- **Raw Data:** Option to view 5 rows of raw data at a time.

## Dataset Description
The data provided by Udacity includes randomly selected data for the first six months of 2017. All three city data files contain the same core six columns:
- Start Time
- End Time
- Trip Duration (in seconds)
- Start Station
- End Station
- User Type

The Chicago and New York City files also include:
- Gender
- Birth Year

## References & Credits
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [NumPy Documentation](https://numpy.org/doc/)
- [Python Datetime Module](https://docs.python.org/3/library/datetime.html)
- Udacity Data Analyst Nanodegree Program materials.
