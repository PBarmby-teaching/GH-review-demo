patients = [[70, 1.8], [80, 1.9], [150, 1.7]]

def calculate_bmi(weight, height):
    return weight / (height ** 2)

count = 0
for patient in patients:
    weight, height = patients[count]
    bmi = calculate_bmi(weight, height)
    count += 1
    print("Patient's BMI is: %f" % bmi)

