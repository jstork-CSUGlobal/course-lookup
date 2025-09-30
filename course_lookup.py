# course_lookup.py
# Create dictionaries for room numbers, instructors, and meeting times

rooms = {
    "CSC101": 3004, "CSC102": 4501,
    "CSC103": 6755, "NET110": 1244,
    "COM241": 1411
}
instructors = {
    "CSC101": "Haynes", "CSC102":"Alvarado",
    "CSC103": "Rich", "NET110": "Burke",
    "COM241": "Lee"
}
times = {
    "CSC101": "8:00 a.m.", "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.","NET110": "11:00 a.m.",
    "COM241": "1:00 p.m."
}

# Prompt the user to enter a course number
course = input("Enter course (e.g., CSC101): ").strip().upper() # strip & upper trims the input & converts it to CAPS

# Check if the course exists in the dictionaries
if course in rooms and course in instructors and course in times:
    # Display the course information if it exists in the dictionaries
    print(f"Course: {course}")
    print(f"Room: {rooms[course]}")
    print(f"Instructor: {instructors[course]}")
    print(f"Meeting time: {times[course]}")
else:
    # Display an error message if the course is not found
    print("Course not found. Valid: CSC101, CSC102, CSC103, NET110, COM241")
