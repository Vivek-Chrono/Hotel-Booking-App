def billing():
    billing_window = tk.Toplevel(root)
    billing_window.title("Billing")
    billing_window.geometry("400x300")

    tk.Label(billing_window, text="Customer Name").pack(pady=5)
    customer_name_entry = tk.Entry(billing_window)
    customer_name_entry.pack(pady=5)

    tk.Label(billing_window, text="Room Rate (per day)").pack(pady=5)
    room_rate_entry = tk.Entry(billing_window)
    room_rate_entry.pack(pady=5)

    tk.Label(billing_window, text="Number of Days").pack(pady=5)
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