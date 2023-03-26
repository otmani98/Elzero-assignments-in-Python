#41-46

#assign01
# Inputs
num1 = int(input("Enter First Number: ").strip())
num2 = int(input("Enter Second Number: ").strip())
operation = input('Enter the Operation "+" Or "-" Or "*" Or "/" Or "%" :==> ').strip()
# Needed Output
# [num1 20] [operation +] [num2]
# Example One 20 + 40 = 60
# Example Two 20 * 40 = 800
if operation == '+' :

    print(f"{num1} {operation} {num2} = {num1 + num2}")

elif operation == '-' :

    print(f"{num1} {operation} {num2} = {num1 - num2}")

elif operation == '*' :

    print(f"{num1} {operation} {num2} = {num1 * num2}")

elif operation == '/' :

    print(f"{num1} {operation} {num2} = {num1 / num2}")

elif operation == '%' :

    print(f"{num1} {operation} {num2} = {num1 % num2}")

else :

    print("Wrong Operation")


#assign02
age = 17
# Needed Output
print("App Is Suitable For You" if age > 16 else "App Is Not Suitable For You")



#assign03
# Input Example 38
# Needed Output
# "Your Age In Months Is 456 Months" # Months Example
# "Your Age In Weeks Is 1824 Weeks" # Weeks Example
age_for_calc = 38

if age_for_calc < 100 and age_for_calc > 10 :

    in_months = age_for_calc * 12
    in_weeks = in_months * 4
    in_days = in_weeks * 7
    in_hours = in_days * 24
    in_minutes = in_hours * 60
    in_seconds = in_minutes * 60
    print(f"Your Age In Monthes Is {in_months} Months")
    print(f"Your Age In Weeks Is {in_weeks} Weeks")
    print(f"Your Age In Days Is {in_days} Days")
    print(f"Your Age In Hours Is {in_hours} Hours")
    print(f"Your Age In Minutes Is {in_minutes} Minutes")
    print(f"Your Age In Seconds Is {in_seconds} Seconds")

else :

    print("This Age is out the range.")


# Input Example One "Egypt"
# Input Example Two "Ghana"
country = input("Input Your Country: ").strip().title()
countries = ["Egypt", "Palestine", "Syria", "Yemen", "Ksa", "Usa", "Bahrain", "England"]
price = 100
discount = 30

if country in countries :

    print(f"Your Country Eligible For Discount And The Price After Discount Is {price - discount}$")

else :

    print(f"Your Country Not Eligible For Discount And The Price Is {price}$")
