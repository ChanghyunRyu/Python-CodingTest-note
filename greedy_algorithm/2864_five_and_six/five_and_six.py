a, b = input().split()

a_only_five = int(a.replace('6', '5'))
b_only_five = int(b.replace('6', '5'))

a_only_six = int(a.replace('5', '6'))
b_only_six = int(b.replace('5', '6'))

print('{} {}'.format(a_only_five+b_only_five, a_only_six+b_only_six))
