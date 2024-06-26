def determine_triangle(side1, side2, side3):
    if side1 == side2 == side3:
        return 'Equilateral'
    elif side1+side2 <= side3 or side1+side3 <= side2 or side2+side3 <= side1:
        return 'Invalid'
    elif side1 == side2 or side1 == side3 or side2 == side3:
        return 'Isosceles'
    return 'Scalene'


while True:
    s1, s2, s3 = map(int, input().split())
    if s1 == s2 == s3 == 0:
        break
    print(determine_triangle(s1, s2, s3))
