## Applying the functions to list, Various Types

regimentNames = ['Night Riflemen', 'Jungle Scouts', 'The Dragoons', 'Midnight Revengence', 'Wily Warriors']

##For loop

# create a variable for the for loop results
regimentNamesCapitalized_f = []

# for every item in regimentNames
for i in regimentNames:
    # capitalize the item and add it to regimentNamesCapitalized_f
    regimentNamesCapitalized_f.append(i.upper())
    
# View the outcome
print(regimentNamesCapitalized_f)

##Map function

capitalizer = lambda x: x.upper()
regimentNamesCapitalized_m = list(map(capitalizer, regimentNames)); 
print(regimentNamesCapitalized_m)

## Using List Comprehension

regimentNamesCapitalized_l = [x.upper() for x in regimentNames]; 
print(regimentNamesCapitalized_l)

