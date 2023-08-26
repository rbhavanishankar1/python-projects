import random
Rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors= """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

no_of_round=int(input("enter the no-of rounds :" ))
user_count=0
com_count=0
for i in range(0,no_of_round):
#user giving input
    user_input=int(input("enter 1.Rock 2.Paper 3.Scissors :"))
    if user_input==1:
        print(Rock)
    elif user_input==2:
        print(Paper)
    elif user_input==3:
        print(Scissors)
    else:
        print("please enter the valid number")

    
    #computer random generated value
    com_input=int(random.randint(1,2))

    if com_input==1:
        print(Rock)
    if com_input==2:
        print(Paper)
    if com_input==3:
        print(Scissors)
    
  
    
    #declaring winner
    image=["","rock","paper","scissors"]
    print(f"computer input {image[com_input]} and user input is {image[user_input]}")
    if user_input==com_input:
        print("you have draw the match but you dont get any points ")
    elif  user_input==1 and com_input==3:
        print("you win! by Rock over a scissors")
        user_count+=1
    elif user_input==2 and com_input==1:
        print("you win! by paper over a rock")
        user_count+=1
    elif  user_input==3 and com_input==2:
        print("you win! by scissors over a paper")
        user_count+=1
    else:
        print("you lose!!!")
        com_count+=1  
print(user_count,com_count)
#adding points to the winner and declaring the winner
if com_count>user_count:
    print("😭😭YOU HAVE LOST THE MATCH😭😭")
elif user_count>com_count:
    print(" 😎😎 YOU HAVE WIN THE GAME BRO!😎😎")
elif user_count==com_count:
    print("you have DRAW the match")
else:
    print("something went wrong")


