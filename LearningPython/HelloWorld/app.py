# import math

# course = "Python Programming"
# print(len(course))
# print(course[0])
# print(course[-1])
# print(course[0:3])
# print(course[0:])
# print(course[:3])
# print(course[:])
# print(course[::3])

# course = 'Python "Programming'
# print(course)


# first = "John"
# last = "Doe"
# full = f"{first} {last}"
# print(full)

# course = "   python programming   "

# print(course.upper())
# print(course.lower())
# print(course.title())
# print(course.strip())
# print(course.find("pro"))
# print(course.replace("p", "j"))
# print("pro" in course)
# print("swift" not in course)


# print(10 + 3)
# print(10 - 3)
# print(10 * 3)
# print(10 / 3)
# print(10 // 3)
# print(10 % 3)
# print(10**3)

# x = 10
# x = x + 3
# x += 3

# print(x)


# print(round(2.9))
# print(abs(-2.9))

# print(math.ceil(2.2))
# print(math.floor(2.2))


# x = input("x: ")
# print(type(x))
# y = int(x) + 1

# print(f"x: {x}, y: {y}")

# print("bag" == "BAG")
# print(ord("b"))

# temparature = 20
# if temparature > 30:
#     print("It's warm")
#     print("Drink water")
# elif temparature > 20:
#     print("It's nice")
# else:
#     print("It's cold")
# print("Done")

# age = 22
# if age >= 18:
#     message = "Eligible"
# else:
#     message = "Not eligible"

# message = "Eligible" if age >= 18 else "Not eligible"
# print(message)


# high_income = False
# good_credit = True
# student = True

# if high_income or good_credit or student:
#     print("Eligible")


# age = input("")
# age = int(age)
# if 19 <= age < 65:
#     print("Eligible")

# for number in range(1, 10, 2):
#     print("Attempt", number, number * ".")

# successful = False
# for number in range(3):
#     print("Attempt")
#     if successful:
#         print("Successful")
#         break
# else:
#     print("Attempted 3 times and failed")


# for x in range(5):
#     for y in range(3):
#         print(f"({x}, {y})")


# print(type(range(5)))

# for x in [1, 2, 3, 4, 5]:
#     print(x)


# number = 100
# while number > 0:
#     print(number)
#     number //= 2


# command = ""
# while command.lower() != "quit":
#     command = input(">")
#     print("ECHO", command)

# command = ""
# while True:
#     command = input(">")
#     print("ECHO", command)
#     if command == "quit":
#         break

# count = 0

# for number in range(1, 10):
#     if number % 2 == 0:
#         count += 1
#     print(number)
# print(f"There are {count} even numbers")


# def greet(first_name, last_name):
#     print(f"Hi {first_name} {last_name}")


# greet("John", "Doe")


# def greet(name):
#     print(f"Hi {name}")


# def get_greet(name):
#     return f"Hi {name}"


# message = get_greet("John")
# print(message)


# def increment(number, by=1):
#     return number + by


# print(increment(2))


def multiply(*numbers):
    product = 1
    for number in numbers:
        product *= number
    return product


print(multiply(2, 3, 4, 5))
