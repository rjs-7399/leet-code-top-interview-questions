def column_number(column):
    result = 0
    for i in range(len(column)):
        result *= 26
        result += ord(column[i]) - ord('A') + 1
    return result
print(column_number('ZZZ'))