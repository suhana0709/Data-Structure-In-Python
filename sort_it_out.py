num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))
num5 = int(input("Enter number 5: "))

numerals = [num1, num2, num3, num4, num5]
print(" Words to be sorted: ", numerals)
def sort(numbers):
    odd = []
    even = []
    odd_count = 0
    even_count = 0
    for number in numbers:
        if number%2==0:
            even.append(number)
            even_count += 1
        else:
            odd.append(number)
            odd_count += 1
    print("List of even numbers:-\n", even)
    print("List of odd numbers:-\n", odd)
    return odd_count, even_count
    
to_be_sorted = sort(numerals)
print("The number of odd and even numbers(respectively) are:- \n",to_be_sorted)