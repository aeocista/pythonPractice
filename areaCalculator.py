"""
This program calculates the area of circles and triangles
Author: Wesley Applequist
"""

print("The area calculator has started. Prepare for the decline of your math skills.")
print("")
print("What shape would you like to calculate the area of?")
print("")

shape = raw_input("Enter C for Circle or T for Triangle: ")

if shape == 'C':
  radius = float(raw_input("Enter the radius of the circle: "))
  pi = 3.14159
  area = (radius ** 2) * pi
  print "The area of the circle is %f square units" % (area)
elif shape == 'T':
  triangle_base = float(raw_input("Enter the base length of the triangle: "))
  triangle_height = float(raw_input("Enter the height of the triangle: "))
  area = 0.5 * triangle_base * triangle_height
  print "The area of the triangle is %f square units" % (area)
else:
  print("You must enter C or T.")

print("Happy? OK, exiting...")
  
  
  