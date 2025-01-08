weight=float(input("ENTER YOUR WEIGHT: "))
unit=input("enter the unit your weight is (lbs or kgs): ")
SI =("Kgs","lbs")
if unit.lower() == "lbs" :
    result= round((weight / 2.205),2)
    print(f"your weight in {SI[0]} is {result}")
elif unit.lower() == "kgs":
    result= round((weight * 2.205),2)
    print(f"your weight in {SI[1]} is {result}")
else :
    print(f"{unit} is INVALID !!!")