cdgreet = "Hello World"
extened_grt = "Hello World, " + "this is a long string"

print(cdgreet)
print(extened_grt)

name = "John"

intrupution = f"Hello {name}"

print(intrupution)

greet_format = "Hello {}"

formatted = greet_format.format(name)
# format() function looks for braces in the string indicated, then replaced it with the value of the variable specified

print(intrupution, formatted)

print(formatted.upper())
print(formatted.lower())

print(extened_grt.lower())

# an additional string can be added after the function to make all letters upper- or lowercase. 
print(extened_grt.upper() + ", and we will have a blast!")
print(intrupution.upper())

# the print function includes an automatic newline function

print(formatted.replace("John", "Jake"))
