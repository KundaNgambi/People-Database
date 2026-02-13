

import csv
from datetime import datetime
from collections import Counter


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


def age_analysis():

    with open(filename, 'r', newline="") as file:
        reader = csv.DictReader(file)

        people = {}

        for row in reader:
            birthday_str = row['Date of birth']
            birthday = datetime.strptime(birthday_str,"%Y-%m-%d")

            fullname = f"{row['First Name']} {row['Last Name']}"
            people[fullname] = birthday

    return people

data = age_analysis()

for name,birthday in data.items():
    print(name, '-', birthday.date())

oldest = min(data,key=data.get)
youngest = max(data, key=data.get)

print("Oldest:", oldest, "-", data[oldest].date())
print("Youngest:", youngest, "-", data[youngest].date())


def job_analysis():


    job_titles = []

    with open(filename,'r', newline = "") as file:
        read = csv.DictReader(file)

        for row in read:

            job_titles.append(row['Job Title'])

        count_titles = Counter(job_titles)
        count_dict = dict(count_titles)

        sorted_items = sorted(count_dict.items(), key=lambda x: x[1],reverse=True)

        first_five = sorted_items[:5]

        print("Top 5 Most Common Jobs:")

        for index, (job, count) in enumerate(first_five, start=1):
            print(f"{index}. {job}: {count} people")




job_analysis()