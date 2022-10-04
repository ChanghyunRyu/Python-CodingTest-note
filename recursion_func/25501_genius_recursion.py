import sys
t = int(input())
tests = []
for i in range(t):
    tests.append(sys.stdin.readline().strip())


def ispalindrome(test, start, end, count):
    if start >= end:
        print("1 {}".format(count+1))
    elif test[start] != test[end]:
        print("0 {}".format(count+1))
    else:
        ispalindrome(test, start+1, end-1, count+1)


for test in tests:
    ispalindrome(test, 0, len(test)-1, 0)
