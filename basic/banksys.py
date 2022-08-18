wit=int(input("Enter amount to be withdrawn:"))
nh=int(wit/100)
wit=wit-100*nh
nf=int(wit/50)
wit=wit-50*nf
nt=int(wit/10)
wit=wit-10*nt
print("The number of notes of 100:",nh)
print("The number of notes of 50:",nf)
print("The number of notes of 10:",nt)
print("The remaining amount of money is:",wit)
