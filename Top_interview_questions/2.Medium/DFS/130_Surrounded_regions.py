def flood_fill(image, x, y, new_color):
    if image[x][y] == new_color:
        return image

    rows = len(image)
    cols = len(image[0])
    original_color = image[x][y]
    stack = [(x, y)]

    while stack:
        row, col = stack.pop()

        if row < 0 or row >= rows or col < 0 or col >= cols:
            continue

        if image[row][col] != original_color:
            continue

        image[row][col] = new_color

        stack.append((row - 1, col))  # Up
        stack.append((row + 1, col))  # Down
        stack.append((row, col - 1))  # Left
        stack.append((row, col + 1))  # Right
    return image


if __name__ == "__main__":
    image = [
         ["X", "O", "X", "O", "X", "O"],
         ["O", "X", "O", "X", "O", "X"],
         ["X", "O", "X", "O", "X", "O"],
         ["O", "X", "O", "X", "O", "X"]
    ]

    m = len(image)
    n = len(image[0])

    #Convert connected 0's to -1 of first and last column of matrix
    for i in range(m):
        if image[i][0] == "O":
            flood_fill(image, i, 0, "N")
        if image[i][n-1] == "O":
            flood_fill(image, i, n-1, "N")


    #Convert connected 0's to -1 of first and last row of matrix
    for i in range(n):
        if image[0][i] == "O":
            flood_fill(image, 0, i, "N")
        if image[m-1][i] == "O":
            flood_fill(image, m-1, i, "N")

    for i in range(m):
        for j in range(n):
            if image[i][j] == "O":
                image[i][j] = "X"
            if image[i][j] == "N":
                image[i][j] = "O"

    for row in image:
        print(row)