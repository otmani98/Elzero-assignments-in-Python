#33-37

#assign01
# Needed Output
# True
# True
# True
# True
# False
# False
# False
# False
print(bool('s'))
print(bool(5))
print(bool(10.5))
print(bool(['df']))
print(bool(""))
print(bool(0))
print(bool([]))
print(bool({}))


#assign02
html = 80
css = 60
javascript = 70
# Needed Output
# True
print(html > 50 and css > 50 and javascript > 50)


#assign03
num_one = 10
num_two = 20
num = 20
# Needed Output
# True
# False
print(num > num_one or num > num_two)
print(num > num_one and num > num_two)


#assign04
num_one = 10
num_two = 20
# Needed Output
# 30
# 27000
# 1000
# 200.0
# <class 'str'>
result = num_one + num_two
print(result)
print(result ** 3)
print((result ** 3)%26000)
print(((result ** 3)%26000)/5)
print(type(str(((result ** 3)%26000)/5)))