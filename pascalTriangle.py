def generate(numRows: int):
    triangle = [[1]]  # first row

    for i in range(1, numRows):
        prev_row = triangle[-1]
        row = [1]  # start with 1
        for j in range(1, i):  # build middle values
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)  # end with 1
        triangle.append(row)

    return triangle
