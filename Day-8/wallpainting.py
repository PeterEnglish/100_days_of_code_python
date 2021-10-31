import math
def paint_wall( wall_width, wall_height, coverage):
    
    area = int(wall_height)*int(wall_width)
    return math.ceil(area/int(coverage))

input_width = int(input("Enter the width of the wall: "))
input_height = int(input("Enter the height of the wall: "))
input_coverage = int(input("Enter the coverage per can: "))
 
print(str(paint_wall(wall_width=input_width, wall_height=input_height, coverage = input_coverage)))