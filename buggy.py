# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 14:40:43 2020

@author: JASON  H.T. BAYER
"""



#a failing code to be fixed
"""
patients = [[70, 1.8], [80, 1.9], [150, 1.7]]

def calculate_bmi(weight, height):
    return weight / (height ** 2)

for patient in patients:
    #incorrect calling of indacies
    weight, height = patients[0]
    #weight and height reversed
    bmi = calculate_bmi(height, weight)
    print("Patient's BMI is: %f" % bmi)
"""

#fixed code

#store patient data
patients = [[70, 1.8], [80, 1.9], [150, 1.7]]

#calculate BMI from weight and height
def calculate_bmi(weight, height):
    return weight / (height ** 2)

#loop through patients and print out their BMI
for patient in patients:
    print("correct input: " + str(patient))
    
    #set weight and height to be printed
    weight, height = patient
    
    print("weight: " + str(weight) + "kg")
    print("height: " + str(height) + "m")
    bmi = calculate_bmi(weight, height)
    print("Patient's BMI is: %f" % bmi + "\n")


