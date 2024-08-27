def solution(id_list, report, k):
    r_number = {}
    mail_number = {}
    for user in id_list:
        r_number[user] = set()
        mail_number[user] = 0

    for r in report:
        record_report(r, r_number)

    for user in id_list:
        if len(r_number[user]) >= k:
            for user_id in r_number[user]:
                mail_number[user_id] += 1

    answer = []
    for user in id_list:
        answer.append(mail_number[user])
    return answer


def record_report(report, reports_number):
    user_id, report_id = report.split()
    reports_number[report_id].add(user_id)


print(solution(["muzi", "frodo", "apeach", "neo"],
               ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],2))

