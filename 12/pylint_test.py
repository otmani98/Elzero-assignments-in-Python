

my_friends = ["Ahmed", "Osama", "Sayed"]

def say_hello(peoples_ofmine) -> list:
    """this is doc for this func"""

    for sing_le in peoples_ofmine:

        print(f"Hello {sing_le}")

say_hello(my_friends)
