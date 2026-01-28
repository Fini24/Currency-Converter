import tkinter as tk

rates = {
    "EUR": 1.0,
    "USD": 1.1,
    "JPY": 160.0,
    "SEK": 11.2
}

languages = {
    "EN": {
        "title": "Currency Converter",
        "amount": "Amount in Euro:",
        "convert": "Convert",
        "result": "Result:",
        "switch": "Switch Language",
        "error": "Please enter a number"
    },
    "DE": {
        "title": "Währungsrechner",
        "amount": "Betrag in Euro:",
        "convert": "Umrechnen",
        "result": "Ergebnis:",
        "switch": "Sprache wechseln",
        "error": "Bitte eine Zahl eingeben"
    }
}

current_lang = "EN"

def convert():
    try:
        amount = float(entry.get())
        result = amount * rates[var.get()]
        result_label.config(
            text=f"{languages[current_lang]['result']} {result:.2f}"
        )
    except ValueError:
        result_label.config(text=languages[current_lang]["error"])

def switch_language():
    global current_lang
    current_lang = "DE" if current_lang == "EN" else "EN"

    root.title(languages[current_lang]["title"])
    amount_label.config(text=languages[current_lang]["amount"])
    convert_btn.config(text=languages[current_lang]["convert"])
    switch_btn.config(text=languages[current_lang]["switch"])
    result_label.config(text=languages[current_lang]["result"])

root = tk.Tk()
root.geometry("700x500")
root.resizable(False, False)
root.title(languages[current_lang]["title"])

# Fonts
title_font = ("Arial", 20, "bold")
label_font = ("Arial", 14)
button_font = ("Arial", 14)

# Title
tk.Label(root, text=languages[current_lang]["title"], font=title_font).pack(pady=20)

# Amount
amount_label = tk.Label(root, text=languages[current_lang]["amount"], font=label_font)
amount_label.pack()
entry = tk.Entry(root, font=label_font, width=20, justify="center")
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

# Buttons
convert_btn = tk.Button(
    root,
    text=languages[current_lang]["convert"],
    font=button_font,
    width=15,
    command=convert
)
convert_btn.pack(pady=10)

switch_btn = tk.Button(
    root,
    text=languages[current_lang]["switch"],
    font=button_font,
    width=20,
    command=switch_language
)
switch_btn.pack(pady=10)

# Result
result_label = tk.Label(root, text=languages[current_lang]["result"], font=label_font)
result_label.pack(pady=20)

root.mainloop()
