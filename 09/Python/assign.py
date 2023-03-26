import os


for i in range(1,51) :

    if i == 25 :

        name = __file__[::-1]

        f = open("special-text.txt", "w")
        f.write(f"{os.getcwd()}\n{os.path.dirname(os.path.abspath(__file__))}\n{name[:name.index('/')][::-1]}")
        f.close()

        continue
 
    f = open(f"{i}.txt".zfill(6), "w")
    f.write(f"Elzero Web School => {i}.txt")
    f.close()



dir_list = os.listdir(os.path.dirname(__file__))

f = open("special-text.txt", "a")

f.write(f"\n{len(dir_list)}")

f.close()