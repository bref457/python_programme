import tkinter as tk
from tkinter import ttk


def calculate_bmi():
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    bmi = weight / (height * height)
    bmi_label.config(text=f"Dein BMI ist: {bmi:.2f}")

    if bmi < 18.5:
        result_label.config(text="Du bist untergewichtig")
    elif 18.5 <= bmi <= 24.9:
        result_label.config(text="Du hast Normalgewicht")
    elif 25 <= bmi <= 29.9:
        result_label.config(text="Du bist übergewichtig")
    elif 30 <= bmi <= 34.9:
        result_label.config(text="Du hast Adipositas (Grad 1)")
    elif 35 <= bmi <= 39.9:
        result_label.config(text="Du hast Adipositas (Grad 2)")
    else:
        result_label.config(text="Du hast Adipositas (Grad 3)")


# GUI erstellen
root = tk.Tk()
root.title("BMI Rechner")
root.config(bg="grey")
root.geometry("450x200")

# Widgets hinzufügen
weight_label = ttk.Label(root, text="Körpergewicht in kg:", font=("Arial", 14))
weight_label.grid(row=0, column=0, padx=10, pady=10)
weight_entry = ttk.Entry(root, font=("Arial", 14))
weight_entry.grid(row=0, column=1, padx=10, pady=10)

height_label = ttk.Label(root, text="Körpergrösse in m:", font=("Arial", 14))
height_label.grid(row=1, column=0, padx=10, pady=10)
height_entry = ttk.Entry(root, font=("Arial", 14))
height_entry.grid(row=1, column=1, padx=10, pady=10)

calculate_button = ttk.Button(root, text="BMI berechnen", command=calculate_bmi)
calculate_button.grid(row=2, columnspan=2)

bmi_label = ttk.Label(root, text="", font=("Arial", 14))
bmi_label.grid(row=3, columnspan=2)

result_label = ttk.Label(root, text="", font=("Arial", 14))
result_label.grid(row=4, columnspan=2)

# Hauptloop
root.mainloop()