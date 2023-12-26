import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")


window.minsize(300,300)
miles_input = tkinter.Entry(width=10)
miles_input.insert(tkinter.END, string="0")
miles_input.grid(row=0,column=1)
miles_label = tkinter.Label(text="Miles")
miles_label.grid(row=0,column=2)
is_equal_label = tkinter.Label(text="is equal to")
is_equal_label.grid(row=1,column=0)
km_label = tkinter.Label(text='0')
km_label.grid(row=1,column=1)
km_label2 = tkinter.Label(text='km')
km_label2.grid(row=1,column=2)
def convert():
    miles = float(miles_input.get())
    km = miles * 1.6
    km_label.config(text=km)
button = tkinter.Button(text='Convert',command=convert)
button.grid(row=2,column=1)

window.mainloop()

