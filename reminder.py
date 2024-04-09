import tkinter as tk
from datetime import datetime, timezone
import threading

class Clock:
    def __init__(self, master):
        self.master = master
        self.time = tk.StringVar()
        self.reminder_time = None
        self.reminder_set = False

        self.label = tk.Label(master, textvariable=self.time, font=('Arial', 24))
        self.label.pack()

        self.set_reminder_button = tk.Button(master, text="Set Reminder", command=self.set_reminder)
        self.set_reminder_button.pack()

        self.update_time()

    def update_time(self):
        self.time.set(datetime.now(timezone.utc).strftime('%H:%M:%S'))
        self.master.after(1000, self.update_time)

    def set_reminder(self):
        if not self.reminder_set:
            self.reminder_time = input("Enter reminder time (HH:MM:SS): ")
            try:
                self.reminder_time = datetime.strptime(self.reminder_time, '%H:%M:%S').replace(tzinfo=timezone.utc)
                self.reminder_set = True
                threading.Thread(target=self.check_reminder).start()
            except ValueError:
                print("Invalid time format. Please enter time in HH:MM:SS format.")
        else:
            print("Reminder already set.")

    def check_reminder(self):
        while True:
            if datetime.now(timezone.utc) >= self.reminder_time:
                print("Reminder: Time's up!")
                self.reminder_set = False
                break
            self.master.after(1000)

root = tk.Tk()
clock = Clock(root)
root.mainloop()