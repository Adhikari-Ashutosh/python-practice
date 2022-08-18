def compound(amt,rate,period):
    principal=amt
    inter=0.0
    for i in range(period):
        inter+=principal*rate/100.0
        principal+=inter
    return inter
amt=float(input("Enter the Start amount:"))
rate=float(input("Input the rate:"))
period=int(input("Enter the period of interest calculation:"))
print(f"The Compound interest accumulated after time period is:{compound(amt,rate,period)}")