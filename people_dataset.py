

import csv

filename = 'people-100.csv'

def User_count():


    with open(filename,'r',newline = "") as file:
        reader = csv.DictReader(file)

        number_males = 0
        number_females = 0
        number_people = 0

        for row in reader:
            number_people += 1

            if row['Sex']  == 'Male':
                number_males +=1
            elif row['Sex']  == 'Female':
                number_females +=1

    print(f"Total Users: {number_people}")
    print(f'Number Males: {number_males}')
    print(f'Number Females: {number_females}')

User_count()
