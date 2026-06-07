# -Lab_3.2_Python_SQLite
Implemented initial Flight Management Database schema.

Changes:
- Added SQLite database connection using FlightMan.db.
- Created Destination table with destination information.
- Created Pilot table with pilot details.
- Created Flight table with flight schedule information and destination foreign key.
- Created PilotAssignment table to support pilot-to-flight assignments using a composite primary key.

- Added sample data insertion for the Flight Management Database. The insert_sample_data method now populates the Destination, Pilot, Flight and PilotAssignment tables.