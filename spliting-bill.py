#claculating the bill and spliting among the members
print("Welcome to the tip calculator.")
Bill=float(input("What was the total bill ? $"))
tip=float(input("What percentage tip do u like to give ? 10,12 or 15 "))
Total_bill=Bill+((tip/100)*Bill)
people=int(input("How many people split the Bill ?"))
pay=(Total_bill)/(people)
Each_pay=round((pay),3)
print("Each person should pay ?",Each_pay)