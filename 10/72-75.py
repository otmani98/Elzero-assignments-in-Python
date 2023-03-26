#72-75

# assign01

friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]
# # Output
# "Eman"
# "Ahmed"
# "Sameh"
# "Osama"

def remove_chars(string) :

    return string[1:-1]

cleaned_list = map(remove_chars, friends_map)

for i in cleaned_list :

    print(i)


for i in map(lambda string : string[1:-1], friends_map) :

    print(i)


# assign02

friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]

def get_names(string) :

    if string[-1] == 'm' :

        return True
    
names = filter(get_names, friends_filter)

for i in names :

    print(i)


for i in filter(lambda string : True if string[-1]=='m' else False, friends_filter) :

    print(i)



# assign03
from functools import reduce

nums = [2, 4, 6, 2]
# Output
# 96

def op(n1, n2) :
    return n1 * n2

mul = reduce(op, nums)
print(mul)

print(reduce(lambda n1,n2 : n1*n2, nums))



# assign04

skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")


for i in  skills[::-1]:
        
    if type(i) == str :

        print(f"{skills[::-1].index(i)+50} - {i}")

print("="*40)

for index, name in enumerate(skills[::-1]) :

    if type(name) == str :

        print(f"{index+50} - {name}")

