#51-55




#assign01
my_nums = [15, 81, 5, 17, 20, 21, 13]
# Needed Output
# "1 => 20"
# "2 => 15"
# "3 => 5"
# "All Numbers Printed"
my_nums.sort(reverse=True)

rank = 1

for i in my_nums :

    if i % 5 == 0 :

        print(f" {rank} => {i} ")

        rank += 1

print("All Numbers Printed")







#assign02

for i in range(1,21) :

    if i == 6 or i == 8 or i == 12 :

        continue

    print(f"{i}".zfill(2))

print("All Numbers Are Printed")







#assign03

my_ranks = {
  'Math': 'A',
  "Science": 'B',
  'Drawing': 'A',
  'Sports': 'C'
}

a, b, c, d = 100, 80, 40, 20

all = 0

for module in my_ranks :

    if my_ranks[module] == 'A' :

        print(f"My rank in {module} is {my_ranks[module]} And this equal {a} points")
        
        all += a
    
    elif my_ranks[module] == 'B' :

        print(f"My rank in {module} is {my_ranks[module]} And this equal {b} points")
        
        all += b

    else:

        print(f"My rank in {module} is {my_ranks[module]} And this equal {c} points")
        
        all += c

print(f"Total Points is {all}")



#assign04

students = {
  "Ahmed": {
    "Math": "A",
    "Science": "D",
    "Draw": "B",
    "Sports": "C",
    "Thinking": "A"
  },
  "Sayed": {
    "Math": "B",
    "Science": "B",
    "Draw": "B",
    "Sports": "D",
    "Thinking": "A"
  },
  "Mahmoud": {
    "Math": "D",
    "Science": "A",
    "Draw": "A",
    "Sports": "B",
    "Thinking": "B"
  }
}

points = 0
    
for student in students :

    print("------------------------------")
    print(f"--Student Name => {student}")
    print("------------------------------")
    
    for module in students[student] :

        if students[student][module] == 'A' :
            print(f"-{module} => {a}")
            points+=a
        elif students[student][module] == 'B' :
            print(f"-{module} => {b}")
            points+=b
        elif students[student][module] == 'C' :
            print(f"-{module} => {c}")
            points+=c
        else :
            print(f"-{module} => {d}")
            points+=d

    print(f"Total Points For Ahmed Is {points}")
    points = 0

print("="*40)
print("="*40)

for student, modules_ranks in students.items() :

    print("------------------------------")
    print(f"--Student Name => {student}")
    print("------------------------------")
    
    for module, rank in modules_ranks.items() :

        if rank == 'A' :
            print(f"-{module} => {a}")
            points+=a
        elif rank == 'B' :
            print(f"-{module} => {b}")
            points+=b
        elif rank == 'C' :
            print(f"-{module} => {c}")
            points+=c
        else :
            print(f"-{module} => {d}")
            points+=d

    print(f"Total Points For Ahmed Is {points}")
    points = 0