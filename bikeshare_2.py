import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    global input_month
    global input_day

    month = ['january','february', 'march','april','may','june','all']
    day = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ['chicago','new york city', 'washington']
    while True:
        input_city = input("Which city would you like to select: chicago, new York city, washington?").lower()
        if input_city not in city:
            print("You may have misspell the city, please try again!", end='')
            continue
        else:
            break
        
    while True:
        input_month = input("Please select a month or all: ").lower()
        if input_month not in month:
            print ("You may have misspell the month, please try again!", end='')
            continue
        else:
            break
    while True:
        input_day = input("Please select a day of the week or all - please use full name: ").lower()
        if input_day not in day:
            print("You may have misspell the day, please try again!", end='')
            continue
        else:
            break
        
    print('-'*40)
    return input_city, input_month, input_day


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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df["hour"] = df["Start Time"].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        print('You have selected the following filters: \nCity: {}\nMonth: {}\nDay: {}'.format(city, month, day))
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Popular month:', popular_hour)
    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('The most common day of the week is:',popular_day)
    # display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('The most common start hour is:'.format(popular_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    # for the below I got help from http://www.datasciencemadesimple.com/mode-function-python-pandas-dataframe-row-column-wise-mode/
    popular_start_station = df.loc[:,"Start Station"].mode()[0]

    # display most commonly used end station
    popular_end_station = df.loc[:,"End Station"].mode()[0]

    # display most frequent combination of start station and end station trip
    # help from https://www.reddit.com/r/learnpython/comments/7s99rk/pandas_sort_by_most_frequent_value_combinations/
    start_end_station = df.groupby(['Start Station', 'End Station']).size()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_duration = df.groupby(['Trip Duration']).sum()

    # display mean travel time
    mean_duration = df.groupby(['Trip Duration']).mean()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
   # advise taken from https://knowledge.udacity.com/questions/55524
    

#Like this

    if "Gender" in df.columns:
        user_gender = df['Gender'].value_counts()
        print(user_gender)
    else:
        print("Gender column does not exists")


    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        min_user_dob= df['Birth Year'].min()
        print(min_user_dob)
    else:
        
        print("Date of birth column does not exist")
    
    if 'Birth Year' in df.columns:
        max_user_dob = df['Birth Year'].max()
        print(max_user_dob)
    
    else:
        print("Date of birth column does not exist")
    
    if 'Birth Year' in df.columns:
        dob_count = df['Birth Year'].mode()[0]
        print(dob_count)
    else:
        print("Date of birth column does not exist")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
