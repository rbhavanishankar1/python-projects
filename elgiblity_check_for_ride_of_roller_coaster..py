#elgiblity_check_for_ride_of_roller_coaster.
height=int(input("enter the height in the cm: "))
if height>=120:
    print("you are elgible for rollercoaster ride")
    age=int(input("enter the your age: "))
    if age<12:
        print("child ticket price is $5")
        bill=5
    elif 12<=age<=18:
        print("youth ticket price is $7")
        bill=7
    else:
        print("Adult ticket price is $12")
        bill=12
    want_photo=input("eneter the Y if u want photo : ").upper()
    if want_photo=="Y":
        print("cost for each photo is $3")
        bill+=3
    print("total bill u have to pay:$",bill)  
else:
    print(f"your are not elgible for ride beacuse u r {height} cm height it is below 120 cm")