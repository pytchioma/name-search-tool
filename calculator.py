import tkinter as tk

# Step 1 Create Window
root = tk.Tk()
root.title("SimpleCalculator")
root.geometry("340x300")
root.configure(bg="Dark grey")

display = tk.Entry(root, font=("Arial", 20), bd=10, relief="ridge",justify="right")
display.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

# Create Functions
def click(number):
    display.insert(tk.END, number)

def clear():
    display.delete(0, tk.END)

def calculate():
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, result)

# Create Buttons
tk.Button(root, text ="7", font=("Arial", 18), command=lambda: click("7")).grid(row=1, column=0)

tk.Button(root, text ="8",font=("Arial", 18), command=lambda: click("8")).grid(row=1, column=1)

tk.Button(root, text ="9", font=("Arial", 18), command=lambda: click("9")).grid(row=1, column=2)

tk.Button(root, text ="+", font=("Arial", 18), command=lambda: click("+")).grid(row=1, column=3)

tk.Button(root, text="4", font=("Arial", 18), command=lambda: click("4")).grid(row=2, column=0)

tk.Button(root, text="5", font=("Arial", 18), command=lambda: click("5")).grid(row=2, column=1)

tk.Button(root, text="6", font=("Arial", 18), command=lambda: click("6")).grid(row=2, column=2)

tk.Button(root, text="-", font=("Arial", 18), command=lambda: click("-")).grid(row=2,column=3)

tk.Button(root, text="1", font=("Arial", 18), command=lambda: click("1")).grid(row=3, column=0)

tk.Button(root, text="2", font=("Arial", 18), command=lambda: click("2")).grid(row=3, column=1)

tk.Button(root, text="3", font=("Arial", 18), command=lambda: click("3")).grid(row=3, column=2)

tk.Button(root, text="*", font=("Arial", 18), command=lambda: click("*")).grid(row=3, column=3)

tk.Button(root, text="C", font=("Arial", 18), command=clear).grid(row=4, column=0)

tk.Button(root, text="=", font=("Arial", 18), command=calculate).grid(row=4, column=1)

tk.Button(root, text="/", font=("Arial", 18), command=lambda: click ("/")).grid(row=4, column=2)

tk.Button(root, text=".", font=("Arial", 18), command=lambda: click (".")).grid(row=4, column=3)

root.mainloop()