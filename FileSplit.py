#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""FileSplit.py: Simple Python script to split a file into smaller output files based on line count."""

__author__ = "Martin Sit"
__license__ = "MIT"
__version__ = "0.1"

import sys
import os
import shutil

# Main function
def split_file():
    try:
        print_title()

        line_count = 0 # Current line count of output file
        split_count = 1 # Number of output files/splits

        max_lines = get_max_lines()

        input_file = get_input_file()
        input_lines = input_file.readlines()

        create_output_directory(input_file.name)
        output_file = create_output_file(split_count, input_file.name)

        for line in input_lines:

            output_file.write(line)
            line_count += 1

            # Create new output file if current output file's line count is greater than max line count
            if line_count > max_lines:
                split_count += 1
                line_count = 0

                output_file.close()

                # Prevent creation of an empty file after splitting is finished
                if not len(input_lines) == max_lines:
                    output_file = create_output_file(split_count, input_file.name)

    # Handle errors
    except Exception as e:
        print(f"An unknown error occurred: {e}")

    # Success message
    else:
        print(
            f"Successfully split {input_file.name} into {split_count} output files!")

# Print ASCII Art title and credits
def print_title():
    print("""
___________.__.__           _________      .__  .__  __   
\\_   _____/|__|  |   ____  /   _____/_____ |  | |__|/  |_ 
 |    __)  |  |  | _/ __ \\ \\_____  \\\\____ \\|  | |  \\   __\\
 |     \\   |  |  |_\\  ___/ /        \\  |_> >  |_|  ||  |  
 \\___  /   |__|____/\\___  >_______  /   __/|____/__||__|  
     \\/                 \\/        \\/|__|           
    """)
    print("version 0.1\n")

# Retrieve and return output file max lines from input
def get_max_lines():
    try:
        return int(input("Max lines per output file: "))
    except ValueError:
        print("Error: Please use a valid number.")
        sys.exit(1)

# Retrieve input filename and return file pointer
def get_input_file():
    try:
        filename = input("Input filename: ")
        return open(filename, 'r')
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)

# Create output file
def create_output_file(num, filename):
    return open(f"./output_{filename}/split_{num}.txt", "a")

# Create output directory
def create_output_directory(filename):
    output_path = f"./output_{filename}"
    try:
        if os.path.exists(output_path): # Remove directory if exists
            shutil.rmtree(output_path)
        os.mkdir(output_path)
    except OSError:
        print("Error: Failed to create output directory.")
        sys.exit(1)

if __name__ == "__main__":
    split_file()
