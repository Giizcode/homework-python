#1
fruits = ["apple", "banana", "cherry", "mango", "orange"]
print(fruits[2])  
#2
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print(combined_list)  
#3
numbers = [10, 20, 30, 40, 50]
new_list = [numbers[0], numbers[len(numbers)//2], numbers[-1]]
print(new_list)  
#4
movies = ["Inception", "The Matrix", "Interstellar", "Titanic", "Avatar"]
movies_tuple = tuple(movies)
print(movies_tuple)
#5
cities = ["London", "Berlin", "New York", "Paris", "Tokyo"]
is_paris_in_list = "Paris" in cities
print(is_paris_in_list)  
#6
numbers = [1, 2, 3]
duplicated_list = numbers * 2
print(duplicated_list)  
#7
nums = [10, 20, 30, 40, 50]
nums[0], nums[-1] = nums[-1], nums[0]
print(nums)  
#8
numbers_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
sliced = numbers_tuple[3:8]
print(sliced)  
#9
colors = ["red", "blue", "green", "blue", "yellow", "blue"]
count_blue = colors.count("blue")
print(count_blue)  
#10
animals = ("cat", "dog", "lion", "tiger", "elephant")
index_lion = animals.index("lion")
print(index_lion)  
#11
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
merged_tuple = tuple1 + tuple2
print(merged_tuple)  
#12
my_list = [1, 2, 3, 4]
my_tuple = (5, 6, 7)
print(len(my_list))  
print(len(my_tuple)) 
#13
num_tuple = (10, 20, 30, 40, 50)
num_list = list(num_tuple)
print(num_list)
#14
values = (12, 45, 2, 99, 34)
print(max(values))  
print(min(values))  
#15
words = ("hello", "world", "python", "is", "awesome")
reversed_words = words[::-1]
print(reversed_words)
