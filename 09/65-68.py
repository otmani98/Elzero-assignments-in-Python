#65-68



#assign01 in folder python in the same directory of this file.



# assign02

# f = open(rf"/home/yhwach/python_elzero_again/09/Python/01.txt", 'a')
# f.write('\n')

# for i in range(1,51) :

#     f.write('Appended => Elzero Web School\n')

# f.close()


#assign03

f = open(r"/home/yhwach/python_elzero_again/09/Python/01.txt", 'r')

lines = 0 
for i in f.read() :

    if i == '\n'  :
        lines += 1
    
print(f'the number of lines {lines}')

f = open(r"/home/yhwach/python_elzero_again/09/Python/01.txt", 'r')
words = 0
for i in f.read() :

    if i == '\n' or i == ' ' :

        words += 1

print(f'the number of words {words}')


f = open(r"/home/yhwach/python_elzero_again/09/Python/01.txt", 'r')
chars = 0

for i in f.read() :

    if i == '\n' or i == ' ' :

        continue

    chars += 1

print(f'the number of chars {chars}')


f = open(r"/home/yhwach/python_elzero_again/09/Python/01.txt", 'r')
l = 0

for i in f.read() :

    if i == 'l' :

        l += 1

print(f'the number of char l {l}')




# assign03
# import os 

# for i in range(41,51) :

#     if os.path.exists(f"{i}.txt"):

#         os.remove(f"{i}.txt")