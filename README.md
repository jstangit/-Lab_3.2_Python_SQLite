# -Lab_3.2_Python_SQLite
Implemented initial Flight Management Database schema.

The Flight Management System is a command-line application developed in Python using SQLite. The system allows airline staff to manage flight information through a menu interface. Users can add new flights, search for flights by status, update or delete flight records, assign pilots to flights, view pilot schedules, manage destination information, and generate summary reports. All information is stored in a relational database consisting of the Destination, Flight, Pilot and PilotAssignment tables.

To use the system:

Enter 1 to add a new flight and provide the requested flight details.
Enter 2 to search for flights by status (e.g. Scheduled, Delayed, Cancelled).
Enter 3 to update the status of an existing flight using its Flight ID.
Enter 4 to delete a flight by entering its Flight ID.
Enter 5 to assign a pilot to a flight by entering a Flight ID, Pilot ID and role.
Enter 6 to view the schedule for a specific pilot.
Enter 7 to view all destination records.
Enter 8 to update destination information.
Enter 9 to view summary reports showing the number of flights assigned to each destination.
Enter 10 to exit the application.

The menu will continue to display after each operation until the user chooses to exit.

Changes:
- Added SQLite database connection using FlightMan.db.
- Created Destination table with destination information.
- Created Pilot table with pilot details.
- Created Flight table with flight schedule information and destination foreign key.
- Created PilotAssignment table to support pilot-to-flight assignments using a composite primary key.

- Added sample data insertion for the Flight Management Database. The insert_sample_data method now populates the Destination, Pilot, Flight and PilotAssignment tables.