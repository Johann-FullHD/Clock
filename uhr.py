###########################
##        Build by       ##
##     Johann Kramer     ##
##         2023          ##
###########################

import tkinter as tk
from time import strftime

def aktualisiere_uhr():
    aktuelle_zeit = strftime('%H:%M:%S') # Setzt das Anzeigenformat fest
    uhr_label.config(text=aktuelle_zeit)
    uhr_label.after(1000, aktualisiere_uhr) # Setzt die Zeit fest, nach wie vielen Milisekunden die Uhr aktualisiert wird
fenster = tk.Tk() # Erstellt Anzeigenfenster
fenster.title("Uhr") # Beschreibt den Fenstertitel
uhr_label = tk.Label(fenster, font=('calibri', 40, 'bold'), background='black', foreground='white') # Legt Design fest
uhr_label.pack(anchor='center')
aktualisiere_uhr()

fenster.minsize(195, 70) # Setzt Mindestgröße fest
fenster.maxsize(195, 70) # Setzt Maximalgröße fest
fenster.mainloop() # Führt den Mainloop aus
