import math
import random

def findDistance(pt1, pt2):
    return math.sqrt(math.pow((pt2[0] - pt1[0]), 2) + math.pow((pt2[1] - pt1[1]), 2))

def bruteForce(point):
    minimum_dis = 1000
    for i in range(len(point) - 1):
        for j in range(i + 1, len(point)):
            if findDistance(point[i], point[j]) < minimum_dis:
                minimum_dis = findDistance(point[i], point[j])

    return minimum_dis

def stripClosest(strip, n, d):
    minimum = d
    j = 1
    for i in range(n):
        if j < n and (strip[j][1] - strip[i][1]) < minimum:
            for j in range(i + 1, n):
                if findDistance(strip[i], strip[j]) < minimum:
                    minimum = findDistance(strip[i], strip[j])
    return minimum


def findSmallestDis(X, Y, n):
    if n <= 3:
        return bruteForce(X)

    mid = n // 2
    mid_point = X[mid]
    Yl = []
    Yr = []
    for i in range(n):
        if Y[i][0] <= mid_point[0]:
            Yl.append(Y[i])
        else:
            Yr.append(Y[i])
    dl = findSmallestDis(X[:mid], Yl, mid)
    dr = findSmallestDis(X[mid:], Yr, n - mid)
    d = min(dl, dr)
    strip = []
    for i in range(n):
        if abs(Y[i][0] - mid_point[0]) < d:
            strip.append(Y[i])
    # print(strip)
    return min(d, stripClosest(strip, len(strip), d))


def closestPair(point, n):
    X = point.copy()
    Y = point.copy()
    X = sorted(X, key=lambda x: x[0])
    Y = sorted(Y, key=lambda x: x[1])
    return findSmallestDis(X, Y, n)



if __name__ == '__main__':
    count = int(input("Enter number of points:"))
    point = list()
    maxValue = 100
    minValue = 0
    for i in range(count):
        point.append([random.randint(minValue, maxValue), random.randint(minValue, maxValue)])
    #print(point)
    print(closestPair(point, len(point)))