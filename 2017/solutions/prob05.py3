import sys

lines = sys.stdin.readlines()
num_cases = int(lines[0])
 
case = 1
while case < num_cases + 1:
    word, search, replace = lines[case].split()
    print("%s" % str.replace(word, search, replace))
    case = case + 1

