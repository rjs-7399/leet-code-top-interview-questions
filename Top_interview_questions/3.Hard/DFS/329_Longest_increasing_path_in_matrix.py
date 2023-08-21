def get_neighbours(matrix, x, y, rows, cols):
    stack = [(x, y)]
    ans = []
    while stack:
        min_a, min_b = stack[0]
        min_element = matrix[min_a][min_b]
        for element in stack:
            a,b = element
            if matrix[a][b] < min_element:
                min_a, min_b = a,b
        row, col = min_a, min_b
        stack.remove((min_a,min_b))
        if row < 0 or row >= rows or col < 0 or col >= cols:
            continue
        print(matrix[row][col])
        if len(ans) == 0:
            ans.append(matrix[row][col])
        elif matrix[row][col] > ans[-1]:
            ans.append(matrix[row][col])
        else:
            continue

        stack.append((row - 1, col))  # Up
        stack.append((row + 1, col))  # Down
        stack.append((row, col - 1))  # Left
        stack.append((row, col + 1))  # Right
    return ans

if __name__ == "__main__":
    matrix = [
        [3, 4, 5],
        [3, 2, 6],
        [2, 2, 1]
    ]
    ans = get_neighbours(matrix, 1, 1, 3, 3)
    print(ans)