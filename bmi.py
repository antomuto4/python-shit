weight = int(input("Enter how much you weight in KG (For example: 80) : "))
height = float(input("Enter how tall you are in M (For example: 1.70) : "))

results = weight / height / height

print("\n\nCheck if you are overweight: ")
print("\nNormal Weight = BMI 19–24,9\nOverweight = BMI 25–29,9\nObesity Level I = BMI 30–34,9\nObesity Level II = BMI 35–39,9\nObesity Level III = BMI > 40\n")

print("\nWhat is Recommended for My Age Group?:")
print("\n19 - 24 = Results 19-24\n24-34 = Results 20-25\n 35-44 = Results 21-26\n45-54 = Results 22-27\n55-64 = Results 23-28\nAbove 65 = Results 24-29\n\n")
print("Your results: ")
print(results)

if results > 25:
    print("You are Overweight\n")

if results > 30:
    print("You have Obesity Level I\n")

if results > 35:
    print("You have Obesity Level II\n")

if results > 40:
    print("You have Obesity Level III\n")