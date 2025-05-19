#1
def is_leap(year):
 if not isinstance(year, int):
        raise ValueError("Year must be an integer.")

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

#2
n = int(input("Enter a number: "))

if n % 2 == 1:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")

#3

def even_numbers_with_if(a, b):
    if a > b:
        a, b = b, a
    evens = list(range(a + (a % 2), b + 1, 2)) if a % 2 != 0 else list(range(a, b + 1, 2))
    return evens
