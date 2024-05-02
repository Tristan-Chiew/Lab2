def calculate_bmi(height,weight):
    print("Height = " ,height)
    print("Weight = " ,weight)
    bmi = weight/(height*height)
    print("BMI = ", bmi)
    if bmi < 18.5:
        return -1
    elif bmi > 25.0:
        return 0
    else:
        return 1
print(calculate_bmi(1.73,30))
