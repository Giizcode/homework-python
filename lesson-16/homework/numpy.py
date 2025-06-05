import numpy as np
values = [12.23, 13.32, 100, 36.32] 
array_1d = np.array(values)
print (array_1d)
#2
a = np.array ([[ 2, 3, 4], [ 5, 6, 7], [ 8, 9, 10]])
print (a)
#3
null_vector = np.zeros(10)
print("Original null vector:", null_vector)

null_vector[5] = 11  
print("Updated vector:", null_vector)
#4
n = np.arange (12,38)
print (n)
#5
integer_array = np.array ([1, 2, 3, 4])
float_array = integer_array.astype(float)
print (float_array) 
#6
import numpy as np
celsius = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0.])
fahrenheit = (celsius * 9/5) + 32
print(celsius)
print(fahrenheit)
#7
array = np.array ([10, 20, 30])
new_array = np.append(array,[40, 50, 60, 70, 80, 90])
print (new_array)
#8
import numpy as np 
arr = np.random.rand(10)
print('Random array:', arr)
mean = np.mean(arr)
print('Mean:', mean)
median = np.median(arr)
print('Median:', median)
std_dev = np.std(arr)
print('Standard Deviation:', std_dev)
#9 
import numpy as np
x = np.random.random ((10,10))
xmin,xmax= x.min(),x.max() 
print ("minimum and Maximum value", xmin,xmax)
#10
arr_3x3x3 = np.random.rand(3, 3, 3)
print("3x3x3 Random Array:\n", arr_3x3x3)
