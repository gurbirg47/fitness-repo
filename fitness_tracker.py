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
      
    profile = {
         'Age' : None,
         'Weight': None,
         'Height': None,
         'Goals' : None
    }

    # Collecting user details
    while True:
        print(
            f'\n{username.title()}, can you please enter your age,'
            'weight, height, and fitness goals?'
        )
        print('\n')
        profile['Age'] = int(input('Enter your age: '))
        profile['Weight'] = float(input('Enter your weight (lb): '))
        profile['Height'] = input('Enter your height (ft): ')
        profile['Goals'] = input('What are your fitness goals? ')

        # profile summary
        print('\nSummary of your Profile')
        print(f'Age: {profile['Age']} years')
        print(f'Weight: {profile['Weight']}')
        print(f'Height: {profile['Height']} ft')
        print(f'Goals: {profile['Goals']}')

        # if the user wants to make changes to their profile
        edit = input('\nWould you like to make changes to your profile (yes/no): ').strip().lower()
        if edit == 'yes':
            field_to_edit = input('Which field would you like to edit (Age/Weight/Height/Goals)').strip().title()
            if field_to_edit == 'Age':
                profile['Age'] = int(input('Enter your new Age: '))
            elif field_to_edit == 'Weight':
                profile['Weight'] = float(input('Enter your new weight (ft): '))
            elif field_to_edit == 'Height':
                profile['Height'] = input('Enter new Height: ')
            elif field_to_edit == 'Goals':
                profile['Goals'] = input('Enter new Goals: ')
        else:
            print('Thank you! Your profile is complete.')
            break

#functions call
user_profile()