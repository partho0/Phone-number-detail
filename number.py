import tkinter as tk
from tkinter import messagebox
import phonenumbers
from phonenumbers import timezone, geocoder, carrier

def get_phone_info():
    input_number = phone_number_entry.get()

    try:
        parsed_number = phonenumbers.parse(input_number)
        time_zones = timezone.time_zones_for_number(parsed_number)
        carrier_name = carrier.name_for_number(parsed_number, "en")
        region = geocoder.description_for_number(parsed_number, "en")

        info_text = f"Phone Number: {parsed_number}\n"
        info_text += f"Time Zones: {', '.join(time_zones)}\n"
        info_text += f"Carrier: {carrier_name}\n"
        info_text += f"Region: {region}"

        result_text.config(text=info_text)

    except phonenumbers.phonenumberutil.NumberFormatError:
        messagebox.showerror("Error", "Invalid phone number format")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Phone Number Info")

# Create and set up the GUI components
phone_label = tk.Label(root, text="Enter your phone number (with country code):")
phone_number_entry = tk.Entry(root)
get_info_button = tk.Button(root, text="Get Info", command=get_phone_info)
result_text = tk.Label(root, text="", justify="left")

# Place the components on the window
phone_label.pack()
phone_number_entry.pack()
get_info_button.pack()
result_text.pack()

# Start the main loop
root.mainloop()
