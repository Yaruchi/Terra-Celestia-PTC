import tkinter as tk
from tkinter import ttk

# Planetary time configurations
planets = {
    "Ignis": {"months_in_year": 5, "rotation": 15},
    "Pyros": {"months_in_year": 8, "rotation": 19},
    "Eos": {"months_in_year": 12, "rotation": 24},
    "Astraea": {"months_in_year": 15, "rotation": 24},
    "Cryon": {"months_in_year": 20, "rotation": 34},
    "Glacius": {"months_in_year": 26, "rotation": 42}
}

def get_time_of_day(hour, rotation):
    """Determine the time of day based on planetary rotation."""
    phase_length = rotation / 6  # Divide the planetary day into 6 equal parts
    if 0 <= hour < phase_length:
        return "Midnight 🌌"
    elif phase_length <= hour < 2 * phase_length:
        return "Morning 🌅"
    elif 2 * phase_length <= hour < 3 * phase_length:
        return "Day ☀️"
    elif 3 * phase_length <= hour < 4 * phase_length:
        return "Afternoon 🌆"
    elif 4 * phase_length <= hour < 5 * phase_length:
        return "Evening 🌙"
    else:
        return "Night 🌑"

def convert_time():
    selected_planet = planet_var.get()
    base_planet = planets[selected_planet]

    # Retrieve input values
    base_years = int(year_entry.get() or 0)
    base_months = int(month_entry.get() or 0)
    base_days = int(day_entry.get() or 0)
    base_weeks = int(week_entry.get() or 0)
    base_hours = int(hour_entry.get() or 0)
    base_minutes = int(minute_entry.get() or 0)
    base_seconds = int(second_entry.get() or 0)

    # Convert input time to total seconds
    total_seconds = (base_seconds + base_minutes * 60 + base_hours * 3600 +
                     base_days * base_planet['rotation'] * 3600 +
                      base_weeks * 6 * base_planet['rotation'] * 3600 +  # Include weeks (6 days per week)
                     base_months * 30 * base_planet['rotation'] * 3600 +
                     base_years * base_planet['months_in_year'] * 30 * base_planet['rotation'] * 3600)

    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, f"Time on other planets (starting from {selected_planet}):\n\n")

    for planet, config in planets.items():
        total_planet_seconds = total_seconds
        total_planet_days = total_planet_seconds / (config['rotation'] * 3600)
        years = int(total_planet_days // (config['months_in_year'] * 30))
        remaining_days = total_planet_days % (config['months_in_year'] * 30)
        months = int(remaining_days // 30)
        remaining_days = int(remaining_days % 30)
        weeks = int(remaining_days // 6)  # 1 week = 6 days
        days = int(remaining_days % 6)

        remaining_seconds = total_planet_seconds % (config['rotation'] * 3600)
        hours = int(remaining_seconds // 3600)
        minutes = int((remaining_seconds % 3600) // 60)
        seconds = int(remaining_seconds % 60)

        # Get correct time-of-day phase based on planetary rotation
        time_of_day = get_time_of_day(hours, config['rotation'])

        result_text.insert(tk.END, 
            f"{planet}: {years}Y {months}M {weeks}W {days}D {hours:02}H {minutes}Min {seconds}Sec  ({time_of_day})\n"
        )

# GUI Setup
root = tk.Tk()
root.title("Terra Celestia | Planetary Time Converter")
root.geometry("750x450")
root.resizable(True, True)

# Styling
style = ttk.Style()
style.configure("TLabel", font=("Segoe UI", 10))
style.configure("TButton", font=("Segoe UI", 10))

# Layout Frame
frame = ttk.Frame(root, padding=10)
frame.pack(fill=tk.BOTH, expand=True)

# Planet selection (Top)
planet_frame = ttk.Frame(frame)
planet_frame.pack(pady=5)
ttk.Label(planet_frame, text="Select Planet:").pack(side=tk.LEFT, padx=5)
planet_var = tk.StringVar(value="Ignis")
planet_menu = ttk.Combobox(planet_frame, textvariable=planet_var, values=list(planets.keys()), state="readonly")
planet_menu.pack(side=tk.LEFT, padx=5)

# Inputs (Left to Right)
input_frame = ttk.Frame(frame)
input_frame.pack(pady=5)

fields = ["Years", "Months", "Weeks", "Days", "Hours", "Minutes", "Seconds"]
entries = {}

for i, field in enumerate(fields):
    ttk.Label(input_frame, text=field + ":").grid(row=0, column=i, padx=5, pady=5)
    entry = ttk.Entry(input_frame, width=8)
    entry.grid(row=1, column=i, padx=5, pady=5)
    entries[field.lower()] = entry

year_entry = entries["years"]
month_entry = entries["months"]
week_entry = entries["weeks"]
day_entry = entries["days"]
hour_entry = entries["hours"]
minute_entry = entries["minutes"]
second_entry = entries["seconds"]

# Convert Button (Centered)
convert_btn = ttk.Button(frame, text="Convert", command=convert_time)
convert_btn.pack(pady=10)

# Result Box (Bottom Center)
result_text = tk.Text(frame, height=8, width=90, wrap=tk.WORD, font=("Segoe UI", 10))
result_text.pack(pady=10)

# Run the application
root.mainloop()
