def invert(val):
    return round(1.0/(val*2.0),4)
for i in range(10):
    print(f"The decimal equivalent of 1/{i+1} is {invert(i+1)}")