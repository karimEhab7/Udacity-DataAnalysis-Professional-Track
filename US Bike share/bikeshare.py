import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june']
days=['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday' ]
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    while True:
       city=input("Would you like to see for Chicago, New York or Washington?\n  ").lower()
       if city in CITY_DATA.keys():
              break
       else:
              print("You entered wrong City please try again!\n")
    month='all'
    day='all'
    filterVar=input('\nWould you like to filter the data by Month, day, both or not at all? Type "none for no time filter.\n' ).lower()
    if filterVar.lower()== 'both':
        # TO DO: get user input for month (all, january, february, ... , june) 
        
        while True:
            month=input('\nWhich Month? (all, january, february, march, april, may, june ? \n').lower()
            if month in months or month=='all':
                break
            else:
                print("You entered wrong Month please try again!\n")
            
        
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        while True:
            day=input('\nWhich day? please type ypur response as an integer( all, sunday, monday, tuesday, wednesday, thursday, friday, saturday).  \n').lower()
            if day in days or day=='all':
                break
            else:
                print("You entered wrong day please try again!\n")
          
    elif filterVar== 'month':
        # TO DO: get user input for month (all, january, february, ... , june) 
        while True:
            month=input('\nWhich Month? (all, january, february, march, april, may, june ? \n').lower()
            if month in months or month=='all':
                break
            else:
                print("You entered wrong Month please try again!\n")
            
    elif filterVar== 'day':
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        while True:
            day=input('\nWhich day? please type ypur response as an integer( all, sunday, monday, tuesday, wednesday, thursday, friday, saturday).  \n').lower()
            if day in days or day=='all':
                break
            else:
                print("You entered wrong day please try again!\n")
         
    elif filterVar== 'none':
        month="all"
        day="all"
    else:
        print("you entered wrong value please try again! \n")
        
        
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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day and start hour of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.day_name()

    df['start_hour'] = df['Start Time'].dt.hour   
       
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month']==month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    mostCommonMonth=df['month'].mode()[0]
    print("the most common month: ",mostCommonMonth, "Count: ",df[df['month']==mostCommonMonth].count()[0])

    # TO DO: display the most common day of week
    mostCommonday=df['day_of_week'].mode()[0]
    print("the most common day of week: ",mostCommonday, "Count: ",df[df['day_of_week']==mostCommonday].count()[0])


    # TO DO: display the most common start hour
    mostCommonStart=df['start_hour'].mode()[0]
    print("the most common start hour: ",mostCommonStart , "Count: ",df[df['start_hour']==mostCommonStart].count()[0])   

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    mostCommonStartStation=df['Start Station'].mode()[0]
    print("\nthe most commonly used Start Station: ",mostCommonStartStation, " Count: ",df[df['Start Station']==mostCommonStartStation].count()[0])


    # TO DO: display most commonly used end station
    mostCommonEndStation=df['End Station'].mode()[0]
    print("\nthe most commonly used end Station: ",mostCommonEndStation, " Count: ",df[df['End Station']==mostCommonEndStation].count()[0])


    # TO DO: display most frequent combination of start station and end station trip
    mostCommonStartEnd= df[['Start Station', 'End Station']].mode().loc[0]
    print("\nthe most most frequent combination of start station and end station trip: \n",mostCommonStartEnd)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total travel time: ",df['Trip Duration'].sum())   

    # TO DO: display mean travel time
    print("Mean travel time",df['Trip Duration'].mean())   

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Counts of user types: \n",df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if 'Gender' in df:
       print("\nCounts of gender: \n",df['Gender'].value_counts())
    else:
       print("\nCounts of gender: \n","Gender codes are not available")
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
       earlist=df['Birth Year'].min()
       most_recent=df['Birth Year'].max()
       most_common=df['Birth Year'].mode()[0]
       print("\nEarlist date of birth: ", earlist)
       print("\nMost recent date of birth: ",most_recent)
       print("\nMost common date of birth: ",most_common)
    else:
       print("\nEarlist date of birth: ", "Birthdates are not available")
       print("\nMost recent date of birth: ","Birthdates are not available")
       print("\nMost common date of birth: ","Birthdates are not available")
       
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def displayRows(df):
    """Display 5 lines of raw data."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    index=5
    print(df.head())
    count=0
    while True:
       contBool=input("Do you want to print another 5 raw data? (Yes or No)").lower()
       if contBool =='no':
              break
       else:
              count = count + 5
              print(df.iloc[count:count+5])


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
        displayRows(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
