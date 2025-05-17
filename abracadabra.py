import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("MultiTool")
root.geometry("400x520")

# === Tabs ===
tabs = ctk.CTkTabview(root, width=380, height=500)
tabs.pack(padx=10, pady=10)

tabs.add("Calculator")
tabs.add("Currency")
tabs.add("Speed")

entered_value = ""

def calculate():
    global entered_value
    try:
        result = eval(entered_value)
        entered_value = str(result)
        calc_entry.delete(0, 'end')
        calc_entry.insert(0, entered_value)
    except:
        entered_value = "Error"
        calc_entry.delete(0, 'end')
        calc_entry.insert(0, entered_value)

def button_click(value):
    global entered_value
    if value == "=":
        calculate()
    else:
        entered_value += value
        calc_entry.delete(0, 'end')
        calc_entry.insert(0, entered_value)

calc_entry = ctk.CTkEntry(tabs.tab("Calculator"), width=300, height=50, font=('Arial', 20), justify='right', fg_color="lightgray", text_color="black")
calc_entry.grid(row=0, column=0, columnspan=4, padx=20, pady=20)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, column) in buttons:
    button = ctk.CTkButton(
        tabs.tab("Calculator"), text=text, width=70, height=70, font=('Arial', 20),
        fg_color="orange" if text in ['/', '*', '-', '+', '='] else "black",
        hover_color="darkorange" if text in ['/', '*', '-', '+', '='] else "gray",
        text_color="white", border_width=2, corner_radius=10,
        command=lambda t=text: button_click(t)
    )
    button.grid(row=row, column=column, padx=5, pady=5)

# === Currency Tab ===
currency_tab = tabs.tab("Currency")

currency_entry = ctk.CTkEntry(currency_tab, placeholder_text="Enter amount", width=300, height=50, font=("Arial", 18), justify="right", fg_color="lightgray", text_color="black")
currency_entry.pack(pady=20)

currency_from = ctk.CTkOptionMenu(currency_tab, values=["USD", "EUR", "UAH"], width=130, height=40, font=("Arial", 14))
currency_from.pack(pady=5)

currency_to = ctk.CTkOptionMenu(currency_tab, values=["USD", "EUR", "UAH"], width=130, height=40, font=("Arial", 14))
currency_to.pack(pady=5)

def convert_currency():
    rates = {
        "USD": {"USD": 1, "EUR": 0.92, "UAH": 39},
        "EUR": {"USD": 1.09, "EUR": 1, "UAH": 42},
        "UAH": {"USD": 0.026, "EUR": 0.024, "UAH": 1},
    }
    try:
        amount = float(currency_entry.get())
        from_curr = currency_from.get()
        to_curr = currency_to.get()
        result = amount * rates[from_curr][to_curr]
        currency_result.configure(text=f"Result: {result:.2f} {to_curr}")
    except:
        currency_result.configure(text="Invalid input")

convert_button = ctk.CTkButton(currency_tab, text="Convert", width=300, height=60, font=("Arial", 20),
                               fg_color="black", hover_color="gray", text_color="white",
                               corner_radius=10, command=convert_currency)
convert_button.pack(pady=10)

currency_result = ctk.CTkLabel(currency_tab, text="Result:", font=("Arial", 18))
currency_result.pack(pady=10)

# === Speed Tab ===
speed_tab = tabs.tab("Speed")

speed_entry = ctk.CTkEntry(speed_tab, placeholder_text="Enter speed", width=300, height=50, font=("Arial", 18), justify="right", fg_color="lightgray", text_color="black")
speed_entry.pack(pady=20)

speed_mode = ctk.CTkOptionMenu(speed_tab, values=["km/h to m/s", "m/s to km/h"], width=200, height=40, font=("Arial", 14))
speed_mode.pack(pady=5)

def convert_speed():
    try:
        value = float(speed_entry.get())
        mode = speed_mode.get()
        if mode == "km/h to m/s":
            converted = value / 3.6
        else:
            converted = value * 3.6
        speed_result.configure(text=f"Result: {converted:.2f}")
    except:
        speed_result.configure(text="Invalid input")

speed_button = ctk.CTkButton(speed_tab, text="Convert", width=300, height=60, font=("Arial", 20),
                             fg_color="black", hover_color="gray", text_color="white",
                             corner_radius=10, command=convert_speed)
speed_button.pack(pady=10)

speed_result = ctk.CTkLabel(speed_tab, text="Result:", font=("Arial", 18))
speed_result.pack(pady=10)

root.mainloop()

