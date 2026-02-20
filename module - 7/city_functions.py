# Daniel Fryer
# Assignment 7
# 2/20/26

def DisplayCityCountry(city, country, language='Unknown', population=0):
    if language == 'Unknown':        
        if population > 0:
            displayCC = f"{city}, {country} - population {population}"
        else:
            displayCC = f"{city}, {country}"
    else:
        if population > 0:
            displayCC = f"{city}, {country} - population {population}, {language}"
        else:
            displayCC = f"{city}, {country}, {language}"
            
    return(displayCC)

def main():
    print("\n")
    city0 = DisplayCityCountry(city="Ottawa", country="Canada")
    print(city0)
    
    city1 = DisplayCityCountry(city="Santiago", country="Chili", language='Spanish')       
    print(city1)
    
    city2 = DisplayCityCountry(city="Omaha", country="U.S.A", population=350000000)       
    print(city2)
    
    city3 = DisplayCityCountry(city="Bejing", country="China", language="Mandorin", population=1500000000)       
    print(city3 + "\n")

if __name__ == '__main__':
    main()