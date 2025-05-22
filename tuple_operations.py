#creating a tuple with different data types
tuplex = (10, 11, 'False', 3.2)
print(tuplex)
#creating another tuple with integers
tuplex = (12, 2012, 9, 7, 8, 56, 9, 6)
print(tuplex)
#creating a new tuple by adding 9 to the previous tuple
tuple1 = tuplex + (9,)
print(tuple1)
#counting the occurances of 9 in "tuple1"
print(tuple1.count(9))
#slicing
#giving the starting and ending range
slice1 = tuple1[3:7]
print(slice1)
#giving only the ending range
slice2 = tuple1[:6]
print(slice2)