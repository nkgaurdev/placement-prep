n = abs(int(input("Enter a number: ")))
count = 0

if n == 0:
    count = 1

while n > 0:
    n //= 10  
    count += 1

print(count)
