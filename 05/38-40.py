#38-40

#assign01
# Input
name = input("Enter You Name:")
# Needed Output
# "Hello Osama, Happy To See You Here."
print(f"Hello {name.title().strip()}, Happy To See You Here.")


#assign02
age = int(input("Enter your Age: "))

if age < 16 :

    print("Hello Your Age Is Under 16, Some Articles Is Not Suitable For You")

else :

    print(f"Hello Your Age Is {age}, All Articles Is Suitable For You")


#assign03
f_name = input("Enter You First Name:").strip().title()
s_name = input("Enter You Second Name:").strip().title()
print(f"Hello {f_name} {s_name[0]}.")


#assign04
# Inputs
"Osama@Nn.Sa" # Email
# Needed Output
"Your Name Is Osama"
"Email Service Provider Is nn"
"Top Level Domain Is sa"
email = input("Enter Your Email:" ).strip().lower()
print(f"Your Name Is {(email[0:email.index('@')]).title()}")
print(f"Email Service Provider Is {email[email.index('@')+1:email.index('.')]}")
print(f"Top Level Domain Is {email[email.index('.')+1:]}")