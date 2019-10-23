import sys

for line in sys.stdin:
    words = line.split()
    at_bats = 0
    bases = 0

    for word in words:
        at_bat = int(word)
        if at_bat == -1:
            continue

        at_bats += 1
        bases += at_bat

    if at_bats == 0:
        continue

    print("{0:0.4f}".format(float(bases) / float(at_bats)))