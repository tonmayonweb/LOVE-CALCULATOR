# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
new_name = name1 + name2
new_name_lower= new_name.lower()
T = new_name_lower.count("t")
R = new_name_lower.count("r")
U = new_name_lower.count("u")
E = new_name_lower.count("e")
L = new_name_lower.count("l")
O = new_name_lower.count("o")
V = new_name_lower.count("v")
E =new_name_lower.count("e")
true_count = T+R+U+E
love_count = L+O+V+E
# print(f" Love percentage{true_count}{love_count} %")
love_percentage = str(true_count) + str(love_count)
love_percentage_int = int(love_percentage)

if love_percentage_int<=10 or love_percentage_int>90:
  print(f"Your score is {love_percentage_int}, you go together like coke and mentos.")
elif love_percentage_int>=40 and love_percentage_int<=50:
  print(f"Your score is {love_percentage_int}, you are alright together.")
else:
  print(f"Your score is {love_percentage_int}.")