"""
Write function bmi that calculates body mass index (bmi = weight / height2)

if bmi <= 18.5 return "Underweight"
if bmi <= 25.0 return "Normal"
if bmi <= 30.0 return "Overweight"
if bmi > 30 return "Obese

"""


def bmi(weight, height):
    bmi_cof = weight/height**2

    return 'Underweight' if bmi_cof <= 18.5 else 'Normal' if bmi_cof <= 25.0 else 'Overweight' if bmi_cof <= 30.0 else 'Obese'
