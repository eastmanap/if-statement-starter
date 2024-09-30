# Apollos Eastman
# Sep 30 2024
# Station 5 If Statements

# Task 1
superheroes = {'Batman', 'Spiderman', 'Superman', 'Ironman', 'Captain America', 'Hulk' }

favorite = input('Who is your favorite superhero?')

if favorite in superheroes:
    print (f'{favorite} is your favorite superhero!')

# Task 2
print()

quiz_scores = int(input('What was your score on a recent quiz?'))

if quiz_scores >= 85:
    print('You earned a B or better!')

# Task 3
print()

quote = input('Enter a movie quote:')

if quote.startswith('M'):
    print('Your quote starts with an uppercase M!')

# Task 4
print()

filename =  input('Enter the name of a file, be sure to include the extension:')

if filename.endswith('.png'):
    print('The filename ends with .png.')

# Task 5
print()

is_registered = 'false'

if is_registered == 'false':
    print('You are not registered for classes at NMC.')
