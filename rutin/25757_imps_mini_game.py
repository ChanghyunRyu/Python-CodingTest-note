import sys


people = set()
n, g = input().split()
n = int(n)

for _ in range(n):
    person = sys.stdin.readline()
    people.add(person)

if g == 'Y':
    print(len(people))
elif g == 'F':
    print(len(people)//2)
elif g == 'O':
    print(len(people)//3)
