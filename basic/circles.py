def circle(radius):
    area=round(3.14*radius*radius,2)
    circ=round(2.0*3.14*radius,2)
    return area,circ
 
radius=float(input("Enter the radius of the circle:"))
area,circ=circle(radius)
print(f"The circumference of the circle is {circ}. The area of the circle is {area}.")