import tkinter as tk
from tkinter import ttk
 
print("CHIOMA")
# Step 1 Create window
root = tk.Tk()
root.title("SpendWise")
root.geometry("500x400")
root.configure(bg="Dark Grey")

# ========== Header ==========


welcome_text = "Welcome To SpendWise!"
displayed_text = ""
typing_running = True # Control Flag (flag variable)
label1 = tk.Label(root, text = "", font = ("Georgia", 30) , fg = "white",  bg = "Dark Grey")
label1.place(relx=0.5, rely=0.5, anchor="center")

# ====== TYPING EFFECT ======
def typing_effect(index=0):
    global displayed_text, typing_running
    if not typing_running:
        return
    if index < len(welcome_text):
        displayed_text += welcome_text[index]
        label1.config(text=displayed_text)

        if index == 0:
            label1.bind("<Button-1>", label_click)


        root.after(100, typing_effect, index + 1)


    
# Step 2  ====== DATA STRUCTURE ======

# ======== CREATE DASHBOARD =========
def create_dashboard():
    canvas_size = 250
    canvas = tk.Canvas(root,
                       width=445,
                       height=150,
                       bg="Light blue",
                       highlightthickness=0)
    canvas.place (relx=0.9, rely=0.3, anchor = "e")
    

     # categories
    categories = ["Groceries", "Dining Out", "Medical", "Personal Care","Transportation","Utilities"]
    
        # ======== CLICK EFFECT ========
def label_click(event):
    global typing_running
    typing_running = False    #Stop Typing Loop
    label1.destroy()          #Remove Text
    create_dashboard()

typing_effect()




# Run the application
root.mainloop()


