import tkinter as tk

rates = {
    "EUR": 1.0,
    "USD": 1.1,
    "JPY": 160.0,
    "SEK": 11.2
}


"test"
def convert():
    try:
        amount = float(entry.get())
        result = amount * rates[var.get()]
        result_label.config(text=f"Result: {result:.2f}")
    except ValueError:
        result_label.config(text="Please enter a number")

root = tk.Tk()
root.title("Currency Converter")
root.geometry("700x500")
root.resizable(False, False)

# Fonts
title_font = ("Arial", 20, "bold")
label_font = ("Arial", 14)
button_font = ("Arial", 14)
entry_font = ("Arial", 14)

# Title
tk.Label(root, text="Currency Converter", font=title_font).pack(pady=20)

# Entry
tk.Label(root, text="Amount in Euro:", font=label_font).pack()
entry = tk.Entry(root, font=entry_font, width=20, justify="center")
entry.pack(pady=10)

# Currency selection
var = tk.StringVar(value="USD")
radio_frame = tk.Frame(root)
radio_frame.pack(pady=10)

for currency in rates:
    tk.Radiobutton(
        radio_frame,
        text=currency,
        variable=var,
        value=currency,
        font=label_font
    ).pack(anchor="w")

# Convert button
tk.Button(
    root,
    text="Convert",
    command=convert,
    font=button_font,
    width=15
).pack(pady=20)

# Result
result_label = tk.Label(root, text="Result:", font=label_font)
result_label.pack(pady=10)

root.mainloop()
