#from 11 to 18

#assign01
Name = 'Ahmed'
Age = '38'
Country = 'Algeria'
print("\"Hello '" + Name + "', How You Doing \\ \"\"\" Your Is \"" + Age + "\"\" + And your Country Is: "+ Country )

#assign02
print("\"Hello '" + Name + "', How You Doing \\\n\"\"\" Your Is \"" + Age + "\"\" + \nAnd your Country Is: "+ Country )

#assign03-4
name = 'Elzero'
print('Second Letter Is "'+ name[1] + "\"")
print('Second Letter Is "'+ name[2] + "\"")
print('Second Letter Is "'+ name[-1] + "\"")
# Needed Output
# Second Letter Is "l"
# Third Letter Is "z"
# Last Letter Is "o"
print("\"" + name[1:4] + "\"")
print("\"" + name[0:3] + "\"")
print("\"" + name[:-1:2][::-1] + "\"")
# Needed Output
# "lze"
# "Ezr"
# "rzE"


#assign05
name = "#@#@Elzero#@#@"
print(name.strip('#@'))

#assign06
num = "20"
print(num.zfill(4))



#assign07
name_one = "Osama"
name_two = "Osama_Elzero"
# Needed Output
# @@@@@@@@@@@@@@@Osama
# @@@@@@@@Osama_Elzero
print(name_one.rjust(20,"@"))
print(name_two.rjust(20,"@"))

#assign08
name_one = "OSamA"
name_two = "osaMA"
# Needed Output
# osAMa
# OSAma
print(name_one.swapcase())
print(name_two.swapcase())

#assign09
msg = "I Love Python And Although Love Elzero Web School"
# Needed Output
# 2
print(msg.count('Love'))

#assign010
name = "Elzero"
# Needed Output
# 2
print(name.index('z'))

#assign011-12
msg = "I <3 Python And Although <3 Elzero Web School"
# Needed Output
# I Love Python And Although <3 Elzero Web School
print(msg.replace('<3', 'Love', 1))
print(msg.replace('<3', 'Love'))

#assign013
name = "Osama"
age = 38
country = "Egypt"
# Needed Output Using f""
# My Name Is Osama, And My Age Is 38, And My Country Is Egypt
print(f"My Name Is {name}, And My Age Is {age}, And My Country Is {country}")