
def conformation():
    global user_input
    user_input=input("Type 'encode' to encrypt,type 'decode' to decrypt :  ").lower()
    print(user_input)
    global user_message
    user_message=input("Type your message : ")
    print(user_message)
    global shift_number
    shift_number=int(input("Type the shift number : "))
    print(f"your shift number is: {shift_number}")

def encryption(user_input1,user_message1):
    st=""
    st1=""
    if user_input1=="encode":
        for i in user_message1:
            encode=chr(ord(i)+shift_number)
            st+=encode
        print(f"your message is before encode : {user_message1}")
        print("your encode message is : ",st)

    elif user_input1=="decode":
        for j in user_message1:
            decode=chr(ord(j)-shift_number)
            st1+=decode
        print(f"your message is before decode : {user_message1}")
        print("your decode messgae is :",st1)

    else:
        print(f"please! check the input u have entered {user_input1}")

# conformation()
# encryption(user_input1=user_input,user_message1=user_message)

should_conform=True
while should_conform: 
    conform=input("Type 'yes' if you want to go again.Otherwise type 'no' :").lower()
    if conform=="yes":
        conformation()
        encryption(user_input1=user_input,user_message1=user_message)
    elif conform=="no":
        should_conform=False
        print("byee you are sucess fully terminated")
