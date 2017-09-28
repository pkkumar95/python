import Method1
import time


def stripClosest(strip, n, d):
    minimum = d
    j = 1
    for i in range(n):
        if j < n and (strip[j][1] - strip[i][1]) < minimum:
            for j in range(i + 1, n):
                if Method1.findDistance(strip[i], strip[j]) < minimum:
                    minimum = Method1.findDistance(strip[i], strip[j])
    return minimum


def findSmallestDis(X, Y, n):
    if n <= 3:
        return Method1.bruteForce(X)

    mid = n // 2
    mid_point = X[mid]
    Yl = []
    Yr = []
    for i in range(n):
        if Y[i][0] <= mid_point[0]:
            Yl.append(Y[i])
        else:
            Yr.append(Y[i])
    dl = findSmallestDis(X, Yl, mid)
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
    point = [[2, 3], [12, 30], [40, 50], [5, 1], [12, 10], [3, 4]]
    start_time = time.time()
    print(closestPair(point, len(point)))
    elapsed = time.time() - start_time
    print(elapsed)
