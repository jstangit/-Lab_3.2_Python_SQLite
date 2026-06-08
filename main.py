import sqlite3

# Define DBOperation class to manage all data into the database.
# Give a name of your choice to the database


class DBOperations:

  def __init__(self):
    pass
  

  def get_connection(self):
    self.conn = sqlite3.connect("FlightMan.db")
    self.cur = self.conn.cursor()

  def create_table(self):
    try:
      self.get_connection()
      self.cur.execute("""
      CREATE TABLE IF NOT EXISTS Destination (
        DestinationID INTEGER PRIMARY KEY AUTOINCREMENT,
        AirportCode TEXT NOT NULL UNIQUE,
        City TEXT NOT NULL,
        Country TEXT NOT NULL,
        TerminalInfo TEXT
      )
      """)

      self.cur.execute("""
      CREATE TABLE IF NOT EXISTS Pilot (
        PilotID INTEGER PRIMARY KEY AUTOINCREMENT,
        FirstName TEXT NOT NULL,
        LastName TEXT NOT NULL,
        LicenceNumber TEXT NOT NULL UNIQUE,
        Phone TEXT,
        Rank TEXT
      )
    """)

      self.cur.execute("""
      CREATE TABLE IF NOT EXISTS Flight (
        FlightID INTEGER PRIMARY KEY AUTOINCREMENT,
        FlightNumber TEXT NOT NULL UNIQUE,
        DestinationID INTEGER NOT NULL,
        DepartureDate TEXT NOT NULL,
        DepartureTime TEXT NOT NULL,
        ArrivalTime TEXT,
        Status TEXT NOT NULL,
        FOREIGN KEY (DestinationID) REFERENCES Destination(DestinationID)
      )
      """)

      self.cur.execute("""
      CREATE TABLE IF NOT EXISTS PilotAssignment (
        FlightID INTEGER NOT NULL,
        PilotID INTEGER NOT NULL,
        Role TEXT NOT NULL,
        PRIMARY KEY (FlightID, PilotID),
        FOREIGN KEY (FlightID) REFERENCES Flight(FlightID),
        FOREIGN KEY (PilotID) REFERENCES Pilot(PilotID)
      )
      """)
      self.conn.commit()
      print("Tables created successfully")
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  def insert_sample_data(self):
    try:
      self.get_connection()

      self.cur.executemany("""
      INSERT OR IGNORE INTO Destination
      (DestinationID, AirportCode, City, Country, TerminalInfo)
      VALUES (?, ?, ?, ?, ?)
      """, [
        (1, "LHR", "London", "United Kingdom", "Terminal 5"),
        (2, "CDG", "Paris", "France", "Terminal 2"),
        (3, "AMS", "Amsterdam", "Netherlands", "Main Terminal"),
        (4, "FCO", "Rome", "Italy", "Terminal 1"),
        (5, "MAD", "Madrid", "Spain", "Terminal 4"),
        (6, "JFK", "New York", "United States", "Terminal 8"),
        (7, "DXB", "Dubai", "United Arab Emirates", "Terminal 3"),
        (8, "SIN", "Singapore", "Singapore", "Terminal 1"),
        (9, "DUB", "Dublin", "Ireland", "Terminal 2"),
        (10, "BER", "Berlin", "Germany", "Terminal 1")
      ])

      self.cur.executemany("""
      INSERT OR IGNORE INTO Pilot
      (PilotID, FirstName, LastName, LicenceNumber, Phone, Rank)
      VALUES (?, ?, ?, ?, ?, ?)
      """, [
        (1, "John", "Smith", "LIC1001", "07111111111", "Captain"),
        (2, "Sarah", "Jones", "LIC1002", "07222222222", "First Officer"),
        (3, "Michael", "Brown", "LIC1003", "07333333333", "Captain"),
        (4, "Emma", "Wilson", "LIC1004", "07444444444", "First Officer"),
        (5, "David", "Taylor", "LIC1005", "07555555555", "Captain"),
        (6, "Laura", "Evans", "LIC1006", "07666666666", "First Officer"),
        (7, "James", "Thomas", "LIC1007", "07777777777", "Captain"),
        (8, "Olivia", "Walker", "LIC1008", "07888888888", "First Officer"),
        (9, "Daniel", "White", "LIC1009", "07999999999", "Captain"),
        (10, "Sophie", "Harris", "LIC1010", "07000000000", "First Officer")
      ])

      self.cur.executemany("""
      INSERT OR IGNORE INTO Flight
      (FlightID, FlightNumber, DestinationID, DepartureDate, DepartureTime, ArrivalTime, Status)
      VALUES (?, ?, ?, ?, ?, ?, ?)
      """, [
        (1, "FM101", 1, "2026-07-01", "08:00", "09:00", "Scheduled"),
        (2, "FM102", 2, "2026-07-01", "09:30", "11:45", "Scheduled"),
        (3, "FM103", 3, "2026-07-02", "10:00", "11:20", "Delayed"),
        (4, "FM104", 4, "2026-07-02", "12:00", "14:30", "Scheduled"),
        (5, "FM105", 5, "2026-07-03", "13:15", "15:50", "Cancelled"),
        (6, "FM106", 6, "2026-07-03", "14:00", "21:00", "Scheduled"),
        (7, "FM107", 7, "2026-07-04", "16:20", "23:40", "Scheduled"),
        (8, "FM108", 8, "2026-07-04", "18:00", "06:30", "Scheduled"),
        (9, "FM109", 9, "2026-07-05", "07:45", "09:05", "Delayed"),
        (10, "FM110", 10, "2026-07-05", "11:10", "13:40", "Scheduled")
      ])

      self.cur.executemany("""
      INSERT OR IGNORE INTO PilotAssignment
      (FlightID, PilotID, Role)
      VALUES (?, ?, ?)
      """, [
        (1, 1, "Captain"),
        (1, 2, "First Officer"),
        (2, 3, "Captain"),
        (2, 4, "First Officer"),
        (3, 5, "Captain"),
        (3, 6, "First Officer"),
        (4, 7, "Captain"),
        (4, 8, "First Officer"),
        (5, 9, "Captain"),
        (5, 10, "First Officer"),
        (6, 1, "Captain"),
        (6, 4, "First Officer")
      ])

      self.conn.commit()
      print("Sample data inserted successfully")

    except Exception as e:
      print(e)

    finally:
      self.conn.close()

  def add_new_flight(self):
    try:
      self.get_connection()

      flightNumber = input("Enter Flight Number: ")
      destinationID = int(input("Enter Destination ID: "))
      departureDate = input("Enter Departure Date (YYYY-MM-DD): ")
      departureTime = input("Enter Departure Time (HH:MM): ")
      arrivalTime = input("Enter Arrival Time (HH:MM): ")
      status = input("Enter Status: ")

      result = self.cur.execute(
        """
        INSERT INTO Flight
        (FlightNumber, DestinationID, DepartureDate, DepartureTime, ArrivalTime, Status)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (flightNumber, destinationID, departureDate, departureTime, arrivalTime, status)
      )

      self.conn.commit()
      print("New flight added successfully")

    except Exception as e:
      print(e)

    finally:
      self.conn.close()

  def assign_pilot(self):
    try:
      self.get_connection()

      flightID = int(input("Enter Flight ID: "))
      pilotID = int(input("Enter Pilot ID: "))
      role = input("Enter Role: ")

      result = self.cur.execute(
        """
        INSERT INTO PilotAssignment
        (FlightID, PilotID, Role)
        VALUES (?, ?, ?)
        """,
        (flightID, pilotID, role)
      )

      self.conn.commit()
      print("Pilot assigned to flight successfully")

    except Exception as e:
      print(e)

    finally:
      self.conn.close()

      # think how you could develop this method to show the records

  def search_data(self):
    try:
      self.get_connection()
      status = input("Enter Flight Status: ")

      self.cur.execute("SELECT * FROM Flight WHERE Status = ?", (status,))
      result = self.cur.fetchall()

      if len(result) > 0:
       for row in result:
        for index, detail in enumerate(row):
          if index == 0:
            print("Flight ID: " + str(detail))
          elif index == 1:
            print("Flight Number: " + detail)
          elif index == 2:
            print("Destination ID: " + str(detail))
          elif index == 3:
            print("Departure Date: " + detail)
          elif index == 4:
            print("Departure Time: " + detail)
          elif index == 5:
            print("Arrival Time: " + detail)
          else:
            print("Status: " + str(detail))
      else:
        print("No Record")

    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  def update_data(self):
    try:
      self.get_connection()

      flightID = int(input("Enter Flight ID: "))
      status = input("Enter New Status: ")

      result = self.cur.execute(
        """
        UPDATE Flight
        SET Status = ?
        WHERE FlightID = ?
        """,
        (status, flightID)
      )

      self.conn.commit()

      if result.rowcount != 0:
        print(str(result.rowcount) + "Row(s) affected.")
      else:
        print("Cannot find this record in the database")

    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  def view_pilot_schedule(self):
    try:
      self.get_connection()

      pilotID = int(input("Enter Pilot ID: "))

      self.cur.execute(
        """
        SELECT Pilot.FirstName, Pilot.LastName, Flight.FlightNumber,
               Flight.DepartureDate, Flight.DepartureTime, Flight.ArrivalTime,
               Flight.Status, PilotAssignment.Role
        FROM PilotAssignment
        JOIN Pilot ON PilotAssignment.PilotID = Pilot.PilotID
        JOIN Flight ON PilotAssignment.FlightID = Flight.FlightID
        WHERE Pilot.PilotID = ?
        """,
        (pilotID,)
      )

      result = self.cur.fetchall()

      for row in result:
        print("Pilot: " + row[0] + " " + row[1])
        print("Flight Number: " + row[2])
        print("Departure Date: " + row[3])
        print("Departure Time: " + row[4])
        print("Arrival Time: " + row[5])
        print("Status: " + row[6])
        print("Role: " + row[7] + "\n")

    except Exception as e:
      print(e)

    finally:
      self.conn.close()


# Define Delete_data method to delete data from the table. The user will need to input the flight id to delete the corrosponding record.

  def delete_data(self):
    try:
      self.get_connection()

      flightID = int(input("Enter Flight ID: "))

      result = self.cur.execute(
        "DELETE FROM Flight WHERE FlightID = ?",
        (flightID,)
      )

      self.conn.commit()

      if result.rowcount != 0:
        print(str(result.rowcount) + "Row(s) affected.")
      else:
        print("Cannot find this record in the database")

    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  def view_destinations(self):
    try:
      self.get_connection()

      self.cur.execute("SELECT * FROM Destination")
      result = self.cur.fetchall()

      for row in result:
        print(row)

    except Exception as e:
      print(e)

    finally:
      self.conn.close()

  def update_destination(self):
    try:
      self.get_connection()

      destinationID = int(input("Enter Destination ID: "))
      terminalInfo = input("Enter New Terminal Information: ")

      result = self.cur.execute(
        """
        UPDATE Destination
        SET TerminalInfo = ?
        WHERE DestinationID = ?
        """,
        (terminalInfo, destinationID)
      )

      self.conn.commit()

      if result.rowcount != 0:
        print(str(result.rowcount) + " Row(s) affected.")
      else:
        print("Cannot find this record in the database")

    except Exception as e:
      print(e)

    finally:
      self.conn.close()

  def summary_reports(self):
    try:
      self.get_connection()

      self.cur.execute("""
      SELECT DestinationID, COUNT(*)
      FROM Flight
      GROUP BY DestinationID
      """)

      result = self.cur.fetchall()

      for row in result:
        print("Destination ID: " + str(row[0]))
        print("Number of Flights: " + str(row[1]) + "\n")

    except Exception as e:
      print(e)

    finally:
      self.conn.close()

# The main function will parse arguments.
# These argument will be definded by the users on the console.
# The user will select a choice from the menu to interact with the database.

# Create and populate the database before the staff menu opens.
db_setup = DBOperations()
db_setup.create_table()
db_setup.insert_sample_data()

while True:
  print("\n Menu:")
  print("**********")
  print(" 1. Add a new flight")
  print(" 2. View flights by status")
  print(" 3. Update flight information")
  print(" 4. Delete flight")
  print(" 5. Assign pilot to flight")
  print(" 6. View pilot schedule")
  print(" 7. View destination information")
  print(" 8. Update destination information")
  print(" 9. View summary reports")
  print(" 10. Exit\n")

  __choose_menu = int(input("Enter your choice: "))
  db_ops = DBOperations()
  if __choose_menu == 1:
    db_ops.add_new_flight()
  elif __choose_menu == 2:
    db_ops.search_data()
  elif __choose_menu == 3:
    db_ops.update_data()
  elif __choose_menu == 4:
    db_ops.delete_data()
  elif __choose_menu == 5:
    db_ops.assign_pilot()
  elif __choose_menu == 6:
    db_ops.view_pilot_schedule()
  elif __choose_menu == 7:
    db_ops.view_destinations()
  elif __choose_menu == 8:
    db_ops.update_destination()
  elif __choose_menu == 9:
    db_ops.summary_reports()
  elif __choose_menu == 10:
    exit(0)
  else:
    print("Invalid Choice")
