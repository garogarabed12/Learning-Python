num = 0
print("Sum of:")
for i in range(1, 100):
    num += i

print("All numbers:", num)

num = 0
for i in range(1, 100, 2):
    num += i
print("Even numbers:", num)

num = 0
for i in range(1, 100):
    if(i % 4 == 0):
        num += i
print("Numbers divisable by 4:", num)
