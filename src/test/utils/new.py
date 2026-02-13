#Declare a variable with value "Good morning" and count each character how many times its repeated in dictionary
# format(key: char, Value: count)

variable = "Good morning"

dict = {}

for char in variable:
    if char in dict:
        dict[char] =+1
    else:
        dict[char]=1

print(f"The formated dictionary format is given {dict}")
