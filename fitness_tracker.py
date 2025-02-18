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
        profile['Height'] = float(input('Enter your height (ft): '))
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
                profile['Height'] = float(input('Enter new Height (ft): '))
            elif field_to_edit == 'Goals':
                profile['Goals'] = input('Enter new Goals: ')
        else:
            print('Thank you! Your profile is complete.')
            break

user_data = user_profile()

#main interface for the program

def main():

    activities = []  # empty list to store activties
    print('Welcome To the Fitness Tracker')

    while True:
        print('\n---Menu---')
        print('1. Log an Activity')
        print('2. View Summary')
        print('3. Calculate BMI')
        print('4. Quit')

        user_choice = int(input('Enter your choice (1,2,3,4): '))

        if user_choice == 1:     #user wants to log an activity
            excercise = input('Enter the type of Excercise: ').strip()
            category = input('Enter the category (Cardio, Strength, Flexibility, etc.): ')
            time_spent = int(input('Enter the time spent(in minutes): '))
            calories = int(input('Enter the calories burned: '))
            activities.append((excercise, category, time_spent, calories))    #adding the activties to the list
        
        elif user_choice == 2:
            print('\n---Daily Summary---')
            if activities:
                for activity in activities:
                    print(f'Exercise: {activity[0]}, Category: {activity[1]}, Time spent: {activity[2]} mins, Calories: {activity[3]} calories')
            
                #display the totals


def total_cal(activities):
    total_calories = 0
    
    for activity in activities:
        total_calories += activity[3]

    return total_calories


def calculate_bmi():
    height_m = user_data['Height'] / 3.281
    weight_kg = user_data['Weight'] * 0.453592    #convert lbs to kg
    bmi = weight_kg / (height_m**2)
    return bmi

def highest_cal_activity(activities):
    if not activities:
        return None
    else:
        return max(activities, key=lambda x: x[3])  #this finds the tuple with the max calories burned

def calc_total_time(activities):
    total_time = 0 

    for activity in activities:
        total_time += activity[2]
    
    return total_time


