# Hotel-Booking-App

#Code


import tkinter as tk
from tkinter import messagebox
import sqlite3

root = tk.Tk()
root.title("Hotel Booking System")
root.geometry("600x400")
root.config(bg="red")


conn = sqlite3.connect('hotel_booking.db')
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS reservations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT NOT NULL,
    room_type TEXT NOT NULL,
    days INTEGER NOT NULL
)
''')
conn.commit()

def room_reservation():
    res_window = tk.Toplevel(root)
    res_window.title("Room Reservation")
    res_window.geometry("400x300")
    res_window.config(bg="blue") 

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

def check_in():
    check_in_window = tk.Toplevel(root)
    check_in_window.title("Check-In")
    check_in_window.geometry("400x300")
    check_in_window.config(bg="green") 

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
    check_out_window.config(bg="yellow") 

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
    billing_window.config(bg="pink") 

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


tk.Button(root, text="Room Reservation", command=room_reservation, bg="blue").pack(pady=10)
tk.Button(root, text="Check-In", command=check_in, bg="green").pack(pady=10)
tk.Button(root, text="Check-Out", command=check_out, bg="yellow").pack(pady=10)
tk.Button(root, text="Billing", command=billing, bg="pink").pack(pady=10)


root.mainloop()


conn.close()

#output
![Screenshot 2024-08-26 233237](https://github.com/user-attachments/assets/75a08dc8-ea78-41be-917e-0822c9ed6a59)


![Screenshot 2024-08-26 233254](https://github.com/user-attachments/assets/2b803fc5-054f-4bfa-8f8c-1577334b690d)


![Screenshot 2024-08-26 233316](https://github.com/user-attachments/assets/ed230057-63c0-4d93-a1b6-ae65c306d3da)


![Screenshot 2024-08-26 233339](https://github.com/user-attachments/assets/282ae780-71f2-4d95-9134-eb390f8a4b26)


![Screenshot 2024-08-26 233349](https://github.com/user-attachments/assets/41499468-b332-4bf0-9b4c-ce8beefd2008)






