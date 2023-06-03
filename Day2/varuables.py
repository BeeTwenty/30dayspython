# Day 2: 30 days of python
first_name = "Sindre"
last_name = "Berge"
full_name = first_name + " " + last_name
country = "Norway"
city = "Stavanger"
age = 27
year = 1996
is_married = False
is_true = True
is_light_on = False
yes, no = True, False

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(yes))
print(type(no))

print(len(first_name))
print("first name is",len(first_name), "letters and last name is ", len(last_name), " long")

num_one = 5
num_two = 4
total = num_two + num_two
print(total)
diff = num_one - num_two
print(diff)
multiple = num_one * num_two
print(multiple)
devide = num_one / num_two
print(devide)
reminder = num_one % num_two
print(reminder)
exp = num_one ** num_two
print(exp)
floor_devision = num_one // num_two
print(floor_devision)


area_of_circle = 3.14 * 30**2
print(area_of_circle)

c = 2 * 3.14 * 30
print(c)

user_circle = input("Enter radius of circle: ")
user_circle  = int(user_circle)
user_area = 3.14 * user_circle ** 2
user_c = 2 * 3.14 * user_circle
print("your circle area is ", user_area, " and the c is ", user_c )

user_firstname = input("What is your first name? ")
user_lastname  = input("and your last name? ")
user_country = input("and where are you from? ")
user_age = input("and lastly how old are you? ")
print("Hello", user_firstname,  user_lastname, "! good to see you i can see that you are from", user_country, "and that you are", user_age, "old!")

