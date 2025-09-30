# Course Lookup Program

This Python program allows users to search for course information by entering a course number. The program retrieves and displays the course details (room, instructor, and meeting time) if the course number is valid.

## Installation

To run this program, you need to have Python installed on your computer. You can download Python from the official website: https://www.python.org/downloads/

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory where you have saved the `course_lookup.py` file.
3. Run the program by typing `python course_lookup.py` and pressing Enter.
4. The program will prompt you to enter a course number.
5. If the course number is valid, the program will display the course details. If not, it will display a message with a list of valid course numbers.

## Code Structure

The code is organized into the following sections:

1. Data Setup: Define dictionaries for course information (course numbers, instructors, times, and rooms).
2. User Input: Prompt the user to enter a course number and convert it to uppercase.
3. Data Lookup & Display: Check if the user's selection is valid. If it is, retrieve the corresponding course information from the `courses` dictionary and display the details. If not, display a message indicating valid options.
