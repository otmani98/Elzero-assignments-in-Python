#47-50



#assing01
num = 5 #int(input("enter number: ").strip())
counter = 0

if type(num) == int and num > 0 :

    while num > 1 :

        num -= 1

        if num == 6 :

            continue

        print(num)

        counter += 1

    else :

        print(f"{counter} Numbers Printed Successfully.")

else :

    print("The Numeber Must be greater than Zero")





#assing02
# Input
friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]
a = 0
count = 0
# Needed Output
# "Mohamed"
# "Shady"
# "Sherif"
# "Friends Printed And Ignored Names Count Is 2"
while a < len(friends) :

    if friends[a].islower() :

        count += 1
    
    else :

        print(friends[a])

    a += 1

else :

    print(f"Friends Printed And Ignored Names Count Is {count}")


#assign 03
skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]

while skills:

  # Type The Code Here in One Line
  print(skills.pop(0))

# Needed Output
# "HTML"
# "CSS"
# "JavaScript"
# "PHP"
# "Python"





#assign 04
my_friends = []
while len(my_friends) != 4 :

    name = input("Enter Name To Add the list of friends:").strip()

    if name.isupper() :

        print("This is A valid Name")

    else :

        my_friends.append(name.title())

        print(f"Friend {name} Added => 1st Letter Become Capital")

        print(f"Names Left in List Is {4-len(my_friends)}")


else :

    print(my_friends)