def reader(filename):
    a = 0
    lines = 0
    with open(filename, 'r') as file:
        for line in file:
            lines += 1
            if line.strip() == 'A':
                a += 1
    return a, a/lines

s = reader('aa.txt')
print(s)