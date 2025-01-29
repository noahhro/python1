#conession food stand.
menu ={"pocorn" : 300,
       "samosa" : 30,
       "pizza"  : 700,
       "water"  : 70,
       "nachos" : 250,}
print("--------- MENU ---------")
cart=[]
total = 0
for key, value in menu.items():
    print(f" {key:10}: Rs.{value:.2f}")
print("------------------------")

while True :
    order=input("WHAT WOULD YOU LIKE TO ORDER(TYPE 'DONE' WHEN YOU ARE DONE): ").lower()
    if order == "done" :
        break
    elif menu.get(order) is not None :
        cart.append(order)
for order in cart:
    total += menu.get(order)
    print (order, end=" ")
print ()
print(f"YOUR TOTAL IS Rs.{total:.2f}")



    