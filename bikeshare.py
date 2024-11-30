import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# get user filters for city, month, and day
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # Get city input from user
    while True:
        city = input("Which city would you like to analyze? (chicago, new york city, washington): ").lower()
        if city in CITY_DATA:
            break
        else:
            print("Invalid city! Please choose a valid city (chicago, new york city, washington).")

    # Get month input from user
    while True:
        month = input("Which month would you like to filter by? (January, February, ..., June) or type 'all' for no filter: ").lower()
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
        if month in months:
            break
        else:
            print("Invalid month! Please choose a valid month or 'all'.")

    # Get day input from user
    while True:
        day = input("Which day would you like to filter by? (Monday, Tuesday, ..., Sunday) or type 'all' for no filter: ").lower()
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
        if day in days:
            break
        else:
            print("Invalid day! Please choose a valid day or 'all'.")

    print('-'*40)
    return city, month, day

# Function to load and filter the data
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    """
    df = pd.read_csv(CITY_DATA[city])

    # Convert Start Time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month, day, and hour from 'Start Time'
    df['Month'] = df['Start Time'].dt.month
    df['Day'] = df['Start Time'].dt.day_name().str.lower()
    df['Hour'] = df['Start Time'].dt.hour

    # Filter by month if applicable
    if month != 'all':
        month_num = ['january', 'february', 'march', 'april', 'may', 'june'].index(month) + 1
        df = df[df['Month'] == month_num]

    # Filter by day if applicable
    if day != 'all':
        df = df[df['Day'] == day.lower()]

    return df

# Function to display raw data in chunks
def display_data(df):
    start_loc = 0
    while True:
        # Show the next 5 rows
        print(df.iloc[start_loc:start_loc+5])

        # Ask the user if they want to see more data
        user_input = input("Do you want to see the next 5 rows of data? (yes/no): ").lower()
        if user_input == 'yes':
            start_loc += 5
            # If there are no more rows to display
            if start_loc >= len(df):
                print("No more data to display.")
                break
        elif user_input == 'no':
            break
        else:
            print("Invalid input! Please enter 'yes' or 'no'.")

# Calculate the most frequent times of travel
def time_stats(df):
    print('\nThe Most Frequent Times of Travel:\n')
    start_time = time.time()

    # Most common month
    popular_month = df['Month'].mode()[0]
    print(f"Most common month: {['January', 'February', 'March', 'April', 'May', 'June'][popular_month-1]}")

    # Most common day of week
    popular_day = df['Day'].mode()[0]
    print(f"Most common day of week: {popular_day.title()}")

    # Most common start hour
    popular_hour = df['Hour'].mode()[0]
    print(f"Most common start hour: {popular_hour}")

    print('-'*40)

# Calculate the most popular stations and trip
def station_stats(df):
    print('\nThe Most Popular Stations and Trip:\n')
    start_time = time.time()

    # Most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print(f"Most common start station: {popular_start_station}")

    # Most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print(f"Most common end station: {popular_end_station}")

    # Most frequent combination of start station and end station trip
    popular_trip = (df['Start Station'] + ' to ' + df['End Station']).mode()[0]
    print(f"Most frequent trip: {popular_trip}")

    print('-'*40)

# Calculate trip duration
def trip_duration_stats(df):
    print('\nTrip Duration calculation\n')
    start_time = time.time()

    # Total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(f"Total travel time: {total_travel_time} seconds")

    # Mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(f"Average travel time: {mean_travel_time} seconds")

    print('-'*40)

# Calculate userinformation
def user_stats(df, city):
    print('\nUser Statsinformation:\n')
    start_time = time.time()

    # Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    print(f"User types:\n{user_type_counts}")

    # Gender counts (if available)
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print(f"Gender counts:\n{gender_counts}")
    
    # Birth year stats (if available)
    if 'Birth Year' in df.columns:
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode()[0]
        print(f"Earliest birth year: {earliest_birth_year}")
        print(f"Most recent birth year: {most_recent_birth_year}")
        print(f"Most common birth year: {most_common_birth_year}")

    print('-'*40)

# Main function to execute the program
def main():
    while True:
        # Get user input for filters
        city, month, day = get_filters()

        # Load data based on filters
        df = load_data(city, month, day)

        # Calculate and display statistics
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        
if __name__ == "__main__":
    main()