from tkinter import *

def miles_to_km():
 km = km_input.get()
 miles = float(km)*0.6214
 mile_result.config(text=f"{miles}")

window = Tk()
window.title("Miles to Kilometre Converter")
window.configure(padx=20, pady=20)

km_input = Entry(width=5)
km_input.grid(column=1, row=0)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0,row=1)

mile_result = Label(text="0")
mile_result.grid(column=1, row=1)

mile_label = Label(text="Miles")
mile_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command = miles_to_km)
calculate_button.grid(column=1,row=2)

window.mainloop()

