try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Enter a number,")
tuplex = (2,3,4)
for i in tuplex:
    a = num*i
    print(a)