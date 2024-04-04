value = 3053456

a = 0
for _ in range(len(str(value))):
    b = value % 10
    value //= 10
    if b > a:
        a = b
print(a)