# Collections

# lists,  arrays = lists

# First List = Shopping List ([] = list)
shopping_list = ["Milk", "Bread", "Eggs", "Chocolate", "Jam"]
print(shopping_list)
print(type(shopping_list))

# Indexing a list
print(shopping_list[2::])

# Change element in list
shopping_list[2] = "Butter"
print(shopping_list)
print(shopping_list[2])

# USING LIST METHODS

# adding to list
shopping_list.append("Fish")
print(shopping_list)

# remove items
shopping_list.remove("Bread")
print(shopping_list)

# removing the last item of a list using pop method
shopping_list.pop()
print(shopping_list)
shopping_list.pop()
print(shopping_list)

# Can I have a list with multiple data types? Yes
mixture = [1, 2, 3, 4, 5, "five", "six"]

# Slicing
print(mixture[1:3])

# Reverse order of slice + step over
print(mixture[-2::-1])

# Tuples are IMMUTABLE

tuple_example = ("bread", "eggs", "milk")
print(tuple_example)

# Dictionaries, another way to manage data but more complex and dynamic
# Key - Value pairs : Key is the reference , Value is the data to store

student_1 = {
    "name": "Reis",
    "stream": "DevOps",
    "Completed Lessons": 4,
    "completed_lesson_names": ["variables", "data_types", "setup"]
}

# Access Dict
print(student_1["stream"])

# Access a specific part of the list in the dict
print(student_1["completed_lesson_names"][0])

# Change an element within the dict
student_1["Completed Lessons"] = 3
print(student_1["Completed Lessons"])

# Changing element in a list in within a dict
student_1["completed_lesson_names"].remove("data_types")
print(student_1["completed_lesson_names"])

# Dictionary methods
print(student_1.keys())
print(student_1.values())

# Sets and Frozen Sets
# a set is a list that has no order/indexing
car_parts = {"wheels", "doors", "exhaust"}
print(car_parts)

car_parts.add("windows")
print(car_parts)

car_parts.discard("windows")
print(car_parts)

# Frozen Set - Immutable set - Not commonly used
x = frozenset({1, 2, 3, 4})
print(x)
