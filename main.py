import tkinter as tk
from tkinter import messagebox
import sqlite3

# Initialize the main window
root = tk.Tk()
root.title("Hotel Booking System")
root.geometry("600x400")
root.config(bg="red")  # Set background color (e.g., light gray)

# Database connection setup (as explained previously)
conn = sqlite3.connect('hotel_booking.db')
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS reservations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT NOT NULL,
    room_type TEXT NOT NULL,
    days INTEGER NOT NULL
)
''')
conn.commit()

# Room reservation function
def room_reservation():
    res_window = tk.Toplevel(root)
    res_window.title("Room Reservation")
    res_window.geometry("400x300")
    res_window.config(bg="blue")  # Change background color (e.g., light blue)

    tk.Label(res_window, text="Customer Name", bg="#e6f2ff").pack(pady=5)
    customer_name_entry = tk.Entry(res_window)
    customer_name_entry.pack(pady=5)

    tk.Label(res_window, text="Room Type", bg="#e6f2ff").pack(pady=5)
    room_type_entry = tk.Entry(res_window)
    room_type_entry.pack(pady=5)

    tk.Label(res_window, text="Number of Days", bg="#e6f2ff").pack(pady=5)
    days_entry = tk.Entry(res_window)
    days_entry.pack(pady=5)

    def confirm_reservation():
        customer_name = customer_name_entry.get()
        room_type = room_type_entry.get()
        days = days_entry.get()

        if customer_name and room_type and days.isdigit():
            cursor.execute('INSERT INTO reservations (customer_name, room_type, days) VALUES (?, ?, ?)',
                           (customer_name, room_type, int(days)))
            conn.commit()
            
            messagebox.showinfo("Reservation Confirmed", f"Room reserved for {customer_name} for {days} days.")
            res_window.destroy()
        else:
            messagebox.showerror("Input Error", "Please enter valid details.")

    tk.Button(res_window, text="Reserve", command=confirm_reservation).pack(pady=20)

# Functions for Check-In, Check-Out, and Billing (with customized background color)
def check_in():
    check_in_window = tk.Toplevel(root)
    check_in_window.title("Check-In")
    check_in_window.geometry("400x300")
    check_in_window.config(bg="green")  # Set background color

    tk.Label(check_in_window, text="Customer Name", bg="#e6f2ff").pack(pady=5)
    customer_name_entry = tk.Entry(check_in_window)
    customer_name_entry.pack(pady=5)

    def confirm_check_in():
        customer_name = customer_name_entry.get()
        messagebox.showinfo("Check-In Successful", f"{customer_name} has been checked in.")
        check_in_window.destroy()

    tk.Button(check_in_window, text="Check In", command=confirm_check_in).pack(pady=20)

def check_out():
    check_out_window = tk.Toplevel(root)
    check_out_window.title("Check-Out")
    check_out_window.geometry("400x300")
    check_out_window.config(bg="yellow")  # Set background color

    tk.Label(check_out_window, text="Customer Name", bg="#e6f2ff").pack(pady=5)
    customer_name_entry = tk.Entry(check_out_window)
    customer_name_entry.pack(pady=5)

    def confirm_check_out():
        customer_name = customer_name_entry.get()
        messagebox.showinfo("Check-Out Successful", f"{customer_name} has been checked out.")
        check_out_window.destroy()

    tk.Button(check_out_window, text="Check Out", command=confirm_check_out).pack(pady=20)

def billing():
    billing_window = tk.Toplevel(root)
    billing_window.title("Billing")
    billing_window.geometry("400x300")
    billing_window.config(bg="pink")  # Set background color

    tk.Label(billing_window, text="Customer Name", bg="pink").pack(pady=5)
    customer_name_entry = tk.Entry(billing_window)
    customer_name_entry.pack(pady=5)

    tk.Label(billing_window, text="Room Rate (per day)", bg="pink").pack(pady=5)
    room_rate_entry = tk.Entry(billing_window)
    room_rate_entry.pack(pady=5)

    tk.Label(billing_window, text="Number of Days", bg="pink").pack(pady=5)
    days_entry = tk.Entry(billing_window)
    days_entry.pack(pady=5)

    def calculate_bill():
        try:
            customer_name = customer_name_entry.get()
            room_rate = float(room_rate_entry.get())
            days = int(days_entry.get())
            total_bill = room_rate * days
            messagebox.showinfo("Billing", f"Total bill for {customer_name} is {total_bill} Rs.")
            billing_window.destroy()
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for rate and days.")

    tk.Button(billing_window, text="Calculate Bill", command=calculate_bill).pack(pady=20)

# Main menu buttons with customized background color
tk.Button(root, text="Room Reservation", command=room_reservation, bg="blue").pack(pady=10)
tk.Button(root, text="Check-In", command=check_in, bg="green").pack(pady=10)
tk.Button(root, text="Check-Out", command=check_out, bg="yellow").pack(pady=10)
tk.Button(root, text="Billing", command=billing, bg="pink").pack(pady=10)

# Run the main loop
root.mainloop()

# Close the database connection when the application is closed
conn.close()
