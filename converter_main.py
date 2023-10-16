#!/usr/bin/env python3
# Take input from the user to convert either Celsius or Fahrenheit
# Created by Max Hyland
# CIS 410

# Import converter module
import converter

# Function to display title for the program.
def display_title():
    print("Fahrenheit & Celcius Converter")
    print()


def display_menu():
    print("MENU")
    print("1. Farenheit to Celsius")
    print("2. Celsius to Farenheit")
    print()

# Ask user either to convert to F -> C, or C -> F.
def convert_temp():
    option = int(input("Choose either of the converter options (1 or 2): "))
    f = 0
    c = 0
    if option == 1:
        f = int(input("Enter degrees Fahrenheit: "))
        c = converter.temp_to_celsius(f)
        c = round(c, 2)
        print("Degrees Celsius:", c)

    elif option == 2:
        c = int(input("Enter degrees Celsius: "))
        f = converter.temp_to_farenheit(c)
        f = round(f, 2)
        print("Degrees to Fahrenheit: ", f)

    else:
        print("You must enter a valid number")

def main():
    display_title()

    #  While loop for user to repeatedly go multiple times.
    again = "y"
    display_menu()
    while again.lower() == "y":
        # Call converter function.
        convert_temp()
        print()
        # Ask user if they want to go again.
        again = input("Convert again? (y/n): ")
        print()
        
        
    #End loop and end program

    print("Bye!")

if __name__ == "__main__":
    main()

