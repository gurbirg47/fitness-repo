### Fitness tracker

# User Profile to store (age, weight, height and fitness goals)

def greet(username):
    print(f'Hi {username.title()} Welcome to the Fitness tracker')

username = input('Enter your Name: ')

greet(username)


def user_profile():
    print(
        f'{username.title()}, can you please enter your age,'
        'weight, fitness goals to help us personalize your experience'
        'and provide the best recommendations for your journey'
    )

    while True:
        print('\n')
        age = int(input('Enter your age: '))
        weight = float(input('Enter your weight (lb): '))
        height = (input('Enter your height (ft): '))
        goals = input('What are your fitness goals? ')

        print('/nSummary of your details: ')
        print(f'Age: {age} years')
        print(f'Weight: {weight} lb')
        print(f'Height: {height} ft')
        print(f'Goals: {goals}')

        repeat = input('\nWould you like to enter details again? (yes/no): ').strip().lower()
        if repeat != 'yes':
            print('Thank You!')
            break

#functions call
user_profile()