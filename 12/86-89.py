#86-89


#assign01
my_list = ["E", "Z", "R", 1, 2, 3]
my_tuple = ("L", "E", "O")
my_data = []

for data in zip(my_list, my_tuple):
  # Write Your Code Here
  my_data.append(data[0])
  my_data.append(data[1])

final_string = ''.join(my_data).title()

print(final_string) # Elzero


#assign02
my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
my_tuple = ("E", "Z", "R", 1, 2, "E", "R", "O")
my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
my_data = []

for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):
  # Write Your Code Here
  if type(item1) == int :
    continue
  my_data.append(item1)

final_string = ''.join(my_data).title()

print(final_string)



#assign03
from PIL import Image

myImage = Image.open(r"/home/yhwach/elzero-pillow.png")


myBox = (400, 10, 800, 400)
myNewImage = myImage.crop(myBox)
myConverted = myNewImage.convert("L")
myConverted.show()
myConverted.save(r"/home/yhwach/elzero-pillow-L.png")


myBox2 = (10, 400, 1200, 800)
myNewImage2 = myImage.crop(myBox2)
myConverted2 = myNewImage2.convert("L").rotate(180)
myConverted2.show()
myConverted2.save(r"/home/yhwach/elzero-pillow-L2.png")


# assign04

def say_hello_to(name) -> str :
  
  """parameter(someone) => Person Name
  Function To Say Hello To Anyone"""
  
  return f"Hello {name}"
 

print(say_hello_to("Osama"))

print(say_hello_to.__doc__)


# sudo apt install pylint
# pylint file.py
# pylint file.py --disable=missing-docstring   ===> to skip this role
# tab with 4 spaces
# new line in the final
# function with snake_case naming and variables...
# docs are important for functions and modules
# (assign05) the tests in pylint_test.py not here