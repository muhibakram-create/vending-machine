print("Welcome to snack vending machine")
print("Insert required coins to get snacks!")
functioning = True
snackprice = 100
totalcoin=0
#make it false when machine is not working
while functioning==True:
    print("We accept coins of 1,2,5,10 tk")
    coin_inserted = int(input("which coin did you insert?"))
    if coin_inserted==1 or coin_inserted==2 or coin_inserted==5 or coin_inserted==10:
        print("Your coin has been accepted")
    else:
        print("Sorry this coin is not valid, try again")
        continue 
    totalcoin = totalcoin + coin_inserted
    if totalcoin >= snackprice:
        break
print("Snack is being dispensed")
def change(total,price):
    change=total - price
    return change
change_returned= change(totalcoin,snackprice)
if change_returned==0:
    pass
else:    
    print(f"Here is your change of {change_returned} tk")
print()
print()
print("Purchase Summary")
print(f"TOTAL MONEY INSERTED:{coin_inserted}tk")
print(f"TOTAL SPENT {snackprice}tk")
print(f"CHANGE RETURNED {change_returned} tk")
print("THANK YOU 4 THE PURHASE")