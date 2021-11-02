student_heights = [180, 175, 174, 155, 201, 210, 189, 191]
def get_average_heights(student_heights_list):
    number_of_measurements = 0
    total_of_all_heights = 0
    average_height = 0
    for height in student_heights:
        number_of_measurements +=1
        total_of_all_heights += height

    average_height = total_of_all_heights/number_of_measurements
    print("The average height is: " + str(average_height) + "cm")

get_average_heights(student_heights)