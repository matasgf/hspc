import sys

def trib(val):
    if val == 0:
        return 1

    if val == 1:
        return 1

    if val == 2:
        return 2

    return trib(val - 1) + trib(val - 2) + trib(val - 3)

for line in sys.stdin:
    val = int(line)
    print(trib(val))
