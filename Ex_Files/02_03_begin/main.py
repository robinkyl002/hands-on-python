NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

HEROES = ["Jason", "Percy", "Annabeth", "Leo", "Frank", "Hazel", "Piper", "Reyna", "Nico", "Thalia", "Clarisse", "Bianca", "Zoe", "Castor", "Pollux", "Tyson"]

JOHN = NAMES[0]
PAUL = NAMES[1]

# Items in NAMES before index 2
JOHN_PAUL = NAMES[:2]
# Items in NAMES from index 2 to the end
GEORGE_RINGO = NAMES[2:]
# All items in NAMES but starting at the back and moving to the front of the list
REVERSE = NAMES[::-1]
# Items in NAMES starting from the beginning and increasing index by two until you reach the end of the list
EVERY_OTHER = NAMES[::2]

# Sum of all items in "AGES" list
print(sum(AGES))
print(max(HEROES))
# Smallest of all items in "AGES" list
print(min(AGES))
# Largest of all items in "AGES" list
print(max(AGES))

print(JOHN_PAUL)
print(GEORGE_RINGO)
print(REVERSE)
print(EVERY_OTHER)

EVERY_OTHER_HERO = HEROES[::2]
EVERY_THIRD_HERO = HEROES[::3]
REVERSE_EVERY_OTHER = HEROES[::-2]
# Last one to print is the index before the one indicated
# If you use 1:4, you only get three names
SECOND_TO_FIFTH = HEROES[1:5]

print(EVERY_OTHER_HERO)
print(EVERY_THIRD_HERO)
print(REVERSE_EVERY_OTHER)
print(SECOND_TO_FIFTH)
