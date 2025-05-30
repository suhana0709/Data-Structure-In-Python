num = int(input("Enter a number: "))
odd = [x for x in range(num) if x%2!=0]
print("All the odd numbers under ",num," = ",odd)
print("\n")
fruit = ['apple', 'banana', 'mango', 'orange']
print("Original list: ",fruit)
FRUIT = [fruit.capitalize() for fruit in fruit ]
print("After capitalizing:-")
print(FRUIT)