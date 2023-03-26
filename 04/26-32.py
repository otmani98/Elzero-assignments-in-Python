#26-32

#assign01
my_list = [1, 2, 3, 3, 4, 5, 1]
# Needed Output
# 1, 2, 3, 4, 5
# <class 'list'>
# 1, 2, 3, 4
unique_list = list(set(my_list))
print(unique_list)
print(type(unique_list))
unique_list.remove(5)
print(unique_list)

#assign02
nums = {1, 2, 3}
letters = {"A", "B", "C"}
# Needed Output
# {1, 2, 3, "A", "B", "C"}
# {1, 2, 3, "A", "B", "C"}
# {1, 2, 3, "A", "B", "C"}
print(nums | letters)
print(nums.union(letters))
print(set(list(nums) + list(letters)))

#assign03
my_set = {1, 2, 3}
letters = {"A", "B", "C"}
# Needed Output
# {1, 2, 3}
# set()
# {"A", "B"}
print(my_set)
my_set.clear()
print(my_set)
letters.remove("C")
my_set = my_set.union(letters)
print(my_set)
my_set.discard("C")

#assign04
set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}
# Needed Output
# True
print(set_one.issubset(set_two))


# Create Dictionary Here
my_dic = {
    "Html" : "90%",
    "Css" : "80%",
    "Python" : "70%"
}
# Needed Output
# "HTML Progress Is 90%"
# "CSS Progress Is 80%"
# "Python Progress Is 30%"
# "AI Progress Is 20%"
print(f"{list(my_dic.keys())[0]} Progress Is {my_dic[list(my_dic.keys())[0]]}")
print(f"{list(my_dic.keys())[1]} Progress Is {my_dic[list(my_dic.keys())[1]]}")
print(f"{list(my_dic.keys())[2]} Progress Is {my_dic[list(my_dic.keys())[2]]}")
my_dic["AI"] = "20%"
print(f"{list(my_dic.keys())[3]} Progress Is {my_dic[list(my_dic.keys())[3]]}")

