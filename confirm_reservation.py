import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('hotel_booking.db')
cursor = conn.cursor()

# Create tables if not exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS reservations (
    id INTEGER PRIMARY KEY,
    customer_name TEXT,
    room_type TEXT,
    days INTEGER
)
''')
conn.commit()

def confirm_reservation():
    customer_name = customer_name_entry.get()
    room_type = room_type_entry.get()
    days = int(days_entry.get())
    
    # Insert into database
    cursor.execute('INSERT INTO reservations (customer_name, room_type, days) VALUES (?, ?, ?)',
                   (customer_name, room_type, days))
    conn.commit()
    
    messagebox.showinfo("Reservation Confirmed", f"Room reserved for {customer_name} for {days} days.")
    res_window.destroy()