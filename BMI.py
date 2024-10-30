def calculate_bmi(height, weight):
    height = float(height)
    weight = float(weight)
    print("Height =", height)
    print("Weight =", weight)
    
    BMI = weight / (height ** 2)
    print("Your BMI is =", round(BMI,2))
    print ("Weight Classification:" ,end="")


    if BMI <18.5:
        print("Underweight")    
    elif BMI >25.0:
        print ("Overweight")
    else:
        print("Normal")

calculate_bmi(weight="57", height="1.73")





