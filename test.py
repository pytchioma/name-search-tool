import tkinter
print("Tkinter is working")


import tkinter as tk


# Create window
root = tk.Tk()
root.title = ("SpendWise")
root.geometry = ("400x350")
root.config = ("bg = blue")


root.mainloop()

# Step 4 Store labels so we can update them later 
total_labels = {}
percent_labels = {}

# Create Input Section
input_frame = tk.Frame(root, bg="Light Grey")
input_frame.pack(pady=10)

amount_entry = tk.Entry(input_frame, width=15)
amount_entry.grid(row=0, column=0, padx=5)
def add_expense():
    try: 
        amount = float(amount_entry.get())
    except ValueError:
        return

amount_entry = tk.Entry(input_frame, width=15)
amount_entry.grid(row=0, column=0, padx=5)


    # Draw Outline 
    margin = 20
    canvas.create_oval(margin, margin,
                                    canvas_size - margin,
                                    canvas_size - margin,
                                    outline = "Light Grey",
                                    width=3)


# ======== DASHBOARD ========
dashboard_frame = tk.Frame(root, bg="Light blue")

 # -------- Functions --------

category_var = tk.StringVar()
category_dropdown = ttk.Combobox(input_frame, textvariable=category_var, values=categories, state="readonly")
category_dropdown.grid(row=0, column=1, padx=5)
category_dropdown.current(0)

add_button = tk.Button (input_frame, text="Add", command=add_expense)
add_button.grid(row=0, column=2, padx=5)



#Draw The Container
    canvas.create_rectangle(40, 40, canvas_size-40, canvas_size-40, outline="Light grey", width=8, fill="Dark grey")

     
     # categories
    categories = ["Groceries", "Dining Out", "Medical", "Personal Care","Transportation","Utilities"]
    import math
    center_x = canvas_size / 2
    center_y = canvas_size / 2
    radius = (canvas_size / 2) - 80

    for i, in categories in enumerate(categories):
        angle = 2 *math.pi*i/len(categories)
    

    btn = tk.Button(root,
                        text = categories,
                        font=("Georgia", 10,),
                        bg="Light grey",
                        fg="white")
        canvas.create_window(x, y, window=btn)


if name == user_input:
           print("found!")

time.sleep(10)