# Import combinations with replacements from itertools
from itertools import combinations_with_replacement


# Create some text, add padding around text(left/right) ,Add *
def create_formatting(text, padding_value):
    return format(text, padding_value)


text = 'Chapter 1'
print(text)
print(create_formatting(text, '>20'))
print(create_formatting(text, '<20'))
print(create_formatting(text, '^20'))
print(create_formatting(text, '*^20'))


# Create a list of objects to combine
list_of_objects = ['abc', '123', 'eins']
combinations = []  # to hold results
# Create a loop for every item in the length of list_of_objects, that,
for i in list(range(len(list_of_objects))):
    # Finds every combination (with replacement) for each object in the list
    combinations.append(list(combinations_with_replacement(list_of_objects, i + 1)))

# View the results
print(combinations)
# Flatten the list of lists into just a list
combinations = [i for row in combinations for i in row]

# View the results
print(combinations)
