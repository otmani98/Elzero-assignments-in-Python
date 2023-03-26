#24-25

#assign01
# Needed Output
# "Osama"
# <class 'tuple'>
tup= 'Ahmed',
print(tup)
print(type(tup))

#assign02
friends = ("Osama", "Ahmed", "Sayed")
# Needed Output
# ("Elzero", "Ahmed", "Sayed")
# <class 'tuple'>
# 3 Elements
friends = list(friends)
friends.remove("Osama")
friends.insert(0, "Elzero")
friends = tuple(friends)
print(friends)
print(type(friends))


#assign03
nums = (1, 2, 3)
letters = ("A", "B", "C")
# Needed Output
# nums_and_letters_one = (1, 2, 3, "A", "B", "C")
# 6 Elements
new_tup = nums + letters
print(new_tup)
print(len(new_tup))


#assign04
my_tuple = (1, 2, 3, 4)
# Needed Output
# 1
# 2
# 4
a, b, _,c = my_tuple   #this is Destruct
print(a)
print(b)
print(c)