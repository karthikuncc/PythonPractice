# while loop in python
count = 0
while (count < 10):
    count = count + 1
    print("Hello world is printed " + str(count))
print("Above statement is printed 10 times")

# for loop in python
# access items of a list using for loop
items = ['Pen', 'Pencil', 'Eraser', 'Scale']
for item in items:
    print(item)
# iterating characters in a String
str = "Hello World"
for ch in str:
    print(ch)
"""using range function--range(start(optional-default is 0), 
stop(required--not included), step(number--default 1))"""
for x in range(3):
    print("Printing:", x)
print("End of for loop 1")
for x in range(1, 3):
    print("Printing:", x)
print("End of for loop 2")
for x in range(3, 10, 2):
    print("Printing:", x)
print("End of for loop 3")
