#1
name=input("What is your name ")
birth_year=input("what is your birth year ")
age=2025-int(birth_year)
print(name)
print(age)

#2
Extract car names from the following text:
txt = 'LMaasleitbtui'
name = 'LMaasleitbtui'
print(name[::2])
print(name[1::11])

#3
Extract car names from the following text:
txt = 'MsaatmiazD'   
name='MsaatmiazD'
print(name[::2])
print(name[::-2])

#4
Extract the residence area from the following text:
txt = "I'am John. I am from London"
name="I'am John. I am from London"
words=(name.split())
print(words[-1])


#5 
user_input=input('Enter a string')
reversed_string=user_input[::-1]
print(reversed_string)



#6
user_input = input("Enter a string: ")
count = 0
for char in user_input:
    if char.lower() in "aeiou":
        count += 1
print( count)



#7
user_input=input("enter numbers with space")
numbers=list(map(int,user_input.split()))
maximum_value=max(numbers)
print(maximum_value)

#8
word = input("Enter a word: ")
if word == word[::-1]:
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")

#9

email = input("Enter your email address: ")
username,domain = email.split('@')

print("The domain of the email is:", domain)
