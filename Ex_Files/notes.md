# Intro to Python notes

## Strings - 02_02
For examples see [02_02_begin](02_02_begin/main.py)

- `format()` function looks for braces in the string indicated, then replaced it with the value of the variable specified
- After using `upper()` or `lower()` function another string can be added to the end of it using concatenation, but that piece of the new string will not be affected by the function
- the `print()` function includes an automatic newline

## Lists - 02_03
### Functions
- `max()` function finds the largest item in the list inside the parentheses (when used on a string, finds last string in alphabetical order)
- `min()` function finds the smallest item in the list inside the parentheses(when used on a string, finds first string in alphabetical order)
- `sum()` function adds together all of the items in the list and returns the total (As expected, only works on numbers)

### Accessing part of a list
For examples, see [02_03_begin](02_03_begin/main.py)

- If you **just want a section of a list**, use the index of the first item, then the index of the item after the last item you want (i.e. `NAMES[2:6]` for items at indexes 2, 3, 4, and 5)
- If you want everything from the **start of the list up to a certain index**, just put a colon and then the index after the last item you want (i.e. `NAMES[:5]` for items through index 4)
- If you want everything **from a certain index up to the end**, just put the index of that item and then a colon (i.e. `NAMES[5:]` for items starting at index 5 until the end of the list)
- If you want to **specify how much the iterator should change**, put the number after the start and stop values (i.e. `NAMES[20:60:3]` will give you the value at every third index between 20 and 60)
- If you want to **iterate backward** through the list, just make the iterator negative (i.e. `NAMES[::-1]` will iterate backward through the entire list, starting with the ending item)


## Loops - 02_04
For examples see [02_04_begin](02_04_begin/main.py)

### Functions
- The `zip()` function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.
  - If the passed iterables have different lengths, the iterable with the least items decides the length of the new iterator.
- The `reversed()` function runs through a list from the last index to the first

### Other Notes
- Using f in a print statement before a string lets the program know that anything inside of braces should be treated as a variable
- For loops are used more often than while loops as they are less prone to endless looping

## Logic (if/elif/else) - 02_05_begin
For examples, see [02_05_begin](02_05_begin/main.py)

- `import os` - Python has a built-in os module with methods for interacting with the operating system, like creating files and directories, management of files and directories, input, output, environment variables, process management, etc.
- You can change an environment variable in the terminal, just by using `export variable_name='value'`
