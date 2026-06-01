# US Bikeshare Data Explorer

An interactive Python script to explore US bikeshare data for Chicago, New York City, and Washington.

## Project Description
This project was developed as part of the Udacity Data Analyst Nanodegree. It provides an interactive command-line experience where users can filter and analyze bikeshare data to uncover trends such as:
- Popular travel times (Month, Day, Hour)
- Station usage (Start, End, and most frequent trips)
- Trip duration metrics (Total and Average)
- User demographics (Type, Gender, and Birth Year)

## Prerequisites
To run this project, you will need to have Python installed on your system along with the following libraries:
- [Python 3.x](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)
- [NumPy](https://numpy.org/)

## Installation & Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
   cd YOUR_REPOSITORY_NAME
   ```

2. **Install dependencies:**
   ```bash
   pip install pandas numpy
   ```

3. **Data Files:**
   Ensure the following CSV files are present in the project directory:
   - `chicago.csv`
   - `new_york_city.csv`
   - `washington.csv`

## Usage
Run the script using the following command:
```bash
python bikeshare.py
```

### Interactive Prompts
Upon running the script, you will be prompted to:
1. **Select a City:** Chicago, New York City, or Washington.
2. **Select a Month:** All, January, February, March, April, May, or June.
3. **Select a Day:** All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday.

The script will then calculate and display the statistics for your chosen filters. You will also have the option to view 5 rows of raw data at a time.

## Dataset Details
The data is provided by [Motivate](https://www.motivateco.com/), a bikeshare system provider for many major cities in the United States. The datasets contain information for the first six months of 2017.

> **Note:** The Washington dataset does not contain 'Gender' or 'Birth Year' information. The script is designed to handle this gracefully.

## Author
- [Your Name] - Udacity Data Analyst Nanodegree

## Credits & Resources
- [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)
- [Stack Overflow](https://stackoverflow.com/)
- Udacity Data Analyst Nanodegree Program
