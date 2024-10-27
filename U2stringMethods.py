#Program 9: Strign Methods

# Sample string
text = " Hello, Python World! "

print(dir(text))



# 1. .strip(): Removes leading and trailing spaces
print("strip():", text.strip())

# 2. .lower(): Converts the string to lowercase
print("lower():", text.lower())

# 3. .upper(): Converts the string to uppercase
print("upper():", text.upper())

# 4. .title(): Converts the first character of each word to uppercase
print("title():", text.title())

# 5. .replace(): Replaces a substring with another substring
print("replace():", text.replace("Python", "Coding"))

# 6. .find(): Finds the first occurrence of a substring and returns its index (returns -1 if not found)
print("find():", text.find("Python"))

# 7. .count(): Counts occurrences of a substring in the string
print("count():", text.count("o"))

# 8. .startswith(): Checks if the string starts with a specified substring
print("startswith():", text.startswith(" Hello"))

# 9. .endswith(): Checks if the string ends with a specified substring
print("endswith():", text.endswith("!"))

# 10. .split(): Splits the string into a list based on a delimiter
print("split():", text.split())

# 11. .join(): Joins elements of a list with the string as the delimiter
words = ["Hello", "Python", "World"]
print("join():", " ".join(words))

# 12. .capitalize(): Capitalizes the first character of the string
print("capitalize():", text.capitalize())

# 13. .isalpha(): Checks if all characters are alphabetic
alpha_text = "HelloWorld"
print("isalpha():", alpha_text.isalpha())

# 14. .isdigit(): Checks if all characters are digits
digit_text = "12345"
print("isdigit():", digit_text.isdigit())

# 15. .isspace(): Checks if the string contains only whitespace characters
space_text = "   "
print("isspace():", space_text.isspace())

# 16. .islower(): Checks if all characters in the string are lowercase
print("islower():", text.islower())

# 17. .isupper(): Checks if all characters in the string are uppercase
print("isupper():", text.isupper())

# 18. .swapcase(): Swaps the case of all characters in the string
print("swapcase():", text.swapcase())

# 19. .center(): Centers the string within a specified width, padding with spaces
print("center():", text.center(30, '-'))

# 20. .ljust() and .rjust(): Left- and right-justify the string within a specified width
print("ljust():", text.ljust(30, '-'))
print("rjust():", text.rjust(30, '-'))
