print("please enter ten numbers")

odd_count = 0

for i in range(1, 11):
    num = float(input(f"Enter number {i}: "))
    if num % 2 != 0:
        odd_count += 1
        
print(" The total odd numbers are:", odd_count)