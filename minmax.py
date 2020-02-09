gradingStrategy = [
    [0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
    [0, 100, -10,  10,   3,   3,  10, -10, 100,   0],
    [0, -10, -20,  -3,  -3,  -3,  -3, -20, -10,   0],
    [0,  10,  -3,   8,   1,   1,   8,  -3,  10,   0],
    [0,   3,  -3,   1,   1,   1,   1,  -3,   3,   0],
    [0,   3,  -3,   1,   1,   1,   1,  -3,   3,   0],
    [0,  10,  -3,   8,   1,   1,   8,  -3,  10,   0],
    [0, -10, -20,  -3,  -3,  -3,  -3, -20, -10,   0],
    [0, 100, -10,  10,   3,   3,  10, -10, 100,   0],
    [0,   0,   0,   0,   0,   0,   0,   0,   0,   0]
]


class Minimax():

    def calc(self, availableArr):
        getStrategy = []

        for i in range(len(availableArr)):
            x = availableArr[i][0] + 1
            y = availableArr[i][1] + 1
            #print(f'x : {x}, y : {y}')
            getStrategy.append(gradingStrategy[x][y])

        # print(getStrategy)
        Max = getStrategy.index(max(getStrategy))
        #print(f'max : {Max}')

        return availableArr[Max]
