# A program to create List and Tuple and perform few functions of them
my_list = [1, 2, 3, 4, 5]
print("List:", my_list)

# Create a Tuple
my_tuple = (10, 20, 30, 40, 50)
print("Tuple:", my_tuple)

# Access List and Tuple Items
print("Third item in the list:", my_list[2])
print("Second item in the tuple:", my_tuple[1])

# Change List Items
my_list[3] = 99
print("Updated list:", my_list)

# Length of List and Tuple
print("Length of the list:", len(my_list))
print("Length of the tuple:", len(my_tuple))

# Concatenate Lists
new_list = my_list + [6, 7, 8]
print("Concatenated list:", new_list)

# Slicing a List
sliced_list = my_list[1:4]
print("Sliced list:", sliced_list)

# Convert Tuple to List
tuple_to_list = list(my_tuple)
print("Converted tuple to list:", tuple_to_list)

# Check if an Item Exists in the List
print("Is 3 in the list?", 3 in my_list)

# Delete an Item from the List
del my_list[1]
print("List after deletion:", my_list)
