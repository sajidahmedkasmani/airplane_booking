# import sqlite3

# conn = sqlite3.connect("aeroplane.db")

# cursor = conn.cursor()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS flights(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     seat_no TEXT UNIQUE,
#     is_booked INTEGER DEFAULT 0
# )
# """)

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS bookings(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     passenger_name TEXT,
#     seat_no TEXT
# )
# """)



# conn.commit()
# conn.close()

# print("Database Created Successfully")

import sqlite3

conn = sqlite3.connect("aeroplane.db")

cursor = conn.cursor()

# seats = [
#     ("A1",),
#     ("A2",),
#     ("A3",),
#     ("A4",),
#     ("B1",),
#     ("B2",),
#     ("B3",),
#     ("B4",)
# ]

# cursor.executemany("""
# INSERT INTO flights(seat_no)
# VALUES(?)
# """, seats)

# conn.commit()
# conn.close()

# print("Seats Added")




# cursor.execute("""
# CREATE TABLE IF NOT EXISTS bookings(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     passenger_name TEXT,
#     seat_no TEXT
# )
# """)


# cursor.execute("""
# ALTER TABLE bookings
# ADD COLUMN cnic VARCHAR(255),
# ADD COLUMN dob DATE,
# ADD COLUMN phone VARCHAR(255),
# ADD COLUMN email VARCHAR(255),
# ADD COLUMN cabin ENUM('economy', 'business', 'first_class') NOT NULL,
# ADD COLUMN meal ENUM('standard', 'halal', 'vegetarian', 'no') NOT NULL;
# """)

# cursor.execute("ALTER TABLE bookings ADD COLUMN cnic TEXT;")
# cursor.execute("ALTER TABLE bookings ADD COLUMN dob DATE;")
# cursor.execute("ALTER TABLE bookings ADD COLUMN phone TEXT;")
# cursor.execute("ALTER TABLE bookings ADD COLUMN email TEXT;")

# cursor.execute("""
# ALTER TABLE bookings
# ADD COLUMN cabin TEXT
# CHECK(cabin IN ('economy', 'business', 'first_class'));
# """)

cursor.execute("""
ALTER TABLE bookings
ADD COLUMN meal TEXT
CHECK(meal IN ('standard', 'halal', 'vegetarian', 'no'));
""")
