import sys
s = input()
q = int(input())
questions = []
for i in range(q):
    a, start, end = sys.stdin.readline().split()
    start, end = int(start), int(end)
    questions.append((a, start, end))
r = [[0]*26 for i in range(len(s) + 1)]
alphabet = [0]*26
for i in range(len(s)):
    alphabet[ord(s[i])-97] += 1
    r[i+1] = list(alphabet)

for question in questions:
    a, start, end = question[0], question[1], question[2]
    answer = r[end+1][ord(a)-97] - r[start][ord(a)-97]
    print(answer)
