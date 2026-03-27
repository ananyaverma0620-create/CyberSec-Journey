 Python Notes

1.Data Types
The data types define what kind of data we store in variables like numbers or text.It basically store different kinds of
 data.Python automatically detects the type when we assign a value.Python has  built-in data types.

i)Integer(int):
They are used for whole numbers,(either positive or negative)
a=25
b=-10
print(a*b)  #-250

ii)Float (float):
They are used for decimal values. 
price = 19.99
print(price * 2)  # 39.98

iii)String (str):
They are used for text data (sequence of characters).
name = "Ananya"
age = "20"
print("Hello " + name + " " + age)  # Hello Ananya 20

iv)Boolean (bool):
They are used for True/False values.
is_valid = True
not_valid = False
print(is_valid)  # True

v)List (list):
It is used to store multiple values.They are ordered collection .They are mutable.
num_list = [1, 2, 3]
num_list.append(4)
print(num_list)  # [1, 2, 3, 4]

vi)Dictionary (dict):
It stores data in key-value pair form.
data = {"name": "Ananya", "age": 20}
print(student["name"])  # Ananya

vii)Tuple (tuple):
It is similar to  list but it cannot change .i.e it is immutable.
point = (5, 10).

2.Loops
Loops are used to repeat a block of code..It is used as it repeats tasks efficiently.
Loops are important for processing large data step-by-step.

i)While Loop
It keeps running while condition is True.
Condition must become False or loop runs forever.
count = 1
while count <= 3:
    print(count)
    count += 1

ii)For Loop
It used to loop through a sequence.
for i in range(5):
    print(i)

iii)Loop through a list:
It uses list to loop.
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

3.Functions
Functions are reusable blocks of code that perform a specific task.Functions reduce repetition and improve readability.
In short ,it is  reusable code.

i)Basic Function:
def greet():
    print("Hello!")
greet()

ii)Function with parameters and return value:
def add(a, b):
    return a + b
print(add(2, 3))

iii)Function with default value:
def welcome(name="Guest"):
    print("Welcome", name)
welcome()
welcome("Ananya")


4.File Handling
File handling is used to store and read data from files.It work with external data.

i)Opening a file
It is used to open the file to do the task.
file = open("data.txt", "r")

ii)Reading a file
It is used to read the file.i.e read function is performed using this.
file = open("data.txt", "r")
for line in file:
    print(line)
file.close()

iii)Writing to a file
It used to perform write function on a file .i.e. it writes on the file.
file = open("data.txt", "w")
file.write("Hi Ananya . What is your age?")
file.close()

iv)Using with
It is the best option.It automatically closes the file.
with open("data.txt", "r") as file:
    content = file.read()
    print(content)

