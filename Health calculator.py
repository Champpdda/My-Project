import tkinter as tk
from tkinter import ttk, messagebox

# คำนวณมวลกายที่ไม่มีไขมัน
def calculate_lean_body_mass(weight_kg, height_cm, gender):
    if gender == "Male":
        lbm = (0.407 * weight_kg) + (0.267 * height_cm) - 19.2
    else:  # Female
        lbm = (0.252 * weight_kg) + (0.473 * height_cm) - 48.3
    return lbm

# คำนวณความต้องการแคลอรี
def calculate_calorie_needs(weight_kg, height_cm, age, gender, activity_level):
    if gender == "Male":
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
    else:  # Female
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161

    activity_multipliers = {
        "Sedentary": 1.2,
        "Lightly Active": 1.375,
        "Moderately Active": 1.55,
        "Very Active": 1.725,
        "Super Active": 1.9
    }

    calorie_needs = bmr * activity_multipliers.get(activity_level, 1.2)
    return calorie_needs

# คำนวณสารอาหารหลัก
def calculate_macronutrients(calories):
    carb_percentage = 0.55
    protein_percentage = 0.15
    fat_percentage = 0.30

    carbs_grams = (calories * carb_percentage) / 4
    protein_grams = (calories * protein_percentage) / 4
    fats_grams = (calories * fat_percentage) / 9

    return carbs_grams, protein_grams, fats_grams

# คำนวณโซนการเต้นของหัวใจ
def calculate_heart_rate_zones(max_hr):
    return {
        "Zone 1": (0.50 * max_hr, 0.60 * max_hr),
        "Zone 2": (0.60 * max_hr, 0.70 * max_hr),
        "Zone 3": (0.70 * max_hr, 0.80 * max_hr),
        "Zone 4": (0.80 * max_hr, 0.90 * max_hr),
        "Zone 5": (0.90 * max_hr, max_hr)
    }

# คำนวณมวลกายที่ไม่มีไขมัน (LBM)
def calculate_lbm():
    try:
        weight_kg = float(weight_entry.get())
        height_cm = float(height_entry.get())
        gender = gender_var.get()

        lean_body_mass = calculate_lean_body_mass(weight_kg, height_cm, gender)
        fat_mass = weight_kg - lean_body_mass
        fat_percentage = (fat_mass / weight_kg) * 100

        lbm_result_text.set(
            f"Lean Body Mass: {lean_body_mass:.2f} kg\n"
            f"Fat Mass: {fat_mass:.2f} kg\n"
            f"Body Fat Percentage: {fat_percentage:.2f}%"
        )
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

# คำนวณความต้องการแคลอรี
def calculate_calories():
    try:
        weight_kg = float(weight_entry.get())
        height_cm = float(height_entry.get())
        age = int(age_entry.get())
        gender = gender_var.get()
        activity_level = activity_var.get()

        daily_calories = calculate_calorie_needs(weight_kg, height_cm, age, gender, activity_level)
        carbs_grams, protein_grams, fats_grams = calculate_macronutrients(daily_calories)

        calorie_result_text.set(
            f"Daily Calorie Needs: {daily_calories:.2f} kcal\n"
            f"Carbohydrates: {carbs_grams:.2f} grams\n"
            f"Protein: {protein_grams:.2f} grams\n"
            f"Fat: {fats_grams:.2f} grams"
        )
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

# คำนวณโซนการเต้นของหัวใจ
def calculate_hr_zones():
    try:
        age = int(age_entry.get())
        if age <= 0 or age > 120:
            raise ValueError("Please enter a valid age.")

        max_hr = calculate_max_heart_rate(age)
        hr_zones = calculate_heart_rate_zones(max_hr)
        hr_result_text.set(
            f"Heart Rate Zones:\n"
            f"Zone 1: {hr_zones['Zone 1'][0]:.0f} - {hr_zones['Zone 1'][1]:.0f} bpm\n"
            f"Zone 2: {hr_zones['Zone 2'][0]:.0f} - {hr_zones['Zone 2'][1]:.0f} bpm\n"
            f"Zone 3: {hr_zones['Zone 3'][0]:.0f} - {hr_zones['Zone 3'][1]:.0f} bpm\n"
            f"Zone 4: {hr_zones['Zone 4'][0]:.0f} - {hr_zones['Zone 4'][1]:.0f} bpm\n"
            f"Zone 5: {hr_zones['Zone 5'][0]:.0f} - {hr_zones['Zone 5'][1]:.0f} bpm"
        )
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

# คำนวณอัตราการเต้นของหัวใจสูงสุด
def calculate_max_heart_rate(age):
    return 220 - age

# ฟังก์ชันสำหรับเปลี่ยนสีของปุ่มเมื่อเมาส์ชี้
def on_button_enter(event):
    event.widget['background'] = button_hover_color
    event.widget['borderwidth'] = 2

# ฟังก์ชันสำหรับเปลี่ยนสีของปุ่มกลับเมื่อเมาส์ออก
def on_button_leave(event):
    event.widget['background'] = button_color
    event.widget['borderwidth'] = 1

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("Health Calculator")
root.geometry("550x700")
root.configure(bg='#26a69a')  # สีพื้นหลังเขียว

# กำหนดฟอนต์และสี
font_large = ('Arial', 16, 'bold')
font_medium = ('Arial', 12)
font_small = ('Arial', 10)
background_color = '#009688'  # สีพื้นหลังเขียว
foreground_color = '#FFFFFF'  # สีข้อความขาว
button_color = '#e84e40'  # สีปุ่มแดง
button_hover_color = '#CC0000'  # สีปุ่มแดงเข้มเมื่อชี้
entry_color = '#FFFFFF'  # สีพื้นหลังของช่องกรอกข้อมูลขาว
label_color = '#FFFFFF'  # สีข้อความของป้ายขาว
result_bg_color = '#80cbc4'  # สีพื้นหลังผลลัพธ์เขียวอ่อน
result_border_color = '#2baf2b'  # สีกรอบผลลัพธ์เขียวเข้ม

# สร้าง Notebook สำหรับแท็บต่างๆ
notebook = ttk.Notebook(root)
notebook.pack(pady=20, expand=True)

# สร้างช่องกรอกข้อมูลพื้นฐาน
input_frame = tk.Frame(root, bg=background_color)
input_frame.pack(padx=20, pady=20, fill='x')

tk.Label(input_frame, text="Weight (kg):", font=font_medium, bg=background_color, fg=foreground_color).grid(row=0, column=0, padx=10, pady=10, sticky='w')
weight_entry = tk.Entry(input_frame, font=font_medium, width=25, bg=entry_color, bd=2, relief='solid')
weight_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(input_frame, text="Height (cm):", font=font_medium, bg=background_color, fg=foreground_color).grid(row=1, column=0, padx=10, pady=10, sticky='w')
height_entry = tk.Entry(input_frame, font=font_medium, width=25, bg=entry_color, bd=2, relief='solid')
height_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(input_frame, text="Age (years):", font=font_medium, bg=background_color, fg=foreground_color).grid(row=2, column=0, padx=10, pady=10, sticky='w')
age_entry = tk.Entry(input_frame, font=font_medium, width=25, bg=entry_color, bd=2, relief='solid')
age_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Label(input_frame, text="Gender:", font=font_medium, bg=background_color, fg=foreground_color).grid(row=3, column=0, padx=10, pady=10, sticky='w')
gender_var = tk.StringVar(value="Male")
gender_menu = ttk.Combobox(input_frame, textvariable=gender_var, values=["Male", "Female"], state="readonly", font=font_medium)
gender_menu.grid(row=3, column=1, padx=10, pady=10)

tk.Label(input_frame, text="Activity Level:", font=font_medium, bg=background_color, fg=foreground_color).grid(row=4, column=0, padx=10, pady=10, sticky='w')
activity_var = tk.StringVar(value="Sedentary")
activity_menu = ttk.Combobox(input_frame, textvariable=activity_var, 
                             values=["Sedentary", "Lightly Active", "Moderately Active", "Very Active", "Super Active"], 
                             state="readonly", font=font_medium)
activity_menu.grid(row=4, column=1, padx=10, pady=10)

# สร้างแท็บมวลกายที่ไม่มีไขมัน
lbm_frame = tk.Frame(notebook, bg=background_color)
notebook.add(lbm_frame, text='Lean Body Mass')

lbm_result_text = tk.StringVar()
lbm_result_frame = tk.Frame(lbm_frame, bg=result_bg_color, bd=2, relief='groove')
lbm_result_frame.pack(pady=20, padx=20, fill='both', expand=True)

lbm_label = tk.Label(lbm_result_frame, textvariable=lbm_result_text, font=font_medium, bg=result_bg_color, fg=foreground_color, justify="left", anchor='w')
lbm_label.pack(pady=10, padx=10, fill='both', expand=True)

lbm_button = tk.Button(lbm_frame, text="Calculate LBM", command=calculate_lbm, font=font_large, bg=button_color, fg=foreground_color, relief='flat', padx=20, pady=10)
lbm_button.pack(pady=20)
lbm_button.bind("<Enter>", on_button_enter)
lbm_button.bind("<Leave>", on_button_leave)

# สร้างแท็บความต้องการแคลอรี
calorie_frame = tk.Frame(notebook, bg=background_color)
notebook.add(calorie_frame, text='Calorie Needs')

calorie_result_text = tk.StringVar()
calorie_result_frame = tk.Frame(calorie_frame, bg=result_bg_color, bd=2, relief='groove')
calorie_result_frame.pack(pady=20, padx=20, fill='both', expand=True)

calorie_label = tk.Label(calorie_result_frame, textvariable=calorie_result_text, font=font_medium, bg=result_bg_color, fg=foreground_color, justify="left", anchor='w')
calorie_label.pack(pady=10, padx=10, fill='both', expand=True)

calorie_button = tk.Button(calorie_frame, text="Calculate Calories", command=calculate_calories, font=font_large, bg=button_color, fg=foreground_color, relief='flat', padx=20, pady=10)
calorie_button.pack(pady=20)
calorie_button.bind("<Enter>", on_button_enter)
calorie_button.bind("<Leave>", on_button_leave)

# สร้างแท็บโซนการเต้นของหัวใจ
hr_frame = tk.Frame(notebook, bg=background_color)
notebook.add(hr_frame, text='Heart Rate Zones')

hr_result_text = tk.StringVar()
hr_result_frame = tk.Frame(hr_frame, bg=result_bg_color, bd=2, relief='groove')
hr_result_frame.pack(pady=20, padx=20, fill='both', expand=True)

hr_label = tk.Label(hr_result_frame, textvariable=hr_result_text, font=font_medium, bg=result_bg_color, fg=foreground_color, justify="left", anchor='w')
hr_label.pack(pady=10, padx=10, fill='both', expand=True)

hr_button = tk.Button(hr_frame, text="Calculate HR Zones", command=calculate_hr_zones, font=font_large, bg=button_color, fg=foreground_color, relief='flat', padx=20, pady=10)
hr_button.pack(pady=20)
hr_button.bind("<Enter>", on_button_enter)
hr_button.bind("<Leave>", on_button_leave)

# เริ่มต้นลูปหลัก
root.mainloop()