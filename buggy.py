patients = [[70, 1.8], [80, 1.9], [150, 1.7], [90, 2.8]]

def calculate_bmis(wheight, hweight):
    return wheight / (hweight ** 2)

for patient in patients:
    weight, height = patient
    bmi = calculate_bmi(weight, height)
    print("Patient's BMI is: %f" % bmi)
<<<<<<< HEAD


##EDITS MAKE THINGS BETTER###
=======
>>>>>>> 488b22235d6d38fbb43eddf717f9e29756de2e65
