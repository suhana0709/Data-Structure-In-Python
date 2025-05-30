#zipping two lists
s1 = {1, 2 , 3}
s2 = {'b', 'c', 'a'}
s3 = list(zip(s1, s2))
print(s3, "\n")

#zipping two lists but one is reversed
lst1 = (200, 300, 400)
lst2 = (1000, 5000, 6000)
for x, y in  zip(lst1, lst2[::-1]):
    print(x, y,"\n")

#zip in dictionaries
a = ['apple', 'banana', 'mango']
b = [5, 10, 30]
new_dict = {a:b for a,b in zip(a,b)}
print("{}".format(new_dict))