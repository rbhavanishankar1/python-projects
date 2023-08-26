#BMI CHALLENGE
weight=float(input("enter the weight in kgs : "))
height=float(input("enter the height in meter : "))
BMI=round(weight/(height**2),2)
if BMI<18.5:
    print(f"your BMI is {BMI},you are under weight")
elif 18.5<=BMI<25:
    print(f"your BMI is {BMI},you are normal weight")
elif 25<=BMI<30:
    print(f"your BMI is {BMI},you are over weight")
elif 30<=BMI<35:
    print(f"your BMI is {BMI},you are obesity")
else:
    print(f"your BMI is {BMI},you have abnormal obeycity")