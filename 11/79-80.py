#79-80



#assign 01
import datetime

print(f"Days From 2023-02-17 To 2021-08-10 Is => {(datetime.datetime.now() - datetime.datetime(2021, 8, 10)).days}")

# assign02

# Today Is "2021, 8, 10"

"2021-08-10"
"Aug 10, 2021"
"10 - Aug - 2021"
"10 / Aug / 21"
"10 / August / 2021"
"Tue, 10 August 2021"

my_date = datetime.datetime(2021, 4, 15)

print(my_date.date())
print(my_date.strftime('%b %d, %Y'))
print(my_date.strftime('%d - %b - %Y'))
print(my_date.strftime('%d / %b / %y'))
print(my_date.strftime('%d / %B / %Y'))
print(my_date.strftime('%a, %d %B %Y'))

