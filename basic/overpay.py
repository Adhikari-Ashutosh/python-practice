def overpay(workhours):
    if workhours>40:
        return 12.0*(workhours-40)
    else:
         return 0
 
for i in range(10):
    print(50*"*")
    workhrs=int(input(f"Enter the work hours of Employee {i+1}:"))
    print(f"The overtime paid to employee {i+1} is {overpay(workhrs)}")
    print(50*"*")