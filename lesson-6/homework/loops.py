#1
i = 1
while i <= 10:
    print(i)
    i += 1
#2
for i in range(1, 6):
    for y in range(1, i + 1):
        print(y, end=" ")
    print()
#4

num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num * i)
#5
numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num > 500:
        break  
    if num > 150:
        continue  
    if num % 5 == 0:
        print(num)
#7
for i in range(5, 0, -1):
    for n in range(i, 0, -1):
        print(n, end=" ")
    print()
#8
list1 = [10, 20, 30, 40, 50]
for item in reversed(list1):
    print(item)
#9
for i in range(-10, 0):
    print(i)
#10
for i in range(5):
    print(i)

print("Done!")









