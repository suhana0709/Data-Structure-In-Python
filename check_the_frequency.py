test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'Coding': 1}
print(test_dict)

num = int(input("Enter the value which you want to check the frequency of: "))
    
frequency = 0

for key in test_dict:
    if test_dict[key] == num:
        frequency = frequency + 1

print(frequency)
