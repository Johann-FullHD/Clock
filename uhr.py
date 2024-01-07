import tkinter as tk
from time import strftime

def aktualisiere_uhr():
    aktuelle_zeit = strftime('%H:%M:%S')
    uhr_label.config(text=aktuelle_zeit)
    uhr_label.after(1000, aktualisiere_uhr)
fenster = tk.Tk()
fenster.title("Uhr")
uhr_label = tk.Label(fenster, font=('calibri', 40, 'bold'), background='black', foreground='white')
uhr_label.pack(anchor='center')
aktualisiere_uhr()

fenster.minsize(195, 70)
fenster.maxsize(195, 70)
fenster.mainloop()