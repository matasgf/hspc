import math
import sys

lines = sys.stdin.readlines()
correct = int(lines[0])
num_cases = int(lines[1])
 
best = -1
bestNames = []
case = 2
while case < num_cases + 2:
    guess, name = lines[case].split()

    diff = math.fabs(int(correct) - int(guess))
    if (best == -1):
        best = diff
        bestNames.append(name)
    elif (diff == best):
        bestNames.append(name)
    elif (diff < best):
        bestNames = [name]
        best = diff
    case = case + 1

print("%s" % " ".join(bestNames) )


