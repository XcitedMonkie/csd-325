import csv
from datetime import datetime
import sys
from matplotlib import pyplot as plt

import os

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
            current_date = datetime.strptime(row[2], '%m/%d/%Y') #datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            high = int(row[5])
            highs.append(high)
            low = int(row[6])
            lows.append(low)
            
    return dates, highs, lows

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
    
def Main():
    dates, highs, lows = GetWeatherData()
    
    while True:
        print("Welcome to the Sitka Weather Program")
        print("Please make a selection from below")
        print()
        print("1. View High Temps")
        print("2. View Low Temps")
        print("3. Exit")
        print()
        
        userSelect = input("Enter your choice (1,2,3) ")
        
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