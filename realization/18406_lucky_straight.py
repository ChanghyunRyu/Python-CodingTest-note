n = input()
length = int(len(n)/2)
left = n[0:length]
right = n[length: length+length]
right_sum = left_sum = 0
for num in left:
    left_sum += int(num)
for num in right:
    right_sum += int(num)
if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")
