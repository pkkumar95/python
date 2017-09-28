
import math
# import time


def findDistance(x, y):
    return math.sqrt(math.pow((x[0] - y[0]), 2) + math.pow((x[1] - y[1]), 2))


def bruteForce(point):
    # point.sort()
    minimum_dis = 1000
    for i in range(len(point) - 1):
        for j in range(i + 1, len(point)):
            if findDistance(point[i], point[j]) < minimum_dis:
                minimum_dis = findDistance(point[i], point[j])

    return minimum_dis


if __name__ == '__main__':
    point = [[2, 3], [12, 30], [40, 50], [5, 1], [12, 10], [3, 4]]
    # start_time = time.time()
    print(bruteForce(point))
    # elapsed = time.time() - start_time
    # print(elapsed)
