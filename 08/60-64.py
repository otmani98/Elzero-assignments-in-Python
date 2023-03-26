#60-64


#assign01

def get_score(**data) :

    for module, score in data.items() :

        print(f"{module} => {score}")


get_score(Math=90, Science=80, Language=70)
get_score(Logic=70, Problems=60)



print("="*40)


#assign2

def get_people_scores(name="", **data) :

    if name and data:

        print(f"Hello {name} This Is Your Score Table:")

        for module, score in data.items() :

            print(f"{module} => {score}")

    elif not name and data :

        for module, score in data.items() :

            print(f"{module} => {score}")

    elif name and not data :

        print(f"Hello {name} You Have No Scores To Show")



get_people_scores("Osama", Math=90, Science=80, Language=70)
get_people_scores("Mahmoud", Logic=70, Problems=60)
get_people_scores(Logic=70, Problems=60)
get_people_scores("Ahmed")







#assign3

scores_list = {
    "Math" : 90,
    "Science" : 80,
    "Language" : 70
}

# Test 1
get_people_scores("Osama", **scores_list)

# Test 2
get_people_scores("Osama")

# Test 3
get_people_scores(**scores_list)
