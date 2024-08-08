def solution(records):
    answer = []
    record_id = {}
    record_chat = []
    for record in records:
        record = record.split()
        command, uid = record[0], record[1]
        if command == 'Enter':
            record_id[uid] = record[2]
            record_chat.append((command, uid))
        elif command == 'Leave':
            record_chat.append((command, uid))
        elif command == 'Change':
            record_id[uid] = record[2]

    for record in record_chat:
        if record[0] == 'Enter':
            answer.append('{}님이 들어왔습니다.'.format(record_id[record[1]]))
        elif record[0] == 'Leave':
            answer.append('{}님이 나갔습니다.'.format(record_id[record[1]]))
    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234", "Enter uid1234 Prodo","Change uid4567 Ryan"]))
