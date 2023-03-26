#56-59


#assign01
def calculate(n1, n2, op="a") :

    op = op.lower()

    if op == "add" or op == "a" :

        return (n1 + n2)
    
    elif op == "subtract" or op == "s" :

        return (n1 - n2)
    
    elif op == "multiply" or op == "m" :

        return (n1 * n2)
    
    else :

        return "Wrong operator"

# Tests
print(calculate(10, 20)) # 30
print(calculate(10, 20, "AdD")) # 30
print(calculate(10, 20, "a")) # 30
print(calculate(10, 20, "A")) # 30

print(calculate(10, 20, "S")) # -10
print(calculate(10, 20, "subTRACT")) # -10

print(calculate(10, 20, "Multiply")) # 200
print(calculate(10, 20, "m")) # 200






#assign2

def addition(*tup) :

    sum = 0

    for i in tup :

        if i == 10 :

            continue
        
        if i == 5 :

            sum -= 10

        sum+= i

    return sum

print(addition(10, 20, 30, 10, 15)) # 65
print(addition(10, 20, 30, 10, 15, 5, 100)) # 160






#assign3

def show_skills(name, *skills) :

    if len(skills) < 1 :

        print(f"Hello {name} You Have No Skills To Show")

    else :

        print(f"Hello {name} your skills is:")

        for skill in skills :

            print(f"-{skill}")


show_skills("Osama", "HTML", "CSS", "JS", "Python")
show_skills("Ahmed")








# assign04

def say_hello(name="Unknown",age="Unknown",country="Unknown") :

    return f"Hello {name} Your Age Is {age} And You Live In {country}"

print(say_hello("Osama", 38, "Egypt"))
print(say_hello())



