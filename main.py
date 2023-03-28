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
