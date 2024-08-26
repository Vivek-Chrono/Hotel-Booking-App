def check_in():
    check_in_window = tk.Toplevel(root)
    check_in_window.title("Check-In")
    check_in_window.geometry("400x300")

    tk.Label(check_in_window, text="Customer Name").pack(pady=5)
    customer_name_entry = tk.Entry(check_in_window)
    customer_name_entry.pack(pady=5)

    def confirm_check_in():
        customer_name = customer_name_entry.get()
        messagebox.showinfo("Check-In Successful", f"{customer_name} has been checked in.")
        check_in_window.destroy()

    tk.Button(check_in_window, text="Check In", command=confirm_check_in).pack(pady=20)

# Check-Out window
def check_out():
    check_out_window = tk.Toplevel(root)
    check_out_window.title("Check-Out")
    check_out_window.geometry("400x300")

    tk.Label(check_out_window, text="Customer Name").pack(pady=5)
    customer_name_entry = tk.Entry(check_out_window)
    customer_name_entry.pack(pady=5)

    def confirm_check_out():
        customer_name = customer_name_entry.get()
        messagebox.showinfo("Check-Out Successful", f"{customer_name} has been checked out.")
        check_out_window.destroy()

    tk.Button(check_out_window, text="Check Out", command=confirm_check_out).pack(pady=20)