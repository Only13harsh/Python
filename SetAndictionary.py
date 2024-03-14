#Program to Create Set and dictionaries and perform few functions
# Creating a Set
my_set = {1, 2, 3, 4}
print("Set:", my_set)

# Creating a Dictionary
country_capitals = {
    "Germany": "Berlin",
    "Canada": "Ottawa",
    "England": "London"
}
print("Dictionary:", country_capitals)

# Set Operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union_result = set1.union(set2)
intersection_result = set1.intersection(set2)
difference_result = set1.difference(set2)

print("Union:", union_result)
print("Intersection:", intersection_result)
print("Difference:", difference_result)

# Accessing Dictionary Items
print("Capital of Germany:", country_capitals["Germany"])

# Adding and Changing Dictionary Entries
country_capitals["France"] = "Paris"
country_capitals["Germany"] = "Bonn"  # Change the capital of Germany
print("Updated Dictionary:", country_capitals)

# Removing an Entry from a Dictionary
del country_capitals["Canada"]
print("Updated Dictionary (after deletion):", country_capitals)
