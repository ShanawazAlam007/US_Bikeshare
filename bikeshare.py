import time
import pandas as pd
import numpy as np

# Mapping of cities to their corresponding CSV data files
CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def validate_input(prompt, valid_options):
    """
    Reusable input validator that cleans input and handles retries.
    
    Args:
        prompt (str): The message to display to the user.
        valid_options (list): A list of valid lowercase strings.
    Returns:
        str: The validated user input.
    """
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_options:
            return user_input
        print(f"Invalid entry. Please choose from: {', '.join(valid_options)}")

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\n' + '='*40)
    print('US BIKESHARE DATA EXPLORATION')
    print('='*40)
    
    # Get user input for city
    cities = list(CITY_DATA.keys())
    city = validate_input(f"Enter city ({', '.join(cities)}): ", cities)

    # Get user input for month
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    month = validate_input(f"Enter month ({', '.join(months)}): ", months)

    # Get user input for day of week
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = validate_input(f"Enter day ({', '.join(days)}): ", days)

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month, day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # Filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month_idx = months.index(month) + 1
        df = df[df['month'] == month_idx]

    # Filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\n[SECTION: TIME STATISTICS]')
    start_time = time.time()

    # Display the most common month
    if not df['month'].empty:
        popular_month_idx = df['month'].mode()[0]
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        print(f"Most Common Month: {months[popular_month_idx - 1]}")

    # Display the most common day of week
    if not df['day_of_week'].empty:
        popular_day = df['day_of_week'].mode()[0]
        print(f"Most Common Day of Week: {popular_day}")

    # Display the most common start hour
    if not df['hour'].empty:
        popular_hour = df['hour'].mode()[0]
        print(f"Most Common Start Hour: {popular_hour}:00")

    print(f"\nExecution time: {(time.time() - start_time):.4f} seconds.")
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\n[SECTION: STATION STATISTICS]')
    start_time = time.time()

    # Display most commonly used start station
    if not df['Start Station'].empty:
        popular_start = df['Start Station'].mode()[0]
        print(f"Most Common Start Station: {popular_start}")

    # Display most commonly used end station
    if not df['End Station'].empty:
        popular_end = df['End Station'].mode()[0]
        print(f"Most Common End Station: {popular_end}")

    # Display most frequent combination of start station and end station trip
    if not (df['Start Station'].empty or df['End Station'].empty):
        # Concatenate columns for a clean combination check
        df['Trip Path'] = df['Start Station'] + " -> " + df['End Station']
        popular_path = df['Trip Path'].mode()[0]
        print(f"Most Common Trip: {popular_path}")

    print(f"\nExecution time: {(time.time() - start_time):.4f} seconds.")
    print('-'*40)

def format_duration(seconds):
    """Helper to format seconds into a readable string."""
    days = int(seconds // (24 * 3600))
    seconds %= (24 * 3600)
    hours = int(seconds // 3600)
    seconds %= 3600
    minutes = int(seconds // 60)
    seconds %= 60
    
    parts = []
    if days > 0: parts.append(f"{days}d")
    if hours > 0: parts.append(f"{hours}h")
    if minutes > 0: parts.append(f"{minutes}m")
    parts.append(f"{int(seconds)}s")
    return ", ".join(parts)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\n[SECTION: TRIP DURATION STATISTICS]')
    start_time = time.time()

    # Display total travel time
    total_duration = df['Trip Duration'].sum()
    print(f"Total Travel Time: {format_duration(total_duration)}")

    # Display mean travel time
    avg_duration = df['Trip Duration'].mean()
    print(f"Average Travel Time: {format_duration(avg_duration)}")

    print(f"\nExecution time: {(time.time() - start_time):.4f} seconds.")
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\n[SECTION: USER STATISTICS]')
    start_time = time.time()

    # Display counts of user types
    print("User Type Breakdown:")
    print(df['User Type'].value_counts().to_string())

    # Display counts of gender (if available)
    if 'Gender' in df.columns:
        print("\nGender Breakdown:")
        print(df['Gender'].value_counts().to_string())
    else:
        print("\nGender data is not available for this city.")

    # Display birth year stats (if available)
    if 'Birth Year' in df.columns:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common = int(df['Birth Year'].mode()[0])
        print(f"\nBirth Year Stats:")
        print(f"  Earliest: {earliest}")
        print(f"  Most Recent: {recent}")
        print(f"  Most Common: {common}")
    else:
        print("Birth year data is not available for this city.")

    print(f"\nExecution time: {(time.time() - start_time):.4f} seconds.")
    print('-'*40)

def display_raw_data(df):
    """
    Iteratively displays 5 rows of raw data upon user request.
    """
    row_idx = 0
    while True:
        view_data = validate_input("Would you like to view 5 rows of raw data? (yes/no): ", ['yes', 'no'])
        if view_data == 'yes':
            print(df.iloc[row_idx : row_idx + 5])
            row_idx += 5
            if row_idx >= len(df):
                print("End of dataset reached.")
                break
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        if not df.empty:
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            display_raw_data(df)
        else:
            print("\nNo data found for the selected filters. Please try again.")

        restart = validate_input("\nWould you like to restart? (yes/no): ", ['yes', 'no'])
        if restart != 'yes':
            print("\nThank you for using the US Bikeshare Explorer. Goodbye!")
            break

if __name__ == "__main__":
    main()
