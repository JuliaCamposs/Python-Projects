""""
Functions needed: 

# 1. add_volunteer(volunteers, name, skills, availability)
#    → adds a new volunteer to the list

# 2. log_hours(volunteers, name, hours)
#    → adds hours to a specific volunteer

# 3. total_hours(volunteers, name)
#    → returns total hours for a specific volunteer

# 4. most_active_volunteer(volunteers)
#    → returns the volunteer with the most hours

# 5. match_volunteers(volunteers, events, required_skill)
#    → finds volunteers whose skills match an event

# 6. generate_report(volunteers)
#    → saves a full summary to a .txt file

# 7. main()
#    → menu to tie everything together

"""

# step 1

def add_volunteer(volunteers, name, skills, availability):
    volunteer = {'name': name, 'skills': skills, 'availability': availability , 'hours': 0}
    volunteers.append(volunteer)
    return volunteers

# step 2

def log_hours(volunteers, name, hours):
    for volunteer in volunteers:
        if volunteer['name'] == name:
            volunteer['hours'] += hours
    return volunteers

# step 3

def total_hours(volunteers, name):
    for volunteer in volunteers:
        if volunteer['name'] == name:
            return volunteer['hours']
        
# step 4

def most_active_volunteer(volunteers):
    return max(volunteers, key=lambda x: x['hours'])


# step 5 

def match_volunteers(volunteers, required_skills):
    matched = []
    for volunteer in volunteers:
        if required_skills in volunteer['skills']:
            matched.append(volunteer)
    return matched 


# step 6 

def generate_report(volunteers):
    file = open("report.txt", "w") # creates file
    for volunteer in volunteers:
        file.write("Name: " + volunteer['name'] + "\n")
        file.write("Skills: " + str(volunteer['skills']) + "\n")
        file.write("Availability: " + volunteer['availability'] + "\n")
        file.write("Hours: " + str(volunteer['hours']) + "\n")
        file.write("--------------------\n")
    file.close()  # always close it 
    print("Report saved to report.txt! ✅")


# step 7 

def main():
    volunteers = []
    while True:
        print("\n1. Add volunteer")
        print("2. Log hours")
        print("3. Total hours")
        print("4. Most active volunteer")
        print("5. Match volunteers by skill")
        print("6. Generate report")
        print("7. Quit")

        choice = input("Pick an option: ").strip()

        if choice == '7':
            print("Goodbye!")
            break

        elif choice == '1':
            name = input("Name: ")
            skills = input("Skills (comma separated): ").split(",") # turns input into list automatically
            availability = input("Availability: ")
            volunteers = add_volunteer(volunteers, name, skills, availability)
            print("Volunteer added! ✅")

        elif choice == '2':
            name = input("Volunteer name: ")
            hours = float(input("Hours to log: "))
            log_hours(volunteers, name, hours)
            print("Hours logged! ✅")

        elif choice == '3':
            name = input("Volunteer name: ")
            print(f"Total hours: {total_hours(volunteers, name)}")

        elif choice == '4':
            result = most_active_volunteer(volunteers)
            print(f"Most active: {result['name']} with {result['hours']} hours")

        elif choice == '5':
            skill = input("Required skill: ")
            matched = match_volunteers(volunteers, skill)
            for v in matched:
                print(f"- {v['name']}")

        elif choice == '6':
            generate_report(volunteers)

main()

