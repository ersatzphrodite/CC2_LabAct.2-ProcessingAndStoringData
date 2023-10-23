import pandas as pd

# PART I

# 1. User Profile/ PART III: Error Handling
print("+ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ User Profile ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ +")
name = input("Enter your name: ")

while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError:
        print("Error: Age should be a whole number. Please enter a valid age.")

degree = input("Enter your degree: ")

valid_degrees = ["BS IT", "BS CS", "BS DA"]  # Add more valid degrees as needed
while degree not in valid_degrees:
    print("Error: Invalid degree. Please enter a valid degree (e.g., BS IT, BS CS, BS DA).")
    degree = input("Enter your degree: ")

email = input("Enter your email: ")

while "@" not in email:
    print("Error: Email should contain '@'. Please enter a valid email.")
    email = input("Enter your email: ")

hobbies = []
skills = []

for i in range(3):
    while True:
        hobby = input(f"Enter hobby {i + 1}: ")
        if hobby in hobbies:
            print("Error: Duplicate hobby. Please enter a unique hobby.")
        else:
            hobbies.append(hobby)
            break

for i in range(3):
    while True:
        skill = input(f"Enter skill {i + 1}: ")
        if skill in skills:
            print("Error: Duplicate skill. Please enter a unique skill.")
        else:
            skills.append(skill)
            break

print("+ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ +")

profile = f"""

+ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ User Profile ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ +        
  NAME:    {name}               
  AGE:     {age}                
  DEGREE:  {degree}             
  EMAIL:   {email}              
  HOBBIES: {', '.join(hobbies)} 
  SKILLS:  {', '.join(skills)}  
+ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ +

"""

print(profile)

# 2. Item List
print("+ ~ ~ ~ ~ ~ Item List: Music Composers from the Classical Era ~ ~ ~ ~ ~ +")
initial_composers = ['Mozart', 'Tchaikovsky', 'Beethoven', 'JS Bach', 'Schubert']
composers_df = pd.DataFrame(initial_composers, columns=['Classical Composers'])
composers_df.index = range(1, len(composers_df) + 1)
print(composers_df)

new_composers = [input("Enter a new music composer: ") for _ in range(5)]
updated_composers = initial_composers + new_composers
updated_composers_df = pd.DataFrame(updated_composers, columns=['Classical Composers'])
updated_composers_df.index = range(1, len(updated_composers_df) + 1)

print("\n+ ~ ~ ~ ~ ~ Item List: Music Composers from the Classical Era ~ ~ ~ ~ ~ +")
print(updated_composers_df)
print("+ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ +")

# PART II: chArlIz EphIny bEllO mAcAlAndA = 10 vowels/SET C

time_units = {
    1: "SECOND",
    2: "MINUTE",
    3: "HOUR",
    4: "DAY",
    5: "MONTH",
    6: "YEAR",
}


def main():
    print("TIME CONVERSION")
    print("1 - SECOND, 2 - MINUTE, 3 - HOUR, 4 - DAY, 5 - MONTH, 6 - YEAR")

    while True:
        try:
            from_unit = int(input("Select the time unit to convert from (1-6): "))
            if from_unit not in time_units:
                print("Invalid input. Please select a valid time unit.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number (1-6).")

    while True:
        try:
            to_unit = int(input("Select the time unit to convert to (1-6, different from the previous choice): "))
            if to_unit not in time_units or to_unit == from_unit:
                print("Invalid input. Please select a valid and different time unit.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number (1-6).")

    while True:
        try:
            number_to_convert = float(
                input(f"Enter the number to convert from {time_units[from_unit]} to {time_units[to_unit]}: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    converted_value = convert_time(number_to_convert, from_unit, to_unit)

    print(f"{number_to_convert} {time_units[from_unit]} is equal to {converted_value} {time_units[to_unit]}.")


def convert_time(value, from_unit, to_unit):

    conversion_factors = {
        (1, 2): 1 / 60,
        (1, 3): 1 / 3600,
        (1, 4): 1 / 86400,
        (1, 5): 1 / 2628000,
        (1, 6): 1 / 31536000,
        (2, 3): 1 / 60,
        (2, 4): 1 / 1440,
        (2, 5): 1 / 43800,
        (2, 6): 1 / 525600,
        (3, 4): 1 / 24,
        (3, 5): 1 / 720,
        (3, 6): 1 / 8760,
        (4, 5): 30.44,
        (4, 6): 365,
        (5, 6): 12
    }

    conversion_key = (from_unit, to_unit)

    if conversion_key in conversion_factors:
        return value * conversion_factors[conversion_key]
    else:
        return value / conversion_factors[(to_unit, from_unit)]


 if __name__ == "__main__":
    main()
