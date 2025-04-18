import tkinter as tk

root = tk.Tk()
root.title("BMI calculator")
root.geometry("350x200")

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if height > 3:
            height /= 100
        
        if weight < 0 or height < 0:
            return result_label.config(text="error: Weight and height cannot be negative numbers.")
        
        return result_label.config(text=f"Your BMI is: {(weight / (height * height)):.2f}")
    except ValueError:
        result_label.config(text="error: You entered incorrect data, please enter both numbers.")


# 0 row
weight_label = tk.Label(root, text="Weight (kg):")
weight_label.grid(row=0, column=0, padx=10, pady=10)

weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1, padx=10, pady=10)

# 1 row
height_label = tk.Label(root, text="Height (m):")
height_label.grid(row=1, column=0, padx=10, pady=10)

height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1, padx=10, pady=10)

# 2 row
accept_button = tk.Button(root, text="Accept", command=calculate_bmi)
accept_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# 3 row
result_label = tk.Label(root, text="Your BMI will be displayed here.")
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()