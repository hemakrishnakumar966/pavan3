num1=int(input("give first no: "))
num2=int(input("give second no: "))
operator=input("give operator: ")

if operator =="+":
    print(f"add :({num1+num2})")
elif operator =="-":
    print(f"sub :({num1-num2})")
elif operator =="*":
    print(f"mul :({num1*num2})")    
elif operator =="/":
    print(f"div :({num1/num2})")
else:
    print("invalid")