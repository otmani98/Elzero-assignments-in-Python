#69-71


#assign01
#tuple of numbers
values = (0, 1, 2)
#this any will assign variable  my_var because there are False Value in tuple 
#So the Condition will be come true
if any(values):

  my_var = 0

#list of values
my_list = [True, 1,  1, ["A", "B"], 10.5, my_var]

#this Condition Will Come True if any of these will be True
#the first One return True because there is no false value
if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):

  print("Good")  # That's what will happend 

else:

  print("Bad")




#assign02
v = 40

my_range = list(range(v))

print(sum(my_range, v) + pow(v, v, v))  # 820



#assign03
n = 20

l = list(range(n))

if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):

  print("Good")
# Output => Good



#assign04

#build All Function

def my_all(iter):
  
    value = True
  
    for i in iter :

        if not i :
      
            value = False

    return value
        

def my_any(iter) :
   
    value = False

    for i in iter :
      
      if i :
         
        value = True

    return value
 

print(my_all([1, 2, 3])) # True
print(my_all([1, 2, 3, []])) # False

# my_any
print(my_any([0, 1, [], False])) # True
print(my_any([(), 0, False])) # False


def my_min(iter) :
   
    min_value = iter[0]

    for i in iter :
      
        if i < min_value :
         
            min_value = i

    return min_value


def my_max(iter) :
   
    max_value = iter[0]

    for i in iter :
      
        if i > max_value :
         
            max_value = i

    return max_value


# my_min
print(my_min([10, 100, -20, -100, 50])) # -100
print(my_min((10, 100, -20, -100, 50))) # -100

# my_max
print(my_max([10, 100, -20, -100, 50, 700])) # 700
print(my_max((10, 100, -20, -100, 50, 700))) # 700