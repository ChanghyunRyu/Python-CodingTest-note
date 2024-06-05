def solution(new_id):
    # 1단계
    answer = new_id.lower()

    # 2단계
    temp = []
    for char in answer:
        if char.isalpha() or char.isdigit() or char in ('-', '_', '.'):
            temp.append(char)
    answer = ''.join(temp)

    # 3단계
    while '..' in answer:
        answer = answer.replace('..', '.')

    # 4단계
    answer = answer.strip('.')

    # 5단계
    if answer == '':
        answer = 'a'

    # 6단계
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    # 7단계
    while len(answer) < 3:
        answer = ''.join([answer, answer[-1]])
    return answer

