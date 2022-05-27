#Write a programnwhich accepts the radius of a circle from the user and computes area.
r=float(input("Input the radius of the circle:"))
area=3.14*r*r
print("The area of the circle with radius",r, "is:",area)








#Write a python program to accept a filename from the user and print the extension of that.

x= input("Input the Filename: ")

y = x.split(".")

print ("Extension of the file is : " + y[-1])
