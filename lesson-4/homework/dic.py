#1
my_dict = {
    'python': 3,
    'sql': 2,
    'excel': 1,
    'powerBI': 4
}
sorted_asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))
sorted_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print(sorted_asc)
print(sorted_desc)

#2
my_dict = {0:10,1:20}
my_dict[2]=30
print(my_dict)



#3 
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)

#4
n=5
square_dict = {}
for x in range(1, n+1):
    square_dict[x]=x*x
    print(square_dict)


#5
square_dict = {}
for x in range(1,16):
    square_dict[x]=x*x
    print(square_dict)




#1
my_set={1,3,3,6,7,7,8,9}
print(my_set)

#2
my_set = {"python", "sql", "powerBI"}

for item in my_set:
    print(item)

#3
my_set = {"python", "sql"}
my_set.update(["excel","powerBI","tableau"])
print(my_set)

#4
my_set = {"python", "sql","excel","powerBI","tableau"}
my_set.remove("tableau")
print(my_set)


#5
my_set = {"python", "sql","excel","powerBI","tableau"}
my_set.discard("tableau")
print(my_set)




