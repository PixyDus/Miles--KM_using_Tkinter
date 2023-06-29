from tkinter import *

# Title
window = Tk()
window.title("Miles -> Kilometer")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
label = Label()
label.config(text="Miles", font=("Arial", 22), padx=20, pady=20)
label.grid(column=3, row=0)

# Entry
entry = Entry()
print(entry.get())
entry.config(width=7)
entry.grid(column=2, row=0)


def button_response():
    miles = float(entry.get())  # Retrieve the value from the entry and convert it to float
    kilometers = round(miles * 1.609344)  # Convert the miles to kilometers
    label_output.config(text=kilometers)

# Label
label_is_equal_to = Label()
label_is_equal_to.config(text="Is equal to", font=("Arial", 22))
label_is_equal_to.grid(column=1, row=1)

# Label
label_output = Label()
label_output.config(text="0", font=("Arial", 22))
label_output.grid(column=2, row=1)

# Label
label_km = Label()
label_km.config(text="KM", font=("Arial", 22))
label_km.grid(column=3, row=1)

# Button
button = Button(text="Calculate", fg="white", bg="green", font=("Arial", 30), command=button_response)
button.config()
button.grid(column=2, row=2)

window.mainloop()
