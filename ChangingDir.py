def changing_direction(elements: list[int]) -> int:
    prev = elements[0]
    count = 0
    flag = int(elements[0] > elements[1])
    for i in range(len(elements)):
        postflag = flag
        if prev <= elements[i]:
            flag = 0
            if flag != postflag:
                count += 1
        elif prev >= elements[i]:
            flag = 1
            if flag != postflag:
                count += 1
        prev = elements[i]
    return count


print("Example:")
print(changing_direction([1, 2, 3, 4, 5]))

# These "asserts" are used for self-checking
assert changing_direction([1, 2, 3, 4, 5]) == 0
assert changing_direction([1, 2, 3, 2, 1]) == 1
assert changing_direction([1, 2, 2, 1, 2, 2]) == 2