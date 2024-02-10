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
For examples see [02_03_begin](02_03_begin/main.py)

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

## Logic (if/elif/else) - 02_05
For examples see [02_05_begin](02_05_begin/main.py)

- `import os` - Python has a built-in os module with methods for interacting with the operating system, like creating files and directories, management of files and directories, input, output, environment variables, process management, etc.
- You can change an environment variable in the terminal, just by using `export variable_name='value'`

## CSV - 03_01
For examples see [03_01_begin](03_01_begin/main.py)

- `csv` module helps handle CSV files
- `pprint` helps output to the console be better formatted and more readable
- CSV is better for customers than for development
- Format of key value pairs is similar to JS, but it requires double quotes around both key and pair

```
with open("laureates.csv", "r") as f:
  reader = csv.DictReader(f)
  laureates = list(reader)

```
- `with` handles both the opening and closing of the file specified
- `r` specifies that it should be read only mode, so no changes will be made to the file
- `f` is now what the file is called
- The file is read, then a list called `laureates` is created using the information that was copied to `reader`
  - This list can be used outside of the code block
- The for loop looks through each item in the list `laureates`, checks the surname, and prints out the laureate if the surname is "Einstein"
  - Once the surname "Einstein" is found it breaks out of the loop

## Making Calculations - 03_02
For examples see [03_02_begin](03_02_begin/main.py)

- `datetime` creates data structures that allow you to find out things like how old a laureate would have been when they received their prize
- The file finds Einstein, prints out all of the info on him, then goes through the data to find when he received the prize, and his birthdate, subtracts the years and returns the age

## Outputting JSON - 03_03
For examples see [03_03_begin](03_03_begin/main.py)

- use `json` module to allow for handling JSON
- JSON is used more widely than CSV for everything except spreadsheets
- `json.dumps()` takes a dictionary and turns it into a JSON string
- `json.loads` takes the JSON string and turns it back into a dictionary
- `pprint` just modifies how the output looks when printed to the console. 
- the first `with` code block essentially creates a list of Python dictionaries that is named laureates, so that allows us to convert it easily to JSON in the next code block
- `w` in the next code block tells the system that you will be writing to the JSON file
- when dealing with whole files, use `json.dump()` and `json.load()` both without the "s" at the end

## Challenge - 03_04
Link to the code: [03_04](03_04/main.py)

- Access the value in a key-value pair from a dictionary using the following syntax `dictionary_name["key"]`

## Loading a JSON dataset - 04_01
For examples see [04_01_begin](04_01_begin/main.py)

- using the `requests` module requires installing it using pip
- python allows you to multiply strings

## Extending a small web server - 04_02
For examples see [04_02_begin](04_02_begin/main.py)

- 
