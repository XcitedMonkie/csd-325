import csv
from datetime import datetime
import sys
from matplotlib import pyplot as plt

import os

# Create a function to get the data from the CSV file
def GetWeatherData():
    
    script_dir = os.path.dirname(__file__)
    filename = os.path.join(script_dir, 'sitka_weather_2018_simple.csv')


    #filename = r'csd-325/module - 4/sitka_weather_2018_simple.csv'

    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Get dates and high temperatures from this file. 
        dates, highs, lows= [], [], []
        for row in reader:
            current_date = datetime.strptime(row[2], '%m/%d/%Y') #datetime.strptime(row[2], '%Y-%m-%d') Had to change this line as the datetime was not in the same format defaulted here
            dates.append(current_date)
            high = int(row[5])
            highs.append(high)
            low = int(row[6])
            lows.append(low)
            
    return dates, highs, lows

# create a function to display the display get the dates, temps, line color, and title from the main function
def PlotAndDisplay(dates, temps, color, title):
    # Plot the high temperatures.
    #plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, temps, c=color)

    # Format plot.
    plt.title(title, fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
    
# Start of the program here.
def Main():
    # start by getting the dates,highs, and lows from the function 
    dates, highs, lows = GetWeatherData()
    
    # create a "Menu" and keep it looping until the user exits with a number 3
    while True:
        print("Welcome to the Sitka Weather Program")
        print("Please make a selection from below")
        print()
        print("1. View High Temps")
        print("2. View Low Temps")
        print("3. Exit")
        print()
        
        userSelect = input("Enter your choice (1,2,3) ")
        
        # determin what the user selected. If its a 1 or 2 call the plot and display function if its a 3 exit the program any other option start the loop over.
        if userSelect == "1":
            PlotAndDisplay(dates, highs, color = 'red', title= "Daily High Temps - 2018")
        elif userSelect == "2":
            PlotAndDisplay(dates, lows, color = 'blue', title= "Daily Low Temps - 2018")
        elif userSelect == "3":
            print()
            print("Thanks for using the weather program")
            sys.exit()
        else:
            print("Selection not found. Please select 1, 2, or 3")
            
if __name__ == "__main__":
    Main()