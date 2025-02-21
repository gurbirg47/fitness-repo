# Global list to store activities
activities = []

def greet(username):
    print(f'Hi {username.title()}, Welcome to the Fitness Tracker!')

username = input('Enter your Name: ')
greet(username)

# Get details from user for fitness profile
def user_profile():
    print(
        f'{username.title()}, please enter your age, weight, and fitness goals '
        'so we can personalize your experience and provide recommendations.'
    )

    profile = {
        'Age': None,
        'Weight': None,
        'Height': None,
        'Goals': None
    }

    while True:
        print(f'\n{username.title()}, please enter your details:')
        try:
            profile['Age'] = int(input('Enter your age: '))
            profile['Weight'] = float(input('Enter your weight (lb): '))
            profile['Height'] = float(input('Enter your height (ft): '))
            profile['Goals'] = input('What are your fitness goals? ').strip()

            # Display Profile Summary
            print('\n--- Summary of Your Profile ---')
            print(f'Age: {profile["Age"]} years')
            print(f'Weight: {profile["Weight"]} lbs')
            print(f'Height: {profile["Height"]} ft')
            print(f'Goals: {profile["Goals"]}')

            # Ask user if they want to edit profile
            edit = input('\nWould you like to make changes to your profile? (yes/no): ').strip().lower()
            if edit == 'yes':
                field_to_edit = input('Which field would you like to edit? (Age/Weight/Height/Goals) ').strip().title()
                if field_to_edit in profile:
                    new_value = input(f"Enter new value for {field_to_edit}: ")
                    profile[field_to_edit] = float(new_value) if field_to_edit in ['Weight', 'Height'] else new_value
                else:
                    print("Invalid choice. No changes made.")
            else:
                print('Thank you! Your profile is complete.')
                break
        except ValueError:
            print("Invalid input. Please enter numeric values for Age, Weight, and Height.")

    return profile

# Store user profile data
user_data = user_profile()

# Main Function for the Program
def main():
    print('\nWelcome To the Fitness Tracker')

    while True:
        print('\n---Menu---')
        print('1. Log an Activity')
        print('2. View Summary')
        print('3. Calculate BMI')
        print('4. View User Profile')
        print('5. Quit')

        user_choice = input('Enter your choice (1,2,3,4,5): ').strip()

        # Validate user input
        if not user_choice.isdigit() or int(user_choice) not in range(1, 6):
            print("Invalid choice. Please enter a number between 1 and 5.")
            continue

        user_choice = int(user_choice)  

        # Log an Activity
        if user_choice == 1:
            global activities  # Ensure we modify the global list
            exercise = input('Enter the type of exercise: ').strip()
            category = input('Enter the category (Cardio, Strength, Flexibility, etc.): ').strip()
            try:
                time_spent = int(input('Enter the time spent (in minutes): '))
                calories = int(input('Enter the calories burned: '))
                activities.append((exercise, category, time_spent, calories))
                print("Activity logged successfully!")
            except ValueError:
                print("Error: Please enter a valid number for time and calories.")

        # View Summary
        elif user_choice == 2:
            print('\n---Daily Summary---')

            if activities:
                for activity in activities:
                    print(f'Exercise: {activity[0]}, Category: {activity[1]}, Time: {activity[2]} mins, Calories: {activity[3]}')

                # Display Totals
                total_calories = total_cal(activities)
                total_time = calc_total_time(activities)
                print(f'Total Calories Burned: {total_calories}')
                print(f'Total Time Spent Exercising: {total_time} mins')

                # Display highest calorie-burning activity
                top_activity = highest_cal_activity(activities)
                if top_activity:
                    print(f'Highest Calorie-Burning Activity: {top_activity[0]} ({top_activity[3]} calories)')
            else:
                print("No activities logged yet. Log an activity first!")

        # Calculate BMI
        elif user_choice == 3:
            bmi = calculate_bmi(user_data)
            print(f'Your BMI is: {bmi:.2f}')

        # View User Profile
        elif user_choice == 4:
            print('\n---User Profile---')
            print(f'Name: {username.title()}')
            print(f'Age: {user_data["Age"]} years')  
            print(f'Weight: {user_data["Weight"]} lbs')  
            print(f'Height: {user_data["Height"]} ft')  
            print(f'Goals: {user_data["Goals"]}')  

        # Quit
        elif user_choice == 5:
            print('Thank you for using the Fitness Tracker! Exiting...')
            break 

# Function to calculate total calories burned
def total_cal(activities):
    return sum(activity[3] for activity in activities)

# Function to calculate BMI
def calculate_bmi(user_data):
    height_m = user_data["Height"] / 3.281  # Convert feet to meters
    weight_kg = user_data["Weight"] * 0.453592  # Convert lbs to kg
    return weight_kg / (height_m ** 2)  # BMI formula

# Function to find the highest calorie-burning activity
def highest_cal_activity(activities):
    return max(activities, key=lambda x: x[3]) if activities else None

# Function for total excercise time
def calc_total_time(activities):
    return sum(activity[2] for activity in activities)

#run program
if __name__ == '__main__':
    main()