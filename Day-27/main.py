from tkinter import *
KILOMETER = 1.60934
window = Tk()

# Main Window
window.title("Miles to Kilometer")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

def mile_to_km():
    miles =float(user_input.get())
    km = round(miles * KILOMETER)
    km_result_label.config(text=km)


# input area 
user_input = Entry(width=10)
user_input.grid(column=1, row=0)

# Miles
miles = Label(text="Miles", font=("Courier M",10, "bold"))
miles.config(padx=10, pady=10)
miles.grid(column=2, row=0)

# text area 
show_up_text = Label(text="Is Equal to",font=("Courier M",10, "bold"))
show_up_text.config(padx=10, pady=10)
show_up_text.grid(column=0,row=1)
# Value Area 
km_result_label = Label(text="0",font=("Courier M",10, "bold"))
km_result_label.grid(column=1, row=1)

km_label= Label(text="Km", font=("Courier M",10, "bold"))
km_label.grid(column=2, row=1)

# Calculate Button
calculate = Button(text="Calculate",command=mile_to_km)
calculate.config(font=("Courier M",10, "bold"))
calculate.grid(column=1, row=2)




window.mainloop()