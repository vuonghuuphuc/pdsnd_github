import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    valid_cities = ["chicago", "new york city", "washington"]
    while True:
        city = input("Please input for city (chicago, new york city, washington): ").lower()
        if city in valid_cities:
            break  # Exit the loop if the input is valid
        print("Invalid city. Please enter again.")

    # get user input for month (all, january, february, ... , june)
    valid_month = ["all", "january", "february", "march", "april", "may", "june"]
    while True:
        month = input("Please input for month (all, january, february, ... , june): ").lower()
        if month in valid_month:
            break  # Exit the loop if the input is valid
        print("Invalid month. Please enter again.")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    valid_day = ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    while True:
        day = input("Please input for for day of week (all, monday, tuesday, ... sunday): ").lower()
        if day in valid_day:
            break  # Exit the loop if the input is valid
        print("Invalid day. Please enter again.")

    print('-'*40)
    return city, month, day

def day_text_to_number(day_text):
    # Define a dictionary to map day names to numerical values
    day_to_number = {
        "monday": 0,
        "tuesday": 1,
        "wednesday": 2,
        "thursday": 3,
        "friday": 4,
        "saturday": 5,
        "sunday": 6
    }

    # Convert the day name to its numerical representation
    if day_text in day_to_number:
        return day_to_number[day_text]
    else:
        return None  # Return None for invalid day names

def month_text_to_number(month_text):
    # Define a dictionary to map month names to numerical values
    month_to_number = {
        "january": 1,
        "february": 2,
        "march": 3,
        "april": 4,
        "may": 5,
        "june": 6,
    }

    # Convert the month name to its numerical representation
    if month_text in month_to_number:
        return month_to_number[month_text]
    else:
        return None  # Return None for invalid month names

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

    # Read the CSV file into a DataFrame
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    if month != "all":
        df = df[df['Start Time'].dt.month == month_text_to_number(month)]

    if day != "all":
        df = df[df['Start Time'].dt.weekday == day_text_to_number(day)]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    month_calculated = df["Start Time"].dt.month.value_counts()
    print("display the most common month: ", month_calculated.idxmax())

    # display the most common day of week
    day_calculated = df["Start Time"].dt.month.value_counts()
    print("display the most common day of week: ", day_calculated.idxmax())

    # display the most common start hour
    hour_calculated = df["Start Time"].dt.hour.value_counts()
    print("display the most common start hour: ", hour_calculated.idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    station_calculated = df["Start Station"].value_counts()
    print("display most commonly used start station: ", station_calculated.idxmax())

    # display most commonly used end station
    station_calculated = df["End Station"].value_counts()
    print("display most commonly used end station: ", station_calculated.idxmax())

    # display most frequent combination of start station and end station trip
    combined_stations = pd.concat([df['Start Station'], df['End Station']])
    station_calculated = combined_stations.value_counts()
    print("display most frequent combination of start station and end station trip: ", station_calculated.idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("display total travel time: ", total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("display mean travel time: ", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_counts = df.groupby('User Type').size().reset_index(name='Count')
    print("Display counts of user types: ")
    print(user_type_counts)

    if city != "washington":
        # Display counts of gender
        gender_counts = df.groupby('Gender').size().reset_index(name='Count')
        print("Display counts of gender: ")
        print(gender_counts)

        # Display earliest, most recent, and most common year of birth
        df['Birth Year'] = pd.to_numeric(df['Birth Year'])
        earliest_birth_year = df['Birth Year'].min()
        print("Display earliest year of birth: ", earliest_birth_year)

        most_recent_birth_year = df['Birth Year'].max()
        print("Display most recent year of birth: ", most_recent_birth_year)

        most_common_birth_year = df['Birth Year'].mode().values[0]
        print("Display most common year of birth: ", most_common_birth_year)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):

    start_loc = 0
    while start_loc < len(df):
        user_input = input("\nWould you like to view 5 rows of individual trip data? Enter yes or no\n").lower()
        if user_input == 'yes':
            chunk = df.iloc[start_loc:start_loc + 5]
            print(chunk)
            start_loc += 5
        elif user_input == 'no':
            break
        else:
            print("Invalid input. Please enter 'YES' or 'NO'.")


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
