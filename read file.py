line_number = int(input('Enter the line number: '))
with open('testfile.txt') as f:
    i = 1
    for line in f:
        if i == line_number:
            break
        i += 1
