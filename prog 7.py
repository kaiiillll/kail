print("please enter ten numbers")

total = 0

for i in range(1, 11):
    num = float(input(f"Enter number {i}: "))
    total += num
    
print("The sum of ten numbers is:", total)
 