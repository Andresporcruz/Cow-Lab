#Andres Portillo
#3/26/2023
#COP3509

import sys
from heifer_generator import HeiferGenerator

def error(msg):
    # Raise an exception with the given message
    raise Exception(msg)

def main():
    # Generate cow objects from HeiferGenerator class
    cows = HeiferGenerator.get_cows()
    file_cows = HeiferGenerator.get_file_cows()

    # Check if there is at least one command-line argument
    if not len(sys.argv) > 1:
        error("no args!")

    # Get the first command-line argument
    first_argv = sys.argv[1]

    # If the first argument is "-l", print the available cow names
    if first_argv == "-l":
        # Get the names of all cows and file cows and print them
        cow_names = " ".join(map(lambda cow: cow.name, cows))
        file_cow_names = " ".join(map(lambda cow: cow.name, file_cows))
        print(f"Cows available: {cow_names}")
        print(f"File cows available: {file_cow_names}")

    # If the first argument is "-n" or "-f", find the matching cow object and print the message
    elif first_argv == "-n" or first_argv == "-f":
        # Check if there are at least 3 command-line arguments
        if not len(sys.argv) > 3:
            error("no args!")

        # Get the name of the cow and the message to print from the command-line arguments
        maybe_a_cow_name = sys.argv[2]
        msg = " ".join(sys.argv[3:])

        # Determine if we are working with cows or file cows
        list_of_cows_or_file_cows = cows if first_argv == "-n" else file_cows

        # Loop through each cow and print the message if the name matches
        for cow in list_of_cows_or_file_cows:
            if cow.name == maybe_a_cow_name:
                cow.print(msg)
                break
        else:
            # If the loop doesn't break, print an error message
            print(f"Could not find {maybe_a_cow_name} cow!")

    # If the first argument is not "-l", "-n", or "-f", print the arguments as a message
    else:
        # Print the arguments as a message using the first cow object
        cows[0].print(" ".join(sys.argv[1:]))

    # print sys.argv[0] as the msg


if __name__ == "__main__":
    main()