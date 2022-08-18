print("*"*50)
(dayb,monthb,yearb)=input("Enter the date of last date of return in dd/mm/yyyy format: ").split("/")
dayb=int(dayb)
monthb=int(monthb)
yearb=int(yearb)
print("*"*50)
(dayr,monthr,yearr)=input("Enter the date of return of the book in dd/mm/yyyy format: ").split("/")
dayr=int(dayr)
monthr=int(monthr)
yearr=int(yearr)
print("*"*50)
days=dayr-dayb+30*(monthr-monthb)+365*(yearr-yearb)
if(days<0):
    print("Invalid input")
elif days==0:
    print("No fine.")
elif(days<5):
    print(f"Fine is 50 paisa for {days} days late return")
elif days<10:
    print(f"Fine is 1 rupees for {days} days late return")
elif days<30:
    print(f"Fine is 5 rupees for {days} days late return")
else:
    print(f"Your membership has been cancelled for returning the book {days} late.")