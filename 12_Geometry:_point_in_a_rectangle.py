"""
Write a program that prompts the user to enter
a point (x, y) and checks whether the point is within the rectangle centered at
( 0 , 0 ) with width 10 and height 5 . For example, ( 2 , 2 ) is inside the rectangle and
( 6 , 4 ) is outside the rectangle, as shown in Figure 4.8b. (Hint: A point is in the
rectangle if its horizontal distance to ( 0 , 0 ) is less than or equal to 10 / 2 and
its vertical distance to ( 0 , 0 ) is less than or equal to 5.0 / 2 . Test your program
to cover all cases.)
"""

# Prompt user to enter a point (x,y)
points_x1, points_y2 = eval(input("Enter a point with two coordinates : "))

points_x2 = 0
points_y1 = 0

if (points_x1 >= 0) and (points_x1 <= (10.0/2)):
    if (points_y2 >= 0) and (points_y2 <= (5.0/2)):
        print(f"{points_x1, points_x2} and {points_y1, points_y2} is in the rectangle")
    else:
        print(f"{points_x1, points_x2} and {points_y1, points_y2} is not in the rectangle")
else:
    print(f"{points_x1, points_x2} and {points_y1, points_y2} is not in the rectangle")