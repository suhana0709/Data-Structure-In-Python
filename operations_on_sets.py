#set of integers
my_set = {1, 2, 3}
print(my_set)
#set of different elements
my_set = {1.0, 4, 'Hello', (4, 7, 8)}
print(my_set)
#another set
my_set = {1,2,3,4,3,2}
print(my_set)
#converting a list into a set
my_set = set([1,2,3,2])
print(my_set, "\n")

#remove a number from a set
num_set = set([0, 2,2,3, 5,4,4])
print("Original set:-")
print(num_set)
num_set.pop()
print("After removing the first element:-")
print(num_set, "\n")