# Starting with Varibles and Datatypes in python

# integer vars
first_number = 12 # integer variable
second_number = 14 # integer variable
tot = first_number + second_number

# string vars
first_name = 'Sam'

print('Performing some computations in Python\'s...')
print("Performing some computations in Python's modules...")
print('=' * 80)
print() # Display an empty line

print(f'The value for the first number is: { first_number }')
print(f'The value for the second number is: { second_number }')
print()

print(f'The sum of { first_number } and { second_number } is: { tot }')
print('The sum of {} and {} is: {}'.format( first_number, second_number, tot))
print('The sum of', first_number, 'and', second_number, 'is', tot)

print() # Display an empty line
print('Displaying the data types of the variables')
print(f' { first_number } is of type: { type(first_number) }')
print(f' { first_name } is of type: { type(first_name) }')