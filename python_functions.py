# Challenge 1

def sum_to(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


print(sum_to(6)) # returns 21
print(sum_to(10)) # returns 55

# Challenge 2

def largest(num):
    max_num = num[0]
    for num in num:
        if num > max_num:
            max_num = num
    return max_num
    
print(largest([1, 2, 3, 4, 0])) # returns 4
print(largest([10, 4, 2, 231, 91, 54])) # returns 231

# Challenge 3

def occurrences(string, char):
    count = 0
    i = 0

    while i < len(string):
        if string[i:].startswith(char):
            count += 1
            i += len(char)
        else:
            i += 1
    return count

print(occurrences('fleep floop', 'e')) # returns 2
print(occurrences('fleep floop', 'p')) # returns 2
print(occurrences('fleep floop', 'ee')) # returns 1
print(occurrences('fleep floop', 'fe')) # returns 0

# Challenge 4

def product(*num):
    total = 1
    for num in num:
        total *= num
    return total

print(product(-1, 4)) # returns -4
print(product(2, 5, 5)) # returns 50
print(product(4, 0.5, 5)) # returns 10.0