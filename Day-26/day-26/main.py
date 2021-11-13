# list comprehension
numbers = [1, 2, 3]
new_numbers = [item + 1 for item in numbers]
print(new_numbers)

# Destructuring string to list
name = "Angela"
letters = [letter for letter in name]
print(letters)

# range as list
times_two_numbers = [number * 2 for number in range(1, 5)]
print(times_two_numbers)

# conditional list
numbers = [number for number in range(1, 100)]
divisible_by_3 = [number for number in numbers if number % 3 == 0]
print(divisible_by_3)

# conditonal strings
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

# all of it.
uppercase_names = [name.upper() for name in names if len(names) > 5]
print(uppercase_names)

numbers = [1, 1, 2, 3, 4, 8, 13, 34, 55]
squared_numbers = [number * number for number in numbers]
print(squared_numbers)
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)

data1 = open("file1.txt")
content1 = data1.readlines()
data2 = open("file2.txt")
content2 = data2.readlines()

shared_numbers = [int(number) for number in content1 if number in content2]
print(shared_numbers)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split()}
print(result)

print(result)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {key:value*9/5+32 for (key, value) in weather_c.items()}
print(weather_f)


