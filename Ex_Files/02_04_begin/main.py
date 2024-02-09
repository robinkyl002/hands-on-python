NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

HEROES = ["Jason", "Percy", "Annabeth", "Leo", "Frank", "Hazel", "Piper", "Reyna", "Nico", "Thalia", "Clarisse", "Bianca", "Zoe", "Castor", "Pollux", "Tyson"]
PARENTS = ["Jupiter", "Poseidon", "Athena", "Hephaestus", "Mars", "Pluto", "Aphrodite", "Bellona", "Hades", "Zeus", "Ares", "Hades", "Atlas", "Dionysus", "Dionysus", "Poseidon"]

# i = 0
# while i < len(NAMES):
#     print(NAMES[i], AGES[i])
#     i += 1

j = 0
while j < len(HEROES):
    print(HEROES[j], PARENTS[j])
    j += 1

# For loops are used more often than while loops as they are less prone to endless looping
# for name in NAMES:
#     print(name)

for hero in HEROES:
    print(hero)

# for name, age in zip(NAMES, AGES):
#     print(f"{name} {age}")


# The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, 
# and then the second item in each passed iterator are paired together etc.
# If the passed iterables have different lengths, the iterable with the least items decides the length of the new iterator.
for hero, parent in zip(HEROES, PARENTS):
    # Using f in the print statement lets the program know that anything inside of braces is a variable
    print(f"{hero} {parent}")



# for name in reversed(NAMES):
#     print(name)

for hero in reversed(HEROES):
    print(hero)

# for i in range(5):
#     print(i)

for i in range(18):
    print(i * (i + 1))

# enumerate

for i, name in enumerate(NAMES):
    print(f"{i} {name}")

for j, hero in enumerate(HEROES):
    print(f"{j} {hero}")