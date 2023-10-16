#!/usr/bin/env python3
# Take input from the user to convert either to 

# Import converter module
import converter as CONVERT

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
    if option == 1:
        f = int(input("Enter degrees Fahrenheit: "))
        c =CONVERT.temp_to_celsius(f)
        c = round(c, 2)
        print("Degrees Celsius:", c)

    elif option == 2:
        c = int(input("Enter degrees Celsius: "))
        f = CONVERT.temp_to_farenheit(c)
        f = round(f, 2)
        print("Degrees to Fahrenheit: ", f)

    else:
        print("You must enter a valid number")

def main():
    display_title()

    #  While loop for user to repeatedly go multiple times.
    again = "y"

    while again.lower() == "y":
        convert_temp()
        print()
        again = input("Convert again? (y/n): ")
        print()
        # Call converter function.
        # Ask user if they want to go again.
    #End loop and end program
    pass

print("Bye!")

if __name__ == "__main__":
    main()

