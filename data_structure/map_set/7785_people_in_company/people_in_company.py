import sys

n = int(input())
company = set()
for _ in range(n):
    name, command = sys.stdin.readline().split()
    if command == 'enter':
        company.add(name)
    elif command == 'leave':
        company.remove(name)

company = sorted(list(company), reverse=True)
for person in company:
    print(person)
