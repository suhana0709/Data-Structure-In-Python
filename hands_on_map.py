#adding two lists
lst1 = [1, 3, 8, 11, 15]
lst2 = [5, 6, 2, 1, 4]
lst = map(lambda x, y : x+y, lst1 , lst2)
print("Addition of two lists:- ")
print(list(lst))

#using map
nums = [1, 2, 3, 4, 5]
def sq(n):
    return n*n
result = list(map(sq, nums))
print("Square of numbers in a list:-")
print(result)