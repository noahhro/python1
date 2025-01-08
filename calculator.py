
operator=input("ENTER THE OPERATION (*/+-): ")
num1=int(input("ENTER THE FIRST NUMBER: "))
num2=int(input("ENTER THE SECOND NUMBER: "))
if operator == "*" :
    print(f"ANSWER: {num1*num2}")
elif operator == "/" :
    print(f"ANSWER: {num1/num2}")
elif operator == "*" :
    print(f"ANSWER: {num1+num2}")
elif operator =="-" and num1 > num2 :
    print(f"ANSWER: {num1-num2}")
elif operator =="-" and num2 > num1 :
    print(f"ANSWER: {num2-num1}")
elif operator =="+" :
    print(f"ANSWER: {num1+num2}")
else :
    print(f"{operator} is INVALID!!!")