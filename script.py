import tkinter as tk
from tkinter import ttk
from datetime import datetime
import pytz

class TimezoneConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Timezone Converter")

        # Set default time and format
        self.current_time = tk.StringVar()
        self.current_time.set(self.get_current_time())

        # Create labels
        self.label_timezone_from = ttk.Label(root, text="From Timezone:")
        self.label_timezone_to = ttk.Label(root, text="To Timezone:")
        self.label_time = ttk.Label(root, text="Current Time:")

        # Create dropdowns
        self.timezone_from_var = tk.StringVar()
        self.timezone_to_var = tk.StringVar()
        self.dropdown_timezone_from = ttk.Combobox(
            root, textvariable=self.timezone_from_var)
        self.dropdown_timezone_to = ttk.Combobox(
            root, textvariable=self.timezone_to_var)

        # Populate timezones
        self.timezones = sorted(pytz.all_timezones)
        self.dropdown_timezone_from['values'] = self.timezones
        self.dropdown_timezone_to['values'] = self.timezones

        # Set default timezone values
        self.dropdown_timezone_from.set('UTC')
        self.dropdown_timezone_to.set('UTC')

        # Create entry for current time
        self.entry_current_time = ttk.Entry(
            root, textvariable=self.current_time, state='readonly')

        # Create 12/24 hour clock dropdown
        self.clock_format_var = tk.StringVar()
        self.dropdown_clock_format = ttk.Combobox(
            root, textvariable=self.clock_format_var)
        self.dropdown_clock_format['values'] = ['24-hour', '12-hour']
        self.dropdown_clock_format.set('24-hour')

        # Create convert button
        self.convert_button = ttk.Button(
            root, text="Convert", command=self.convert_time)

        # Grid layout
        self.label_timezone_from.grid(row=0, column=0, padx=10, pady=10, sticky='e')
        self.dropdown_timezone_from.grid(row=0, column=1, padx=10, pady=10)
        self.label_timezone_to.grid(row=1, column=0, padx=10, pady=10, sticky='e')
        self.dropdown_timezone_to.grid(row=1, column=1, padx=10, pady=10)
        self.label_time.grid(row=2, column=0, padx=10, pady=10, sticky='e')
        self.entry_current_time.grid(row=2, column=1, padx=10, pady=10)
        self.dropdown_clock_format.grid(row=3, column=0, padx=10, pady=10, columnspan=2)
        self.convert_button.grid(row=4, column=0, columnspan=2, pady=10)

    def get_current_time(self):
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return current_time

    def convert_time(self):
        try:
            from_timezone = pytz.timezone(self.timezone_from_var.get())
            to_timezone = pytz.timezone(self.timezone_to_var.get())

            current_time = datetime.now(from_timezone)
            converted_time = current_time.astimezone(to_timezone)

            if self.clock_format_var.get() == '12-hour':
                converted_time_str = converted_time.strftime('%Y-%m-%d %I:%M:%S %p')
            else:
                converted_time_str = converted_time.strftime('%Y-%m-%d %H:%M:%S')

            self.current_time.set(converted_time_str)

        except Exception as e:
            self.current_time.set("Error converting time")

if __name__ == "__main__":
    root = tk.Tk()
    app = TimezoneConverterApp(root)
    root.mainloop()
