#python code to implement simple string operations
# Concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print("Full name:", full_name)

# String Slicing
my_string = "Hello, World!"
substring = my_string[7:12]
print("Substring:", substring)

# Changing Case
message = "Python is Fun"
print("Uppercase:", message.upper())
print("Lowercase:", message.lower())

# String Length
text = "Hello, Python!"
length = len(text)
print("Length of the string:", length)

# Formatted Strings (f-strings)
age = 30
print(f"I am {age} years old.")

# Multiline Strings
multiline_text = """
This is a multiline string.
It spans across multiple lines.
"""
print(multiline_text)
