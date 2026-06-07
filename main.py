import sqlite3

# Define DBOperation class to manage all data into the database.
# Give a name of your choice to the database


class DBOperations:
  sql_create_table_firsttime = "create table if not exists "

  sql_create_table = "create table TableName"

  sql_insert = ""
  sql_select_all = "select * from TableName"
  sql_search = "select * from TableName where FlightID = ?"
  sql_alter_data = ""
  sql_update_data = ""
  sql_delete_data = ""
  sql_drop_table = ""

  def __init__(self):
    try:
      self.conn = sqlite3.connect("FlightMan.db")
      self.cur = self.conn.cursor()
      self.cur.execute(self.sql_create_table_firsttime)
      self.conn.commit()
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

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

  def select_all(self):
    try:
      self.get_connection()

      self.cur.execute("SELECT * FROM Flight")
      result = self.cur.fetchall()

      for row in result:
        print(row)

    except Exception as e:
      print(e)

    finally:
      self.conn.close()

      # think how you could develop this method to show the records

  def search_data(self):
    try:
      self.get_connection()
      flightID = int(input("Enter FlightNo: "))
      self.cur.execute(self.sql_search, tuple(str(flightID)))
      result = self.cur.fetchone()
      if type(result) == type(tuple()):
        for index, detail in enumerate(result):
          if index == 0:
            print("Flight ID: " + str(detail))
          elif index == 1:
            print("Flight Origin: " + detail)
          elif index == 2:
            print("Flight Destination: " + detail)
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

      # Update statement

      if result.rowcount != 0:
        print(str(result.rowcount) + "Row(s) affected.")
      else:
        print("Cannot find this record in the database")

    except Exception as e:
      print(e)
    finally:
      self.conn.close()


# Define Delete_data method to delete data from the table. The user will need to input the flight id to delete the corrosponding record.

  def delete_data(self):
    try:
      self.get_connection()

      if result.rowcount != 0:
        print(str(result.rowcount) + "Row(s) affected.")
      else:
        print("Cannot find this record in the database")

    except Exception as e:
      print(e)
    finally:
      self.conn.close()


class FlightInfo:

  def __init__(self):
    self.flightID = 0
    self.flightOrigin = ''
    self.flightDestination = ''
    self.status = ''

  def set_flight_id(self, flightID):
    self.flightID = flightID

  def set_flight_origin(self, flightOrigin):
    self.flight_origin = flightOrigin

  def set_flight_destination(self, flightDestination):
    self.flight_destination = flightDestination

  def set_status(self, status):
    self.status = status

  def get_flight_id(self):
    return self.flightID

  def get_flight_origin(self):
    return self.flightOrigin

  def get_flight_destination(self):
    return self.flightDestination

  def get_status(self):
    return self.status

  def __str__(self):
    return str(
      self.flightID
    ) + "\n" + self.flightOrigin + "\n" + self.flightDestination + "\n" + str(
      self.status)


# The main function will parse arguments.
# These argument will be definded by the users on the console.
# The user will select a choice from the menu to interact with the database.

while True:
  print("\n Menu:")
  print("**********")
  print(" 1. Create table FlightInfo")
  print(" 2. Insert data into FlightInfo")
  print(" 3. View all flights")
  print(" 4. Search a flight")
  print(" 5. Update data some records")
  print(" 6. Delete data some records")
  print(" 7. Exit\n")

  __choose_menu = int(input("Enter your choice: "))
  db_ops = DBOperations()
  if __choose_menu == 1:
    db_ops.create_table()
  elif __choose_menu == 2:
    db_ops.insert_data()
  elif __choose_menu == 3:
    db_ops.select_all()
  elif __choose_menu == 4:
    db_ops.search_data()
  elif __choose_menu == 5:
    db_ops.update_data()
  elif __choose_menu == 6:
    db_ops.delete_data()
  elif __choose_menu == 7:
    exit(0)
  else:
    print("Invalid Choice")
