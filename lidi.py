# Working with lists, tuples and dictionaries.

# List
schools = [ 'Accra Girls SHS', 'St. Augustine SHS', 'Accra Academy SHS' ]

# Tuple
school_population = ( 2300, 1900, 2100 )

# Dictionary
section_population = {
  'boys': 800,
  'girls': 900,
}

print(f'Printing list content => { schools }')
print(f'Printing tuple content => { school_population }')
print(f'Printing dictionary content => { section_population }')

print()

print('Getting the position of items in the various variables')
print('=' * 70)

print()

print('Starting with the list variable')
print(f'Item in the 0th position is => { schools[0] }')
print(f'Item in the 1st position is => { schools[1] }')
print(f'Item in the 2nd position is => { schools[2] }')
print('=' * 70)

print()

print('Using the tuple variable')
print(f'Item in the 0th position is => { school_population[0] }')
print(f'Item in the 1st position is => { school_population[1] }')
print(f'Item in the 2nd position is => { school_population[2] }')
print('=' * 70)

print()

print('Using the dictionary variable')
print(f'Item in the 0th position is => { section_population.get("boys") }')
print(f'Item in the 1st position is => { section_population.get("girls") }')
print('=' * 70)

print()