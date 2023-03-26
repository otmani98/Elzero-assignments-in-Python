#81-85


#assign01

def reverse_string(my_string):
  # Your Code Here
  yield my_string[::-1]

# Reverse The String
for c in reverse_string("Elzero"):
  print(c)



#assign02

def my_decarator(func) :
    def function_wrapper() :
        print("Sugar Added From Decorators")
        func()
        print("#"*30)
    return function_wrapper


@my_decarator
def make_tea():
  print("Tea Created")


@my_decarator
def make_coffe():
  print("Coffe Created")

make_tea()
make_coffe()