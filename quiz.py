
#1.What is the result of the following code?
# import numpy as np
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# c = a + b
# print(c)
#c=[5 7 9]

#Question 2
#Create a numpy array of 10 zeros. and reshape it to (2, 5)
# import numpy as np
# arr=np.array([0,0,0,0,0,0,0,0,0,0])
# new_arr=np.reshape(arr, [2,5])
# print(new_arr)

#Question 3
#Find Mean, Mode, Median, Standard Deviation of the following data

#data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
import numpy as np
import statistics as st
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
mean=np.mean(data)
mode=st.mode(data)
median=np.median(data)
std=np.std(data)
print(f"mean is {mean}, mode is {mode}, median is {median} and standard deviation is {std}")




"""Question 4
create a 6x6 numpy array with random values and find the min and max values

Question 5
create a 3D numpy array and reshape it to 2D

Question 6
create 1D array from this data

    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


"""