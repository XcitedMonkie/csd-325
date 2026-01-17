# Daniel Fryer
# 1/16/2026
# Assignment 1_3
# This will take the number of beer(s) from the user and then repeat the song back to the user

# This is the function that will print out the count down of the beers
def BeerSongCntDown(beerCount):
    while beerCount > 0:
        print(f"{beerCount} bottles of beer on the wall, {beerCount} bottles of beer.")
        print(f"Take one down and pass it around, {beerCount - 1} bottle(s) of beer on the wall.")
        print()
        beerCount = beerCount - 1
    print("Time to go get more beer!")
    
    
def Main():
    # Get the number of beers from the user and make sure that its an integer and not 0 or negative
    while True:
        try:
            nbrOfBeers =int(input(f"How many beer(s) do you have: "))
            if nbrOfBeers <= 0:
                print("Number entered is 0 or is negative please try again")
            else:
                break
        except ValueError:
            print("Please enter a valid number")

    # Call the function
    BeerSongCntDown(nbrOfBeers)


if __name__ == "__main__":
    Main()