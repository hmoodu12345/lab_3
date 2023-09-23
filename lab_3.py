print("Q1:")
dic = {}
while (True):
    name = input("enter emp name")
    if name.lower() == "no":
        break

    if not name.isalpha():
        print("name must be string")
        continue

    sal = input("enter emp salary")

    if sal.lower() == "no":
        break

    if not sal.isdigit():
        print("salary must be float")

        continue

    dic[name] = sal

print("the dictionry is:")
print(dic)

print("===============================")
print("Q2:")

lis = []
c = 0
for i in range(10):
    try:
        num = int(input("enter a number"))
    except:
        print("wrong input!!")
        c += 1
        continue

    lis.append(num)
    max = lis[0]
    for i in lis:
        if i > max:
            max = i
if c == 10:
    print("you did not put any vaild number on the list!!")
else:
    print(f"the max is {max}")

print("===============================")
print("Q3:")

try:
    cel = float(input("enter the temperature in Celsius"))
    print(f"the temperature in Fahrenheit is: {9 / 5 * cel + 32}")
except:
    print("wrong input!!")

print("===============================")
print("Q4:")

try:
    a = int(input("enter a number"))
    for i in range(1, 11):
        r = a * i
        print(f"{a} * {i} = {r}")
except:
    print("wrong input!!")

print("===============================")
print("Q5:")


# Define the decorator function
def repeat_hello(num_repetitions):
    def decorator(func):
        def wrapper():
            for _ in range(num_repetitions):
                func()

        return wrapper

    return decorator


# Get the number of repetitions from the user
x = int(input("Enter a number of repetitions: "))


# Decorate the hello function
@repeat_hello(x)
def hello():
    print('Hello')


# Call the decorated hello function
hello()
