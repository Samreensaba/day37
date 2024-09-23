import os, time

os.system("clear")

title = f"STAR WARS NAME GENERATOR"


userDetails = input("Enter your first name, last name, mum's maiden name and the city you were born in(seperated by space): ")
x = userDetails.split()


a = x[0][0:3]
b = x[1][0:2]
c = x[2][0:2]
d = x[3][0:3]

firstName = a + b
lastName = c + d

starWars = f"{firstName.capitalize()} {lastName.capitalize()}"

print(f"Your Star Wars name is {starWars}")