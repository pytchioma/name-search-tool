import tkinter as tk

#create window
root = tk.Tk()
root.title("Smart Sort App")
root.geometry("400x300")

#Instruction label
label = tk.Label(root, text="Enter values seperated by commas:")
label.pack()


#Input box
entry = tk.Entry(root, width=40)
entry.pack()

def sort_values():
    print("button clicked") #temporary tests
    button = tk.Button (root, text="Sort", command=sort_values)
    button.pack()

root.mainloop()