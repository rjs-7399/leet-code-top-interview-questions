def generate(num):
    triangle = []
    for index in range(num):
        if index == 0:
            triangle.append([1])
        elif index == 1:
            triangle.append([1,1])
        else:
            level = []
            for itr in range(index+1):
                if itr == 0 or itr == index:
                    level.append(1)
                else:
                    misc_number = triangle[index-1][itr] + triangle[index-1][itr-1]
                    level.append(misc_number)
            triangle.append(level)
    return triangle
if __name__ == "__main__":
    num = 100
    triangle = generate(num)
    for element in triangle:
        print(element)