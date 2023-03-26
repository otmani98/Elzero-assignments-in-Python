#21-23

#assign01
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
# Needed Output
# "Osama" => Method One
# "Osama" => Method Two
# "Mahmoud" => Method One
# "Mahmoud" => Method Two
print(friends[0])
print(friends[friends.index('Osama')])
print(friends.pop(0))

print(friends[-1])
print(friends[friends.index('Mahmoud')])
print(friends.pop(-1))



#assign02
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
# Needed Output
# "Osama", "Sayed", "Mahmoud"
# "Ahmed", "Ali"
print(friends[::2])
print(friends[1::2])

#assign03
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
# Needed Output
# "Ahmed", "Sayed", "Ali",
# "Ali", "Mahmoud"
print(friends[:5:2])
print(friends[1:5:2])


#assign04
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
# Needed Output
# ["Osama", "Ahmed", "Sayed", "Elzero", "Elzero"]
friends.remove("Ali")
friends.remove("Mahmoud")
friends.append("Elzero")
friends.append("Elzero")
print(friends)


#assign05
friends = ["Osama", "Ahmed", "Sayed"]
# Needed Output
# ["Nasser", "Osama", "Ahmed", "Sayed"]
# ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]
friends.append("Salem")
friends.insert(0, "Nacer")
print(friends)


#assign06
friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]
# Needed Output
# ["Ahmed", "Sayed", "Salem"]
# ["Ahmed", "Sayed"]
friends.remove("Nasser")
friends.remove("Osama")
print(friends)
friends.remove("Salem")
print(friends)


#assign07
friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]
# Needed Output
# ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
friends.extend(employees)
friends += school
print(friends)


#assign08
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
# Needed Output
# ['Ahmed', 'Eman', 'Ramy', 'Samah', 'Sayed', 'Shady']
# ['Shady', 'Sayed', 'Samah', 'Ramy', 'Eman', 'Ahmed']
friends.sort()
print(friends)
friends.sort(reverse=True)
print(friends)

#assign09
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
# Needed Output
# 6
print(len(friends))


#assign010
technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]
# Needed Output
# Django
# Web
print(technologies[-1][0])
print(technologies[-1][-1])