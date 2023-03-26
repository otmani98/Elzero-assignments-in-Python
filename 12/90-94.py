#90-94

#assign01

NUM = input("Add Your Number ")

if len(NUM) > 1 :

    raise IndexError("Only One Character Allowed")

elif NUM.isalpha():

    raise Exception("Only Numbers Allowed")

elif len(NUM) == 1 :

    if int(NUM) <= 0 :

        raise ValueError("Number Must Be Larger Than 0")
    
    else:

        print("#"*25)
        print(f"The Number Is {NUM}")
        print("#"*25)


#assign02

LETTER = input("Add Letter From A to Z")

try:

    if len(LETTER) > 1 :

        raise Exception

    elif not LETTER.isupper():

        raise Exception

except:

    if len(LETTER) > 1 :

        print("You Must Write One Character Only")

    elif not LETTER.isupper():

        print("The Letter Not In A - Z")

else:

    print(f"You typed {LETTER}")
    
        
#assign03

def calculate(num1, num2) -> int:
  return num1 + num2

print(calculate(20, 30))
