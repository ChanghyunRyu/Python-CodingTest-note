import sys

t = int(input())
result = []
for _ in range(t):
    n = int(input())
    applicant = []
    for _ in range(n):
        doc, interview = map(int, sys.stdin.readline().split())
        applicant.append((doc, interview))

    applicant.sort()
    check = applicant[0][1]
    people = 0
    for a in applicant:
        if a[1] <= check:
            people += 1
            check = a[1]
    result.append(people)
for r in result:
    print(r)
