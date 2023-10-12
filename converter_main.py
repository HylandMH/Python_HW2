#!/usr/bin/env python3
# Take input from the user to convert either to 

# Import converter module
import converter as CONVERT

# Function to display title for the program.
def display_title():
    print("Fahrenheit & Celcius Converter")
    print()

# Ask user either to convert to F -> C, or C -> F.

def main():
    # Call display function
    display_title()
    # While loop for user to repeatedly go multiple times.
    again = "y"

    while again.lower() == "y":
        again = input("Convert again? (y/n): ")
        print()
        # Call converter function.
        # Ask user if they want to go again.
    #End loop and end program
    pass

print("Bye!")

if __name__ == "__main__":
    main()

