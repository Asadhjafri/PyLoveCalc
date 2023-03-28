# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#concatenate strings and change to lowercase.
couples_string = name1 + name2
lowercase_couples_string = couples_string.lower()

#check count for the word TRUE against couples names.
t = lowercase_couples_string.count("t")
r = lowercase_couples_string.count("r")
u = lowercase_couples_string.count("u")
e = lowercase_couples_string.count("e")

true = t + r + u + e

#check count for the word LOVE against couples names.
l = lowercase_couples_string.count("l")
o = lowercase_couples_string.count("o")
v = lowercase_couples_string.count("v")
e = lowercase_couples_string.count("e")

love = l + o + v + e

love_score = str(true) + str(love)

#Message based of result
if (love_score < 10) or (love_score > 90):
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
  print(f"Your score is {love_score}, you are alright together.")