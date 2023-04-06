## This file is a love meter ##

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
add_name = name1 + name2
lower_add_name = add_name.lower()

t = add_name.count("t")
r = add_name.count("r")
u = add_name.count("u")
e = add_name.count("e")
l = add_name.count("l")
o = add_name.count("o")
v = add_name.count("v")
e = add_name.count("e")

true = (t + r + u + e) * 10
love = l + o + v + e

love_score = true + love

if (love_score < 10) or (love_score > 90):
  print(f"Your love score is {love_score}, you go together like coke and Mentos")
elif (love_score >= 40) and (love_score <= 50):
  print(f"Yout score is {love_score}, you are alright together")
else:
  print(f"Your score is {love_score}")