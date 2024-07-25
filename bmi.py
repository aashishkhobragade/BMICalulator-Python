import tkinter as tk
from PIL import Image, ImageTk

def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get()) / 100  # convert cm to meters
        bmi = weight / (height ** 2)
        result_label.config(text=f"Your BMI is: {bmi:.2f}")
        update_bmi_image(bmi)
    except ValueError:
        result_label.config(text="Please enter valid numbers")

def update_bmi_image(bmi):
    if bmi < 18.5:
        img_path = "Resources/underweight.png"
        category_text = "Underweight"
    elif 18.5 <= bmi < 24.9:
        img_path = "Resources/normal.png"
        category_text = "Normal weight"
    elif 25 <= bmi < 29.9:
        img_path = "Resources/overweight.png"
        category_text = "Overweight"
    elif 30 <= bmi < 39.9:
        img_path = "Resources/obese.png"
        category_text = "Obese"
    else:
        img_path = "Resources/extremeobese.png"
        category_text = "Extreme obese"
    
    image = Image.open(img_path)
    image = image.resize((150, 250), Image.Resampling.LANCZOS)
    bmi_image = ImageTk.PhotoImage(image)
    
    bmi_image_label.config(image=bmi_image)
    bmi_image_label.image = bmi_image  # Keep a reference to the image to prevent garbage collection
    category_label.config(text=category_text)

master = tk.Tk()
master.title("BMI Calculator")
master.geometry("900x650")

bgcolor = "#3572EF"
bgcolor2 = "#CAF4FF"

container1 = tk.Frame(master, bg=bgcolor, width=400, height=700)
container1.pack(side="left", fill="both", expand=True)

label = tk.Label(container1, text="BMI Calculator", font=("Helvetica", 25), bg=bgcolor)
label.pack(padx=30, pady=30)

# Create the details frame and add it to container1
details = tk.Frame(container1, bg=bgcolor)
details.pack(padx=30, pady=10, fill="both", expand=True)

weight_label = tk.Label(details, text="Weight (in kg)", font=("Helvetica", 16), bg=bgcolor)
weight_label.grid(row=1, column=0, padx=20, pady=10)

entry_weight = tk.Entry(details)
entry_weight.grid(row=1, column=1, padx=20, pady=10)

height_label = tk.Label(details, text="Height (in cm)", font=("Helvetica", 16), bg=bgcolor)
height_label.grid(row=2, column=0, padx=20, pady=10)

entry_height = tk.Entry(details)
entry_height.grid(row=2, column=1, padx=20, pady=10)

# Load and resize the image
image_path = "Resources/chart.png"
image = Image.open(image_path)
image = image.resize((400, 300), Image.Resampling.LANCZOS)  # Resize image to fit the container
image = ImageTk.PhotoImage(image)

# Create the image label and set background color
image_label = tk.Label(container1, image=image, bg=bgcolor)
image_label.pack(pady=10)

# Add the calculate button
calculate = tk.Button(container1, text="Calculate", font=("Helvetica", 16), command=calculate_bmi)
calculate.pack(padx=40, pady=20)

container2 = tk.Frame(master, bg=bgcolor2, width=400, height=300)
container2.pack(side="right", fill="both", expand=True)

label = tk.Label(container2, text="Result", font=("Helvetica", 25), bg=bgcolor2)
label.pack(padx=30, pady=30)

result_label = tk.Label(container2, text="", font=("Helvetica", 20), bg=bgcolor2)
result_label.pack(pady=20)

# Add a label to hold the BMI image
bmi_image_label = tk.Label(container2,text="Your BMI result", bg=bgcolor2)
bmi_image_label.pack(pady=20)
# Add a label to display the BMI category
category_label = tk.Label(container2, text="_ _ _", font=("Helvetica", 25), bg=bgcolor2)
category_label.pack(pady=10)

master.mainloop()

